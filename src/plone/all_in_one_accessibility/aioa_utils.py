# -*- coding: utf-8 -*-

from html import escape
from urllib.parse import urlencode
from urllib.parse import urlparse

WIDGET_SCRIPT = "accessibility/js/all-in-one-accessibility-js-widget-minify.js"
NON_EU_LOADER = "https://www.skynettechnologies.com/" + WIDGET_SCRIPT
EU_LOADER = "https://eu.skynettechnologies.com/" + WIDGET_SCRIPT

#: Icon-size CSS classes the widget understands, when "custom icon size"
#: is switched off (see IAllInOneAccessibilitySetting.aioa_icon_size).
NAMED_ICON_SIZES = {
    "aioa-big-icon",
    "aioa-medium-icon",
    "aioa-default-icon",
    "aioa-small-icon",
    "aioa-extra-small-icon",
}


def get_canonical_domain(request):
    """Return "https://" + hostname, with no port and no scheme surprises.

    Skynet's backend keys a registered site by "https://" + hostname
    (no port). request ACTUAL_URL/URL can be "http://" on a local/dev
    instance sitting behind no TLS-terminating proxy, or can carry a
    port (e.g. "http://example.com:8080"); either would register/sync
    under a key that never matches what the widget's own domain-based
    settings lookup queries for later. This mirrors aioa_domain_util.js's
    getAioaCanonicalDomain() exactly, including deliberately using this
    canonical form ONLY for values sent to Skynet's API. The JavaScript
    canonicalDomain() in aioa_skynet_sync.js applies the same rule.
    """
    actual_url = ""
    if request is not None:
        actual_url = request.get("ACTUAL_URL", "") or request.get("URL", "")
    hostname = urlparse(actual_url).hostname
    if not hostname:
        hostname = "localhost"
    return "https://%s" % hostname


def _cache_buster(setting):
    """Millisecond timestamp of the settings object's last modification.

    Skynet's own plugins append a random "t" so the widget script is never
    served from a stale cache. A random number would defeat caching on
    every page view; the modification time changes exactly when the
    settings do, which is the only moment the cache must be bypassed.
    Returns None if unavailable.
    """
    modified = getattr(setting, "modified", None)
    if modified is None:
        return None
    try:
        return int(modified().millis())
    except (AttributeError, TypeError, ValueError):
        return None


def build_widget_query(setting):
    """Query parameters for the widget script, in Skynet's standard shape.

    colorcode is the bare hex value (no "#"): a literal "#" is either
    percent-encoded to "%23" or, unencoded, starts the URL fragment and
    truncates the query. (The *API* payload in aioa_skynet_sync.js sends the
    bare hex, like the plone module.)

    position is "<place>.<icon type>.<named icon size>". The named icon
    size is always included, as Skynet's plone plugin does; when
    custom icon size or precise positioning is enabled, Skynet applies
    those from its server-side copy of the settings instead.
    """
    color = (setting.aioa_color or "420083").strip().lstrip("#")
    place = setting.aioa_place or "bottom_right"
    icon_type = setting.aioa_icon_type or "aioa-icon-type-1"
    icon_size = setting.aioa_icon_size or "aioa-default-icon"

    params = {
        "colorcode": color,
        "token": getattr(setting, "aioa_token", "") or "",
    }
    stamp = _cache_buster(setting)
    if stamp is not None:
        params["t"] = stamp
    params["position"] = "%s.%s.%s" % (place, icon_type, icon_size)
    return params


def build_widget_script_url(setting):
    """Full widget script URL (EU or non-EU host) for `setting`."""
    loader = EU_LOADER if not getattr(setting, "no_required_eu", True) else NON_EU_LOADER
    return "%s?%s" % (loader, urlencode(build_widget_query(setting)))


def build_widget_script_tag(setting):
    """The <script> element that loads the widget.

    A classic script with id="aioa-adawidget", exactly like every Skynet
    integration -- not type="module" (document.currentScript is null in a
    module script and it is fetched in CORS mode, both of which can stop a
    loader from reading its own query string).

    The URL is HTML-escaped ("&" -> "&amp;") so it is valid in the
    attribute.
    """
    return '<script id="aioa-adawidget" defer="defer" src="%s"></script>' % escape(
        build_widget_script_url(setting), quote=True
    )
