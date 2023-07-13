# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/description.pt'

__tokens = {40: ('context/Description', 1, 40), 102: ('description', 1, 102), 74: ('description', 1, 74)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310475896240 = {'class': 'lead', }

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

            # <Static value=<ast.Dict object at 0x7f9c9412f5b0> name=None at 7f9c9412c490> -> __attrs_140310475882992
            __attrs_140310475882992 = _static_140310475896240
            __backup_description_140310475410592 = get('description', __marker)

            # <Value 'context/Description' (1:40)> -> __value
            __token = 40
            try:
                __zt_tmp = __attrs_140310475882992
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'context/Description', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['description'] = __value

            # <Value 'description' (1:102)> -> __condition
            __token = 102
            try:
                __zt_tmp = __attrs_140310475882992
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'description', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475894944
                __default_140310475894944 = _DEFAULT_MARKER

                # <Value 'description' (1:74)> -> __cache_140310475886544
                __token = 74
                try:
                    __zt_tmp = __attrs_140310475882992
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310475886544 = _static_140310567013776('path', 'description', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'description' (1:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9412cee0> -> __condition
                __expression = __cache_140310475886544

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n  Description\n')
                else:
                    __content = __cache_140310475886544
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</p>')
            if (__backup_description_140310475410592 is __marker):
                del econtext['description']
            else:
                econtext['description'] = __backup_description_140310475410592
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }