# -*- coding: utf-8 -*-
"""Event subscribers for the "All in One Accessibility Setting" object.

Only the singleton handling lives here: once a settings object exists, the
add form is switched off, and it is switched back on when that object is
deleted.

The Skynet API calls (add-user-domain and widget-setting-update-platform)
are NOT made from Zope. As in the Skynet plone module, they are made from
the browser -- see browser/static/aioa_skynet_sync.js. Calling them from the
server sent every site's requests from one IP address, which Skynet
rate-limited (HTTP 429), and hid the calls from DevTools.
"""
from plone.all_in_one_accessibility.content.all_in_one_accessibility_setting import (
    IAllInOneAccessibilitySetting,
)
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import adapter
from zope.component import getUtility
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from zope.lifecycleevent.interfaces import IObjectRemovedEvent


@adapter(IAllInOneAccessibilitySetting, IObjectAddedEvent)
def disable_add_after_creation(obj, event):
    fti = getUtility(IDexterityFTI, name='All in One Accessibility Setting')
    if fti.global_allow:
        fti.global_allow = False
        fti._p_changed = True


@adapter(IAllInOneAccessibilitySetting, IObjectRemovedEvent)
def enable_add_after_deletion(obj, event):
    fti = getUtility(IDexterityFTI, name='All in One Accessibility Setting')
    if not fti.global_allow:
        fti.global_allow = True
        fti._p_changed = True
