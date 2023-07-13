# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.z3cform-4.2.1-py3.10.egg/plone/app/z3cform/templates/select_input.pt'

__tokens = {385: ('ss string:form-select ${view/kla', 14, 15), 252: ('view/id', 11, 15), 277: (' string:${view/name}:lis', 12, 16), 1104: ('iple;\n   ', 33, 30), 939: ('         tabi', 29, 3), 323: ("d python:view.required and 'required' or No", 13, 19), 436: ('yle view/s', 15, 14), 465: ('itle view/', 16, 13), 493: (' lang vie', 17, 11), 523: ('nclick view/', 18, 13), 559: ('blclick view/on', 19, 15), 599: ('ousedown view/on', 20, 15), 638: ('onmouseup view', 21, 12), 677: ('nmouseover view/', 22, 13), 718: ('onmousemove view', 23, 12), 758: ('  onmouseout vi', 24, 10), 797: ('   onkeypress v', 25, 9), 835: ('     onkeydown', 26, 7), 870: ('        onke', 27, 4), 904: ('        disab', 28, 4), 973: ('           o', 30, 1), 1005: ('\n          ', 30, 33), 1038: ('            o', 32, 0), 1073: ('\n            ', 32, 35), 1182: ('view/items', 37, 28), 1294: ('item/selected', 40, 29), 1400: ('item/id', 43, 19), 1430: (' item/valu', 44, 21), 1336: ('item/content', 41, 27), 1546: ('not:item/selected', 48, 29), 1656: ('item/id', 51, 19), 1686: (' item/valu', 52, 21), 1592: ('item/content', 49, 27), 1880: ('string:${view/name}-empty-marker', 60, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882098505424 = {'name': 'field-empty-marker', 'type': 'hidden', 'value': '1', }
_static_139882098492464 = {'id': '', 'value': '', }
_static_139882098503936 = {'id': '', 'selected': 'selected', 'value': '', }
_static_139882337226896 = {}
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882215983712 = {'class': '', 'id': '', 'name': '', 'size': '', 'tabindex': '', 'required': "python:view.required and 'required' or None", 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'multiple': 'view/multiple', }
_static_139882098564768 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f38d6cb9ea0> name=None at 7f38d6cba3e0> -> __attrs_139882098563136
            __attrs_139882098563136 = _static_139882098564768
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f38ddcb4a60> name=None at 7f38ddcb55a0> -> __attrs_139882098502976
            __attrs_139882098502976 = _static_139882215983712

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098570768
            __default_139882098570768 = _DEFAULT_MARKER

            # <Substitution 'string:form-select ${view/klass}' (14:15)> -> __attr_class
            __token = 385
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139882257081264('string', 'form-select ${view/klass}', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098557184
            __default_139882098557184 = _DEFAULT_MARKER

            # <Substitution 'view/id' (11:15)> -> __attr_id
            __token = 252
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_139882257081264('path', 'view/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098557952
            __default_139882098557952 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}:list' (12:16)> -> __attr_name
            __token = 277
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_139882257081264('string', '${view/name}:list', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098568224
            __default_139882098568224 = _DEFAULT_MARKER

            # <Substitution 'view/size' (33:30)> -> __attr_size
            __token = 1104
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_139882257081264('path', 'view/size', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098561264
            __default_139882098561264 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (29:3)> -> __attr_tabindex
            __token = 939
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_139882257081264('path', 'view/tabindex', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098562464
            __default_139882098562464 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (13:19)> -> __attr_required
            __token = 323
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_139882257081264('python', "view.required and 'required' or None", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098571392
            __default_139882098571392 = _DEFAULT_MARKER

            # <Substitution 'view/style' (15:14)> -> __attr_style
            __token = 436
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_139882257081264('path', 'view/style', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098572160
            __default_139882098572160 = _DEFAULT_MARKER

            # <Substitution 'view/title' (16:13)> -> __attr_title
            __token = 465
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_139882257081264('path', 'view/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098571152
            __default_139882098571152 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (17:11)> -> __attr_lang
            __token = 493
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_139882257081264('path', 'view/lang', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098566592
            __default_139882098566592 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (18:13)> -> __attr_onclick
            __token = 523
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_139882257081264('path', 'view/onclick', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098564912
            __default_139882098564912 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (19:15)> -> __attr_ondblclick
            __token = 559
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_139882257081264('path', 'view/ondblclick', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098563424
            __default_139882098563424 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (20:15)> -> __attr_onmousedown
            __token = 599
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_139882257081264('path', 'view/onmousedown', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098568992
            __default_139882098568992 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (21:12)> -> __attr_onmouseup
            __token = 638
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_139882257081264('path', 'view/onmouseup', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205904512
            __default_139882205904512 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (22:13)> -> __attr_onmouseover
            __token = 677
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_139882257081264('path', 'view/onmouseover', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098493136
            __default_139882098493136 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (23:12)> -> __attr_onmousemove
            __token = 718
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_139882257081264('path', 'view/onmousemove', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098501008
            __default_139882098501008 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (24:10)> -> __attr_onmouseout
            __token = 758
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_139882257081264('path', 'view/onmouseout', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098495776
            __default_139882098495776 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (25:9)> -> __attr_onkeypress
            __token = 797
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_139882257081264('path', 'view/onkeypress', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098496976
            __default_139882098496976 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (26:7)> -> __attr_onkeydown
            __token = 835
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_139882257081264('path', 'view/onkeydown', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098493424
            __default_139882098493424 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (27:4)> -> __attr_onkeyup
            __token = 870
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_139882257081264('path', 'view/onkeyup', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098492224
            __default_139882098492224 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (28:4)> -> __attr_disabled
            __token = 904
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_139882257081264('path', 'view/disabled', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098500720
            __default_139882098500720 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (30:1)> -> __attr_onfocus
            __token = 973
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_139882257081264('path', 'view/onfocus', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098499376
            __default_139882098499376 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (30:33)> -> __attr_onblur
            __token = 1005
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_139882257081264('path', 'view/onblur', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098500768
            __default_139882098500768 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (32:0)> -> __attr_onchange
            __token = 1038
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_139882257081264('path', 'view/onchange', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098496832
            __default_139882098496832 = _DEFAULT_MARKER

            # <Boolean 'view/multiple' (32:35)> -> __attr_multiple
            __token = 1073
            try:
                __zt_tmp = __attrs_139882098502976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_multiple = _static_139882257081264('path', 'view/multiple', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if (__attr_multiple is _DEFAULT_MARKER):
                __attr_multiple = None
            else:
                if __attr_multiple:
                    __attr_multiple = 'multiple'
                else:
                    __attr_multiple = None
            if (__attr_multiple is not None):
                __append((' multiple="%s"' % __attr_multiple))
            __append(' >\n    ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882098500672
            __attrs_139882098500672 = _static_139882337226896
            __backup_item_139882098409376 = get('item', __marker)

            # <Value 'view/items' (37:28)> -> __iterator
            __token = 1182
            try:
                __zt_tmp = __attrs_139882098500672
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139882257081264('path', 'view/items', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            (__iterator, ____index_139882098497552, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item

                # <Static value=<ast.Dict object at 0x7f38d6cab100> name=None at 7f38d6cab6a0> -> __attrs_139882098505136
                __attrs_139882098505136 = _static_139882098503936

                # <Value 'item/selected' (40:29)> -> __condition
                __token = 1294
                try:
                    __zt_tmp = __attrs_139882098505136
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'item/selected', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098502784
                    __default_139882098502784 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (43:19)> -> __attr_id
                    __token = 1400
                    try:
                        __zt_tmp = __attrs_139882098505136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139882257081264('path', 'item/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' selected="selected"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098505568
                    __default_139882098505568 = _DEFAULT_MARKER

                    # <Substitution 'item/value' (44:21)> -> __attr_value
                    __token = 1430
                    try:
                        __zt_tmp = __attrs_139882098505136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139882257081264('path', 'item/value', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098495488
                    __default_139882098495488 = _DEFAULT_MARKER

                    # <Value 'item/content' (41:27)> -> __cache_139882098501056
                    __token = 1336
                    try:
                        __zt_tmp = __attrs_139882098505136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882098501056 = _static_139882257081264('path', 'item/content', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/content' (41:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6caa380> -> __condition
                    __expression = __cache_139882098501056

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('label')
                    else:
                        __content = __cache_139882098501056
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')

                # <Static value=<ast.Dict object at 0x7f38d6ca8430> name=None at 7f38d6cab580> -> __attrs_139882098507056
                __attrs_139882098507056 = _static_139882098492464

                # <Value 'not:item/selected' (48:29)> -> __condition
                __token = 1546
                try:
                    __zt_tmp = __attrs_139882098507056
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('not', 'item/selected', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098494336
                    __default_139882098494336 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (51:19)> -> __attr_id
                    __token = 1656
                    try:
                        __zt_tmp = __attrs_139882098507056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139882257081264('path', 'item/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098504656
                    __default_139882098504656 = _DEFAULT_MARKER

                    # <Substitution 'item/value' (52:21)> -> __attr_value
                    __token = 1686
                    try:
                        __zt_tmp = __attrs_139882098507056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139882257081264('path', 'item/value', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098491888
                    __default_139882098491888 = _DEFAULT_MARKER

                    # <Value 'item/content' (49:27)> -> __cache_139882098504272
                    __token = 1592
                    try:
                        __zt_tmp = __attrs_139882098507056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882098504272 = _static_139882257081264('path', 'item/content', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/content' (49:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6caa7d0> -> __condition
                    __expression = __cache_139882098504272

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('label')
                    else:
                        __content = __cache_139882098504272
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                ____index_139882098497552 -= 1
                if (____index_139882098497552 > 0):
                    __append('')
            if (__backup_item_139882098409376 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_139882098409376
            __append('\n  </select>\n  ')

            # <Static value=<ast.Dict object at 0x7f38d6cab6d0> name=None at 7f38d6caba00> -> __attrs_139882098506288
            __attrs_139882098506288 = _static_139882098505424

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098501968
            __default_139882098501968 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (60:16)> -> __attr_name
            __token = 1880
            try:
                __zt_tmp = __attrs_139882098506288
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_139882257081264('string', '${view/name}-empty-marker', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" value="1" />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }