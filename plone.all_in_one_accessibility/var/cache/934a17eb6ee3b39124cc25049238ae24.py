# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.content-4.0.2-py3.10.egg/plone/app/content/browser/contents/templates/folder_contents.pt'

__tokens = {861: ('context/@@authenticator/authenticator', 20, 37), 982: ('view/options', 22, 45), 449: ("python:request.set('enable_border', 1)", 11, 32), 533: (" python:request.set('disable_plone.leftcolumn', 1", 12, 44), 628: ("o python:request.set('disable_plone.rightcolumn', ", 13, 43), 408: ('nothing', 10, 33), 261: ('context/main_template/macros/master', 6, 23), 261: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140148358558768 = 'master'
_static_140148357037360 = {'class': 'pat-structure', 'data-pat-structure': 'view/options', }
_static_140148447782144 = __C2ZContextWrapper
_static_140148447782432 = __compile_zt_expr
_static_140148447476128 = {}

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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f76da6d79a0> name=None at 7f76da6d7cd0> -> __attrs_140148357034192
            __attrs_140148357034192 = _static_140148447476128
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f76da6d79a0> name=None at 7f76da6d7cd0> -> __attrs_140148357032080
            __attrs_140148357032080 = _static_140148447476128

            # <Symbol value=<DEFAULT> at 7f76da6a9fc0> -> __default_140148357034288
            __default_140148357034288 = _DEFAULT_MARKER

            # <Value 'context/@@authenticator/authenticator' (20:37)> -> __cache_140148357034048
            __token = 861
            try:
                __zt_tmp = __attrs_140148357032080
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140148357034048 = _static_140148447782432('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/@@authenticator/authenticator' (20:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f76da6a9fc0> at 7f76d5096a40> -> __condition
            __expression = __cache_140148357034048

            # <Symbol value=<DEFAULT> at 7f76da6a9fc0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span/>')
            else:
                __content = __cache_140148357034048
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f76d5097d30> name=None at 7f76d5096da0> -> __attrs_140148357032608
            __attrs_140148357032608 = _static_140148357037360

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="pat-structure"')

            # <Symbol value=<DEFAULT> at 7f76da6a9fc0> -> __default_140148357029344
            __default_140148357029344 = _DEFAULT_MARKER

            # <Substitution 'view/options' (22:45)> -> __attr_data_pat_structure
            __token = 982
            try:
                __zt_tmp = __attrs_140148357032608
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_structure = _static_140148447782432('path', 'view/options', econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))
            __attr_data_pat_structure = __quote(__attr_data_pat_structure, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_pat_structure is not None):
                __append((' data-pat-structure="%s"' % __attr_data_pat_structure))
            __append(' />\n    ')
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

            # <Static value=<ast.Dict object at 0x7f76da6d79a0> name=None at 7f76da6d7cd0> -> __attrs_140148358554928
            __attrs_140148358554928 = _static_140148447476128
            __previous_i18n_domain_140148358560016 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140148432052800 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f76d520b430> name=None at 7f76d5208ee0> -> __value
            __value = _static_140148358558768
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f76da6d79a0> name=None at 7f76da6d7cd0> -> __attrs_140148358560784
                __attrs_140148358560784 = _static_140148447476128
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f76da6d79a0> name=None at 7f76da6d7cd0> -> __attrs_140148357032800
                __attrs_140148357032800 = _static_140148447476128
                __backup_dummy_140148358808624 = get('dummy', __marker)

                # <Value "python:request.set('enable_border', 1)" (11:32)> -> __value
                __token = 449
                try:
                    __zt_tmp = __attrs_140148357032800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140148447782432('python', "request.set('enable_border', 1)", econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_140148358028048 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn', 1)" (12:44)> -> __value
                __token = 533
                try:
                    __zt_tmp = __attrs_140148357032800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140148447782432('python', "request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140148358819232 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn', 1)" (13:43)> -> __value
                __token = 628
                try:
                    __zt_tmp = __attrs_140148357032800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140148447782432('python', "request.set('disable_plone.rightcolumn', 1)", econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value

                # <Symbol value=<DEFAULT> at 7f76da6a9fc0> -> __default_140148357033760
                __default_140148357033760 = _DEFAULT_MARKER

                # <Value 'nothing' (10:33)> -> __cache_140148357035344
                __token = 408
                try:
                    __zt_tmp = __attrs_140148357032800
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140148357035344 = _static_140148447782432('path', 'nothing', econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))

                # <BinOp left=<Value 'nothing' (10:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f76da6a9fc0> at 7f76d50948b0> -> __condition
                __expression = __cache_140148357035344

                # <Symbol value=<DEFAULT> at 7f76da6a9fc0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140148357035344
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                if (__backup_disable_column_two_140148358819232 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140148358819232
                if (__backup_disable_column_one_140148358028048 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140148358028048
                if (__backup_dummy_140148358808624 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_140148358808624
                __append('\n      ')
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f76da6d79a0> name=None at 7f76da6d7cd0> -> __attrs_140148357032464
                __attrs_140148357032464 = _static_140148447476128
                __append('\n    ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140148358554928
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140148447782432('path', 'context/main_template/macros/master', econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140148432052800 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140148432052800
            __i18n_domain = __previous_i18n_domain_140148358560016
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }