# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.dexterity-3.1.1-py3.10.egg/plone/app/dexterity/browser/item.pt'

__tokens = {476: ('view/widgets/values|nothing', 15, 34), 542: ("python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", 16, 36), 685: ('widget/@@ploneform-render-widget', 17, 47), 803: ('view/groups|nothing', 21, 36), 882: ("python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", 23, 23), 1020: ('group/label', 26, 31), 1083: ('group/widgets/values|nothing', 27, 40), 1161: ('widget/@@ploneform-render-widget', 28, 47), 247: ('context/@@main_template/macros/master', 6, 23), 247: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139922442462608 = 'master'
_static_139922442652208 = {'id': "python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", }
_static_139922496189968 = __C2ZContextWrapper
_static_139922496190256 = __compile_zt_expr
_static_139922496178928 = {}

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

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442655040
            __attrs_139922442655040 = _static_139922496178928
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442654080
            __attrs_139922442654080 = _static_139922496178928
            __backup_widget_139922452782896 = get('widget', __marker)

            # <Value 'view/widgets/values|nothing' (15:34)> -> __iterator
            __token = 476
            try:
                __zt_tmp = __attrs_139922442654080
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139922496190256('path', 'view/widgets/values|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            (__iterator, ____index_139922442653888, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442652448
                __attrs_139922442652448 = _static_139922496178928

                # <Value "python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)" (16:36)> -> __condition
                __token = 542
                try:
                    __zt_tmp = __attrs_139922442652448
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('python', "widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442650144
                    __attrs_139922442650144 = _static_139922496178928

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922442650864
                    __default_139922442650864 = _DEFAULT_MARKER

                    # <Value 'widget/@@ploneform-render-widget' (17:47)> -> __cache_139922442651008
                    __token = 685
                    try:
                        __zt_tmp = __attrs_139922442650144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139922442651008 = _static_139922496190256('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/@@ploneform-render-widget' (17:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f423b7d8610> -> __condition
                    __expression = __cache_139922442651008

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139922442651008
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')
                __append('\n        ')
                ____index_139922442653888 -= 1
                if (____index_139922442653888 > 0):
                    __append('')
            if (__backup_widget_139922452782896 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_139922452782896
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f423b7d8a30> name=None at 7f423b7d8d60> -> __attrs_139922442650192
            __attrs_139922442650192 = _static_139922442652208
            __backup_group_139922452989264 = get('group', __marker)

            # <Value 'view/groups|nothing' (21:36)> -> __iterator
            __token = 803
            try:
                __zt_tmp = __attrs_139922442650192
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139922496190256('path', 'view/groups|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            (__iterator, ____index_139922442649760, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset')

                # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922442651920
                __default_139922442651920 = _DEFAULT_MARKER

                # <Substitution "python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')" (23:23)> -> __attr_id
                __token = 882
                try:
                    __zt_tmp = __attrs_139922442650192
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_139922496190256('python', "''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' >\n          ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442659408
                __attrs_139922442659408 = _static_139922496178928

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')

                # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922442658832
                __default_139922442658832 = _DEFAULT_MARKER

                # <Value 'group/label' (26:31)> -> __cache_139922442658352
                __token = 1020
                try:
                    __zt_tmp = __attrs_139922442659408
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139922442658352 = _static_139922496190256('path', 'group/label', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                # <BinOp left=<Value 'group/label' (26:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f423b7da2f0> -> __condition
                __expression = __cache_139922442658352

                # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139922442658352
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</legend>\n          ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442660128
                __attrs_139922442660128 = _static_139922496178928
                __backup_widget_139922452783952 = get('widget', __marker)

                # <Value 'group/widgets/values|nothing' (27:40)> -> __iterator
                __token = 1083
                try:
                    __zt_tmp = __attrs_139922442660128
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139922496190256('path', 'group/widgets/values|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                (__iterator, ____index_139922442660272, ) = getname('repeat')('widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442661856
                    __attrs_139922442661856 = _static_139922496178928

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922442661664
                    __default_139922442661664 = _DEFAULT_MARKER

                    # <Value 'widget/@@ploneform-render-widget' (28:47)> -> __cache_139922442661136
                    __token = 1161
                    try:
                        __zt_tmp = __attrs_139922442661856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139922442661136 = _static_139922496190256('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/@@ploneform-render-widget' (28:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f423b7dae00> -> __condition
                    __expression = __cache_139922442661136

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139922442661136
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')
                    ____index_139922442660272 -= 1
                    if (____index_139922442660272 > 0):
                        __append('')
                if (__backup_widget_139922452783952 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_139922452783952
                __append('\n        </fieldset>')
                ____index_139922442649760 -= 1
                if (____index_139922442649760 > 0):
                    __append('\n        ')
            if (__backup_group_139922452989264 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_139922452989264
            __append('\n\n      ')
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

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442467600
            __attrs_139922442467600 = _static_139922496178928
            __previous_i18n_domain_139922442465248 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139922495483456 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f423b7aa590> name=None at 7f423b7aa9b0> -> __value
            __value = _static_139922442462608
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922442655952
                __attrs_139922442655952 = _static_139922496178928
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_139922442467600
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139922496190256('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139922495483456 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139922495483456
            __i18n_domain = __previous_i18n_domain_139922442465248
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }