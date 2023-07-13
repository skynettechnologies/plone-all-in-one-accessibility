# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/contentviews.pt'

__tokens = {61: ('context/@@plone', 2, 30), 131: ('ploneview/showToolbar', 4, 33), 240: ('view/tabSet1', 9, 23), 302: ('python: view.menu_template(actions=actions)', 11, 32), 459: ('provider:plone.contentmenu', 17, 34), 606: ('view/tabSet2', 23, 27), 676: ('python: view.menu_template(actions=actions)', 25, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310476016848 = {'class': 'border-top my-2', }
_static_140310476020880 = {'class': 'border-top my-2', }
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476025344
            __attrs_140310476025344 = _static_140310566789392
            __backup_ploneview_140310475670960 = get('ploneview', __marker)

            # <Value 'context/@@plone' (2:30)> -> __value
            __token = 61
            try:
                __zt_tmp = __attrs_140310476025344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'context/@@plone', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value 'ploneview/showToolbar' (4:33)> -> __condition
            __token = 131
            try:
                __zt_tmp = __attrs_140310476025344
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'ploneview/showToolbar', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140310476019728 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476022416
                __attrs_140310476022416 = _static_140310566789392
                __backup_actions_140310475508944 = get('actions', __marker)

                # <Value 'view/tabSet1' (9:23)> -> __value
                __token = 240
                try:
                    __zt_tmp = __attrs_140310476022416
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'view/tabSet1', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476015216
                __attrs_140310476015216 = _static_140310566789392

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476020640
                __default_140310476020640 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (11:32)> -> __cache_140310476021072
                __token = 302
                try:
                    __zt_tmp = __attrs_140310476015216
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310476021072 = _static_140310567013776('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (11:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9414d930> -> __condition
                __expression = __cache_140310476021072

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_140310476021072
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
                if (__backup_actions_140310475508944 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_140310475508944
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c9414dc90> name=None at 7f9c9414c5e0> -> __attrs_140310476017904
                __attrs_140310476017904 = _static_140310476020880

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2">\n\n    ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476018288
                __attrs_140310476018288 = _static_140310566789392
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476013632
                __attrs_140310476013632 = _static_140310566789392

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476016176
                __default_140310476016176 = _DEFAULT_MARKER

                # <Value 'provider:plone.contentmenu' (17:34)> -> __cache_140310476016320
                __token = 459
                try:
                    __zt_tmp = __attrs_140310476013632
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310476016320 = _static_140310567013776('provider', 'plone.contentmenu', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.contentmenu' (17:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9414c7f0> -> __condition
                __expression = __cache_140310476016320

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_140310476016320
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    \n\n    ')

                # <Static value=<ast.Dict object at 0x7f9c9414ccd0> name=None at 7f9c9414cd00> -> __attrs_140310476017040
                __attrs_140310476017040 = _static_140310476016848

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2">\n\n      ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476020208
                __attrs_140310476020208 = _static_140310566789392
                __backup_actions_140310476959280 = get('actions', __marker)

                # <Value 'view/tabSet2' (23:27)> -> __value
                __token = 606
                try:
                    __zt_tmp = __attrs_140310476020208
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'view/tabSet2', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476019968
                __attrs_140310476019968 = _static_140310566789392

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476024720
                __default_140310476024720 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (25:36)> -> __cache_140310476024576
                __token = 676
                try:
                    __zt_tmp = __attrs_140310476019968
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310476024576 = _static_140310567013776('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (25:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9414dff0> -> __condition
                __expression = __cache_140310476024576

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_140310476024576
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')
                if (__backup_actions_140310476959280 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_140310476959280
                __append('\n\n    </li></li>')
                __i18n_domain = __previous_i18n_domain_140310476019728
            if (__backup_ploneview_140310475670960 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_140310475670960
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }