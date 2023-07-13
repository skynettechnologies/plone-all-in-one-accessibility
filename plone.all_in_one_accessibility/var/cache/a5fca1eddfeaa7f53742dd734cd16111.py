# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/z3c.form-4.3-py3.10.egg/z3c/form/browser/select_display.pt'

__tokens = {165: ('view/id', 5, 25), 201: (' view/klas', 6, 27), 240: ('e view/sty', 7, 26), 279: ('le view/ti', 8, 25), 317: ('ang view/', 9, 23), 357: ('lick view/on', 10, 25), 403: ('click view/ondb', 11, 27), 453: ('sedown view/onmo', 12, 27), 502: ('mouseup view/o', 13, 24), 551: ('ouseover view/on', 14, 25), 602: ('mousemove view/o', 15, 24), 652: ('onmouseout view', 16, 22), 701: (' onkeypress vie', 17, 21), 749: ('   onkeydown v', 18, 19), 794: ('      onkeyu', 19, 16), 851: ('view/displayValue', 20, 18), 929: ('value', 22, 24), 964: ('not:repeat/value/end', 23, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139922408313360 = {'class': 'selected-option', }
_static_139922496178928 = {}
_static_139922496189968 = __C2ZContextWrapper
_static_139922496190256 = __compile_zt_expr
_static_139922408347040 = {'id': '', 'class': '', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', }
_static_139922408351504 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f4239722710> name=None at 7f42397228c0> -> __attrs_139922408351264
            __attrs_139922408351264 = _static_139922408351504
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f42397215a0> name=None at 7f4239721570> -> __attrs_139922408344064
            __attrs_139922408344064 = _static_139922408347040

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408349680
            __default_139922408349680 = _DEFAULT_MARKER

            # <Substitution 'view/id' (5:25)> -> __attr_id
            __token = 165
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_139922496190256('path', 'view/id', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408348528
            __default_139922408348528 = _DEFAULT_MARKER

            # <Substitution 'view/klass' (6:27)> -> __attr_class
            __token = 201
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139922496190256('path', 'view/klass', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408346656
            __default_139922408346656 = _DEFAULT_MARKER

            # <Substitution 'view/style' (7:26)> -> __attr_style
            __token = 240
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_139922496190256('path', 'view/style', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408349104
            __default_139922408349104 = _DEFAULT_MARKER

            # <Substitution 'view/title' (8:25)> -> __attr_title
            __token = 279
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_139922496190256('path', 'view/title', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408349440
            __default_139922408349440 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (9:23)> -> __attr_lang
            __token = 317
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_139922496190256('path', 'view/lang', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408350304
            __default_139922408350304 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (10:25)> -> __attr_onclick
            __token = 357
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_139922496190256('path', 'view/onclick', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408350064
            __default_139922408350064 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (11:27)> -> __attr_ondblclick
            __token = 403
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_139922496190256('path', 'view/ondblclick', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408346464
            __default_139922408346464 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (12:27)> -> __attr_onmousedown
            __token = 453
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_139922496190256('path', 'view/onmousedown', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408346128
            __default_139922408346128 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (13:24)> -> __attr_onmouseup
            __token = 502
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_139922496190256('path', 'view/onmouseup', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408345792
            __default_139922408345792 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (14:25)> -> __attr_onmouseover
            __token = 551
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_139922496190256('path', 'view/onmouseover', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408345456
            __default_139922408345456 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (15:24)> -> __attr_onmousemove
            __token = 602
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_139922496190256('path', 'view/onmousemove', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408345120
            __default_139922408345120 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (16:22)> -> __attr_onmouseout
            __token = 652
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_139922496190256('path', 'view/onmouseout', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408344784
            __default_139922408344784 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (17:21)> -> __attr_onkeypress
            __token = 701
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_139922496190256('path', 'view/onkeypress', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408343008
            __default_139922408343008 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (18:19)> -> __attr_onkeydown
            __token = 749
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_139922496190256('path', 'view/onkeydown', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408343824
            __default_139922408343824 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (19:16)> -> __attr_onkeyup
            __token = 794
            try:
                __zt_tmp = __attrs_139922408344064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_139922496190256('path', 'view/onkeyup', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))
            __append('>')

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408342576
            __attrs_139922408342576 = _static_139922496178928
            __backup_value_139922408072928 = get('value', __marker)

            # <Value 'view/displayValue' (20:18)> -> __iterator
            __token = 851
            try:
                __zt_tmp = __attrs_139922408342576
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139922496190256('path', 'view/displayValue', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            (__iterator, ____index_139922408342384, ) = getname('repeat')('value', __iterator)
            econtext['value'] = None
            for __item in __iterator:
                econtext['value'] = __item

                # <Static value=<ast.Dict object at 0x7f4239719210> name=None at 7f423971b130> -> __attrs_139922408320128
                __attrs_139922408320128 = _static_139922408313360

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="selected-option">')

                # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408316240
                __default_139922408316240 = _DEFAULT_MARKER

                # <Value 'value' (22:24)> -> __cache_139922408341952
                __token = 929
                try:
                    __zt_tmp = __attrs_139922408320128
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139922408341952 = _static_139922496190256('path', 'value', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                # <BinOp left=<Value 'value' (22:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f4239720220> -> __condition
                __expression = __cache_139922408341952

                # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139922408341952
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408323632
                __attrs_139922408323632 = _static_139922496178928

                # <Value 'not:repeat/value/end' (23:28)> -> __condition
                __token = 964
                try:
                    __zt_tmp = __attrs_139922408323632
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('not', 'repeat/value/end', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:
                    __append(', ')
                ____index_139922408342384 -= 1
                if (____index_139922408342384 > 0):
                    __append('')
            if (__backup_value_139922408072928 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_139922408072928
            __append('</span>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }