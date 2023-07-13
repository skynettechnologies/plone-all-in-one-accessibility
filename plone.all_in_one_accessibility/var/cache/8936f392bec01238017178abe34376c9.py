# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Zope-5.8.3-py3.10.egg/Products/Five/utilities/browser/manage_interfaces.pt'

__tokens = {27: ('context/manage_page_header', 1, 27), 99: ('context/manage_tabs', 2, 27), 193: ('context/@@edit-markers.html/main', 6, 30), 193: ('context/@@edit-markers.html/main', 6, 30), 267: ('context/manage_page_footer', 10, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140568620323632 = 'main'
_static_140568620324784 = {'class': 'container-fluid', }
_static_140568781877216 = __C2ZContextWrapper
_static_140568781877504 = __compile_zt_expr
_static_140568781866176 = {}

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

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568620334384
            __attrs_140568620334384 = _static_140568781866176

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568620334768
            __default_140568620334768 = _DEFAULT_MARKER

            # <Value 'context/manage_page_header' (1:27)> -> __cache_140568620328768
            __token = 27
            try:
                __zt_tmp = __attrs_140568620334384
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140568620328768 = _static_140568781877504('path', 'context/manage_page_header', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aeae78b0> -> __condition
            __expression = __cache_140568620328768

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>PAGE HEADER</h1>')
            else:
                __content = __cache_140568620328768
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568620322192
            __attrs_140568620322192 = _static_140568781866176

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568620320608
            __default_140568620320608 = _DEFAULT_MARKER

            # <Value 'context/manage_tabs' (2:27)> -> __cache_140568620319024
            __token = 99
            try:
                __zt_tmp = __attrs_140568620322192
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140568620319024 = _static_140568781877504('path', 'context/manage_tabs', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aeae53c0> -> __condition
            __expression = __cache_140568620319024

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>TABS</h2>')
            else:
                __content = __cache_140568620319024
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7fd8aeae57b0> name=None at 7fd8aeae47f0> -> __attrs_140568620323824
            __attrs_140568620323824 = _static_140568620324784

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568620323104
            __attrs_140568620323104 = _static_140568781866176
            __backup_macroname_140568618430144 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd8aeae5330> name=None at 7fd8aeae52d0> -> __value
            __value = _static_140568620323632
            econtext['macroname'] = __value

            # <Value 'context/@@edit-markers.html/main' (6:30)> -> __macro
            __token = 193
            try:
                __zt_tmp = __attrs_140568620323104
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140568781877504('path', 'context/@@edit-markers.html/main', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            __token = 193
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140568618430144 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140568618430144
            __append('\n\n</main>\n\n')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568620321280
            __attrs_140568620321280 = _static_140568781866176

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568620321376
            __default_140568620321376 = _DEFAULT_MARKER

            # <Value 'context/manage_page_footer' (10:27)> -> __cache_140568620321760
            __token = 267
            try:
                __zt_tmp = __attrs_140568620321280
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140568620321760 = _static_140568781877504('path', 'context/manage_page_footer', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_footer' (10:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aeae5180> -> __condition
            __expression = __cache_140568620321760

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>PAGE FOOTER</h1>')
            else:
                __content = __cache_140568620321760
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }