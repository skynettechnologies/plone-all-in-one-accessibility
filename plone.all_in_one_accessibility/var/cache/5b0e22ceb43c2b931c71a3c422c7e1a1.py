# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.dexterity-3.1.1-py3.10.egg/plone/app/dexterity/browser/item.pt'

__tokens = {476: ('view/widgets/values|nothing', 15, 34), 542: ("python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", 16, 36), 685: ('widget/@@ploneform-render-widget', 17, 47), 803: ('view/groups|nothing', 21, 36), 882: ("python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", 23, 23), 1020: ('group/label', 26, 31), 1083: ('group/widgets/values|nothing', 27, 40), 1161: ('widget/@@ploneform-render-widget', 28, 47), 247: ('context/@@main_template/macros/master', 6, 23), 247: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139673029891728 = 'master'
_static_139673029896960 = {'id': "python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", }
_static_139673118568320 = __C2ZContextWrapper
_static_139673118568608 = __compile_zt_expr
_static_139673198743600 = {}

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

            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029894944
            __attrs_139673029894944 = _static_139673198743600
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029895952
            __attrs_139673029895952 = _static_139673198743600
            __backup_widget_139673029891440 = get('widget', __marker)

            # <Value 'view/widgets/values|nothing' (15:34)> -> __iterator
            __token = 476
            try:
                __zt_tmp = __attrs_139673029895952
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139673118568608('path', 'view/widgets/values|nothing', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            (__iterator, ____index_139673029896288, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029897104
                __attrs_139673029897104 = _static_139673198743600

                # <Value "python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)" (16:36)> -> __condition
                __token = 542
                try:
                    __zt_tmp = __attrs_139673029897104
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139673118568608('python', "widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                if __condition:
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029898928
                    __attrs_139673029898928 = _static_139673198743600

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673029898736
                    __default_139673029898736 = _DEFAULT_MARKER

                    # <Value 'widget/@@ploneform-render-widget' (17:47)> -> __cache_139673029898208
                    __token = 685
                    try:
                        __zt_tmp = __attrs_139673029898928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139673029898208 = _static_139673118568608('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/@@ploneform-render-widget' (17:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f082eb5a980> at 7f082954f0d0> -> __condition
                    __expression = __cache_139673029898208

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139673029898208
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')
                __append('\n        ')
                ____index_139673029896288 -= 1
                if (____index_139673029896288 > 0):
                    __append('')
            if (__backup_widget_139673029891440 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_139673029891440
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f082954eb00> name=None at 7f082954ea70> -> __attrs_139673029899312
            __attrs_139673029899312 = _static_139673029896960
            __backup_group_139673029896048 = get('group', __marker)

            # <Value 'view/groups|nothing' (21:36)> -> __iterator
            __token = 803
            try:
                __zt_tmp = __attrs_139673029899312
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139673118568608('path', 'view/groups|nothing', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            (__iterator, ____index_139673029899552, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset')

                # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673029896864
                __default_139673029896864 = _DEFAULT_MARKER

                # <Substitution "python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')" (23:23)> -> __attr_id
                __token = 882
                try:
                    __zt_tmp = __attrs_139673029899312
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_139673118568608('python', "''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' >\n          ')

                # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029901136
                __attrs_139673029901136 = _static_139673198743600

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')

                # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673029900560
                __default_139673029900560 = _DEFAULT_MARKER

                # <Value 'group/label' (26:31)> -> __cache_139673029900080
                __token = 1020
                try:
                    __zt_tmp = __attrs_139673029901136
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139673029900080 = _static_139673118568608('path', 'group/label', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))

                # <BinOp left=<Value 'group/label' (26:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f082eb5a980> at 7f082954f7f0> -> __condition
                __expression = __cache_139673029900080

                # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139673029900080
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</legend>\n          ')

                # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029901856
                __attrs_139673029901856 = _static_139673198743600
                __backup_widget_139673029896096 = get('widget', __marker)

                # <Value 'group/widgets/values|nothing' (27:40)> -> __iterator
                __token = 1083
                try:
                    __zt_tmp = __attrs_139673029901856
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139673118568608('path', 'group/widgets/values|nothing', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                (__iterator, ____index_139673029902144, ) = getname('repeat')('widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673030002000
                    __attrs_139673030002000 = _static_139673198743600

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030001808
                    __default_139673030001808 = _DEFAULT_MARKER

                    # <Value 'widget/@@ploneform-render-widget' (28:47)> -> __cache_139673030001280
                    __token = 1161
                    try:
                        __zt_tmp = __attrs_139673030002000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139673030001280 = _static_139673118568608('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/@@ploneform-render-widget' (28:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f082eb5a980> at 7f0829568370> -> __condition
                    __expression = __cache_139673030001280

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139673030001280
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')
                    ____index_139673029902144 -= 1
                    if (____index_139673029902144 > 0):
                        __append('')
                if (__backup_widget_139673029896096 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_139673029896096
                __append('\n        </fieldset>')
                ____index_139673029899552 -= 1
                if (____index_139673029899552 > 0):
                    __append('\n        ')
            if (__backup_group_139673029896048 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_139673029896048
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

            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029892064
            __attrs_139673029892064 = _static_139673198743600
            __previous_i18n_domain_139673029892208 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139673111699008 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f082954d690> name=None at 7f082954d6c0> -> __value
            __value = _static_139673029891728
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029893984
                __attrs_139673029893984 = _static_139673198743600
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_139673029892064
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139673118568608('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139673111699008 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139673111699008
            __i18n_domain = __previous_i18n_domain_139673029892208
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }