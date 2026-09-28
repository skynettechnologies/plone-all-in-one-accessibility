# -*- coding: utf-8 -*-
"""@@aioa-diagnose -- what this site is configured with.

Manager-only. The Skynet API calls are made from the browser (see
browser/static/aioa_skynet_sync.js), so this view does not call Skynet. It
shows what the widget <script> tag will load, which settings object is in
use, and which domain the browser-side calls send to Skynet.

    /<site>/@@aioa-diagnose

To see the Skynet calls themselves, open the settings form with DevTools ->
Network (filter: Fetch/XHR), press Save, and look for
widget-setting-update-platform. From the console, AIOA_SKYNET.buildPayload()
prints what would be sent and AIOA_SKYNET.sync() sends it.

Open this view on the SAME hostname the public site is served on: the domain
sent to Skynet is derived from the hostname, and it must equal the hostname
the widget loads on.
"""
import json

from plone.all_in_one_accessibility.aioa_utils import build_widget_script_tag
from plone.all_in_one_accessibility.aioa_utils import build_widget_script_url
from plone.all_in_one_accessibility.aioa_utils import get_canonical_domain
from plone.all_in_one_accessibility.browser.viewlets import get_all_widget_settings_urls
from plone.all_in_one_accessibility.browser.viewlets import get_widget_settings
from plone.all_in_one_accessibility.content.all_in_one_accessibility_setting import (
    IAllInOneAccessibilitySetting,
)
from Products.Five.browser import BrowserView
from zope.schema import getFieldNames


class AioaDiagnoseView(BrowserView):
    def __call__(self):
        setting = get_widget_settings()
        domain = get_canonical_domain(self.request)

        out = {
            "domain_sent_to_skynet": domain,
            "note": (
                "domain_sent_to_skynet must equal the hostname the browser "
                "loads the widget on, or Skynet stores your settings under a "
                "domain the widget never asks for. The Skynet API calls are "
                "made by the browser (aioa_skynet_sync.js); check DevTools -> "
                "Network for add-user-domain and widget-setting-update-platform."
            ),
            "settings_object": None,
        }

        if setting is None:
            out["error"] = "No 'All in One Accessibility Setting' object exists yet."
            return self._respond(out)

        out["settings_object"] = setting.absolute_url()
        all_urls = get_all_widget_settings_urls()
        out["settings_objects_found"] = all_urls
        if len(all_urls) > 1:
            out["warning"] = (
                "More than one settings object exists. The most recently "
                "edited one (settings_object above) is used for the widget; "
                "delete the others so there is no doubt."
            )
        out["stored_values"] = {
            name: getattr(setting, name, None)
            for name in getFieldNames(IAllInOneAccessibilitySetting)
            if name != "aioa_token"
        }
        out["loader_script_tag"] = build_widget_script_tag(setting)
        out["loader_script_url"] = build_widget_script_url(setting)

        return self._respond(out)

    def _respond(self, data):
        self.request.response.setHeader("Content-Type", "application/json")
        return json.dumps(data, indent=2, default=str, sort_keys=False)
