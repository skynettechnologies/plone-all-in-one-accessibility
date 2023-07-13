# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.contenttypes-3.0.3-py3.10.egg/plone/app/contenttypes/browser/templates/document.pt'

__tokens = {519: ("python:  getattr(context, 'table_of_contents', False)", 15, 32), 781: ("python:getattr(context, 'text', None)", 22, 30), 669: ("${python: toc and 'pat-autotoc' or ''}", 20, 22), 671: ("python: toc and 'pat-autotoc' or ''", 20, 24), 858: ('python:context.text.output_relative_to(view.context)', 23, 38), 247: ('context/@@main_template/macros/master', 6, 23), 247: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310476840848 = 'master'
_static_140310475278080 = {'class': "${python: toc and 'pat-autotoc' or ''}", 'id': 'parent-fieldname-text', }
_static_140310475257936 = {'id': 'section-text', }
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475250976
            __attrs_140310475250976 = _static_140310566789392
            __backup_toc_140310475253088 = get('toc', __marker)

            # <Value "python:  getattr(context, 'table_of_contents', False)" (15:32)> -> __value
            __token = 519
            try:
                __zt_tmp = __attrs_140310475250976
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "  getattr(context, 'table_of_contents', False)", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['toc'] = __value
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f9c94093850> name=None at 7f9c94093a00> -> __attrs_140310475188848
            __attrs_140310475188848 = _static_140310475257936

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="section-text">\n          ')

            # <Static value=<ast.Dict object at 0x7f9c94098700> name=None at 7f9c94098730> -> __attrs_140310475278608
            __attrs_140310475278608 = _static_140310475278080

            # <Value "python:getattr(context, 'text', None)" (22:30)> -> __condition
            __token = 781
            try:
                __zt_tmp = __attrs_140310475278608
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('python', "getattr(context, 'text', None)", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475277552
                __default_140310475277552 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution "${python: toc and 'pat-autotoc' or ''}" (20:22)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c94098580> -> __attr_class
                __token = 669
                __token = 671
                try:
                    __zt_tmp = __attrs_140310475278608
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140310567013776('python', " toc and 'pat-autotoc' or ''", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_class = __attr_class
                if (__attr_class is None):
                    pass
                else:
                    if (__attr_class is _DEFAULT_MARKER):
                        __attr_class = None
                    else:
                        __tt = type(__attr_class)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_class = str(__attr_class)
                        else:
                            if (__tt is bytes):
                                __attr_class = decode(__attr_class)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_class = __attr_class.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_class)
                                        __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                    else:
                                        __attr_class = __attr_class()
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' id="parent-fieldname-text" >')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475277120
                __default_140310475277120 = _DEFAULT_MARKER

                # <Value 'python:context.text.output_relative_to(view.context)' (23:38)> -> __cache_140310475276640
                __token = 858
                try:
                    __zt_tmp = __attrs_140310475278608
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310475276640 = _static_140310567013776('python', 'context.text.output_relative_to(view.context)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:context.text.output_relative_to(view.context)' (23:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94098220> -> __condition
                __expression = __cache_140310475276640

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      Text\n          ')
                else:
                    __content = __cache_140310475276640
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n        </section>\n\n      ')
            if (__backup_toc_140310475253088 is __marker):
                del econtext['toc']
            else:
                econtext['toc'] = __backup_toc_140310475253088
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475209696
            __attrs_140310475209696 = _static_140310566789392
            __previous_i18n_domain_140310475200432 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140310547141952 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f9c94215f90> name=None at 7f9c94268fd0> -> __value
            __value = _static_140310476840848
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475248000
                __attrs_140310475248000 = _static_140310566789392
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140310475209696
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140310567013776('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140310547141952 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140310547141952
            __i18n_domain = __previous_i18n_domain_140310475200432
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }