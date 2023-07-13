# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/controlpanel/browser/overview.pt'

__tokens = {421: ("python:request.set('disable_plone.leftcolumn',1)", 12, 47), 517: (" python:request.set('disable_plone.rightcolumn',1", 13, 46), 979: ('view/upgrade_warning', 26, 23), 1261: ('string:${context/portal_url}/@@plone-upgrade', 34, 35), 1644: ('view/mailhost_warning', 46, 23), 2215: ('string:${portal_url}/@@mail-controlpanel', 57, 39), 2449: ('view/timezone_warning', 66, 23), 2982: ('string:${portal_url}/@@dateandtime-controlpanel', 78, 39), 3241: ('not:view/pil', 87, 23), 3522: ('view/categories', 96, 37), 3574: ("python:view.sublists(category.get('id'))", 97, 34), 3680: ('sublist', 98, 63), 3724: ('category/title', 99, 34), 3823: ('sublist', 102, 40), 3978: ('sublist', 105, 29), 4032: ('sublist', 106, 44), 4092: ('action/visible', 107, 50), 4244: ('action/icon', 109, 37), 4297: (" python:'http' in action['icon'", 110, 40), 4372: ('action/url', 111, 41), 4466: ('icon_url', 113, 42), 4571: ('action/icon', 115, 44), 4627: (' action/titl', 116, 43), 4736: ('not: icon_url', 118, 47), 4798: ("python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", 119, 47), 4976: ('action/title', 121, 38), 5339: ('not:sublist', 133, 31), 5702: ('view/version_overview', 145, 41), 5751: ('version', 146, 25), 5842: ('view/server_info', 148, 42), 5898: (' server_info/wsg', 149, 38), 6042: ('has_wsgi', 152, 51), 6113: ('not:has_wsgi', 153, 51), 6246: ('${server_info/server_name}', 157, 18), 6248: ('server_info/server_name', 157, 20), 6298: ('${server_info/version}', 158, 18), 6300: ('server_info/version', 158, 20), 6397: ('not:view/is_dev_mode', 163, 22), 6969: ('view/is_dev_mode', 175, 22), 261: ('here/prefs_main_template/macros/master', 6, 23), 261: ('here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_139882206247376 = {'class': '', }
_static_139882206237968 = {'class': '', }
_static_139882205842640 = {'class': 'controlPanelSectionFooter', }
_static_139882215143840 = {'class': 'discreet', }
_static_139882205893088 = {'class': 'text-decoration-none text-center ', }
_static_139882101065184 = {'src': '', 'alt': '', 'class': 'icon', }
_static_139882217712816 = {'class': 'mb-3', }
_static_139882213733616 = {'href': '', 'class': 'd-block text-dark text-center py-4 rounded btn btn-light h-100', }
_static_139882208051936 = {'class': 'col mb-4', }
_static_139882205973952 = {'class': 'configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100', }
_static_139882205851040 = {'class': 'row', }
_static_139882205846720 = {'class': '', }
_static_139882205843312 = {'class': 'controlPanelSection mb-4', }
_static_139882205649776 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_139882205650496 = {'href': '', }
_static_139882205657216 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_139882205657456 = {'href': '', }
_static_139882205622672 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_139882205620992 = {'href': '#', 'title': 'Go to the upgrade page', }
_static_139882205621136 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_139882205623008 = {'class': 'lead', }
_static_139882205616624 = {'class': 'documentFirstHeading', }
_static_139882206072256 = {'class': 'controlPanel controlPanelOverview', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882206069568 = 'master'
_static_139882337226896 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales, zope_version_5_8_3_):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206072400
            __attrs_139882206072400 = _static_139882337226896
            __previous_i18n_domain_139882206080032 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139882238648640 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f38dd340340> name=None at 7f38dd3413f0> -> __value
            __value = _static_139882206069568
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206084736
                __attrs_139882206084736 = _static_139882337226896
                __backup_disable_column_one_139882206077776 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 421
                try:
                    __zt_tmp = __attrs_139882206084736
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_139882206072640 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 517
                try:
                    __zt_tmp = __attrs_139882206084736
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_139882206072640 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_139882206072640
                if (__backup_disable_column_one_139882206077776 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_139882206077776
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f38dd340dc0> name=None at 7f38dd341d50> -> __attrs_139882206080080
                __attrs_139882206080080 = _static_139882206072256

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="controlPanel controlPanelOverview">\n  ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205619216
                __attrs_139882205619216 = _static_139882337226896

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd2d19f0> name=None at 7f38dd2d2320> -> __attrs_139882205618400
                __attrs_139882205618400 = _static_139882205616624

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_139882205618160 = []
                __append_139882205618160 = __stream_139882205618160.append
                __append_139882205618160('Site Setup')
                __msgid_139882205618160 = __re_whitespace(''.join(__stream_139882205618160)).strip()
                if __msgid_139882205618160:
                    __append(translate(__msgid_139882205618160, mapping=None, default=__msgid_139882205618160, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd2d32e0> name=None at 7f38dd2d1150> -> __attrs_139882205624400
                __attrs_139882205624400 = _static_139882205623008

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_139882205623296 = []
                __append_139882205623296 = __stream_139882205623296.append
                __append_139882205623296('\n        Configuration area for Plone and add-on Products.\n    ')
                __msgid_139882205623296 = __re_whitespace(''.join(__stream_139882205623296)).strip()
                if 'description_control_panel':
                    __append(translate('description_control_panel', mapping=None, default=__msgid_139882205623296, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x7f38dd2d2b90> name=None at 7f38dd2d1fc0> -> __attrs_139882205617824
                __attrs_139882205617824 = _static_139882205621136

                # <Value 'view/upgrade_warning' (26:23)> -> __condition
                __token = 979
                try:
                    __zt_tmp = __attrs_139882205617824
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'view/upgrade_warning', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205616480
                    __attrs_139882205616480 = _static_139882337226896

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139882205621280 = []
                    __append_139882205621280 = __stream_139882205621280.append
                    __append_139882205621280('\n          Warning\n      ')
                    __msgid_139882205621280 = __re_whitespace(''.join(__stream_139882205621280)).strip()
                    if __msgid_139882205621280:
                        __append(translate(__msgid_139882205621280, mapping=None, default=__msgid_139882205621280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205612400
                    __attrs_139882205612400 = _static_139882337226896
                    __stream_139882099987552_link_continue_with_the_upgrade = ''
                    __stream_139882205613120 = []
                    __append_139882205613120 = __stream_139882205613120.append
                    __append_139882205613120('\n          The site configuration is outdated and needs to be\n          upgraded. Please\n          ')
                    __stream_139882099987552_link_continue_with_the_upgrade = []
                    __append_139882099987552_link_continue_with_the_upgrade = __stream_139882099987552_link_continue_with_the_upgrade.append

                    # <Static value=<ast.Dict object at 0x7f38dd2d2b00> name=None at 7f38dd2d24d0> -> __attrs_139882205617872
                    __attrs_139882205617872 = _static_139882205620992

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139882099987552_link_continue_with_the_upgrade('<a')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205625744
                    __default_139882205625744 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/portal_url}/@@plone-upgrade' (34:35)> -> __attr_href
                    __token = 1261
                    try:
                        __zt_tmp = __attrs_139882205617872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('string', '${context/portal_url}/@@plone-upgrade', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139882099987552_link_continue_with_the_upgrade((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205622240
                    __default_139882205622240 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f38dd2d1a20> at 7f38dd2d3370> -> __attr_title
                    __attr_title = 'Go to the upgrade page'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append_139882099987552_link_continue_with_the_upgrade((' title="%s"' % __attr_title))
                    __append_139882099987552_link_continue_with_the_upgrade('>')
                    __stream_139882205622768 = []
                    __append_139882205622768 = __stream_139882205622768.append
                    __append_139882205622768('\n            continue with the upgrade\n          ')
                    __msgid_139882205622768 = __re_whitespace(''.join(__stream_139882205622768)).strip()
                    if __msgid_139882205622768:
                        __append_139882099987552_link_continue_with_the_upgrade(translate(__msgid_139882205622768, mapping=None, default=__msgid_139882205622768, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_139882099987552_link_continue_with_the_upgrade('</a>')
                    __append_139882205613120('${link_continue_with_the_upgrade}')
                    __stream_139882099987552_link_continue_with_the_upgrade = ''.join(__stream_139882099987552_link_continue_with_the_upgrade)
                    __append_139882205613120('.\n      ')
                    __msgid_139882205613120 = __re_whitespace(''.join(__stream_139882205613120)).strip()
                    if __msgid_139882205613120:
                        __append(translate(__msgid_139882205613120, mapping={'link_continue_with_the_upgrade': __stream_139882099987552_link_continue_with_the_upgrade, }, default=__msgid_139882205613120, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38dd2d3190> name=None at 7f38dd2d1ab0> -> __attrs_139882205619696
                __attrs_139882205619696 = _static_139882205622672

                # <Value 'view/mailhost_warning' (46:23)> -> __condition
                __token = 1644
                try:
                    __zt_tmp = __attrs_139882205619696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'view/mailhost_warning', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205649392
                    __attrs_139882205649392 = _static_139882337226896

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139882205649536 = []
                    __append_139882205649536 = __stream_139882205649536.append
                    __append_139882205649536('\n          Warning\n      ')
                    __msgid_139882205649536 = __re_whitespace(''.join(__stream_139882205649536)).strip()
                    if __msgid_139882205649536:
                        __append(translate(__msgid_139882205649536, mapping=None, default=__msgid_139882205649536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205658224
                    __attrs_139882205658224 = _static_139882337226896
                    __stream_139882099987552_label_mail_control_panel_link = ''
                    __stream_139882205658416 = []
                    __append_139882205658416 = __stream_139882205658416.append
                    __append_139882205658416("\n          You have not configured a mail host or a site 'From'\n          address, various features including contact forms, email\n          notification and password reset will not work. Go to the\n          ")
                    __stream_139882099987552_label_mail_control_panel_link = []
                    __append_139882099987552_label_mail_control_panel_link = __stream_139882099987552_label_mail_control_panel_link.append

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205657408
                    __attrs_139882205657408 = _static_139882337226896
                    __append_139882099987552_label_mail_control_panel_link('\n              ')

                    # <Static value=<ast.Dict object at 0x7f38dd2db970> name=None at 7f38dd2d9a50> -> __attrs_139882205655056
                    __attrs_139882205655056 = _static_139882205657456

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139882099987552_label_mail_control_panel_link('<a')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205644784
                    __default_139882205644784 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@mail-controlpanel' (57:39)> -> __attr_href
                    __token = 2215
                    try:
                        __zt_tmp = __attrs_139882205655056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('string', '${portal_url}/@@mail-controlpanel', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139882099987552_label_mail_control_panel_link((' href="%s"' % __attr_href))
                    __append_139882099987552_label_mail_control_panel_link(' >')
                    __stream_139882205652224 = []
                    __append_139882205652224 = __stream_139882205652224.append
                    __append_139882205652224('Mail control panel')
                    __msgid_139882205652224 = __re_whitespace(''.join(__stream_139882205652224)).strip()
                    if 'text_no_mailhost_configured_control_panel_link':
                        __append_139882099987552_label_mail_control_panel_link(translate('text_no_mailhost_configured_control_panel_link', mapping=None, default=__msgid_139882205652224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_139882099987552_label_mail_control_panel_link('</a>\n          ')
                    __append_139882205658416('${label_mail_control_panel_link}')
                    __stream_139882099987552_label_mail_control_panel_link = ''.join(__stream_139882099987552_label_mail_control_panel_link)
                    __append_139882205658416('\n          to fix this.\n      ')
                    __msgid_139882205658416 = __re_whitespace(''.join(__stream_139882205658416)).strip()
                    if 'text_no_mailhost_configured':
                        __append(translate('text_no_mailhost_configured', mapping={'label_mail_control_panel_link': __stream_139882099987552_label_mail_control_panel_link, }, default=__msgid_139882205658416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38dd2db880> name=None at 7f38dd2d8610> -> __attrs_139882205642960
                __attrs_139882205642960 = _static_139882205657216

                # <Value 'view/timezone_warning' (66:23)> -> __condition
                __token = 2449
                try:
                    __zt_tmp = __attrs_139882205642960
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'view/timezone_warning', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205647520
                    __attrs_139882205647520 = _static_139882337226896

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139882205643536 = []
                    __append_139882205643536 = __stream_139882205643536.append
                    __append_139882205643536('\n          Warning\n      ')
                    __msgid_139882205643536 = __re_whitespace(''.join(__stream_139882205643536)).strip()
                    if __msgid_139882205643536:
                        __append(translate(__msgid_139882205643536, mapping=None, default=__msgid_139882205643536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205648384
                    __attrs_139882205648384 = _static_139882337226896
                    __stream_139882099987552_label_mail_event_settings_link = ''
                    __stream_139882205643728 = []
                    __append_139882205643728 = __stream_139882205643728.append
                    __append_139882205643728('\n\n          You have not set the portal timezone. Date/Time handling will not\n          work properly for timezone aware date/time values.\n          Go to the\n          ')
                    __stream_139882099987552_label_mail_event_settings_link = []
                    __append_139882099987552_label_mail_event_settings_link = __stream_139882099987552_label_mail_event_settings_link.append

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205644064
                    __attrs_139882205644064 = _static_139882337226896
                    __append_139882099987552_label_mail_event_settings_link('\n              ')

                    # <Static value=<ast.Dict object at 0x7f38dd2d9e40> name=None at 7f38dd2d8c10> -> __attrs_139882205929888
                    __attrs_139882205929888 = _static_139882205650496

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139882099987552_label_mail_event_settings_link('<a')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205935024
                    __default_139882205935024 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@dateandtime-controlpanel' (78:39)> -> __attr_href
                    __token = 2982
                    try:
                        __zt_tmp = __attrs_139882205929888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('string', '${portal_url}/@@dateandtime-controlpanel', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139882099987552_label_mail_event_settings_link((' href="%s"' % __attr_href))
                    __append_139882099987552_label_mail_event_settings_link(' >')
                    __stream_139882205656688 = []
                    __append_139882205656688 = __stream_139882205656688.append
                    __append_139882205656688('Date and Time Settings control panel')
                    __msgid_139882205656688 = __re_whitespace(''.join(__stream_139882205656688)).strip()
                    if 'text_no_timezone_configured_control_panel_link':
                        __append_139882099987552_label_mail_event_settings_link(translate('text_no_timezone_configured_control_panel_link', mapping=None, default=__msgid_139882205656688, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_139882099987552_label_mail_event_settings_link('</a>\n          ')
                    __append_139882205643728('${label_mail_event_settings_link}')
                    __stream_139882099987552_label_mail_event_settings_link = ''.join(__stream_139882099987552_label_mail_event_settings_link)
                    __append_139882205643728('\n          to fix this.\n      ')
                    __msgid_139882205643728 = __re_whitespace(''.join(__stream_139882205643728)).strip()
                    if 'text_no_timezone_configured':
                        __append(translate('text_no_timezone_configured', mapping={'label_mail_event_settings_link': __stream_139882099987552_label_mail_event_settings_link, }, default=__msgid_139882205643728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38dd2d9b70> name=None at 7f38dd31fdf0> -> __attrs_139882205855408
                __attrs_139882205855408 = _static_139882205649776

                # <Value 'not:view/pil' (87:23)> -> __condition
                __token = 3241
                try:
                    __zt_tmp = __attrs_139882205855408
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('not', 'view/pil', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205850512
                    __attrs_139882205850512 = _static_139882337226896

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139882205853536 = []
                    __append_139882205853536 = __stream_139882205853536.append
                    __append_139882205853536('\n          Warning\n      ')
                    __msgid_139882205853536 = __re_whitespace(''.join(__stream_139882205853536)).strip()
                    if __msgid_139882205853536:
                        __append(translate(__msgid_139882205853536, mapping=None, default=__msgid_139882205853536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205847632
                    __attrs_139882205847632 = _static_139882337226896
                    __stream_139882205851376 = []
                    __append_139882205851376 = __stream_139882205851376.append
                    __append_139882205851376('\n          PIL is not installed properly, image scaling will not work.\n      ')
                    __msgid_139882205851376 = __re_whitespace(''.join(__stream_139882205851376)).strip()
                    if 'text_no_pil_installed':
                        __append(translate('text_no_pil_installed', mapping=None, default=__msgid_139882205851376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205847728
                __attrs_139882205847728 = _static_139882337226896
                __backup_category_139882206069472 = get('category', __marker)

                # <Value 'view/categories' (96:37)> -> __iterator
                __token = 3522
                try:
                    __zt_tmp = __attrs_139882205847728
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139882257081264('path', 'view/categories', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                (__iterator, ____index_139882205851280, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205846000
                    __attrs_139882205846000 = _static_139882337226896
                    __backup_sublist_139882206069424 = get('sublist', __marker)

                    # <Value "python:view.sublists(category.get('id'))" (97:34)> -> __value
                    __token = 3574
                    try:
                        __zt_tmp = __attrs_139882205846000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139882257081264('python', "view.sublists(category.get('id'))", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    econtext['sublist'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f38dd308f70> name=None at 7f38dd309000> -> __attrs_139882205842736
                    __attrs_139882205842736 = _static_139882205843312

                    # <Value 'sublist' (98:63)> -> __condition
                    __token = 3680
                    try:
                        __zt_tmp = __attrs_139882205842736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('path', 'sublist', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append('<section class="controlPanelSection mb-4">\n        ')

                        # <Static value=<ast.Dict object at 0x7f38dd309cc0> name=None at 7f38dd309ab0> -> __attrs_139882205844080
                        __attrs_139882205844080 = _static_139882205846720

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3 class="">')

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205841632
                        __default_139882205841632 = _DEFAULT_MARKER

                        # <Value 'category/title' (99:34)> -> __cache_139882205852144
                        __token = 3724
                        try:
                            __zt_tmp = __attrs_139882205844080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882205852144 = _static_139882257081264('path', 'category/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'category/title' (99:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd30a260> -> __condition
                        __expression = __cache_139882205852144

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Category')
                        else:
                            __content = __cache_139882205852144
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</h3>\n\n        ')

                        # <Static value=<ast.Dict object at 0x7f38dd30ada0> name=None at 7f38dd308b20> -> __attrs_139882205852432
                        __attrs_139882205852432 = _static_139882205851040

                        # <Value 'sublist' (102:40)> -> __condition
                        __token = 3823
                        try:
                            __zt_tmp = __attrs_139882205852432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('path', 'sublist', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:

                            # <nav ... (0:0)
                            # --------------------------------------------------------
                            __append('<nav class="row">\n\n          ')

                            # <Static value=<ast.Dict object at 0x7f38dd328dc0> name=None at 7f38dd329e40> -> __attrs_139882206046640
                            __attrs_139882206046640 = _static_139882205973952

                            # <Value 'sublist' (105:29)> -> __condition
                            __token = 3978
                            try:
                                __zt_tmp = __attrs_139882206046640
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139882257081264('path', 'sublist', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            if __condition:

                                # <ul ... (0:0)
                                # --------------------------------------------------------
                                __append('<ul class="configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100">\n            ')

                                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206037472
                                __attrs_139882206037472 = _static_139882337226896
                                __backup_action_139882206038288 = get('action', __marker)

                                # <Value 'sublist' (106:44)> -> __iterator
                                __token = 4032
                                try:
                                    __zt_tmp = __attrs_139882206037472
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_139882257081264('path', 'sublist', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                (__iterator, ____index_139882217083024, ) = getname('repeat')('action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item
                                    __append('\n              ')

                                    # <Static value=<ast.Dict object at 0x7f38dd5242e0> name=None at 7f38dd527be0> -> __attrs_139882208493728
                                    __attrs_139882208493728 = _static_139882208051936

                                    # <Value 'action/visible' (107:50)> -> __condition
                                    __token = 4092
                                    try:
                                        __zt_tmp = __attrs_139882208493728
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_139882257081264('path', 'action/visible', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                    if __condition:

                                        # <li ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<li class="col mb-4">\n                ')

                                        # <Static value=<ast.Dict object at 0x7f38dda8f4f0> name=None at 7f38ddbe6860> -> __attrs_139882238615248
                                        __attrs_139882238615248 = _static_139882213733616
                                        __backup_icon_139882239380112 = get('icon', __marker)

                                        # <Value 'action/icon' (109:37)> -> __value
                                        __token = 4244
                                        try:
                                            __zt_tmp = __attrs_139882238615248
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_139882257081264('path', 'action/icon', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                        econtext['icon'] = __value
                                        __backup_icon_url_139882215131744 = get('icon_url', __marker)

                                        # <Value "python:'http' in action['icon']" (110:40)> -> __value
                                        __token = 4297
                                        try:
                                            __zt_tmp = __attrs_139882238615248
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_139882257081264('python', "'http' in action['icon']", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                        econtext['icon_url'] = __value

                                        # <a ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<a')

                                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882213725408
                                        __default_139882213725408 = _DEFAULT_MARKER

                                        # <Substitution 'action/url' (111:41)> -> __attr_href
                                        __token = 4372
                                        try:
                                            __zt_tmp = __attrs_139882238615248
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_href = _static_139882257081264('path', 'action/url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_href is not None):
                                            __append((' href="%s"' % __attr_href))
                                        __append(' class="d-block text-dark text-center py-4 rounded btn btn-light h-100">\n                    ')

                                        # <Static value=<ast.Dict object at 0x7f38dde5acb0> name=None at 7f38df28a380> -> __attrs_139882101063984
                                        __attrs_139882101063984 = _static_139882217712816

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="mb-3">\n                      ')

                                        # <Static value=<ast.Dict object at 0x7f38d6f1c5e0> name=None at 7f38d6f1c3a0> -> __attrs_139882101072960
                                        __attrs_139882101072960 = _static_139882101065184

                                        # <Value 'icon_url' (113:42)> -> __condition
                                        __token = 4466
                                        try:
                                            __zt_tmp = __attrs_139882101072960
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_139882257081264('path', 'icon_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                        if __condition:

                                            # <img ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<img')

                                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101071136
                                            __default_139882101071136 = _DEFAULT_MARKER

                                            # <Substitution 'action/icon' (115:44)> -> __attr_src
                                            __token = 4571
                                            try:
                                                __zt_tmp = __attrs_139882101072960
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_src = _static_139882257081264('path', 'action/icon', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                            __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                            if (__attr_src is not None):
                                                __append((' src="%s"' % __attr_src))

                                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101077376
                                            __default_139882101077376 = _DEFAULT_MARKER

                                            # <Translate msgid=None node=<Substitution 'action/title' (116:43)> at 7f38d6f1da50> -> __attr_alt

                                            # <Substitution 'action/title' (116:43)> -> __attr_alt
                                            __token = 4627
                                            try:
                                                __zt_tmp = __attrs_139882101072960
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_alt = _static_139882257081264('path', 'action/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            if (__attr_alt is not None):
                                                __append((' alt="%s"' % __attr_alt))
                                            __append(' class="icon">')
                                        __append('\n                      ')

                                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205903072
                                        __attrs_139882205903072 = _static_139882337226896

                                        # <Value 'not: icon_url' (118:47)> -> __condition
                                        __token = 4736
                                        try:
                                            __zt_tmp = __attrs_139882205903072
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_139882257081264('not', ' icon_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                        if __condition:

                                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205891648
                                            __default_139882205891648 = _DEFAULT_MARKER

                                            # <Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> -> __cache_139882205889488
                                            __token = 4798
                                            try:
                                                __zt_tmp = __attrs_139882205903072
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __cache_139882205889488 = _static_139882257081264('python', "icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                            # <BinOp left=<Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd317d90> -> __condition
                                            __expression = __cache_139882205889488

                                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                            __value = _DEFAULT_MARKER
                                            __condition = (__expression is __value)
                                            if __condition:
                                                pass
                                            else:
                                                __content = __cache_139882205889488
                                                __content = __convert(__content)
                                                if (__content is not None):
                                                    __append(__content)
                                        __append('\n                    </div>\n                    ')

                                        # <Static value=<ast.Dict object at 0x7f38dd3151e0> name=None at 7f38dd315f30> -> __attrs_139882205892608
                                        __attrs_139882205892608 = _static_139882205893088

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="text-decoration-none text-center ">')

                                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205904752
                                        __default_139882205904752 = _DEFAULT_MARKER

                                        # <Value 'action/title' (121:38)> -> __cache_139882205904512
                                        __token = 4976
                                        try:
                                            __zt_tmp = __attrs_139882205892608
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_139882205904512 = _static_139882257081264('path', 'action/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                        # <BinOp left=<Value 'action/title' (121:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd314460> -> __condition
                                        __expression = __cache_139882205904512

                                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            __append('\n                        Title\n                    ')
                                        else:
                                            __content = __cache_139882205904512
                                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            __content = __quote(__content, None, '\xad', None, None)
                                            if (__content is not None):
                                                __append(__content)
                                        __append('</div>\n                </a>')
                                        if (__backup_icon_url_139882215131744 is __marker):
                                            del econtext['icon_url']
                                        else:
                                            econtext['icon_url'] = __backup_icon_url_139882215131744
                                        if (__backup_icon_139882239380112 is __marker):
                                            del econtext['icon']
                                        else:
                                            econtext['icon'] = __backup_icon_139882239380112
                                        __append('\n              </li>')
                                    __append('\n            ')
                                    ____index_139882217083024 -= 1
                                    if (____index_139882217083024 > 0):
                                        __append('')
                                if (__backup_action_139882206038288 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_139882206038288
                                __append('\n            </ul>')
                            __append('\n          </nav>')
                        __append('\n\n          ')

                        # <Static value=<ast.Dict object at 0x7f38ddbe79a0> name=None at 7f38dd807df0> -> __attrs_139882205904800
                        __attrs_139882205904800 = _static_139882215143840

                        # <Value 'not:sublist' (133:31)> -> __condition
                        __token = 5339
                        try:
                            __zt_tmp = __attrs_139882205904800
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('not', 'sublist', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="discreet">')
                            __stream_139882206051824 = []
                            __append_139882206051824 = __stream_139882206051824.append
                            __append_139882206051824('\n              No preference panels available.\n          ')
                            __msgid_139882206051824 = __re_whitespace(''.join(__stream_139882206051824)).strip()
                            if 'label_no_prefs_panels_available':
                                __append(translate('label_no_prefs_panels_available', mapping=None, default=__msgid_139882206051824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</div>')
                        __append('\n\n      </section>')
                    __append('\n    ')
                    if (__backup_sublist_139882206069424 is __marker):
                        del econtext['sublist']
                    else:
                        econtext['sublist'] = __backup_sublist_139882206069424
                    __append('\n  ')
                    ____index_139882205851280 -= 1
                    if (____index_139882205851280 > 0):
                        __append('')
                if (__backup_category_139882206069472 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_139882206069472
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38dd308cd0> name=None at 7f38dd30be50> -> __attrs_139882205900960
                __attrs_139882205900960 = _static_139882205842640

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="controlPanelSectionFooter">\n    ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205902400
                __attrs_139882205902400 = _static_139882337226896

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_139882205901536 = []
                __append_139882205901536 = __stream_139882205901536.append
                __append_139882205901536('Version Overview')
                __msgid_139882205901536 = __re_whitespace(''.join(__stream_139882205901536)).strip()
                if 'heading_version_overview':
                    __append(translate('heading_version_overview', mapping=None, default=__msgid_139882205901536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n    ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205896880
                __attrs_139882205896880 = _static_139882337226896

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n      ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205895680
                __attrs_139882205895680 = _static_139882337226896
                __backup_version_139882205624496 = get('version', __marker)

                # <Value 'view/version_overview' (145:41)> -> __iterator
                __token = 5702
                try:
                    __zt_tmp = __attrs_139882205895680
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139882257081264('path', 'view/version_overview', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                (__iterator, ____index_139882205902976, ) = getname('repeat')('version', __iterator)
                econtext['version'] = None
                for __item in __iterator:
                    econtext['version'] = __item
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206247328
                    __attrs_139882206247328 = _static_139882337226896

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205899472
                    __default_139882205899472 = _DEFAULT_MARKER

                    # <Value 'version' (146:25)> -> __cache_139882205898464
                    __token = 5751
                    try:
                        __zt_tmp = __attrs_139882206247328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882205898464 = _static_139882257081264('path', 'version', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'version' (146:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd317d00> -> __condition
                    __expression = __cache_139882205898464

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Version')
                    else:
                        __content = __cache_139882205898464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</li>\n      ')
                    ____index_139882205902976 -= 1
                    if (____index_139882205902976 > 0):
                        __append('')
                if (__backup_version_139882205624496 is __marker):
                    del econtext['version']
                else:
                    econtext['version'] = __backup_version_139882205624496
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206235520
                __attrs_139882206235520 = _static_139882337226896
                __backup_server_info_139882205623968 = get('server_info', __marker)

                # <Value 'view/server_info' (148:42)> -> __value
                __token = 5842
                try:
                    __zt_tmp = __attrs_139882206235520
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/server_info', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['server_info'] = __value
                __backup_has_wsgi_139882205618736 = get('has_wsgi', __marker)

                # <Value 'server_info/wsgi' (149:38)> -> __value
                __token = 5898
                try:
                    __zt_tmp = __attrs_139882206235520
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'server_info/wsgi', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['has_wsgi'] = __value
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206232880
                __attrs_139882206232880 = _static_139882337226896

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206234656
                __attrs_139882206234656 = _static_139882337226896
                __stream_139882206245984 = []
                __append_139882206245984 = __stream_139882206245984.append
                __append_139882206245984('WSGI:')
                __msgid_139882206245984 = __re_whitespace(''.join(__stream_139882206245984)).strip()
                if __msgid_139882206245984:
                    __append(translate(__msgid_139882206245984, mapping=None, default=__msgid_139882206245984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206248816
                __attrs_139882206248816 = _static_139882337226896

                # <Value 'has_wsgi' (152:51)> -> __condition
                __token = 6042
                try:
                    __zt_tmp = __attrs_139882206248816
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'has_wsgi', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139882206241760 = []
                    __append_139882206241760 = __stream_139882206241760.append
                    __append_139882206241760('On')
                    __msgid_139882206241760 = __re_whitespace(''.join(__stream_139882206241760)).strip()
                    if __msgid_139882206241760:
                        __append(translate(__msgid_139882206241760, mapping=None, default=__msgid_139882206241760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206243296
                __attrs_139882206243296 = _static_139882337226896

                # <Value 'not:has_wsgi' (153:51)> -> __condition
                __token = 6113
                try:
                    __zt_tmp = __attrs_139882206243296
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('not', 'has_wsgi', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139882206232832 = []
                    __append_139882206232832 = __stream_139882206232832.append
                    __append_139882206232832('Off')
                    __msgid_139882206232832 = __re_whitespace(''.join(__stream_139882206232832)).strip()
                    if __msgid_139882206232832:
                        __append(translate(__msgid_139882206232832, mapping=None, default=__msgid_139882206232832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n          </li>\n          ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206237152
                __attrs_139882206237152 = _static_139882337226896

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206246272
                __attrs_139882206246272 = _static_139882337226896
                __stream_139882206236240 = []
                __append_139882206236240 = __stream_139882206236240.append
                __append_139882206236240('Server:')
                __msgid_139882206236240 = __re_whitespace(''.join(__stream_139882206236240)).strip()
                if __msgid_139882206236240:
                    __append(translate(__msgid_139882206236240, mapping=None, default=__msgid_139882206236240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206238832
                __attrs_139882206238832 = _static_139882337226896

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/server_name}' (157:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd369570> -> __content_139882343851824
                __token = 6246
                __token = 6248
                try:
                    __zt_tmp = __attrs_139882206238832
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_139882343851824 = _static_139882257081264('path', 'server_info/server_name', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                __content_139882343851824 = __quote(__content_139882343851824, '\x00', '&#0;', None, None)
                __content_139882343851824 = __content_139882343851824
                if (__content_139882343851824 is None):
                    pass
                else:
                    if (__content_139882343851824 is None):
                        __content_139882343851824 = None
                    else:
                        __tt = type(__content_139882343851824)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139882343851824 = str(__content_139882343851824)
                        else:
                            if (__tt is bytes):
                                __content_139882343851824 = decode(__content_139882343851824)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139882343851824 = __content_139882343851824.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139882343851824)
                                        __content_139882343851824 = (str(__content_139882343851824) if (__content_139882343851824 is __converted) else __converted)
                                    else:
                                        __content_139882343851824 = __content_139882343851824()
                if (__content_139882343851824 is not None):
                    __append(__content_139882343851824)
                __append('</span>\n            ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206243200
                __attrs_139882206243200 = _static_139882337226896

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/version}' (158:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd36b820> -> __content_139882343851824
                __token = 6298
                __token = 6300
                try:
                    __zt_tmp = __attrs_139882206243200
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_139882343851824 = _static_139882257081264('path', 'server_info/version', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                __content_139882343851824 = __quote(__content_139882343851824, '\x00', '&#0;', None, None)
                __content_139882343851824 = __content_139882343851824
                if (__content_139882343851824 is None):
                    pass
                else:
                    if (__content_139882343851824 is None):
                        __content_139882343851824 = None
                    else:
                        __tt = type(__content_139882343851824)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139882343851824 = str(__content_139882343851824)
                        else:
                            if (__tt is bytes):
                                __content_139882343851824 = decode(__content_139882343851824)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139882343851824 = __content_139882343851824.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139882343851824)
                                        __content_139882343851824 = (str(__content_139882343851824) if (__content_139882343851824 is __converted) else __converted)
                                    else:
                                        __content_139882343851824 = __content_139882343851824()
                if (__content_139882343851824 is not None):
                    __append(__content_139882343851824)
                __append('</span>\n          </li>\n      ')
                if (__backup_has_wsgi_139882205618736 is __marker):
                    del econtext['has_wsgi']
                else:
                    econtext['has_wsgi'] = __backup_has_wsgi_139882205618736
                if (__backup_server_info_139882205623968 is __marker):
                    del econtext['server_info']
                else:
                    econtext['server_info'] = __backup_server_info_139882205623968
                __append('\n    </ul>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd369510> name=None at 7f38dd3681c0> -> __attrs_139882206241856
                __attrs_139882206241856 = _static_139882206237968

                # <Value 'not:view/is_dev_mode' (163:22)> -> __condition
                __token = 6397
                try:
                    __zt_tmp = __attrs_139882206241856
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('not', 'view/is_dev_mode', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_139882205892752 = []
                    __append_139882205892752 = __stream_139882205892752.append
                    __append_139882205892752('\n      You are running in "production mode". This is the preferred mode of\n      operation for a live Plone site, but means that some\n      configuration changes will not take effect until your server is\n      restarted or a product refreshed. If this is a development instance,\n      and you want to enable debug mode, stop the server, set \'debug-mode=on\'\n      in your buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_139882205892752 = __re_whitespace(''.join(__stream_139882205892752)).strip()
                    if 'description_production_mode':
                        __append(translate('description_production_mode', mapping=None, default=__msgid_139882205892752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd36b9d0> name=None at 7f38dd368880> -> __attrs_139882206156240
                __attrs_139882206156240 = _static_139882206247376

                # <Value 'view/is_dev_mode' (175:22)> -> __condition
                __token = 6969
                try:
                    __zt_tmp = __attrs_139882206156240
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'view/is_dev_mode', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_139882206248048 = []
                    __append_139882206248048 = __stream_139882206248048.append
                    __append_139882206248048('\n      You are running in "debug mode". This mode is intended for sites that\n      are under development. This allows many configuration changes to be\n      immediately visible, but will make your site run more slowly. To turn\n      off debug mode, stop the server, set \'debug-mode=off\' in your\n      buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_139882206248048 = __re_whitespace(''.join(__stream_139882206248048)).strip()
                    if 'description_debug_mode':
                        __append(translate('description_debug_mode', mapping=None, default=__msgid_139882206248048, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n  </section>\n\n</div>')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_139882206072400
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139882257081264('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139882238648640 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139882238648640
            __i18n_domain = __previous_i18n_domain_139882206080032
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }