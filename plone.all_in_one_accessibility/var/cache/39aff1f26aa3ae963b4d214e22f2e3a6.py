# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.z3cform-4.2.1-py3.10.egg/plone/app/z3cform/templates/checkbox_input.pt'

__tokens = {129: ('view/items', 4, 14), 154: (' python:list(items', 5, 13), 197: ('x python:len(items) ==', 6, 22), 277: ('python:len(items) &gt', 10, 22), 324: ('single_checkbox', 11, 21), 377: ('view/id', 13, 12), 453: ('items', 17, 26), 500: ('python:single_checkbox and view.id or None', 19, 14), 826: ('item/checked', 32, 28), 947: ('s string:form-check-input ${view/klas', 36, 19), 888: ('item/id', 34, 18), 1796: ('              ', 58, 1), 1762: ('ly;\n    ', 56, 35), 916: (' item/nam', 35, 19), 1583: ('         tabi', 52, 6), 1070: ('itle view/', 39, 16), 1006: ('ue item/va', 37, 18), 1038: ('yle view/s', 38, 17), 1101: (' lang vie', 40, 14), 1134: ('nclick view/', 41, 16), 1173: ('blclick view/on', 42, 18), 1216: ('ousedown view/on', 43, 18), 1258: ('onmouseup view', 44, 15), 1300: ('nmouseover view/', 45, 16), 1344: ('onmousemove view', 46, 15), 1387: ('  onmouseout vi', 47, 13), 1429: ('   onkeypress v', 48, 12), 1470: ('     onkeydown', 49, 10), 1508: ('        onke', 50, 7), 1545: ('        disab', 51, 7), 1620: ('           o', 53, 4), 1655: ('           ', 54, 2), 1691: ('            o', 55, 3), 1729: ('             ', 56, 2), 1835: ('\n            ', 58, 40), 2126: ('not:item/checked', 70, 28), 2251: ('s string:form-check-input ${view/klas', 74, 19), 2192: ('item/id', 72, 18), 3100: ('              ', 96, 1), 3066: ('ly;\n    ', 94, 35), 2220: (' item/nam', 73, 19), 2887: ('         tabi', 90, 6), 2374: ('itle view/', 77, 16), 2310: ('ue item/va', 75, 18), 2342: ('yle view/s', 76, 17), 2405: (' lang vie', 78, 14), 2438: ('nclick view/', 79, 16), 2477: ('blclick view/on', 80, 18), 2520: ('ousedown view/on', 81, 18), 2562: ('onmouseup view', 82, 15), 2604: ('nmouseover view/', 83, 16), 2648: ('onmousemove view', 84, 15), 2691: ('  onmouseout vi', 85, 13), 2733: ('   onkeypress v', 86, 12), 2774: ('     onkeydown', 87, 10), 2812: ('        onke', 88, 7), 2849: ('        disab', 89, 7), 2924: ('           o', 91, 4), 2959: ('           ', 92, 2), 2995: ('            o', 93, 3), 3033: ('             ', 94, 2), 3139: ('\n            ', 96, 40), 3310: ('item/id', 103, 19), 3397: ('item/label', 107, 27), 3585: ('string:${view/name}-empty-marker', 116, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139856821912432 = {'name': 'field-empty-marker', 'type': 'hidden', 'value': '1', }
_static_139856821918960 = {'class': 'label', }
_static_139856820418688 = {'class': 'form-check-label', 'for': '', }
_static_139856820420560 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'name': '', 'tabindex': '', 'title': '', 'type': 'checkbox', 'value': '', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', }
_static_139856823127056 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'checked': 'checked', 'name': '', 'tabindex': '', 'title': '', 'type': 'checkbox', 'value': '', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', }
_static_139856823049456 = {'class': 'form-check', 'id': 'python:single_checkbox and view.id or None', }
_static_139856823056704 = {'id': 'view/id', }
_static_139856914195856 = __C2ZContextWrapper
_static_139856914196144 = __compile_zt_expr
_static_139856823056368 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f32f441f7f0> name=None at 7f32f441d300> -> __attrs_139856823054544
            __attrs_139856823054544 = _static_139856823056368
            __backup_items_139856820722016 = get('items', __marker)

            # <Value 'view/items' (4:14)> -> __value
            __token = 129
            try:
                __zt_tmp = __attrs_139856823054544
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('path', 'view/items', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_items_139856820729648 = get('items', __marker)

            # <Value 'python:list(items)' (5:13)> -> __value
            __token = 154
            try:
                __zt_tmp = __attrs_139856823054544
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('python', 'list(items)', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_single_checkbox_139856821965280 = get('single_checkbox', __marker)

            # <Value 'python:len(items) == 1' (6:22)> -> __value
            __token = 197
            try:
                __zt_tmp = __attrs_139856823054544
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('python', 'len(items) == 1', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['single_checkbox'] = __value
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f32f441f940> name=None at 7f32f441ec20> -> __attrs_139856823050800
            __attrs_139856823050800 = _static_139856823056704

            # <Value 'python:len(items) > 0' (10:22)> -> __condition
            __token = 277
            try:
                __zt_tmp = __attrs_139856823050800
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139856914196144('python', 'len(items) > 0', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'single_checkbox' (11:21)> at 7f32f441ffd0> -> __cache_139856823058384

                # <Value 'single_checkbox' (11:21)> -> __cache_139856823058384
                __token = 324
                try:
                    __zt_tmp = __attrs_139856823050800
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139856823058384 = _static_139856914196144('path', 'single_checkbox', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __cache_139856823058384 = not __cache_139856823058384
                __condition = __cache_139856823058384
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823054160
                    __default_139856823054160 = _DEFAULT_MARKER

                    # <Substitution 'view/id' (13:12)> -> __attr_id
                    __token = 377
                    try:
                        __zt_tmp = __attrs_139856823050800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139856914196144('path', 'view/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >')
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f32f441dcf0> name=None at 7f32f441d990> -> __attrs_139856823052384
                __attrs_139856823052384 = _static_139856823049456
                __backup_item_139856821975456 = get('item', __marker)

                # <Value 'items' (17:26)> -> __iterator
                __token = 453
                try:
                    __zt_tmp = __attrs_139856823052384
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139856914196144('path', 'items', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                (__iterator, ____index_139856823048832, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823047728
                    __default_139856823047728 = _DEFAULT_MARKER

                    # <Substitution 'python:single_checkbox and view.id or None' (19:14)> -> __attr_id
                    __token = 500
                    try:
                        __zt_tmp = __attrs_139856823052384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139856914196144('python', 'single_checkbox and view.id or None', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n      ')

                    # <Static value=<ast.Dict object at 0x7f32f4430c10> name=None at 7f32f4430bb0> -> __attrs_139856820415136
                    __attrs_139856820415136 = _static_139856823127056

                    # <Value 'item/checked' (32:28)> -> __condition
                    __token = 826
                    try:
                        __zt_tmp = __attrs_139856820415136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('path', 'item/checked', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823128112
                        __default_139856823128112 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (36:19)> -> __attr_class
                        __token = 947
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_139856914196144('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823133392
                        __default_139856823133392 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (34:18)> -> __attr_id
                        __token = 888
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_139856914196144('path', 'item/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823128352
                        __default_139856823128352 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (58:1)> -> __attr_accesskey
                        __token = 1796
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_139856914196144('path', 'view/accesskey', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823048160
                        __default_139856823048160 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (56:35)> -> __attr_alt
                        __token = 1762
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_139856914196144('path', 'view/alt', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))
                        __append(' checked="checked"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823044704
                        __default_139856823044704 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (35:19)> -> __attr_name
                        __token = 916
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_139856914196144('path', 'item/name', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823044176
                        __default_139856823044176 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (52:6)> -> __attr_tabindex
                        __token = 1583
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_139856914196144('path', 'view/tabindex', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823056896
                        __default_139856823056896 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (39:16)> -> __attr_title
                        __token = 1070
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_139856914196144('path', 'view/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append(' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824451376
                        __default_139856824451376 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (37:18)> -> __attr_value
                        __token = 1006
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139856914196144('path', 'item/value', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824466400
                        __default_139856824466400 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (38:17)> -> __attr_style
                        __token = 1038
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_139856914196144('path', 'view/style', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824455072
                        __default_139856824455072 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (40:14)> -> __attr_lang
                        __token = 1101
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_139856914196144('path', 'view/lang', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824460832
                        __default_139856824460832 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (41:16)> -> __attr_onclick
                        __token = 1134
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_139856914196144('path', 'view/onclick', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824454304
                        __default_139856824454304 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (42:18)> -> __attr_ondblclick
                        __token = 1173
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_139856914196144('path', 'view/ondblclick', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824455216
                        __default_139856824455216 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (43:18)> -> __attr_onmousedown
                        __token = 1216
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_139856914196144('path', 'view/onmousedown', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824459728
                        __default_139856824459728 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (44:15)> -> __attr_onmouseup
                        __token = 1258
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_139856914196144('path', 'view/onmouseup', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824462656
                        __default_139856824462656 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (45:16)> -> __attr_onmouseover
                        __token = 1300
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_139856914196144('path', 'view/onmouseover', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824459488
                        __default_139856824459488 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (46:15)> -> __attr_onmousemove
                        __token = 1344
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_139856914196144('path', 'view/onmousemove', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824464192
                        __default_139856824464192 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (47:13)> -> __attr_onmouseout
                        __token = 1387
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_139856914196144('path', 'view/onmouseout', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824463424
                        __default_139856824463424 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (48:12)> -> __attr_onkeypress
                        __token = 1429
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_139856914196144('path', 'view/onkeypress', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824466736
                        __default_139856824466736 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (49:10)> -> __attr_onkeydown
                        __token = 1470
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_139856914196144('path', 'view/onkeydown', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824457328
                        __default_139856824457328 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (50:7)> -> __attr_onkeyup
                        __token = 1508
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_139856914196144('path', 'view/onkeyup', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824457424
                        __default_139856824457424 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (51:7)> -> __attr_disabled
                        __token = 1545
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_139856914196144('path', 'view/disabled', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = None
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856824457280
                        __default_139856824457280 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (53:4)> -> __attr_onfocus
                        __token = 1620
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_139856914196144('path', 'view/onfocus', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820411920
                        __default_139856820411920 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (54:2)> -> __attr_onblur
                        __token = 1655
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_139856914196144('path', 'view/onblur', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820411344
                        __default_139856820411344 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (55:3)> -> __attr_onchange
                        __token = 1691
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_139856914196144('path', 'view/onchange', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820411392
                        __default_139856820411392 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (56:2)> -> __attr_readonly
                        __token = 1729
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_139856914196144('path', 'view/readonly', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = None
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820415808
                        __default_139856820415808 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (58:40)> -> __attr_onselect
                        __token = 1835
                        try:
                            __zt_tmp = __attrs_139856820415136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_139856914196144('path', 'view/onselect', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')

                    # <Static value=<ast.Dict object at 0x7f32f419bfd0> name=None at 7f32f4198c10> -> __attrs_139856820409040
                    __attrs_139856820409040 = _static_139856820420560

                    # <Value 'not:item/checked' (70:28)> -> __condition
                    __token = 2126
                    try:
                        __zt_tmp = __attrs_139856820409040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('not', 'item/checked', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820409376
                        __default_139856820409376 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (74:19)> -> __attr_class
                        __token = 2251
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_139856914196144('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820419984
                        __default_139856820419984 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (72:18)> -> __attr_id
                        __token = 2192
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_139856914196144('path', 'item/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820407744
                        __default_139856820407744 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (96:1)> -> __attr_accesskey
                        __token = 3100
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_139856914196144('path', 'view/accesskey', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820419168
                        __default_139856820419168 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (94:35)> -> __attr_alt
                        __token = 3066
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_139856914196144('path', 'view/alt', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820404528
                        __default_139856820404528 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (73:19)> -> __attr_name
                        __token = 2220
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_139856914196144('path', 'item/name', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820404960
                        __default_139856820404960 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (90:6)> -> __attr_tabindex
                        __token = 2887
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_139856914196144('path', 'view/tabindex', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820405104
                        __default_139856820405104 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (77:16)> -> __attr_title
                        __token = 2374
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_139856914196144('path', 'view/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append(' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820416384
                        __default_139856820416384 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (75:18)> -> __attr_value
                        __token = 2310
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139856914196144('path', 'item/value', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820418832
                        __default_139856820418832 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (76:17)> -> __attr_style
                        __token = 2342
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_139856914196144('path', 'view/style', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820419408
                        __default_139856820419408 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (78:14)> -> __attr_lang
                        __token = 2405
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_139856914196144('path', 'view/lang', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820416240
                        __default_139856820416240 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (79:16)> -> __attr_onclick
                        __token = 2438
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_139856914196144('path', 'view/onclick', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820410720
                        __default_139856820410720 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (80:18)> -> __attr_ondblclick
                        __token = 2477
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_139856914196144('path', 'view/ondblclick', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820413600
                        __default_139856820413600 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (81:18)> -> __attr_onmousedown
                        __token = 2520
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_139856914196144('path', 'view/onmousedown', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820420128
                        __default_139856820420128 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (82:15)> -> __attr_onmouseup
                        __token = 2562
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_139856914196144('path', 'view/onmouseup', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820414704
                        __default_139856820414704 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (83:16)> -> __attr_onmouseover
                        __token = 2604
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_139856914196144('path', 'view/onmouseover', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820420320
                        __default_139856820420320 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (84:15)> -> __attr_onmousemove
                        __token = 2648
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_139856914196144('path', 'view/onmousemove', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820418304
                        __default_139856820418304 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (85:13)> -> __attr_onmouseout
                        __token = 2691
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_139856914196144('path', 'view/onmouseout', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820410480
                        __default_139856820410480 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (86:12)> -> __attr_onkeypress
                        __token = 2733
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_139856914196144('path', 'view/onkeypress', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820404288
                        __default_139856820404288 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (87:10)> -> __attr_onkeydown
                        __token = 2774
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_139856914196144('path', 'view/onkeydown', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820413552
                        __default_139856820413552 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (88:7)> -> __attr_onkeyup
                        __token = 2812
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_139856914196144('path', 'view/onkeyup', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820416912
                        __default_139856820416912 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (89:7)> -> __attr_disabled
                        __token = 2849
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_139856914196144('path', 'view/disabled', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = None
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820411824
                        __default_139856820411824 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (91:4)> -> __attr_onfocus
                        __token = 2924
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_139856914196144('path', 'view/onfocus', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820412016
                        __default_139856820412016 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (92:2)> -> __attr_onblur
                        __token = 2959
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_139856914196144('path', 'view/onblur', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820416048
                        __default_139856820416048 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (93:3)> -> __attr_onchange
                        __token = 2995
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_139856914196144('path', 'view/onchange', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820411728
                        __default_139856820411728 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (94:2)> -> __attr_readonly
                        __token = 3033
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_139856914196144('path', 'view/readonly', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = None
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820410672
                        __default_139856820410672 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (96:40)> -> __attr_onselect
                        __token = 3139
                        try:
                            __zt_tmp = __attrs_139856820409040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_139856914196144('path', 'view/onselect', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f32f419b880> name=None at 7f32f419a290> -> __attrs_139856821919824
                    __attrs_139856821919824 = _static_139856820418688

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821926496
                    __default_139856821926496 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (103:19)> -> __attr_for
                    __token = 3310
                    try:
                        __zt_tmp = __attrs_139856821919824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_139856914196144('path', 'item/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f32f4309cf0> name=None at 7f32f430bd30> -> __attrs_139856821921648
                    __attrs_139856821921648 = _static_139856821918960

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="label" >')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821922272
                    __default_139856821922272 = _DEFAULT_MARKER

                    # <Value 'item/label' (107:27)> -> __cache_139856821926640
                    __token = 3397
                    try:
                        __zt_tmp = __attrs_139856821921648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856821926640 = _static_139856914196144('path', 'item/label', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/label' (107:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f4309660> -> __condition
                    __expression = __cache_139856821926640

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Label')
                    else:
                        __content = __cache_139856821926640
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </label>\n    </div>')
                    ____index_139856823048832 -= 1
                    if (____index_139856823048832 > 0):
                        __append('\n    ')
                if (__backup_item_139856821975456 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_139856821975456
                __append('\n  ')
                __condition = __cache_139856823058384
                if __condition:
                    __append('</div>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f32f4308370> name=None at 7f32f441d180> -> __attrs_139856821920880
            __attrs_139856821920880 = _static_139856821912432

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821912048
            __default_139856821912048 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (116:16)> -> __attr_name
            __token = 3585
            try:
                __zt_tmp = __attrs_139856821920880
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_139856914196144('string', '${view/name}-empty-marker', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" value="1" />\n')
            if (__backup_single_checkbox_139856821965280 is __marker):
                del econtext['single_checkbox']
            else:
                econtext['single_checkbox'] = __backup_single_checkbox_139856821965280
            if (__backup_items_139856820729648 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_139856820729648
            if (__backup_items_139856820722016 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_139856820722016
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }