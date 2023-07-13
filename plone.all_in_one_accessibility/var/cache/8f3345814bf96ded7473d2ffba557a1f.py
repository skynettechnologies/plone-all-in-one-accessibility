# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.z3cform-4.2.1-py3.10.egg/plone/app/z3cform/templates/layout.pt'

__tokens = {484: ('view/label', 15, 25), 583: ('view/contents', 18, 36), 247: ('here/main_template/macros/master', 6, 23), 247: ('here/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882099784192 = 'master'
_static_139882098630400 = {'id': 'content-core', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882098624544 = {'class': 'documentFirstHeading', }
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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882098623776
            __attrs_139882098623776 = _static_139882337226896
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f38d6cc8820> name=None at 7f38d6cca500> -> __attrs_139882098633184
            __attrs_139882098633184 = _static_139882098624544

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading" >')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098626752
            __default_139882098626752 = _DEFAULT_MARKER

            # <Value 'view/label' (15:25)> -> __cache_139882098627376
            __token = 484
            try:
                __zt_tmp = __attrs_139882098633184
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882098627376 = _static_139882257081264('path', 'view/label', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/label' (15:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6ccbb20> -> __condition
            __expression = __cache_139882098627376

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('Title')
            else:
                __content = __cache_139882098627376
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</h1>\n        ')

            # <Static value=<ast.Dict object at 0x7f38d6cc9f00> name=None at 7f38d6cca3e0> -> __attrs_139882098623344
            __attrs_139882098623344 = _static_139882098630400

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="content-core" >')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098637456
            __default_139882098637456 = _DEFAULT_MARKER

            # <Value 'view/contents' (18:36)> -> __cache_139882098632896
            __token = 583
            try:
                __zt_tmp = __attrs_139882098623344
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882098632896 = _static_139882257081264('path', 'view/contents', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/contents' (18:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6cca050> -> __condition
            __expression = __cache_139882098632896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139882098632896
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n      ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882099784864
            __attrs_139882099784864 = _static_139882337226896
            __previous_i18n_domain_139882099782272 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139882215685120 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f38d6de3a00> name=None at 7f38d6de05e0> -> __value
            __value = _static_139882099784192
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882098628288
                __attrs_139882098628288 = _static_139882337226896
                __append('\n      ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'here/main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_139882099784864
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139882257081264('path', 'here/main_template/macros/master', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139882215685120 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139882215685120
            __i18n_domain = __previous_i18n_domain_139882099782272
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }