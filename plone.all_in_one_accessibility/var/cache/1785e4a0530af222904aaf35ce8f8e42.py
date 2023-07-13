# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/controlpanel/browser/overview.pt'

__tokens = {421: ("python:request.set('disable_plone.leftcolumn',1)", 12, 47), 517: (" python:request.set('disable_plone.rightcolumn',1", 13, 46), 979: ('view/upgrade_warning', 26, 23), 1261: ('string:${context/portal_url}/@@plone-upgrade', 34, 35), 1644: ('view/mailhost_warning', 46, 23), 2215: ('string:${portal_url}/@@mail-controlpanel', 57, 39), 2449: ('view/timezone_warning', 66, 23), 2982: ('string:${portal_url}/@@dateandtime-controlpanel', 78, 39), 3241: ('not:view/pil', 87, 23), 3522: ('view/categories', 96, 37), 3574: ("python:view.sublists(category.get('id'))", 97, 34), 3680: ('sublist', 98, 63), 3724: ('category/title', 99, 34), 3823: ('sublist', 102, 40), 3978: ('sublist', 105, 29), 4032: ('sublist', 106, 44), 4092: ('action/visible', 107, 50), 4244: ('action/icon', 109, 37), 4297: (" python:'http' in action['icon'", 110, 40), 4372: ('action/url', 111, 41), 4466: ('icon_url', 113, 42), 4571: ('action/icon', 115, 44), 4627: (' action/titl', 116, 43), 4736: ('not: icon_url', 118, 47), 4798: ("python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", 119, 47), 4976: ('action/title', 121, 38), 5339: ('not:sublist', 133, 31), 5702: ('view/version_overview', 145, 41), 5751: ('version', 146, 25), 5842: ('view/server_info', 148, 42), 5898: (' server_info/wsg', 149, 38), 6042: ('has_wsgi', 152, 51), 6113: ('not:has_wsgi', 153, 51), 6246: ('${server_info/server_name}', 157, 18), 6248: ('server_info/server_name', 157, 20), 6298: ('${server_info/version}', 158, 18), 6300: ('server_info/version', 158, 20), 6397: ('not:view/is_dev_mode', 163, 22), 6969: ('view/is_dev_mode', 175, 22), 261: ('here/prefs_main_template/macros/master', 6, 23), 261: ('here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_139922407000912 = {'class': '', }
_static_139922407004032 = {'class': '', }
_static_139922407182912 = {'class': 'controlPanelSectionFooter', }
_static_139922407286976 = {'class': 'discreet', }
_static_139922407280544 = {'class': 'text-decoration-none text-center ', }
_static_139922407282368 = {'src': '', 'alt': '', 'class': 'icon', }
_static_139922407284480 = {'class': 'mb-3', }
_static_139922407283760 = {'href': '', 'class': 'd-block text-dark text-center py-4 rounded btn btn-light h-100', }
_static_139922407291968 = {'class': 'col mb-4', }
_static_139922407280736 = {'class': 'configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100', }
_static_139922407189104 = {'class': 'row', }
_static_139922407178592 = {'class': '', }
_static_139922407185360 = {'class': 'controlPanelSection mb-4', }
_static_139922407179504 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_139922407192176 = {'href': '', }
_static_139922406967472 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_139922406966320 = {'href': '', }
_static_139922406974240 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_139922406974624 = {'href': '#', 'title': 'Go to the upgrade page', }
_static_139922406966752 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_139922406978464 = {'class': 'lead', }
_static_139922406978896 = {'class': 'documentFirstHeading', }
_static_139922406672368 = {'class': 'controlPanel controlPanelOverview', }
_static_139922496189968 = __C2ZContextWrapper
_static_139922496190256 = __compile_zt_expr
_static_139922406677072 = 'master'
_static_139922496178928 = {}

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

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406674672
            __attrs_139922406674672 = _static_139922496178928
            __previous_i18n_domain_139922406673904 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139922477313984 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f4239589a50> name=None at 7f4239589a20> -> __value
            __value = _static_139922406677072
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406673232
                __attrs_139922406673232 = _static_139922496178928
                __backup_disable_column_one_139922406675488 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 421
                try:
                    __zt_tmp = __attrs_139922406673232
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139922496190256('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_139922406675632 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 517
                try:
                    __zt_tmp = __attrs_139922406673232
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139922496190256('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_139922406675632 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_139922406675632
                if (__backup_disable_column_one_139922406675488 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_139922406675488
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f42395887f0> name=None at 7f42395886a0> -> __attrs_139922406670976
                __attrs_139922406670976 = _static_139922406672368

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="controlPanel controlPanelOverview">\n  ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406977168
                __attrs_139922406977168 = _static_139922496178928

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n    ')

                # <Static value=<ast.Dict object at 0x7f42395d3550> name=None at 7f42395d3820> -> __attrs_139922406980000
                __attrs_139922406980000 = _static_139922406978896

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_139922406979424 = []
                __append_139922406979424 = __stream_139922406979424.append
                __append_139922406979424('Site Setup')
                __msgid_139922406979424 = __re_whitespace(''.join(__stream_139922406979424)).strip()
                if __msgid_139922406979424:
                    __append(translate(__msgid_139922406979424, mapping=None, default=__msgid_139922406979424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f42395d33a0> name=None at 7f42395d33d0> -> __attrs_139922406965312
                __attrs_139922406965312 = _static_139922406978464

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_139922406980624 = []
                __append_139922406980624 = __stream_139922406980624.append
                __append_139922406980624('\n        Configuration area for Plone and add-on Products.\n    ')
                __msgid_139922406980624 = __re_whitespace(''.join(__stream_139922406980624)).strip()
                if 'description_control_panel':
                    __append(translate('description_control_panel', mapping=None, default=__msgid_139922406980624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x7f42395d05e0> name=None at 7f42395d0580> -> __attrs_139922406977600
                __attrs_139922406977600 = _static_139922406966752

                # <Value 'view/upgrade_warning' (26:23)> -> __condition
                __token = 979
                try:
                    __zt_tmp = __attrs_139922406977600
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('path', 'view/upgrade_warning', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406977888
                    __attrs_139922406977888 = _static_139922496178928

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139922406977360 = []
                    __append_139922406977360 = __stream_139922406977360.append
                    __append_139922406977360('\n          Warning\n      ')
                    __msgid_139922406977360 = __re_whitespace(''.join(__stream_139922406977360)).strip()
                    if __msgid_139922406977360:
                        __append(translate(__msgid_139922406977360, mapping=None, default=__msgid_139922406977360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406969872
                    __attrs_139922406969872 = _static_139922496178928
                    __stream_139922408579904_link_continue_with_the_upgrade = ''
                    __stream_139922406976496 = []
                    __append_139922406976496 = __stream_139922406976496.append
                    __append_139922406976496('\n          The site configuration is outdated and needs to be\n          upgraded. Please\n          ')
                    __stream_139922408579904_link_continue_with_the_upgrade = []
                    __append_139922408579904_link_continue_with_the_upgrade = __stream_139922408579904_link_continue_with_the_upgrade.append

                    # <Static value=<ast.Dict object at 0x7f42395d24a0> name=None at 7f42395d1c30> -> __attrs_139922406975536
                    __attrs_139922406975536 = _static_139922406974624

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139922408579904_link_continue_with_the_upgrade('<a')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406968816
                    __default_139922406968816 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/portal_url}/@@plone-upgrade' (34:35)> -> __attr_href
                    __token = 1261
                    try:
                        __zt_tmp = __attrs_139922406975536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139922496190256('string', '${context/portal_url}/@@plone-upgrade', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139922408579904_link_continue_with_the_upgrade((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406975104
                    __default_139922406975104 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f42395d21d0> at 7f42395d2530> -> __attr_title
                    __attr_title = 'Go to the upgrade page'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append_139922408579904_link_continue_with_the_upgrade((' title="%s"' % __attr_title))
                    __append_139922408579904_link_continue_with_the_upgrade('>')
                    __stream_139922406973952 = []
                    __append_139922406973952 = __stream_139922406973952.append
                    __append_139922406973952('\n            continue with the upgrade\n          ')
                    __msgid_139922406973952 = __re_whitespace(''.join(__stream_139922406973952)).strip()
                    if __msgid_139922406973952:
                        __append_139922408579904_link_continue_with_the_upgrade(translate(__msgid_139922406973952, mapping=None, default=__msgid_139922406973952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_139922408579904_link_continue_with_the_upgrade('</a>')
                    __append_139922406976496('${link_continue_with_the_upgrade}')
                    __stream_139922408579904_link_continue_with_the_upgrade = ''.join(__stream_139922408579904_link_continue_with_the_upgrade)
                    __append_139922406976496('.\n      ')
                    __msgid_139922406976496 = __re_whitespace(''.join(__stream_139922406976496)).strip()
                    if __msgid_139922406976496:
                        __append(translate(__msgid_139922406976496, mapping={'link_continue_with_the_upgrade': __stream_139922408579904_link_continue_with_the_upgrade, }, default=__msgid_139922406976496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f42395d2320> name=None at 7f42395d22c0> -> __attrs_139922406975920
                __attrs_139922406975920 = _static_139922406974240

                # <Value 'view/mailhost_warning' (46:23)> -> __condition
                __token = 1644
                try:
                    __zt_tmp = __attrs_139922406975920
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('path', 'view/mailhost_warning', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406965648
                    __attrs_139922406965648 = _static_139922496178928

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139922406970544 = []
                    __append_139922406970544 = __stream_139922406970544.append
                    __append_139922406970544('\n          Warning\n      ')
                    __msgid_139922406970544 = __re_whitespace(''.join(__stream_139922406970544)).strip()
                    if __msgid_139922406970544:
                        __append(translate(__msgid_139922406970544, mapping=None, default=__msgid_139922406970544, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406971840
                    __attrs_139922406971840 = _static_139922496178928
                    __stream_139922408579904_label_mail_control_panel_link = ''
                    __stream_139922406971120 = []
                    __append_139922406971120 = __stream_139922406971120.append
                    __append_139922406971120("\n          You have not configured a mail host or a site 'From'\n          address, various features including contact forms, email\n          notification and password reset will not work. Go to the\n          ")
                    __stream_139922408579904_label_mail_control_panel_link = []
                    __append_139922408579904_label_mail_control_panel_link = __stream_139922408579904_label_mail_control_panel_link.append

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406969344
                    __attrs_139922406969344 = _static_139922496178928
                    __append_139922408579904_label_mail_control_panel_link('\n              ')

                    # <Static value=<ast.Dict object at 0x7f42395d0430> name=None at 7f42395d0400> -> __attrs_139922407191600
                    __attrs_139922407191600 = _static_139922406966320

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139922408579904_label_mail_control_panel_link('<a')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407192848
                    __default_139922407192848 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@mail-controlpanel' (57:39)> -> __attr_href
                    __token = 2215
                    try:
                        __zt_tmp = __attrs_139922407191600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139922496190256('string', '${portal_url}/@@mail-controlpanel', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139922408579904_label_mail_control_panel_link((' href="%s"' % __attr_href))
                    __append_139922408579904_label_mail_control_panel_link(' >')
                    __stream_139922406968000 = []
                    __append_139922406968000 = __stream_139922406968000.append
                    __append_139922406968000('Mail control panel')
                    __msgid_139922406968000 = __re_whitespace(''.join(__stream_139922406968000)).strip()
                    if 'text_no_mailhost_configured_control_panel_link':
                        __append_139922408579904_label_mail_control_panel_link(translate('text_no_mailhost_configured_control_panel_link', mapping=None, default=__msgid_139922406968000, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_139922408579904_label_mail_control_panel_link('</a>\n          ')
                    __append_139922406971120('${label_mail_control_panel_link}')
                    __stream_139922408579904_label_mail_control_panel_link = ''.join(__stream_139922408579904_label_mail_control_panel_link)
                    __append_139922406971120('\n          to fix this.\n      ')
                    __msgid_139922406971120 = __re_whitespace(''.join(__stream_139922406971120)).strip()
                    if 'text_no_mailhost_configured':
                        __append(translate('text_no_mailhost_configured', mapping={'label_mail_control_panel_link': __stream_139922408579904_label_mail_control_panel_link, }, default=__msgid_139922406971120, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f42395d08b0> name=None at 7f42395d0a00> -> __attrs_139922407186320
                __attrs_139922407186320 = _static_139922406967472

                # <Value 'view/timezone_warning' (66:23)> -> __condition
                __token = 2449
                try:
                    __zt_tmp = __attrs_139922407186320
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('path', 'view/timezone_warning', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407181424
                    __attrs_139922407181424 = _static_139922496178928

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139922407192560 = []
                    __append_139922407192560 = __stream_139922407192560.append
                    __append_139922407192560('\n          Warning\n      ')
                    __msgid_139922407192560 = __re_whitespace(''.join(__stream_139922407192560)).strip()
                    if __msgid_139922407192560:
                        __append(translate(__msgid_139922407192560, mapping=None, default=__msgid_139922407192560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407193472
                    __attrs_139922407193472 = _static_139922496178928
                    __stream_139922408579904_label_mail_event_settings_link = ''
                    __stream_139922407193280 = []
                    __append_139922407193280 = __stream_139922407193280.append
                    __append_139922407193280('\n\n          You have not set the portal timezone. Date/Time handling will not\n          work properly for timezone aware date/time values.\n          Go to the\n          ')
                    __stream_139922408579904_label_mail_event_settings_link = []
                    __append_139922408579904_label_mail_event_settings_link = __stream_139922408579904_label_mail_event_settings_link.append

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407194144
                    __attrs_139922407194144 = _static_139922496178928
                    __append_139922408579904_label_mail_event_settings_link('\n              ')

                    # <Static value=<ast.Dict object at 0x7f4239607670> name=None at 7f42396074c0> -> __attrs_139922407179024
                    __attrs_139922407179024 = _static_139922407192176

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139922408579904_label_mail_event_settings_link('<a')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407186560
                    __default_139922407186560 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@dateandtime-controlpanel' (78:39)> -> __attr_href
                    __token = 2982
                    try:
                        __zt_tmp = __attrs_139922407179024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139922496190256('string', '${portal_url}/@@dateandtime-controlpanel', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139922408579904_label_mail_event_settings_link((' href="%s"' % __attr_href))
                    __append_139922408579904_label_mail_event_settings_link(' >')
                    __stream_139922407192320 = []
                    __append_139922407192320 = __stream_139922407192320.append
                    __append_139922407192320('Date and Time Settings control panel')
                    __msgid_139922407192320 = __re_whitespace(''.join(__stream_139922407192320)).strip()
                    if 'text_no_timezone_configured_control_panel_link':
                        __append_139922408579904_label_mail_event_settings_link(translate('text_no_timezone_configured_control_panel_link', mapping=None, default=__msgid_139922407192320, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_139922408579904_label_mail_event_settings_link('</a>\n          ')
                    __append_139922407193280('${label_mail_event_settings_link}')
                    __stream_139922408579904_label_mail_event_settings_link = ''.join(__stream_139922408579904_label_mail_event_settings_link)
                    __append_139922407193280('\n          to fix this.\n      ')
                    __msgid_139922407193280 = __re_whitespace(''.join(__stream_139922407193280)).strip()
                    if 'text_no_timezone_configured':
                        __append(translate('text_no_timezone_configured', mapping={'label_mail_event_settings_link': __stream_139922408579904_label_mail_event_settings_link, }, default=__msgid_139922407193280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f42396044f0> name=None at 7f4239604820> -> __attrs_139922407179984
                __attrs_139922407179984 = _static_139922407179504

                # <Value 'not:view/pil' (87:23)> -> __condition
                __token = 3241
                try:
                    __zt_tmp = __attrs_139922407179984
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('not', 'view/pil', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407190352
                    __attrs_139922407190352 = _static_139922496178928

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139922407189824 = []
                    __append_139922407189824 = __stream_139922407189824.append
                    __append_139922407189824('\n          Warning\n      ')
                    __msgid_139922407189824 = __re_whitespace(''.join(__stream_139922407189824)).strip()
                    if __msgid_139922407189824:
                        __append(translate(__msgid_139922407189824, mapping=None, default=__msgid_139922407189824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407179072
                    __attrs_139922407179072 = _static_139922496178928
                    __stream_139922407181952 = []
                    __append_139922407181952 = __stream_139922407181952.append
                    __append_139922407181952('\n          PIL is not installed properly, image scaling will not work.\n      ')
                    __msgid_139922407181952 = __re_whitespace(''.join(__stream_139922407181952)).strip()
                    if 'text_no_pil_installed':
                        __append(translate('text_no_pil_installed', mapping=None, default=__msgid_139922407181952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407190928
                __attrs_139922407190928 = _static_139922496178928
                __backup_category_139922406674912 = get('category', __marker)

                # <Value 'view/categories' (96:37)> -> __iterator
                __token = 3522
                try:
                    __zt_tmp = __attrs_139922407190928
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139922496190256('path', 'view/categories', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                (__iterator, ____index_139922407180176, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407188624
                    __attrs_139922407188624 = _static_139922496178928
                    __backup_sublist_139922406974960 = get('sublist', __marker)

                    # <Value "python:view.sublists(category.get('id'))" (97:34)> -> __value
                    __token = 3574
                    try:
                        __zt_tmp = __attrs_139922407188624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139922496190256('python', "view.sublists(category.get('id'))", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    econtext['sublist'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f4239605bd0> name=None at 7f4239605de0> -> __attrs_139922407184304
                    __attrs_139922407184304 = _static_139922407185360

                    # <Value 'sublist' (98:63)> -> __condition
                    __token = 3680
                    try:
                        __zt_tmp = __attrs_139922407184304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139922496190256('path', 'sublist', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append('<section class="controlPanelSection mb-4">\n        ')

                        # <Static value=<ast.Dict object at 0x7f4239604160> name=None at 7f4239604fd0> -> __attrs_139922407183056
                        __attrs_139922407183056 = _static_139922407178592

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3 class="">')

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407183776
                        __default_139922407183776 = _DEFAULT_MARKER

                        # <Value 'category/title' (99:34)> -> __cache_139922407188096
                        __token = 3724
                        try:
                            __zt_tmp = __attrs_139922407183056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139922407188096 = _static_139922496190256('path', 'category/title', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                        # <BinOp left=<Value 'category/title' (99:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f4239605600> -> __condition
                        __expression = __cache_139922407188096

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Category')
                        else:
                            __content = __cache_139922407188096
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</h3>\n\n        ')

                        # <Static value=<ast.Dict object at 0x7f4239606a70> name=None at 7f4239606aa0> -> __attrs_139922407178928
                        __attrs_139922407178928 = _static_139922407189104

                        # <Value 'sublist' (102:40)> -> __condition
                        __token = 3823
                        try:
                            __zt_tmp = __attrs_139922407178928
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139922496190256('path', 'sublist', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        if __condition:

                            # <nav ... (0:0)
                            # --------------------------------------------------------
                            __append('<nav class="row">\n\n          ')

                            # <Static value=<ast.Dict object at 0x7f423961d060> name=None at 7f423961dcf0> -> __attrs_139922407291488
                            __attrs_139922407291488 = _static_139922407280736

                            # <Value 'sublist' (105:29)> -> __condition
                            __token = 3978
                            try:
                                __zt_tmp = __attrs_139922407291488
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('path', 'sublist', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <ul ... (0:0)
                                # --------------------------------------------------------
                                __append('<ul class="configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100">\n            ')

                                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407290672
                                __attrs_139922407290672 = _static_139922496178928
                                __backup_action_139922407289184 = get('action', __marker)

                                # <Value 'sublist' (106:44)> -> __iterator
                                __token = 4032
                                try:
                                    __zt_tmp = __attrs_139922407290672
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_139922496190256('path', 'sublist', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                (__iterator, ____index_139922407291392, ) = getname('repeat')('action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item
                                    __append('\n              ')

                                    # <Static value=<ast.Dict object at 0x7f423961fc40> name=None at 7f423961fd90> -> __attrs_139922407292688
                                    __attrs_139922407292688 = _static_139922407291968

                                    # <Value 'action/visible' (107:50)> -> __condition
                                    __token = 4092
                                    try:
                                        __zt_tmp = __attrs_139922407292688
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_139922496190256('path', 'action/visible', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    if __condition:

                                        # <li ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<li class="col mb-4">\n                ')

                                        # <Static value=<ast.Dict object at 0x7f423961dc30> name=None at 7f423961f520> -> __attrs_139922407287504
                                        __attrs_139922407287504 = _static_139922407283760
                                        __backup_icon_139922407291440 = get('icon', __marker)

                                        # <Value 'action/icon' (109:37)> -> __value
                                        __token = 4244
                                        try:
                                            __zt_tmp = __attrs_139922407287504
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_139922496190256('path', 'action/icon', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        econtext['icon'] = __value
                                        __backup_icon_url_139922407288560 = get('icon_url', __marker)

                                        # <Value "python:'http' in action['icon']" (110:40)> -> __value
                                        __token = 4297
                                        try:
                                            __zt_tmp = __attrs_139922407287504
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_139922496190256('python', "'http' in action['icon']", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        econtext['icon_url'] = __value

                                        # <a ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<a')

                                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407288176
                                        __default_139922407288176 = _DEFAULT_MARKER

                                        # <Substitution 'action/url' (111:41)> -> __attr_href
                                        __token = 4372
                                        try:
                                            __zt_tmp = __attrs_139922407287504
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_href = _static_139922496190256('path', 'action/url', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_href is not None):
                                            __append((' href="%s"' % __attr_href))
                                        __append(' class="d-block text-dark text-center py-4 rounded btn btn-light h-100">\n                    ')

                                        # <Static value=<ast.Dict object at 0x7f423961df00> name=None at 7f423961df60> -> __attrs_139922407285296
                                        __attrs_139922407285296 = _static_139922407284480

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="mb-3">\n                      ')

                                        # <Static value=<ast.Dict object at 0x7f423961d6c0> name=None at 7f423961d750> -> __attrs_139922407286352
                                        __attrs_139922407286352 = _static_139922407282368

                                        # <Value 'icon_url' (113:42)> -> __condition
                                        __token = 4466
                                        try:
                                            __zt_tmp = __attrs_139922407286352
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_139922496190256('path', 'icon_url', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        if __condition:

                                            # <img ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<img')

                                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407282272
                                            __default_139922407282272 = _DEFAULT_MARKER

                                            # <Substitution 'action/icon' (115:44)> -> __attr_src
                                            __token = 4571
                                            try:
                                                __zt_tmp = __attrs_139922407286352
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_src = _static_139922496190256('path', 'action/icon', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                            __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                            if (__attr_src is not None):
                                                __append((' src="%s"' % __attr_src))

                                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406643488
                                            __default_139922406643488 = _DEFAULT_MARKER

                                            # <Translate msgid=None node=<Substitution 'action/title' (116:43)> at 7f4239580b50> -> __attr_alt

                                            # <Substitution 'action/title' (116:43)> -> __attr_alt
                                            __token = 4627
                                            try:
                                                __zt_tmp = __attrs_139922407286352
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_alt = _static_139922496190256('path', 'action/title', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            if (__attr_alt is not None):
                                                __append((' alt="%s"' % __attr_alt))
                                            __append(' class="icon">')
                                        __append('\n                      ')

                                        # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407281504
                                        __attrs_139922407281504 = _static_139922496178928

                                        # <Value 'not: icon_url' (118:47)> -> __condition
                                        __token = 4736
                                        try:
                                            __zt_tmp = __attrs_139922407281504
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_139922496190256('not', ' icon_url', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        if __condition:

                                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407280304
                                            __default_139922407280304 = _DEFAULT_MARKER

                                            # <Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> -> __cache_139922407281984
                                            __token = 4798
                                            try:
                                                __zt_tmp = __attrs_139922407281504
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __cache_139922407281984 = _static_139922496190256('python', "icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                                            # <BinOp left=<Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f423961dde0> -> __condition
                                            __expression = __cache_139922407281984

                                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                                            __value = _DEFAULT_MARKER
                                            __condition = (__expression is __value)
                                            if __condition:
                                                pass
                                            else:
                                                __content = __cache_139922407281984
                                                __content = __convert(__content)
                                                if (__content is not None):
                                                    __append(__content)
                                        __append('\n                    </div>\n                    ')

                                        # <Static value=<ast.Dict object at 0x7f423961cfa0> name=None at 7f423961d300> -> __attrs_139922407279680
                                        __attrs_139922407279680 = _static_139922407280544

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="text-decoration-none text-center ">')

                                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407281072
                                        __default_139922407281072 = _DEFAULT_MARKER

                                        # <Value 'action/title' (121:38)> -> __cache_139922407280640
                                        __token = 4976
                                        try:
                                            __zt_tmp = __attrs_139922407279680
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_139922407280640 = _static_139922496190256('path', 'action/title', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                                        # <BinOp left=<Value 'action/title' (121:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f423961d450> -> __condition
                                        __expression = __cache_139922407280640

                                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            __append('\n                        Title\n                    ')
                                        else:
                                            __content = __cache_139922407280640
                                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            __content = __quote(__content, None, '\xad', None, None)
                                            if (__content is not None):
                                                __append(__content)
                                        __append('</div>\n                </a>')
                                        if (__backup_icon_url_139922407288560 is __marker):
                                            del econtext['icon_url']
                                        else:
                                            econtext['icon_url'] = __backup_icon_url_139922407288560
                                        if (__backup_icon_139922407291440 is __marker):
                                            del econtext['icon']
                                        else:
                                            econtext['icon'] = __backup_icon_139922407291440
                                        __append('\n              </li>')
                                    __append('\n            ')
                                    ____index_139922407291392 -= 1
                                    if (____index_139922407291392 > 0):
                                        __append('')
                                if (__backup_action_139922407289184 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_139922407289184
                                __append('\n            </ul>')
                            __append('\n          </nav>')
                        __append('\n\n          ')

                        # <Static value=<ast.Dict object at 0x7f423961e8c0> name=None at 7f423961da20> -> __attrs_139922407276800
                        __attrs_139922407276800 = _static_139922407286976

                        # <Value 'not:sublist' (133:31)> -> __condition
                        __token = 5339
                        try:
                            __zt_tmp = __attrs_139922407276800
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139922496190256('not', 'sublist', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="discreet">')
                            __stream_139922407290720 = []
                            __append_139922407290720 = __stream_139922407290720.append
                            __append_139922407290720('\n              No preference panels available.\n          ')
                            __msgid_139922407290720 = __re_whitespace(''.join(__stream_139922407290720)).strip()
                            if 'label_no_prefs_panels_available':
                                __append(translate('label_no_prefs_panels_available', mapping=None, default=__msgid_139922407290720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</div>')
                        __append('\n\n      </section>')
                    __append('\n    ')
                    if (__backup_sublist_139922406974960 is __marker):
                        del econtext['sublist']
                    else:
                        econtext['sublist'] = __backup_sublist_139922406974960
                    __append('\n  ')
                    ____index_139922407180176 -= 1
                    if (____index_139922407180176 > 0):
                        __append('')
                if (__backup_category_139922406674912 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_139922406674912
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f4239605240> name=None at 7f4239607220> -> __attrs_139922407285584
                __attrs_139922407285584 = _static_139922407182912

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="controlPanelSectionFooter">\n    ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407014016
                __attrs_139922407014016 = _static_139922496178928

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_139922407289856 = []
                __append_139922407289856 = __stream_139922407289856.append
                __append_139922407289856('Version Overview')
                __msgid_139922407289856 = __re_whitespace(''.join(__stream_139922407289856)).strip()
                if 'heading_version_overview':
                    __append(translate('heading_version_overview', mapping=None, default=__msgid_139922407289856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n    ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407001104
                __attrs_139922407001104 = _static_139922496178928

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n      ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406999376
                __attrs_139922406999376 = _static_139922496178928
                __backup_version_139922406980816 = get('version', __marker)

                # <Value 'view/version_overview' (145:41)> -> __iterator
                __token = 5702
                try:
                    __zt_tmp = __attrs_139922406999376
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139922496190256('path', 'view/version_overview', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                (__iterator, ____index_139922407012816, ) = getname('repeat')('version', __iterator)
                econtext['version'] = None
                for __item in __iterator:
                    econtext['version'] = __item
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407012768
                    __attrs_139922407012768 = _static_139922496178928

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407013056
                    __default_139922407013056 = _DEFAULT_MARKER

                    # <Value 'version' (146:25)> -> __cache_139922407004992
                    __token = 5751
                    try:
                        __zt_tmp = __attrs_139922407012768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139922407004992 = _static_139922496190256('path', 'version', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                    # <BinOp left=<Value 'version' (146:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42395dbbb0> -> __condition
                    __expression = __cache_139922407004992

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Version')
                    else:
                        __content = __cache_139922407004992
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</li>\n      ')
                    ____index_139922407012816 -= 1
                    if (____index_139922407012816 > 0):
                        __append('')
                if (__backup_version_139922406980816 is __marker):
                    del econtext['version']
                else:
                    econtext['version'] = __backup_version_139922406980816
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407014304
                __attrs_139922407014304 = _static_139922496178928
                __backup_server_info_139922406973376 = get('server_info', __marker)

                # <Value 'view/server_info' (148:42)> -> __value
                __token = 5842
                try:
                    __zt_tmp = __attrs_139922407014304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139922496190256('path', 'view/server_info', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                econtext['server_info'] = __value
                __backup_has_wsgi_139922406975440 = get('has_wsgi', __marker)

                # <Value 'server_info/wsgi' (149:38)> -> __value
                __token = 5898
                try:
                    __zt_tmp = __attrs_139922407014304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139922496190256('path', 'server_info/wsgi', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                econtext['has_wsgi'] = __value
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407009648
                __attrs_139922407009648 = _static_139922496178928

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406999424
                __attrs_139922406999424 = _static_139922496178928
                __stream_139922407010992 = []
                __append_139922407010992 = __stream_139922407010992.append
                __append_139922407010992('WSGI:')
                __msgid_139922407010992 = __re_whitespace(''.join(__stream_139922407010992)).strip()
                if __msgid_139922407010992:
                    __append(translate(__msgid_139922407010992, mapping=None, default=__msgid_139922407010992, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406998128
                __attrs_139922406998128 = _static_139922496178928

                # <Value 'has_wsgi' (152:51)> -> __condition
                __token = 6042
                try:
                    __zt_tmp = __attrs_139922406998128
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('path', 'has_wsgi', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139922407010800 = []
                    __append_139922407010800 = __stream_139922407010800.append
                    __append_139922407010800('On')
                    __msgid_139922407010800 = __re_whitespace(''.join(__stream_139922407010800)).strip()
                    if __msgid_139922407010800:
                        __append(translate(__msgid_139922407010800, mapping=None, default=__msgid_139922407010800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407000864
                __attrs_139922407000864 = _static_139922496178928

                # <Value 'not:has_wsgi' (153:51)> -> __condition
                __token = 6113
                try:
                    __zt_tmp = __attrs_139922407000864
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('not', 'has_wsgi', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139922407011760 = []
                    __append_139922407011760 = __stream_139922407011760.append
                    __append_139922407011760('Off')
                    __msgid_139922407011760 = __re_whitespace(''.join(__stream_139922407011760)).strip()
                    if __msgid_139922407011760:
                        __append(translate(__msgid_139922407011760, mapping=None, default=__msgid_139922407011760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n          </li>\n          ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407007104
                __attrs_139922407007104 = _static_139922496178928

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407003552
                __attrs_139922407003552 = _static_139922496178928
                __stream_139922407003024 = []
                __append_139922407003024 = __stream_139922407003024.append
                __append_139922407003024('Server:')
                __msgid_139922407003024 = __re_whitespace(''.join(__stream_139922407003024)).strip()
                if __msgid_139922407003024:
                    __append(translate(__msgid_139922407003024, mapping=None, default=__msgid_139922407003024, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406998080
                __attrs_139922406998080 = _static_139922496178928

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/server_name}' (157:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f42395d8970> -> __content_139922583708144
                __token = 6246
                __token = 6248
                try:
                    __zt_tmp = __attrs_139922406998080
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_139922583708144 = _static_139922496190256('path', 'server_info/server_name', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                __content_139922583708144 = __quote(__content_139922583708144, '\x00', '&#0;', None, None)
                __content_139922583708144 = __content_139922583708144
                if (__content_139922583708144 is None):
                    pass
                else:
                    if (__content_139922583708144 is None):
                        __content_139922583708144 = None
                    else:
                        __tt = type(__content_139922583708144)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139922583708144 = str(__content_139922583708144)
                        else:
                            if (__tt is bytes):
                                __content_139922583708144 = decode(__content_139922583708144)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139922583708144 = __content_139922583708144.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139922583708144)
                                        __content_139922583708144 = (str(__content_139922583708144) if (__content_139922583708144 is __converted) else __converted)
                                    else:
                                        __content_139922583708144 = __content_139922583708144()
                if (__content_139922583708144 is not None):
                    __append(__content_139922583708144)
                __append('</span>\n            ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407005232
                __attrs_139922407005232 = _static_139922496178928

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/version}' (158:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f42395d9de0> -> __content_139922583708144
                __token = 6298
                __token = 6300
                try:
                    __zt_tmp = __attrs_139922407005232
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_139922583708144 = _static_139922496190256('path', 'server_info/version', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                __content_139922583708144 = __quote(__content_139922583708144, '\x00', '&#0;', None, None)
                __content_139922583708144 = __content_139922583708144
                if (__content_139922583708144 is None):
                    pass
                else:
                    if (__content_139922583708144 is None):
                        __content_139922583708144 = None
                    else:
                        __tt = type(__content_139922583708144)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139922583708144 = str(__content_139922583708144)
                        else:
                            if (__tt is bytes):
                                __content_139922583708144 = decode(__content_139922583708144)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139922583708144 = __content_139922583708144.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139922583708144)
                                        __content_139922583708144 = (str(__content_139922583708144) if (__content_139922583708144 is __converted) else __converted)
                                    else:
                                        __content_139922583708144 = __content_139922583708144()
                if (__content_139922583708144 is not None):
                    __append(__content_139922583708144)
                __append('</span>\n          </li>\n      ')
                if (__backup_has_wsgi_139922406975440 is __marker):
                    del econtext['has_wsgi']
                else:
                    econtext['has_wsgi'] = __backup_has_wsgi_139922406975440
                if (__backup_server_info_139922406973376 is __marker):
                    del econtext['server_info']
                else:
                    econtext['server_info'] = __backup_server_info_139922406973376
                __append('\n    </ul>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f42395d9780> name=None at 7f42395d9960> -> __attrs_139922407004272
                __attrs_139922407004272 = _static_139922407004032

                # <Value 'not:view/is_dev_mode' (163:22)> -> __condition
                __token = 6397
                try:
                    __zt_tmp = __attrs_139922407004272
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('not', 'view/is_dev_mode', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_139922407006720 = []
                    __append_139922407006720 = __stream_139922407006720.append
                    __append_139922407006720('\n      You are running in "production mode". This is the preferred mode of\n      operation for a live Plone site, but means that some\n      configuration changes will not take effect until your server is\n      restarted or a product refreshed. If this is a development instance,\n      and you want to enable debug mode, stop the server, set \'debug-mode=on\'\n      in your buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_139922407006720 = __re_whitespace(''.join(__stream_139922407006720)).strip()
                    if 'description_production_mode':
                        __append(translate('description_production_mode', mapping=None, default=__msgid_139922407006720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f42395d8b50> name=None at 7f42395d8be0> -> __attrs_139922407002496
                __attrs_139922407002496 = _static_139922407000912

                # <Value 'view/is_dev_mode' (175:22)> -> __condition
                __token = 6969
                try:
                    __zt_tmp = __attrs_139922407002496
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('path', 'view/is_dev_mode', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_139922406999328 = []
                    __append_139922406999328 = __stream_139922406999328.append
                    __append_139922406999328('\n      You are running in "debug mode". This mode is intended for sites that\n      are under development. This allows many configuration changes to be\n      immediately visible, but will make your site run more slowly. To turn\n      off debug mode, stop the server, set \'debug-mode=off\' in your\n      buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_139922406999328 = __re_whitespace(''.join(__stream_139922406999328)).strip()
                    if 'description_debug_mode':
                        __append(translate('description_debug_mode', mapping=None, default=__msgid_139922406999328, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n  </section>\n\n</div>')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_139922406674672
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139922496190256('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139922477313984 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139922477313984
            __i18n_domain = __previous_i18n_domain_139922406673904
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }