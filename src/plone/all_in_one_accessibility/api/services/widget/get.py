# -*- coding: utf-8 -*-
"""@widget REST endpoint.

Previously this returned a literal, unfilled URL template string (the
"{}" placeholders were never substituted with real values), which is
not usable as-is by any client. It now returns the same real,
fully-built widget script URL that browser.viewlets renders
into the page -- useful for a Volto/React frontend that wants to know
the widget URL without server-rendering it, e.g. to load it itself.

Only registered at all when plone.restapi is installed -- see the
`zcml:condition="installed plone.restapi"` guard around
`<include package=".api" />` in configure.zcml.
"""
from plone.all_in_one_accessibility.aioa_utils import build_widget_script_url
from plone.all_in_one_accessibility.browser.viewlets import get_widget_settings
from plone.restapi.services import Service


class WidgetGet(Service):
    def reply(self):
        setting = get_widget_settings()
        if setting is None:
            return {"configured": False, "url": None}
        return {
            "configured": True,
            "url": build_widget_script_url(setting),
        }
