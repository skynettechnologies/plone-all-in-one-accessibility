# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.contentmenu-3.0.2-py3.10.egg/plone/app/contentmenu/contentmenu.pt'

__tokens = {64: ('view/menu', 2, 31), 106: (" python:context.restrictedTraverse('@@iconresolver'", 3, 31), 196: ('s view/toolbar_positi', 4, 36), 282: ('view/available', 6, 35), 374: ('menu', 9, 30), 426: ('menuItem/submenu', 11, 23), 469: (' menuItem/extra/i', 12, 25), 522: ("${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 14, 17), 524: ('menuItem/extra/li_class|nothing', 14, 19), 559: ("python:'dropend' if (submenu and toolbar_pos == 'side') else ''", 14, 54), 639: ('${menuItem/extra/id}', 15, 14), 641: ('menuItem/extra/id', 15, 16), 955: ('menuItem/extra/class | nothing', 24, 25), 1011: (" python:'label-%s' % state_class if state_class else '", 25, 24), 688: ("${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 18, 18), 690: ("python:'nav-link dropdown-toggle' if submenu else 'nav-link'", 18, 20), 779: ("${python:'false' if submenu else ''}", 19, 26), 781: ("python:'false' if submenu else ''", 19, 28), 1127: ("python:menuItem['action'] or 'javascript:void(0)'", 28, 18), 1196: (" python:'cursor: default;; pointer-events: none' if not menuItem['action'] else No", 29, 18), 1298: ('le menuItem/descript', 30, 16), 1426: ("python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", 35, 43), 1598: ('menuItem/title', 38, 31), 1734: ('${state_class}', 43, 25), 1736: ('state_class', 43, 27), 1781: ('menuItem/extra/stateTitle | nothing', 44, 31), 2010: ('submenu | nothing', 54, 27), 2109: ('${menuItem/title}', 58, 14), 2111: ('menuItem/title', 58, 16), 2179: ("python:toolbar_pos == 'top'", 59, 52), 2325: ('menuItem/extra/class | nothing', 62, 36), 2392: (" python:'label-%s' % state_class if state_class else '", 63, 35), 2483: ('e menuItem/extra/stateTitle|nothi', 64, 34), 2581: ('state_title', 66, 37), 2238: ('${state_class}', 60, 29), 2240: ('state_class', 60, 31), 2628: ('${state_title}', 68, 16), 2630: ('state_title', 68, 18), 2778: ('submenu', 73, 38), 2857: ('subMenuItem/extra/class | string:', 75, 37), 3002: ('subMenuItem/extra/separator|nothing', 78, 43), 3112: ('not:subMenuItem/action', 80, 43), 3231: ('is_separator', 83, 35), 3311: ('subMenuItem/title', 85, 48), 3581: ('not:is_separator', 92, 37), 3505: ('nav-link dropdown-item ${extra_class}', 91, 29), 3530: ('extra_class', 91, 54), 3668: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 94, 51), 3813: ('subMenuItem/title', 95, 48), 4131: ('subMenuItem/action', 104, 32), 4034: ('nav-link dropdown-item ${extra_class}', 102, 24), 4059: ('extra_class', 102, 49), 4209: ('subMenuItem/action', 106, 24), 4253: (' subMenuItem/descriptio', 107, 24), 4299: ('d subMenuItem/extra/id | nothi', 108, 20), 4370: ('al subMenuItem/extra/modal | noth', 109, 37), 4534: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 114, 49), 4678: ('subMenuItem/title', 116, 46), 4895: ('not:subMenuItem/action', 122, 37), 4842: ('${extra_class}', 121, 29), 4844: ('extra_class', 121, 31), 4985: ('subMenuItem/extra/id | nothing', 124, 27), 5102: ("python:'active' in extra_class", 127, 43), 5185: ("python:icons.tag('check')", 128, 51), 5280: ('subMenuItem/title', 130, 47)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310475893600 = {'class': '${extra_class}', 'id': 'subMenuItem/extra/id | nothing', }
_static_140310476026832 = {'class': 'nav-link dropdown-item ${extra_class}', 'href': '#', 'title': 'subMenuItem/description', 'id': 'subMenuItem/extra/id | nothing', 'data-pat-plone-modal': 'subMenuItem/extra/modal | nothing', }
_static_140310476024048 = {'class': 'nav-link dropdown-item ${extra_class}', }
_static_140310476027408 = {'class': 'dropdown-header', }
_static_140310475675376 = {'class': '${state_class}', }
_static_140310475675280 = {'class': 'dropdown-header', }
_static_140310475678400 = {'class': 'dropdown-menu', }
_static_140310475673168 = {'class': '${state_class}', }
_static_140310476131056 = {'class': 'toolbar-label', }
_static_140310476133360 = {'class': "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 'aria-expanded': "${python:'false' if submenu else ''}", 'href': '#', 'data-bs-offset': '0,0', 'data-bs-toggle': 'dropdown', 'style': "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None", 'title': 'menuItem/description', }
_static_140310476136432 = {'class': "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 'id': '${menuItem/extra/id}', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310566789392 = {}

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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476140896
            __attrs_140310476140896 = _static_140310566789392
            __backup_menu_140310475166320 = get('menu', __marker)

            # <Value 'view/menu' (2:31)> -> __value
            __token = 64
            try:
                __zt_tmp = __attrs_140310476140896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/menu', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['menu'] = __value
            __backup_icons_140310475162144 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (3:31)> -> __value
            __token = 106
            try:
                __zt_tmp = __attrs_140310476140896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_toolbar_pos_140310475171840 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (4:36)> -> __value
            __token = 196
            try:
                __zt_tmp = __attrs_140310476140896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/toolbar_position', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'view/available' (6:35)> -> __condition
            __token = 282
            try:
                __zt_tmp = __attrs_140310476140896
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'view/available', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140310476140128 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476139216
                __attrs_140310476139216 = _static_140310566789392
                __backup_menuItem_140310513282368 = get('menuItem', __marker)

                # <Value 'menu' (9:30)> -> __iterator
                __token = 374
                try:
                    __zt_tmp = __attrs_140310476139216
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140310567013776('path', 'menu', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                (__iterator, ____index_140310476138976, ) = getname('repeat')('menuItem', __iterator)
                econtext['menuItem'] = None
                for __item in __iterator:
                    econtext['menuItem'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476137968
                    __attrs_140310476137968 = _static_140310566789392
                    __backup_submenu_140310475850416 = get('submenu', __marker)

                    # <Value 'menuItem/submenu' (11:23)> -> __value
                    __token = 426
                    try:
                        __zt_tmp = __attrs_140310476137968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('path', 'menuItem/submenu', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['submenu'] = __value
                    __backup_identifier_140310475822784 = get('identifier', __marker)

                    # <Value 'menuItem/extra/id' (12:25)> -> __value
                    __token = 469
                    try:
                        __zt_tmp = __attrs_140310476137968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('path', 'menuItem/extra/id', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['identifier'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f9c94169ff0> name=None at 7f9c94169fc0> -> __attrs_140310476135616
                    __attrs_140310476135616 = _static_140310476136432

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476136960
                    __default_140310476136960 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}" (14:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9416a170> -> __attr_class
                    __token = 522
                    __token = 524
                    try:
                        __zt_tmp = __attrs_140310476135616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140310567013776('path', 'menuItem/extra/li_class|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 559
                    try:
                        __zt_tmp = __attrs_140310476135616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_557 = _static_140310567013776('python', "'dropend' if (submenu and toolbar_pos == 'side') else ''", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_class_557 = __quote(__attr_class_557, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s%s' % ((__attr_class if (__attr_class is not None) else ''), ' ', (__attr_class_557 if (__attr_class_557 is not None) else ''), ))
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476136144
                    __default_140310476136144 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${menuItem/extra/id}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c94169f60> -> __attr_id
                    __token = 639
                    __token = 641
                    try:
                        __zt_tmp = __attrs_140310476135616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140310567013776('path', 'menuItem/extra/id', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_id = __attr_id
                    if (__attr_id is None):
                        pass
                    else:
                        if (__attr_id is _DEFAULT_MARKER):
                            __attr_id = None
                        else:
                            __tt = type(__attr_id)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_id = str(__attr_id)
                            else:
                                if (__tt is bytes):
                                    __attr_id = decode(__attr_id)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_id = __attr_id.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_id)
                                            __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                        else:
                                            __attr_id = __attr_id()
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n\n        ')

                    # <Static value=<ast.Dict object at 0x7f9c941693f0> name=None at 7f9c941693c0> -> __attrs_140310476131584
                    __attrs_140310476131584 = _static_140310476133360
                    __backup_state_class_140310475167136 = get('state_class', __marker)

                    # <Value 'menuItem/extra/class | nothing' (24:25)> -> __value
                    __token = 955
                    try:
                        __zt_tmp = __attrs_140310476131584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['state_class'] = __value
                    __backup_state_class_140310475817168 = get('state_class', __marker)

                    # <Value "python:'label-%s' % state_class if state_class else ''" (25:24)> -> __value
                    __token = 1011
                    try:
                        __zt_tmp = __attrs_140310476131584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['state_class'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476133216
                    __default_140310476133216 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c941696f0> -> __attr_class
                    __token = 688
                    __token = 690
                    try:
                        __zt_tmp = __attrs_140310476131584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140310567013776('python', "'nav-link dropdown-toggle' if submenu else 'nav-link'", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = __attr_class
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476134656
                    __default_140310476134656 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'false' if submenu else ''}" (19:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c94169840> -> __attr_aria_expanded
                    __token = 779
                    __token = 781
                    try:
                        __zt_tmp = __attrs_140310476131584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_aria_expanded = _static_140310567013776('python', "'false' if submenu else ''", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_aria_expanded = __quote(__attr_aria_expanded, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_aria_expanded = __attr_aria_expanded
                    if (__attr_aria_expanded is None):
                        pass
                    else:
                        if (__attr_aria_expanded is _DEFAULT_MARKER):
                            __attr_aria_expanded = None
                        else:
                            __tt = type(__attr_aria_expanded)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_aria_expanded = str(__attr_aria_expanded)
                            else:
                                if (__tt is bytes):
                                    __attr_aria_expanded = decode(__attr_aria_expanded)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_aria_expanded = __attr_aria_expanded.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_aria_expanded)
                                            __attr_aria_expanded = (str(__attr_aria_expanded) if (__attr_aria_expanded is __converted) else __converted)
                                        else:
                                            __attr_aria_expanded = __attr_aria_expanded()
                    if (__attr_aria_expanded is not None):
                        __append((' aria-expanded="%s"' % __attr_aria_expanded))

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476133120
                    __default_140310476133120 = _DEFAULT_MARKER

                    # <Substitution "python:menuItem['action'] or 'javascript:void(0)'" (28:18)> -> __attr_href
                    __token = 1127
                    try:
                        __zt_tmp = __attrs_140310476131584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140310567013776('python', "menuItem['action'] or 'javascript:void(0)'", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' data-bs-offset="0,0" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476132496
                    __default_140310476132496 = _DEFAULT_MARKER

                    # <Substitution "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None" (29:18)> -> __attr_style
                    __token = 1196
                    try:
                        __zt_tmp = __attrs_140310476131584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_140310567013776('python', "'cursor: default; pointer-events: none' if not menuItem['action'] else None", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((' style="%s"' % __attr_style))

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476132064
                    __default_140310476132064 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution 'menuItem/description' (30:16)> at 7f9c94168f70> -> __attr_title

                    # <Substitution 'menuItem/description' (30:16)> -> __attr_title
                    __token = 1298
                    try:
                        __zt_tmp = __attrs_140310476131584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140310567013776('path', 'menuItem/description', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476130336
                    __attrs_140310476130336 = _static_140310566789392

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476129232
                    __default_140310476129232 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (35:43)> -> __cache_140310476128800
                    __token = 1426
                    try:
                        __zt_tmp = __attrs_140310476130336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310476128800 = _static_140310567013776('python', "icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (35:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c941681c0> -> __condition
                    __expression = __cache_140310476128800

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310476128800
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f9c94168af0> name=None at 7f9c94168ac0> -> __attrs_140310476130912
                    __attrs_140310476130912 = _static_140310476131056

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label">\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475685648
                    __attrs_140310475685648 = _static_140310566789392

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475685024
                    __default_140310475685024 = _DEFAULT_MARKER

                    # <Value 'menuItem/title' (38:31)> -> __cache_140310475670384
                    __token = 1598
                    try:
                        __zt_tmp = __attrs_140310475685648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475670384 = _static_140310567013776('path', 'menuItem/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/title' (38:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c940f9120> -> __condition
                    __expression = __cache_140310475670384

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n              Menu Title\n            </span>')
                    else:
                        __content = __cache_140310475670384
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c940f8e50> name=None at 7f9c940f94e0> -> __attrs_140310475675232
                    __attrs_140310475675232 = _static_140310475673168

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475670000
                    __default_140310475670000 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${state_class}' (43:25)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c940f8eb0> -> __attr_class
                    __token = 1734
                    __token = 1736
                    try:
                        __zt_tmp = __attrs_140310475675232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140310567013776('path', 'state_class', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = __attr_class
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475673648
                    __default_140310475673648 = _DEFAULT_MARKER

                    # <Value 'menuItem/extra/stateTitle | nothing' (44:31)> -> __cache_140310475672880
                    __token = 1781
                    try:
                        __zt_tmp = __attrs_140310475675232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475672880 = _static_140310567013776('path', 'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/extra/stateTitle | nothing' (44:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c940f9090> -> __condition
                    __expression = __cache_140310475672880

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                State title\n            ')
                    else:
                        __content = __cache_140310475672880
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n          </span>\n\n        </a>')
                    if (__backup_state_class_140310475817168 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140310475817168
                    if (__backup_state_class_140310475167136 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140310475167136
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x7f9c940fa2c0> name=None at 7f9c940fa1a0> -> __attrs_140310475676000
                    __attrs_140310475676000 = _static_140310475678400

                    # <Value 'submenu | nothing' (54:27)> -> __condition
                    __token = 2010
                    try:
                        __zt_tmp = __attrs_140310475676000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140310567013776('path', 'submenu | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    if __condition:

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="dropdown-menu" >\n          ')

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475677392
                        __attrs_140310475677392 = _static_140310566789392

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n            ')

                        # <Static value=<ast.Dict object at 0x7f9c940f9690> name=None at 7f9c940f9ba0> -> __attrs_140310475674560
                        __attrs_140310475674560 = _static_140310475675280

                        # <h6 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h6 class="dropdown-header">')

                        # <Interpolation value=<Substitution '\n              ${menuItem/title}\n              ' (57:40)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c940f8130> -> __content_140310653968752
                        __token = 2109
                        __token = 2111
                        try:
                            __zt_tmp = __attrs_140310475674560
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_140310653968752 = _static_140310567013776('path', 'menuItem/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        __content_140310653968752 = __quote(__content_140310653968752, '\x00', '&#0;', None, None)
                        __content_140310653968752 = ('%s%s%s' % ('\n              ', (__content_140310653968752 if (__content_140310653968752 is not None) else ''), '\n              ', ))
                        if (__content_140310653968752 is None):
                            pass
                        else:
                            if (__content_140310653968752 is None):
                                __content_140310653968752 = None
                            else:
                                __tt = type(__content_140310653968752)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_140310653968752 = str(__content_140310653968752)
                                else:
                                    if (__tt is bytes):
                                        __content_140310653968752 = decode(__content_140310653968752)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_140310653968752 = __content_140310653968752.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_140310653968752)
                                                __content_140310653968752 = (str(__content_140310653968752) if (__content_140310653968752 is __converted) else __converted)
                                            else:
                                                __content_140310653968752 = __content_140310653968752()
                        if (__content_140310653968752 is not None):
                            __append(__content_140310653968752)

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475670096
                        __attrs_140310475670096 = _static_140310566789392

                        # <Value "python:toolbar_pos == 'top'" (59:52)> -> __condition
                        __token = 2179
                        try:
                            __zt_tmp = __attrs_140310475670096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140310567013776('python', "toolbar_pos == 'top'", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        if __condition:
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x7f9c940f96f0> name=None at 7f9c940f9870> -> __attrs_140310476028176
                            __attrs_140310476028176 = _static_140310475675376
                            __backup_state_class_140310475408672 = get('state_class', __marker)

                            # <Value 'menuItem/extra/class | nothing' (62:36)> -> __value
                            __token = 2325
                            try:
                                __zt_tmp = __attrs_140310476028176
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140310567013776('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            econtext['state_class'] = __value
                            __backup_state_class_140310475507600 = get('state_class', __marker)

                            # <Value "python:'label-%s' % state_class if state_class else ''" (63:35)> -> __value
                            __token = 2392
                            try:
                                __zt_tmp = __attrs_140310476028176
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140310567013776('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            econtext['state_class'] = __value
                            __backup_state_title_140310475823504 = get('state_title', __marker)

                            # <Value 'menuItem/extra/stateTitle|nothing' (64:34)> -> __value
                            __token = 2483
                            try:
                                __zt_tmp = __attrs_140310476028176
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140310567013776('path', 'menuItem/extra/stateTitle|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            econtext['state_title'] = __value

                            # <Value 'state_title' (66:37)> -> __condition
                            __token = 2581
                            try:
                                __zt_tmp = __attrs_140310476028176
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140310567013776('path', 'state_title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span')

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475672688
                                __default_140310475672688 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution '${state_class}' (60:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c940f8880> -> __attr_class
                                __token = 2238
                                __token = 2240
                                try:
                                    __zt_tmp = __attrs_140310476028176
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140310567013776('path', 'state_class', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_class = __attr_class
                                if (__attr_class is None):
                                    pass
                                else:
                                    if (__attr_class is _DEFAULT_MARKER):
                                        __attr_class = None
                                    else:
                                        __tt = type(__attr_class)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __attr_class = str(__attr_class)
                                        else:
                                            if (__tt is bytes):
                                                __attr_class = decode(__attr_class)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __attr_class = __attr_class.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__attr_class)
                                                        __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                    else:
                                                        __attr_class = __attr_class()
                                if (__attr_class is not None):
                                    __append((' class="%s"' % __attr_class))
                                __append(' >')

                                # <Interpolation value=<Substitution '\n                ${state_title}\n                ' (67:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9414c970> -> __content_140310653968752
                                __token = 2628
                                __token = 2630
                                try:
                                    __zt_tmp = __attrs_140310476028176
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_140310653968752 = _static_140310567013776('path', 'state_title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                __content_140310653968752 = __quote(__content_140310653968752, '\x00', '&#0;', None, None)
                                __content_140310653968752 = ('%s%s%s' % ('\n                ', (__content_140310653968752 if (__content_140310653968752 is not None) else ''), '\n                ', ))
                                if (__content_140310653968752 is None):
                                    pass
                                else:
                                    if (__content_140310653968752 is None):
                                        __content_140310653968752 = None
                                    else:
                                        __tt = type(__content_140310653968752)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_140310653968752 = str(__content_140310653968752)
                                        else:
                                            if (__tt is bytes):
                                                __content_140310653968752 = decode(__content_140310653968752)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_140310653968752 = __content_140310653968752.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_140310653968752)
                                                        __content_140310653968752 = (str(__content_140310653968752) if (__content_140310653968752 is __converted) else __converted)
                                                    else:
                                                        __content_140310653968752 = __content_140310653968752()
                                if (__content_140310653968752 is not None):
                                    __append(__content_140310653968752)
                                __append('</span>')
                            if (__backup_state_title_140310475823504 is __marker):
                                del econtext['state_title']
                            else:
                                econtext['state_title'] = __backup_state_title_140310475823504
                            if (__backup_state_class_140310475507600 is __marker):
                                del econtext['state_class']
                            else:
                                econtext['state_class'] = __backup_state_class_140310475507600
                            if (__backup_state_class_140310475408672 is __marker):
                                del econtext['state_class']
                            else:
                                econtext['state_class'] = __backup_state_class_140310475408672
                            __append('\n              ')
                        __append('\n            </h6>\n          </li>\n          ')

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476015456
                        __attrs_140310476015456 = _static_140310566789392
                        __backup_subMenuItem_140310476958848 = get('subMenuItem', __marker)

                        # <Value 'submenu' (73:38)> -> __iterator
                        __token = 2778
                        try:
                            __zt_tmp = __attrs_140310476015456
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140310567013776('path', 'submenu', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        (__iterator, ____index_140310476014688, ) = getname('repeat')('subMenuItem', __iterator)
                        econtext['subMenuItem'] = None
                        for __item in __iterator:
                            econtext['subMenuItem'] = __item

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li>\n            ')

                            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476024384
                            __attrs_140310476024384 = _static_140310566789392
                            __backup_extra_class_140310475513360 = get('extra_class', __marker)

                            # <Value 'subMenuItem/extra/class | string:' (75:37)> -> __value
                            __token = 2857
                            try:
                                __zt_tmp = __attrs_140310476024384
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140310567013776('path', 'subMenuItem/extra/class | string:', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            econtext['extra_class'] = __value
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476016608
                            __attrs_140310476016608 = _static_140310566789392
                            __backup_is_separator_140310475820192 = get('is_separator', __marker)

                            # <Value 'subMenuItem/extra/separator|nothing' (78:43)> -> __value
                            __token = 3002
                            try:
                                __zt_tmp = __attrs_140310476016608
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140310567013776('path', 'subMenuItem/extra/separator|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            econtext['is_separator'] = __value

                            # <Value 'not:subMenuItem/action' (80:43)> -> __condition
                            __token = 3112
                            try:
                                __zt_tmp = __attrs_140310476016608
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140310567013776('not', 'subMenuItem/action', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            if __condition:
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7f9c9414f610> name=None at 7f9c9414d6f0> -> __attrs_140310476020208
                                __attrs_140310476020208 = _static_140310476027408

                                # <Value 'is_separator' (83:35)> -> __condition
                                __token = 3231
                                try:
                                    __zt_tmp = __attrs_140310476020208
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140310567013776('path', 'is_separator', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                if __condition:

                                    # <h6 ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<h6 class="dropdown-header" >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476014928
                                    __attrs_140310476014928 = _static_140310566789392

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476027648
                                    __default_140310476027648 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (85:48)> -> __cache_140310476024960
                                    __token = 3311
                                    try:
                                        __zt_tmp = __attrs_140310476014928
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140310476024960 = _static_140310567013776('path', 'subMenuItem/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (85:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9414e3b0> -> __condition
                                    __expression = __cache_140310476024960

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append('\n                    Title\n                  ')
                                    else:
                                        __content = __cache_140310476024960
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </h6>')
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7f9c9414e8f0> name=None at 7f9c9414fac0> -> __attrs_140310476021696
                                __attrs_140310476021696 = _static_140310476024048

                                # <Value 'not:is_separator' (92:37)> -> __condition
                                __token = 3581
                                try:
                                    __zt_tmp = __attrs_140310476021696
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140310567013776('not', 'is_separator', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476025056
                                    __default_140310476025056 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (91:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9414c610> -> __attr_class
                                    __token = 3505
                                    __token = 3530
                                    try:
                                        __zt_tmp = __attrs_140310476021696
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_140310567013776('path', 'extra_class', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = ('%s%s' % ('nav-link dropdown-item ', (__attr_class if (__attr_class is not None) else ''), ))
                                    if (__attr_class is None):
                                        pass
                                    else:
                                        if (__attr_class is _DEFAULT_MARKER):
                                            __attr_class = None
                                        else:
                                            __tt = type(__attr_class)
                                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                __attr_class = str(__attr_class)
                                            else:
                                                if (__tt is bytes):
                                                    __attr_class = decode(__attr_class)
                                                else:
                                                    if (__tt is not str):
                                                        try:
                                                            __attr_class = __attr_class.__html__
                                                        except get('AttributeError', AttributeError):
                                                            __converted = convert(__attr_class)
                                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                        else:
                                                            __attr_class = __attr_class()
                                    if (__attr_class is not None):
                                        __append((' class="%s"' % __attr_class))
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476018000
                                    __attrs_140310476018000 = _static_140310566789392

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476022224
                                    __default_140310476022224 = _DEFAULT_MARKER

                                    # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (94:51)> -> __cache_140310476015312
                                    __token = 3668
                                    try:
                                        __zt_tmp = __attrs_140310476018000
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140310476015312 = _static_140310567013776('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                    # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (94:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9414c370> -> __condition
                                    __expression = __cache_140310476015312

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_140310476015312
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476013824
                                    __attrs_140310476013824 = _static_140310566789392

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476016176
                                    __default_140310476016176 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (95:48)> -> __cache_140310476023424
                                    __token = 3813
                                    try:
                                        __zt_tmp = __attrs_140310476013824
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140310476023424 = _static_140310567013776('path', 'subMenuItem/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (95:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9414d420> -> __condition
                                    __expression = __cache_140310476023424

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append('\n                    Title\n                  ')
                                    else:
                                        __content = __cache_140310476023424
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </span>')
                                __append('\n              ')
                            if (__backup_is_separator_140310475820192 is __marker):
                                del econtext['is_separator']
                            else:
                                econtext['is_separator'] = __backup_is_separator_140310475820192
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x7f9c9414f3d0> name=None at 7f9c9414d090> -> __attrs_140310475888080
                            __attrs_140310475888080 = _static_140310476026832

                            # <Value 'subMenuItem/action' (104:32)> -> __condition
                            __token = 4131
                            try:
                                __zt_tmp = __attrs_140310475888080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140310567013776('path', 'subMenuItem/action', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475889040
                                __default_140310475889040 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (102:24)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9412c070> -> __attr_class
                                __token = 4034
                                __token = 4059
                                try:
                                    __zt_tmp = __attrs_140310475888080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140310567013776('path', 'extra_class', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_class = ('%s%s' % ('nav-link dropdown-item ', (__attr_class if (__attr_class is not None) else ''), ))
                                if (__attr_class is None):
                                    pass
                                else:
                                    if (__attr_class is _DEFAULT_MARKER):
                                        __attr_class = None
                                    else:
                                        __tt = type(__attr_class)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __attr_class = str(__attr_class)
                                        else:
                                            if (__tt is bytes):
                                                __attr_class = decode(__attr_class)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __attr_class = __attr_class.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__attr_class)
                                                        __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                    else:
                                                        __attr_class = __attr_class()
                                if (__attr_class is not None):
                                    __append((' class="%s"' % __attr_class))

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475887072
                                __default_140310475887072 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/action' (106:24)> -> __attr_href
                                __token = 4209
                                try:
                                    __zt_tmp = __attrs_140310475888080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140310567013776('path', 'subMenuItem/action', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475890240
                                __default_140310475890240 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<Substitution 'subMenuItem/description' (107:24)> at 7f9c9412d870> -> __attr_title

                                # <Substitution 'subMenuItem/description' (107:24)> -> __attr_title
                                __token = 4253
                                try:
                                    __zt_tmp = __attrs_140310475888080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_title = _static_140310567013776('path', 'subMenuItem/description', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_title is not None):
                                    __append((' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475896864
                                __default_140310475896864 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/id | nothing' (108:20)> -> __attr_id
                                __token = 4299
                                try:
                                    __zt_tmp = __attrs_140310475888080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140310567013776('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475894224
                                __default_140310475894224 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/modal | nothing' (109:37)> -> __attr_data_pat_plone_modal
                                __token = 4370
                                try:
                                    __zt_tmp = __attrs_140310475888080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_data_pat_plone_modal = _static_140310567013776('path', 'subMenuItem/extra/modal | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_data_pat_plone_modal is not None):
                                    __append((' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                                __append(' >\n\n                ')

                                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475886832
                                __attrs_140310475886832 = _static_140310566789392

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475896240
                                __default_140310475896240 = _DEFAULT_MARKER

                                # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (114:49)> -> __cache_140310475882848
                                __token = 4534
                                try:
                                    __zt_tmp = __attrs_140310475886832
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140310475882848 = _static_140310567013776('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (114:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9412d8a0> -> __condition
                                __expression = __cache_140310475882848

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140310475882848
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n\n                ')

                                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475895808
                                __attrs_140310475895808 = _static_140310566789392

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475896960
                                __default_140310475896960 = _DEFAULT_MARKER

                                # <Value 'subMenuItem/title' (116:46)> -> __cache_140310475889664
                                __token = 4678
                                try:
                                    __zt_tmp = __attrs_140310475895808
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140310475889664 = _static_140310567013776('path', 'subMenuItem/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                # <BinOp left=<Value 'subMenuItem/title' (116:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9412eb30> -> __condition
                                __expression = __cache_140310475889664

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Title\n                ')
                                else:
                                    __content = __cache_140310475889664
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7f9c9412eb60> name=None at 7f9c9412fbb0> -> __attrs_140310475884000
                                __attrs_140310475884000 = _static_140310475893600

                                # <Value 'not:subMenuItem/action' (122:37)> -> __condition
                                __token = 4895
                                try:
                                    __zt_tmp = __attrs_140310475884000
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140310567013776('not', 'subMenuItem/action', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475890048
                                    __default_140310475890048 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution '${extra_class}' (121:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9412fe50> -> __attr_class
                                    __token = 4842
                                    __token = 4844
                                    try:
                                        __zt_tmp = __attrs_140310475884000
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_140310567013776('path', 'extra_class', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = __attr_class
                                    if (__attr_class is None):
                                        pass
                                    else:
                                        if (__attr_class is _DEFAULT_MARKER):
                                            __attr_class = None
                                        else:
                                            __tt = type(__attr_class)
                                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                __attr_class = str(__attr_class)
                                            else:
                                                if (__tt is bytes):
                                                    __attr_class = decode(__attr_class)
                                                else:
                                                    if (__tt is not str):
                                                        try:
                                                            __attr_class = __attr_class.__html__
                                                        except get('AttributeError', AttributeError):
                                                            __converted = convert(__attr_class)
                                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                        else:
                                                            __attr_class = __attr_class()
                                    if (__attr_class is not None):
                                        __append((' class="%s"' % __attr_class))

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475898160
                                    __default_140310475898160 = _DEFAULT_MARKER

                                    # <Substitution 'subMenuItem/extra/id | nothing' (124:27)> -> __attr_id
                                    __token = 4985
                                    try:
                                        __zt_tmp = __attrs_140310475884000
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140310567013776('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475883856
                                    __attrs_140310475883856 = _static_140310566789392

                                    # <Value "python:'active' in extra_class" (127:43)> -> __condition
                                    __token = 5102
                                    try:
                                        __zt_tmp = __attrs_140310475883856
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_140310567013776('python', "'active' in extra_class", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                                    if __condition:

                                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475891104
                                        __default_140310475891104 = _DEFAULT_MARKER

                                        # <Value "python:icons.tag('check')" (128:51)> -> __cache_140310475890288
                                        __token = 5185
                                        try:
                                            __zt_tmp = __attrs_140310475883856
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_140310475890288 = _static_140310567013776('python', "icons.tag('check')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                        # <BinOp left=<Value "python:icons.tag('check')" (128:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9412e590> -> __condition
                                        __expression = __cache_140310475890288

                                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            pass
                                        else:
                                            __content = __cache_140310475890288
                                            __content = __convert(__content)
                                            if (__content is not None):
                                                __append(__content)
                                    __append('\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475895664
                                    __attrs_140310475895664 = _static_140310566789392

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475887696
                                    __default_140310475887696 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (130:47)> -> __cache_140310475889616
                                    __token = 5280
                                    try:
                                        __zt_tmp = __attrs_140310475895664
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140310475889616 = _static_140310567013776('path', 'subMenuItem/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (130:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9412ef20> -> __condition
                                    __expression = __cache_140310475889616

                                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<span >\n                    Title\n                  </span>')
                                    else:
                                        __content = __cache_140310475889616
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </span>')
                                __append('\n              </a>')
                            __append('\n            ')
                            if (__backup_extra_class_140310475513360 is __marker):
                                del econtext['extra_class']
                            else:
                                econtext['extra_class'] = __backup_extra_class_140310475513360
                            __append('\n          </li>')
                            ____index_140310476014688 -= 1
                            if (____index_140310476014688 > 0):
                                __append('\n          ')
                        if (__backup_subMenuItem_140310476958848 is __marker):
                            del econtext['subMenuItem']
                        else:
                            econtext['subMenuItem'] = __backup_subMenuItem_140310476958848
                        __append('\n        </ul>')
                    __append('\n\n      </li>\n    ')
                    if (__backup_identifier_140310475822784 is __marker):
                        del econtext['identifier']
                    else:
                        econtext['identifier'] = __backup_identifier_140310475822784
                    if (__backup_submenu_140310475850416 is __marker):
                        del econtext['submenu']
                    else:
                        econtext['submenu'] = __backup_submenu_140310475850416
                    __append('\n  ')
                    ____index_140310476138976 -= 1
                    if (____index_140310476138976 > 0):
                        __append('')
                if (__backup_menuItem_140310513282368 is __marker):
                    del econtext['menuItem']
                else:
                    econtext['menuItem'] = __backup_menuItem_140310513282368
                __append('\n')
                __i18n_domain = __previous_i18n_domain_140310476140128
            if (__backup_toolbar_pos_140310475171840 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_140310475171840
            if (__backup_icons_140310475162144 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140310475162144
            if (__backup_menu_140310475166320 is __marker):
                del econtext['menu']
            else:
                econtext['menu'] = __backup_menu_140310475166320
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }