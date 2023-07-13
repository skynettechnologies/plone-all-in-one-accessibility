# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.contentmenu-3.0.2-py3.10.egg/plone/app/contentmenu/contentmenu.pt'

__tokens = {64: ('view/menu', 2, 31), 106: (" python:context.restrictedTraverse('@@iconresolver'", 3, 31), 196: ('s view/toolbar_positi', 4, 36), 282: ('view/available', 6, 35), 374: ('menu', 9, 30), 426: ('menuItem/submenu', 11, 23), 469: (' menuItem/extra/i', 12, 25), 522: ("${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 14, 17), 524: ('menuItem/extra/li_class|nothing', 14, 19), 559: ("python:'dropend' if (submenu and toolbar_pos == 'side') else ''", 14, 54), 639: ('${menuItem/extra/id}', 15, 14), 641: ('menuItem/extra/id', 15, 16), 955: ('menuItem/extra/class | nothing', 24, 25), 1011: (" python:'label-%s' % state_class if state_class else '", 25, 24), 688: ("${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 18, 18), 690: ("python:'nav-link dropdown-toggle' if submenu else 'nav-link'", 18, 20), 779: ("${python:'false' if submenu else ''}", 19, 26), 781: ("python:'false' if submenu else ''", 19, 28), 1127: ("python:menuItem['action'] or 'javascript:void(0)'", 28, 18), 1196: (" python:'cursor: default;; pointer-events: none' if not menuItem['action'] else No", 29, 18), 1298: ('le menuItem/descript', 30, 16), 1426: ("python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", 35, 43), 1598: ('menuItem/title', 38, 31), 1734: ('${state_class}', 43, 25), 1736: ('state_class', 43, 27), 1781: ('menuItem/extra/stateTitle | nothing', 44, 31), 2010: ('submenu | nothing', 54, 27), 2109: ('${menuItem/title}', 58, 14), 2111: ('menuItem/title', 58, 16), 2179: ("python:toolbar_pos == 'top'", 59, 52), 2325: ('menuItem/extra/class | nothing', 62, 36), 2392: (" python:'label-%s' % state_class if state_class else '", 63, 35), 2483: ('e menuItem/extra/stateTitle|nothi', 64, 34), 2581: ('state_title', 66, 37), 2238: ('${state_class}', 60, 29), 2240: ('state_class', 60, 31), 2628: ('${state_title}', 68, 16), 2630: ('state_title', 68, 18), 2778: ('submenu', 73, 38), 2857: ('subMenuItem/extra/class | string:', 75, 37), 3002: ('subMenuItem/extra/separator|nothing', 78, 43), 3112: ('not:subMenuItem/action', 80, 43), 3231: ('is_separator', 83, 35), 3311: ('subMenuItem/title', 85, 48), 3581: ('not:is_separator', 92, 37), 3505: ('nav-link dropdown-item ${extra_class}', 91, 29), 3530: ('extra_class', 91, 54), 3668: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 94, 51), 3813: ('subMenuItem/title', 95, 48), 4131: ('subMenuItem/action', 104, 32), 4034: ('nav-link dropdown-item ${extra_class}', 102, 24), 4059: ('extra_class', 102, 49), 4209: ('subMenuItem/action', 106, 24), 4253: (' subMenuItem/descriptio', 107, 24), 4299: ('d subMenuItem/extra/id | nothi', 108, 20), 4370: ('al subMenuItem/extra/modal | noth', 109, 37), 4534: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 114, 49), 4678: ('subMenuItem/title', 116, 46), 4895: ('not:subMenuItem/action', 122, 37), 4842: ('${extra_class}', 121, 29), 4844: ('extra_class', 121, 31), 4985: ('subMenuItem/extra/id | nothing', 124, 27), 5102: ("python:'active' in extra_class", 127, 43), 5185: ("python:icons.tag('check')", 128, 51), 5280: ('subMenuItem/title', 130, 47)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882205903600 = {'class': '${extra_class}', 'id': 'subMenuItem/extra/id | nothing', }
_static_139882205987600 = {'class': 'nav-link dropdown-item ${extra_class}', 'href': '#', 'title': 'subMenuItem/description', 'id': 'subMenuItem/extra/id | nothing', 'data-pat-plone-modal': 'subMenuItem/extra/modal | nothing', }
_static_139882206002144 = {'class': 'nav-link dropdown-item ${extra_class}', }
_static_139882205993840 = {'class': 'dropdown-header', }
_static_139882100968560 = {'class': '${state_class}', }
_static_139882100966544 = {'class': 'dropdown-header', }
_static_139882100972688 = {'class': 'dropdown-menu', }
_static_139882100970528 = {'class': '${state_class}', }
_static_139882100977968 = {'class': 'toolbar-label', }
_static_139882245428736 = {'class': "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 'aria-expanded': "${python:'false' if submenu else ''}", 'href': '#', 'data-bs-offset': '0,0', 'data-bs-toggle': 'dropdown', 'style': "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None", 'title': 'menuItem/description', }
_static_139882245438480 = {'class': "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 'id': '${menuItem/extra/id}', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245432336
            __attrs_139882245432336 = _static_139882337226896
            __backup_menu_139882206233312 = get('menu', __marker)

            # <Value 'view/menu' (2:31)> -> __value
            __token = 64
            try:
                __zt_tmp = __attrs_139882245432336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/menu', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['menu'] = __value
            __backup_icons_139882206233600 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (3:31)> -> __value
            __token = 106
            try:
                __zt_tmp = __attrs_139882245432336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_toolbar_pos_139882238611456 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (4:36)> -> __value
            __token = 196
            try:
                __zt_tmp = __attrs_139882245432336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/toolbar_position', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'view/available' (6:35)> -> __condition
            __token = 282
            try:
                __zt_tmp = __attrs_139882245432336
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('path', 'view/available', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139882245439344 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245434064
                __attrs_139882245434064 = _static_139882337226896
                __backup_menuItem_139882206234464 = get('menuItem', __marker)

                # <Value 'menu' (9:30)> -> __iterator
                __token = 374
                try:
                    __zt_tmp = __attrs_139882245434064
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139882257081264('path', 'menu', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                (__iterator, ____index_139882245435216, ) = getname('repeat')('menuItem', __iterator)
                econtext['menuItem'] = None
                for __item in __iterator:
                    econtext['menuItem'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245429648
                    __attrs_139882245429648 = _static_139882337226896
                    __backup_submenu_139882205854832 = get('submenu', __marker)

                    # <Value 'menuItem/submenu' (11:23)> -> __value
                    __token = 426
                    try:
                        __zt_tmp = __attrs_139882245429648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139882257081264('path', 'menuItem/submenu', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    econtext['submenu'] = __value
                    __backup_identifier_139882206243632 = get('identifier', __marker)

                    # <Value 'menuItem/extra/id' (12:25)> -> __value
                    __token = 469
                    try:
                        __zt_tmp = __attrs_139882245429648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139882257081264('path', 'menuItem/extra/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    econtext['identifier'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f38df8cbc10> name=None at 7f38df8cb2b0> -> __attrs_139882245435792
                    __attrs_139882245435792 = _static_139882245438480

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245432000
                    __default_139882245432000 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}" (14:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38df8cb730> -> __attr_class
                    __token = 522
                    __token = 524
                    try:
                        __zt_tmp = __attrs_139882245435792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139882257081264('path', 'menuItem/extra/li_class|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 559
                    try:
                        __zt_tmp = __attrs_139882245435792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_557 = _static_139882257081264('python', "'dropend' if (submenu and toolbar_pos == 'side') else ''", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245437856
                    __default_139882245437856 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${menuItem/extra/id}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38df8cbb50> -> __attr_id
                    __token = 639
                    __token = 641
                    try:
                        __zt_tmp = __attrs_139882245435792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139882257081264('path', 'menuItem/extra/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                    # <Static value=<ast.Dict object at 0x7f38df8c9600> name=None at 7f38df8c9f00> -> __attrs_139882100980416
                    __attrs_139882100980416 = _static_139882245428736
                    __backup_state_class_139882205645504 = get('state_class', __marker)

                    # <Value 'menuItem/extra/class | nothing' (24:25)> -> __value
                    __token = 955
                    try:
                        __zt_tmp = __attrs_139882100980416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139882257081264('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    econtext['state_class'] = __value
                    __backup_state_class_139882205644208 = get('state_class', __marker)

                    # <Value "python:'label-%s' % state_class if state_class else ''" (25:24)> -> __value
                    __token = 1011
                    try:
                        __zt_tmp = __attrs_139882100980416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139882257081264('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    econtext['state_class'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245430800
                    __default_139882245430800 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38df8cb0d0> -> __attr_class
                    __token = 688
                    __token = 690
                    try:
                        __zt_tmp = __attrs_139882100980416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139882257081264('python', "'nav-link dropdown-toggle' if submenu else 'nav-link'", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245424368
                    __default_139882245424368 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'false' if submenu else ''}" (19:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38df8ca650> -> __attr_aria_expanded
                    __token = 779
                    __token = 781
                    try:
                        __zt_tmp = __attrs_139882100980416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_aria_expanded = _static_139882257081264('python', "'false' if submenu else ''", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245431280
                    __default_139882245431280 = _DEFAULT_MARKER

                    # <Substitution "python:menuItem['action'] or 'javascript:void(0)'" (28:18)> -> __attr_href
                    __token = 1127
                    try:
                        __zt_tmp = __attrs_139882100980416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('python', "menuItem['action'] or 'javascript:void(0)'", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' data-bs-offset="0,0" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245430272
                    __default_139882245430272 = _DEFAULT_MARKER

                    # <Substitution "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None" (29:18)> -> __attr_style
                    __token = 1196
                    try:
                        __zt_tmp = __attrs_139882100980416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_139882257081264('python', "'cursor: default; pointer-events: none' if not menuItem['action'] else None", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((' style="%s"' % __attr_style))

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100980272
                    __default_139882100980272 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution 'menuItem/description' (30:16)> at 7f38df8c99f0> -> __attr_title

                    # <Substitution 'menuItem/description' (30:16)> -> __attr_title
                    __token = 1298
                    try:
                        __zt_tmp = __attrs_139882100980416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_139882257081264('path', 'menuItem/description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100978208
                    __attrs_139882100978208 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100976864
                    __default_139882100976864 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (35:43)> -> __cache_139882100979840
                    __token = 1426
                    try:
                        __zt_tmp = __attrs_139882100978208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100979840 = _static_139882257081264('python', "icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (35:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6f069e0> -> __condition
                    __expression = __cache_139882100979840

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882100979840
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f38d6f07130> name=None at 7f38d6f07160> -> __attrs_139882100977536
                    __attrs_139882100977536 = _static_139882100977968

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label">\n            ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100979120
                    __attrs_139882100979120 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100977824
                    __default_139882100977824 = _DEFAULT_MARKER

                    # <Value 'menuItem/title' (38:31)> -> __cache_139882100975328
                    __token = 1598
                    try:
                        __zt_tmp = __attrs_139882100979120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100975328 = _static_139882257081264('path', 'menuItem/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/title' (38:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6f07070> -> __condition
                    __expression = __cache_139882100975328

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n              Menu Title\n            </span>')
                    else:
                        __content = __cache_139882100975328
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f38d6f05420> name=None at 7f38d6f05180> -> __attrs_139882100971152
                    __attrs_139882100971152 = _static_139882100970528

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100970432
                    __default_139882100970432 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${state_class}' (43:25)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38d6f060b0> -> __attr_class
                    __token = 1734
                    __token = 1736
                    try:
                        __zt_tmp = __attrs_139882100971152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139882257081264('path', 'state_class', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100973696
                    __default_139882100973696 = _DEFAULT_MARKER

                    # <Value 'menuItem/extra/stateTitle | nothing' (44:31)> -> __cache_139882100974272
                    __token = 1781
                    try:
                        __zt_tmp = __attrs_139882100971152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100974272 = _static_139882257081264('path', 'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/extra/stateTitle | nothing' (44:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6f059c0> -> __condition
                    __expression = __cache_139882100974272

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                State title\n            ')
                    else:
                        __content = __cache_139882100974272
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n          </span>\n\n        </a>')
                    if (__backup_state_class_139882205644208 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_139882205644208
                    if (__backup_state_class_139882205645504 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_139882205645504
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x7f38d6f05c90> name=None at 7f38d6f04160> -> __attrs_139882100972400
                    __attrs_139882100972400 = _static_139882100972688

                    # <Value 'submenu | nothing' (54:27)> -> __condition
                    __token = 2010
                    try:
                        __zt_tmp = __attrs_139882100972400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('path', 'submenu | nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="dropdown-menu" >\n          ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100973120
                        __attrs_139882100973120 = _static_139882337226896

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n            ')

                        # <Static value=<ast.Dict object at 0x7f38d6f04490> name=None at 7f38d6f04310> -> __attrs_139882100967312
                        __attrs_139882100967312 = _static_139882100966544

                        # <h6 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h6 class="dropdown-header">')

                        # <Interpolation value=<Substitution '\n              ${menuItem/title}\n              ' (57:40)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38d6f047c0> -> __content_139882343851824
                        __token = 2109
                        __token = 2111
                        try:
                            __zt_tmp = __attrs_139882100967312
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139882343851824 = _static_139882257081264('path', 'menuItem/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        __content_139882343851824 = __quote(__content_139882343851824, '\x00', '&#0;', None, None)
                        __content_139882343851824 = ('%s%s%s' % ('\n              ', (__content_139882343851824 if (__content_139882343851824 is not None) else ''), '\n              ', ))
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

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100966352
                        __attrs_139882100966352 = _static_139882337226896

                        # <Value "python:toolbar_pos == 'top'" (59:52)> -> __condition
                        __token = 2179
                        try:
                            __zt_tmp = __attrs_139882100966352
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('python', "toolbar_pos == 'top'", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x7f38d6f04c70> name=None at 7f38d6f07af0> -> __attrs_139882100981232
                            __attrs_139882100981232 = _static_139882100968560
                            __backup_state_class_139882100967072 = get('state_class', __marker)

                            # <Value 'menuItem/extra/class | nothing' (62:36)> -> __value
                            __token = 2325
                            try:
                                __zt_tmp = __attrs_139882100981232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139882257081264('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            econtext['state_class'] = __value
                            __backup_state_class_139882100966016 = get('state_class', __marker)

                            # <Value "python:'label-%s' % state_class if state_class else ''" (63:35)> -> __value
                            __token = 2392
                            try:
                                __zt_tmp = __attrs_139882100981232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139882257081264('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            econtext['state_class'] = __value
                            __backup_state_title_139882100968656 = get('state_title', __marker)

                            # <Value 'menuItem/extra/stateTitle|nothing' (64:34)> -> __value
                            __token = 2483
                            try:
                                __zt_tmp = __attrs_139882100981232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139882257081264('path', 'menuItem/extra/stateTitle|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            econtext['state_title'] = __value

                            # <Value 'state_title' (66:37)> -> __condition
                            __token = 2581
                            try:
                                __zt_tmp = __attrs_139882100981232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139882257081264('path', 'state_title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span')

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100970816
                                __default_139882100970816 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution '${state_class}' (60:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38d6f06200> -> __attr_class
                                __token = 2238
                                __token = 2240
                                try:
                                    __zt_tmp = __attrs_139882100981232
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_139882257081264('path', 'state_class', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                                # <Interpolation value=<Substitution '\n                ${state_title}\n                ' (67:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38d6f055a0> -> __content_139882343851824
                                __token = 2628
                                __token = 2630
                                try:
                                    __zt_tmp = __attrs_139882100981232
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_139882343851824 = _static_139882257081264('path', 'state_title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                __content_139882343851824 = __quote(__content_139882343851824, '\x00', '&#0;', None, None)
                                __content_139882343851824 = ('%s%s%s' % ('\n                ', (__content_139882343851824 if (__content_139882343851824 is not None) else ''), '\n                ', ))
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
                                __append('</span>')
                            if (__backup_state_title_139882100968656 is __marker):
                                del econtext['state_title']
                            else:
                                econtext['state_title'] = __backup_state_title_139882100968656
                            if (__backup_state_class_139882100966016 is __marker):
                                del econtext['state_class']
                            else:
                                econtext['state_class'] = __backup_state_class_139882100966016
                            if (__backup_state_class_139882100967072 is __marker):
                                del econtext['state_class']
                            else:
                                econtext['state_class'] = __backup_state_class_139882100967072
                            __append('\n              ')
                        __append('\n            </h6>\n          </li>\n          ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100981040
                        __attrs_139882100981040 = _static_139882337226896
                        __backup_subMenuItem_139882206142976 = get('subMenuItem', __marker)

                        # <Value 'submenu' (73:38)> -> __iterator
                        __token = 2778
                        try:
                            __zt_tmp = __attrs_139882100981040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_139882257081264('path', 'submenu', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        (__iterator, ____index_139882100980896, ) = getname('repeat')('subMenuItem', __iterator)
                        econtext['subMenuItem'] = None
                        for __item in __iterator:
                            econtext['subMenuItem'] = __item

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li>\n            ')

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205996528
                            __attrs_139882205996528 = _static_139882337226896
                            __backup_extra_class_139882100975184 = get('extra_class', __marker)

                            # <Value 'subMenuItem/extra/class | string:' (75:37)> -> __value
                            __token = 2857
                            try:
                                __zt_tmp = __attrs_139882205996528
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139882257081264('path', 'subMenuItem/extra/class | string:', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            econtext['extra_class'] = __value
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206001616
                            __attrs_139882206001616 = _static_139882337226896
                            __backup_is_separator_139882100969808 = get('is_separator', __marker)

                            # <Value 'subMenuItem/extra/separator|nothing' (78:43)> -> __value
                            __token = 3002
                            try:
                                __zt_tmp = __attrs_139882206001616
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139882257081264('path', 'subMenuItem/extra/separator|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            econtext['is_separator'] = __value

                            # <Value 'not:subMenuItem/action' (80:43)> -> __condition
                            __token = 3112
                            try:
                                __zt_tmp = __attrs_139882206001616
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139882257081264('not', 'subMenuItem/action', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            if __condition:
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7f38dd32db70> name=None at 7f38dd32d000> -> __attrs_139882205999600
                                __attrs_139882205999600 = _static_139882205993840

                                # <Value 'is_separator' (83:35)> -> __condition
                                __token = 3231
                                try:
                                    __zt_tmp = __attrs_139882205999600
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139882257081264('path', 'is_separator', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                if __condition:

                                    # <h6 ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<h6 class="dropdown-header" >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205987840
                                    __attrs_139882205987840 = _static_139882337226896

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205995040
                                    __default_139882205995040 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (85:48)> -> __cache_139882206002912
                                    __token = 3311
                                    try:
                                        __zt_tmp = __attrs_139882205987840
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_139882206002912 = _static_139882257081264('path', 'subMenuItem/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (85:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd32d930> -> __condition
                                    __expression = __cache_139882206002912

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append('\n                    Title\n                  ')
                                    else:
                                        __content = __cache_139882206002912
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </h6>')
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7f38dd32fbe0> name=None at 7f38dd32e0e0> -> __attrs_139882205991392
                                __attrs_139882205991392 = _static_139882206002144

                                # <Value 'not:is_separator' (92:37)> -> __condition
                                __token = 3581
                                try:
                                    __zt_tmp = __attrs_139882205991392
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139882257081264('not', 'is_separator', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205997008
                                    __default_139882205997008 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (91:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd32c5b0> -> __attr_class
                                    __token = 3505
                                    __token = 3530
                                    try:
                                        __zt_tmp = __attrs_139882205991392
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_139882257081264('path', 'extra_class', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206003152
                                    __attrs_139882206003152 = _static_139882337226896

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205988416
                                    __default_139882205988416 = _DEFAULT_MARKER

                                    # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (94:51)> -> __cache_139882205987072
                                    __token = 3668
                                    try:
                                        __zt_tmp = __attrs_139882206003152
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_139882205987072 = _static_139882257081264('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                    # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (94:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd32f370> -> __condition
                                    __expression = __cache_139882205987072

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_139882205987072
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205892800
                                    __attrs_139882205892800 = _static_139882337226896

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205902832
                                    __default_139882205902832 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (95:48)> -> __cache_139882206002480
                                    __token = 3813
                                    try:
                                        __zt_tmp = __attrs_139882205892800
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_139882206002480 = _static_139882257081264('path', 'subMenuItem/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (95:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd317d30> -> __condition
                                    __expression = __cache_139882206002480

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append('\n                    Title\n                  ')
                                    else:
                                        __content = __cache_139882206002480
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </span>')
                                __append('\n              ')
                            if (__backup_is_separator_139882100969808 is __marker):
                                del econtext['is_separator']
                            else:
                                econtext['is_separator'] = __backup_is_separator_139882100969808
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x7f38dd32c310> name=None at 7f38dd32fd90> -> __attrs_139882205897744
                            __attrs_139882205897744 = _static_139882205987600

                            # <Value 'subMenuItem/action' (104:32)> -> __condition
                            __token = 4131
                            try:
                                __zt_tmp = __attrs_139882205897744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139882257081264('path', 'subMenuItem/action', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205889440
                                __default_139882205889440 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (102:24)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd317910> -> __attr_class
                                __token = 4034
                                __token = 4059
                                try:
                                    __zt_tmp = __attrs_139882205897744
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_139882257081264('path', 'extra_class', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205893760
                                __default_139882205893760 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/action' (106:24)> -> __attr_href
                                __token = 4209
                                try:
                                    __zt_tmp = __attrs_139882205897744
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_139882257081264('path', 'subMenuItem/action', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205902064
                                __default_139882205902064 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<Substitution 'subMenuItem/description' (107:24)> at 7f38dd3141f0> -> __attr_title

                                # <Substitution 'subMenuItem/description' (107:24)> -> __attr_title
                                __token = 4253
                                try:
                                    __zt_tmp = __attrs_139882205897744
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_title = _static_139882257081264('path', 'subMenuItem/description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_title is not None):
                                    __append((' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205901152
                                __default_139882205901152 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/id | nothing' (108:20)> -> __attr_id
                                __token = 4299
                                try:
                                    __zt_tmp = __attrs_139882205897744
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_139882257081264('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205900192
                                __default_139882205900192 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/modal | nothing' (109:37)> -> __attr_data_pat_plone_modal
                                __token = 4370
                                try:
                                    __zt_tmp = __attrs_139882205897744
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_data_pat_plone_modal = _static_139882257081264('path', 'subMenuItem/extra/modal | nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_data_pat_plone_modal is not None):
                                    __append((' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                                __append(' >\n\n                ')

                                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205894384
                                __attrs_139882205894384 = _static_139882337226896

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205891792
                                __default_139882205891792 = _DEFAULT_MARKER

                                # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (114:49)> -> __cache_139882205891072
                                __token = 4534
                                try:
                                    __zt_tmp = __attrs_139882205894384
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_139882205891072 = _static_139882257081264('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (114:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd314ac0> -> __condition
                                __expression = __cache_139882205891072

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_139882205891072
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n\n                ')

                                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205892752
                                __attrs_139882205892752 = _static_139882337226896

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205894768
                                __default_139882205894768 = _DEFAULT_MARKER

                                # <Value 'subMenuItem/title' (116:46)> -> __cache_139882205891360
                                __token = 4678
                                try:
                                    __zt_tmp = __attrs_139882205892752
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_139882205891360 = _static_139882257081264('path', 'subMenuItem/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                # <BinOp left=<Value 'subMenuItem/title' (116:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd315e10> -> __condition
                                __expression = __cache_139882205891360

                                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Title\n                ')
                                else:
                                    __content = __cache_139882205891360
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7f38dd317af0> name=None at 7f38dd315c30> -> __attrs_139882205904368
                                __attrs_139882205904368 = _static_139882205903600

                                # <Value 'not:subMenuItem/action' (122:37)> -> __condition
                                __token = 4895
                                try:
                                    __zt_tmp = __attrs_139882205904368
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139882257081264('not', 'subMenuItem/action', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205892704
                                    __default_139882205892704 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution '${extra_class}' (121:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd3159c0> -> __attr_class
                                    __token = 4842
                                    __token = 4844
                                    try:
                                        __zt_tmp = __attrs_139882205904368
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_139882257081264('path', 'extra_class', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205889344
                                    __default_139882205889344 = _DEFAULT_MARKER

                                    # <Substitution 'subMenuItem/extra/id | nothing' (124:27)> -> __attr_id
                                    __token = 4985
                                    try:
                                        __zt_tmp = __attrs_139882205904368
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_139882257081264('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205899952
                                    __attrs_139882205899952 = _static_139882337226896

                                    # <Value "python:'active' in extra_class" (127:43)> -> __condition
                                    __token = 5102
                                    try:
                                        __zt_tmp = __attrs_139882205899952
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_139882257081264('python', "'active' in extra_class", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                                    if __condition:

                                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205897072
                                        __default_139882205897072 = _DEFAULT_MARKER

                                        # <Value "python:icons.tag('check')" (128:51)> -> __cache_139882205890880
                                        __token = 5185
                                        try:
                                            __zt_tmp = __attrs_139882205899952
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_139882205890880 = _static_139882257081264('python', "icons.tag('check')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                        # <BinOp left=<Value "python:icons.tag('check')" (128:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd315360> -> __condition
                                        __expression = __cache_139882205890880

                                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            pass
                                        else:
                                            __content = __cache_139882205890880
                                            __content = __convert(__content)
                                            if (__content is not None):
                                                __append(__content)
                                    __append('\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205900480
                                    __attrs_139882205900480 = _static_139882337226896

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205901920
                                    __default_139882205901920 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (130:47)> -> __cache_139882205901968
                                    __token = 5280
                                    try:
                                        __zt_tmp = __attrs_139882205900480
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_139882205901968 = _static_139882257081264('path', 'subMenuItem/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (130:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd315600> -> __condition
                                    __expression = __cache_139882205901968

                                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<span >\n                    Title\n                  </span>')
                                    else:
                                        __content = __cache_139882205901968
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </span>')
                                __append('\n              </a>')
                            __append('\n            ')
                            if (__backup_extra_class_139882100975184 is __marker):
                                del econtext['extra_class']
                            else:
                                econtext['extra_class'] = __backup_extra_class_139882100975184
                            __append('\n          </li>')
                            ____index_139882100980896 -= 1
                            if (____index_139882100980896 > 0):
                                __append('\n          ')
                        if (__backup_subMenuItem_139882206142976 is __marker):
                            del econtext['subMenuItem']
                        else:
                            econtext['subMenuItem'] = __backup_subMenuItem_139882206142976
                        __append('\n        </ul>')
                    __append('\n\n      </li>\n    ')
                    if (__backup_identifier_139882206243632 is __marker):
                        del econtext['identifier']
                    else:
                        econtext['identifier'] = __backup_identifier_139882206243632
                    if (__backup_submenu_139882205854832 is __marker):
                        del econtext['submenu']
                    else:
                        econtext['submenu'] = __backup_submenu_139882205854832
                    __append('\n  ')
                    ____index_139882245435216 -= 1
                    if (____index_139882245435216 > 0):
                        __append('')
                if (__backup_menuItem_139882206234464 is __marker):
                    del econtext['menuItem']
                else:
                    econtext['menuItem'] = __backup_menuItem_139882206234464
                __append('\n')
                __i18n_domain = __previous_i18n_domain_139882245439344
            if (__backup_toolbar_pos_139882238611456 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_139882238611456
            if (__backup_icons_139882206233600 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139882206233600
            if (__backup_menu_139882206233312 is __marker):
                del econtext['menu']
            else:
                econtext['menu'] = __backup_menu_139882206233312
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }