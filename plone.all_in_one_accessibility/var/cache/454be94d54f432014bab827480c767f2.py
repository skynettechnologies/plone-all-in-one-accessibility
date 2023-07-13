# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.portlets-5.0.6-py3.10.egg/plone/app/portlets/portlets/classic.pt'

__tokens = {47: ('view/use_macro', 2, 23), 91: (' view/path_expressio', 3, 28), 153: ('use_macro', 6, 24), 199: ('python:path(path_expression)', 7, 34), 199: ('python:path(path_expression)', 7, 34), 272: ('not:use_macro', 10, 24), 320: ('python:path(path_expression)', 11, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272299584 = 'python:path(path_expression)'
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272308176
            __attrs_140310272308176 = _static_140310566789392
            __backup_use_macro_140310272586464 = get('use_macro', __marker)

            # <Value 'view/use_macro' (2:23)> -> __value
            __token = 47
            try:
                __zt_tmp = __attrs_140310272308176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/use_macro', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['use_macro'] = __value
            __backup_path_expression_140310272580032 = get('path_expression', __marker)

            # <Value 'view/path_expression' (3:28)> -> __value
            __token = 91
            try:
                __zt_tmp = __attrs_140310272308176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/path_expression', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['path_expression'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272298960
            __attrs_140310272298960 = _static_140310566789392

            # <Value 'use_macro' (6:24)> -> __condition
            __token = 153
            try:
                __zt_tmp = __attrs_140310272298960
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'use_macro', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272302512
                __attrs_140310272302512 = _static_140310566789392
                __backup_macroname_140310547577664 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7f9c87f05240> name=None at 7f9c87f06ec0> -> __value
                __value = _static_140310272299584
                econtext['macroname'] = __value

                # <Value 'python:path(path_expression)' (7:34)> -> __macro
                __token = 199
                try:
                    __zt_tmp = __attrs_140310272302512
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140310567013776('python', 'path(path_expression)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                __token = 199
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140310547577664 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140310547577664
                __append('\n  ')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272302032
            __attrs_140310272302032 = _static_140310566789392

            # <Value 'not:use_macro' (10:24)> -> __condition
            __token = 272
            try:
                __zt_tmp = __attrs_140310272302032
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('not', 'use_macro', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272295312
                __attrs_140310272295312 = _static_140310566789392

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272302272
                __default_140310272302272 = _DEFAULT_MARKER

                # <Value 'python:path(path_expression)' (11:32)> -> __cache_140310272302800
                __token = 320
                try:
                    __zt_tmp = __attrs_140310272295312
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310272302800 = _static_140310567013776('python', 'path(path_expression)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:path(path_expression)' (11:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f068c0> -> __condition
                __expression = __cache_140310272302800

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_140310272302800
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
            __append('\n\n')
            if (__backup_path_expression_140310272580032 is __marker):
                del econtext['path_expression']
            else:
                econtext['path_expression'] = __backup_path_expression_140310272580032
            if (__backup_use_macro_140310272586464 is __marker):
                del econtext['use_macro']
            else:
                econtext['use_macro'] = __backup_use_macro_140310272586464
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }