# -*- coding: utf-8 -*-
import logging

from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.container.interfaces import INameChooser
from zope.interface import implementer

logger = logging.getLogger("plone.all_in_one_accessibility")

_SETTING_TYPE = "All in One Accessibility Setting"
_SETTING_ID = "accessibility-setting"


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "plone.all_in_one_accessibility:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["plone.all_in_one_accessibility.upgrades"]


def _create_default_widget_settings(site):
    """Create the singleton settings object right away, at the site root.

    Without this, browser.viewlets.AccessibilityWidgetViewlet has nothing
    to render: get_widget_settings() only finds a settings object once
    someone has manually gone to Add > All in One Accessibility Setting
    and clicked Save on the form once. That meant the widget script was
    never injected -- and the browser-side Skynet sync in
    aioa_skynet_sync.js never ran either, since it only fires on that
    same settings form -- until after that manual, easy-to-miss step.

    Creating the object here, right after install, with nothing but the
    schema's own defaults (see content/all_in_one_accessibility_setting.py)
    means the widget is live on the site immediately, the same as the
    plone/plone versions of this module behave out of the box. The
    person can still open Site Setup > Add-on Configuration afterwards
    to customise colour, position, icon, etc.
    """
    catalog = api.portal.get_tool("portal_catalog")
    if catalog.unrestrictedSearchResults(portal_type=_SETTING_TYPE):
        # Already exists -- e.g. the profile is being re-imported/upgraded
        # on a site that already has one. Never create a second one.
        return

    settings_id = _SETTING_ID
    if settings_id in site.keys():
        # Extremely unlikely (something else already uses this id) --
        # pick a real, guaranteed-free id ourselves rather than falling
        # back to the type name (which has spaces, and isn't guaranteed
        # free either). We don't rely on plone.api's own safe_id/rename
        # dance for this -- see the comment on safe_id below.
        settings_id = INameChooser(site).chooseName(_SETTING_ID, site)

    api.content.create(
        container=site,
        type=_SETTING_TYPE,
        id=settings_id,
        # NOT safe_id=True: plone.api.content.create() only renames the
        # object (add under a temp UUID, then manage_renameObject to the
        # real id) when `safe_id and id` -- and id is always truthy here.
        # That rename re-checks the container's allowed types, but by then
        # subscribers.disable_add_after_creation has already flipped this
        # FTI's global_allow to False (it reacts to the same object's
        # IObjectAddedEvent, fired by the temp-id add a moment earlier),
        # so the rename fails with "Disallowed subobject type". Since we
        # already picked a known-free id above, we don't need plone.api's
        # own dedup/rename step at all -- create it directly under that id.
        safe_id=False,
        title="All in One Accessibility Setting",
    )
    logger.info(
        "plone.all_in_one_accessibility: created the default "
        "'%s' settings object so the widget is visible right away.",
        _SETTING_TYPE,
    )


def post_install(context):
    """Post install script.

    This is registered as the "default" profile's own post_handler (see
    genericsetup:registerProfile in configure.zcml), NOT as a generic
    <genericsetup:importStep> handler. Those two are passed different
    things under the name "context":

    - an importStep handler gets a GenericSetupContext/ImportContext,
      which has readDataFile()/getSite().
    - a profile's pre_handler/post_handler gets called by
      SetupTool._doRunHandler as handler_function(self) -- "self" being
      the portal_setup tool itself (a Folder), which has neither of
      those methods. Calling context.readDataFile() here raises
      AttributeError (it showed up as a 'RequestContainer' object,
      portal_setup's acquisition wrapper, having no such attribute).

    So there is no data file to check here, and no need for one: this
    handler is already only ever invoked when this specific profile
    finishes importing. Fetch the site via plone.api instead, which
    does not need anything from `context`.
    """
    _create_default_widget_settings(api.portal.get())


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
