# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/sections.pt'

__tokens = {218: ('python:view.navtree', 4, 29), 369: ('python:view.render_globalnav()', 11, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272556048 = {'class': 'navbar-toggler-icon', }
_static_140310272544768 = {'class': 'navbar-toggler', 'aria-label': 'Toggle navigation', 'type': 'button', }
_static_140310272541552 = {'class': 'navbar-nav', 'id': 'portal-globalnav', }
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272553792
            __attrs_140310272553792 = _static_140310566789392

            # <Value 'python:view.navtree' (4:29)> -> __condition
            __token = 218
            try:
                __zt_tmp = __attrs_140310272553792
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('python', 'view.navtree', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140310272543472 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c87f40370> name=None at 7f9c87f41e70> -> __attrs_140310272546640
                __attrs_140310272546640 = _static_140310272541552

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="navbar-nav" id="portal-globalnav" >\n    ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272550336
                __attrs_140310272550336 = _static_140310566789392

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272545776
                __default_140310272545776 = _DEFAULT_MARKER

                # <Value 'python:view.render_globalnav()' (11:36)> -> __cache_140310272544672
                __token = 369
                try:
                    __zt_tmp = __attrs_140310272550336
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310272544672 = _static_140310567013776('python', 'view.render_globalnav()', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.render_globalnav()' (11:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f41120> -> __condition
                __expression = __cache_140310272544672

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <navtree ... (0:0)
                    # --------------------------------------------------------
                    __append('<navtree></navtree>')
                else:
                    __content = __cache_140310272544672
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </ul>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c87f41000> name=None at 7f9c87f43a90> -> __attrs_140310272556000
                __attrs_140310272556000 = _static_140310272544768

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="navbar-toggler"')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272556720
                __default_140310272556720 = _DEFAULT_MARKER

                # <Translate msgid='label_toggle_navigation' node=<ast.Constant object at 0x7f9c87f41690> at 7f9c87f42e00> -> __attr_aria_label
                __attr_aria_label = 'Toggle navigation'
                __attr_aria_label = translate('label_toggle_navigation', default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' type="button" >\n    ')

                # <Static value=<ast.Dict object at 0x7f9c87f43c10> name=None at 7f9c87f42740> -> __attrs_140310272556192
                __attrs_140310272556192 = _static_140310272556048

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="navbar-toggler-icon"></span>\n  </button>\n\n')
                __i18n_domain = __previous_i18n_domain_140310272543472
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }