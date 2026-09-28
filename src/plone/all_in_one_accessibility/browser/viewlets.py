from plone import api
from urllib.parse import unquote
from plone.app.layout.viewlets.common import ViewletBase
from plone.all_in_one_accessibility.aioa_utils import build_widget_script_tag

_SETTING_TYPE = 'All in One Accessibility Setting'


def _settings_brains():
    # unrestricted + newest-edited first; see get_widget_settings().
    catalog = api.portal.get_tool('portal_catalog')
    return catalog.unrestrictedSearchResults(
        portal_type=_SETTING_TYPE, sort_on='modified', sort_order='reverse'
    )


def get_widget_settings():
    """Return the settings object in use, or None if not configured yet.

    Normally there is exactly one "All in One Accessibility Setting"
    object (subscribers.disable_add_after_creation blocks a second one).
    If more than one exists anyway -- e.g. one was deleted and re-added, so
    the edit page's URL ends in "-setting-2" -- the MOST RECENTLY EDITED
    one wins. That is the one the person is actually working on; taking
    the catalog's arbitrary first hit could silently load an old copy and
    make new settings look like they are being ignored.

    Uses unrestrictedSearchResults on purpose. The settings object is
    ordinary content with the site's default workflow, so it is normally
    *private*; a plain catalog() call filters by the current user's
    permissions and returns nothing for anonymous visitors. That made
    the widget (and the @widget REST endpoint) appear only to logged-in
    editors and be missing for the very visitors it exists for.
    """
    brains = _settings_brains()
    if not brains:
        return None
    return brains[0]._unrestrictedGetObject()


def get_all_widget_settings_urls():
    """URLs of every settings object (newest-edited first), for diagnostics."""
    return [brain.getURL() for brain in _settings_brains()]

def _on_settings_form(context, request):
    """True on the settings object's own pages and on its add form."""
    if getattr(context, 'portal_type', None) == _SETTING_TYPE:
        return True
    url = unquote(request.get('ACTUAL_URL', '') or '')
    return ('++add++' + _SETTING_TYPE) in url


#: Substrings of ACTUAL_URL that mark a Plone *backend* screen: Site Setup's
#: overview and every individual control panel (their view names all end in
#: "-controlpanel", e.g. "@@overview-controlpanel", "@@security-controlpanel",
#: "@@usergroups-controlpanel"), older-style "prefs_*" preference panels, and
#: the ZMI. None of these are pages a site *visitor* ever sees, so the widget
#: has no business loading there -- it was previously rendering underneath
#: Site Setup and every control panel because only the settings object's own
#: add/edit form was excluded (see _on_settings_form above).
_ADMIN_URL_MARKERS = (
    '-controlpanel',
    '/prefs_',
    '/manage_main',
    '/manage-',
    '/manage_tabs',
)


def _on_admin_page(context, request):
    """True on the settings object's own pages/add form, and on Plone's
    backend/control-panel screens -- everywhere the widget must stay off.
    """
    if _on_settings_form(context, request):
        return True
    url = unquote(request.get('ACTUAL_URL', '') or '')
    return any(marker in url for marker in _ADMIN_URL_MARKERS)


class AccessibilityWidgetViewlet(ViewletBase):
    """Injects the actual Skynet AIOA widget <script> tag on every page.

    This is the Plone equivalent of the plone module's
    templates/base_url_passing.xml: it reads the stored widget settings
    and renders a single <script id="aioa-adawidget"> tag pointing at
    Skynet's widget script with the site's configured colour, position
    and icon options in the query string (see aioa_utils).

    Volto/headless front ends don't render viewlets; they read the same
    URL from the @widget REST endpoint instead.
    """

    def available(self):
        return (
            self.setting is not None
            and not _on_admin_page(self.context, self.request)
        )

    def update(self):
        super(AccessibilityWidgetViewlet, self).update()
        self.setting = get_widget_settings()

    def render(self):
        if not self.available():
            return ''
        return build_widget_script_tag(self.setting)


class AccessibilityCSSViewlet(ViewletBase):
    """Loads this add-on's own UI-enhancement CSS/JS.

    custom.css/custom.js enhance the "All in One Accessibility Setting"
    form (grouping fields, the icon-type picker grid, etc.).
    aioa_skynet_sync.js makes the two Skynet API calls from the browser,
    like the plone module does (add-user-domain, and
    widget-setting-update-platform after Save).

    None of this has anything to do with the public-facing widget, so it
    only loads on the settings object's own views -- its edit view AND the
    add view, because the very first Save happens on the add form (whose
    context is the folder the object is added to, not the object).
    """

    _ADD_MARKER = '++add++' + _SETTING_TYPE
    _ASSET_VERSION = '2.4.1' 

    def _is_add_view(self):
        url = unquote(self.request.get('ACTUAL_URL', '') or '')
        return self._ADD_MARKER in url

    def available(self):
        return (
            getattr(self.context, 'portal_type', None) == _SETTING_TYPE
            or self._is_add_view()
        )

    def render(self):
        if not self.available():
            return ''
        base = '%s/++plone++plone.all_in_one_accessibility' % self.site_url
        v = self._ASSET_VERSION
        return """
<link rel="stylesheet" href="%(base)s/custom.css?v=%(v)s" />
<script src="%(base)s/custom.js?v=%(v)s"></script>
<script src="%(base)s/aioa_skynet_sync.js?v=%(v)s"></script>
""" % {'base': base, 'v': v}
