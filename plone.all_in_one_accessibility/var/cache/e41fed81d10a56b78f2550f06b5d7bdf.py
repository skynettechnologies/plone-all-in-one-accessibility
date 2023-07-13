# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/default_page_warning.pt'

__tokens = {165: ('context/@@plone_context_state/is_default_page|nothing', 6, 22), 444: ('string:${context/aq_inner/aq_parent/absolute_url}/edit', 12, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139962602621584 = {'href': '', }
_static_139962655708768 = __C2ZContextWrapper
_static_139962655709056 = __compile_zt_expr
_static_139962602504144 = {'class': 'alert alert-info', 'role': 'alert', }
_static_139962655435520 = {}

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

            # <Static value=<ast.Dict object at 0x7f4b985beb00> name=None at 7f4b985bee30> -> __attrs_139962602503040
            __attrs_139962602503040 = _static_139962655435520
            __previous_i18n_domain_139962602503184 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f4b95343fd0> name=None at 7f4b95343e80> -> __attrs_139962602619568
            __attrs_139962602619568 = _static_139962602504144

            # <Value 'context/@@plone_context_state/is_default_page|nothing' (6:22)> -> __condition
            __token = 165
            try:
                __zt_tmp = __attrs_139962602619568
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139962655709056('path', 'context/@@plone_context_state/is_default_page|nothing', econtext=econtext)(_static_139962655708768(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info" role="alert" >\n    ')

                # <Static value=<ast.Dict object at 0x7f4b985beb00> name=None at 7f4b985bee30> -> __attrs_139962602620528
                __attrs_139962602620528 = _static_139962655435520

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_139962602286752_go_here = ''
                __stream_139962602435872 = []
                __append_139962602435872 = __stream_139962602435872.append
                __append_139962602435872('\n      You are editing the default view of a container. If you wanted to edit the container itself,\n      ')
                __stream_139962602286752_go_here = []
                __append_139962602286752_go_here = __stream_139962602286752_go_here.append

                # <Static value=<ast.Dict object at 0x7f4b95360a90> name=None at 7f4b95360ac0> -> __attrs_139962602622208
                __attrs_139962602622208 = _static_139962602621584

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_139962602286752_go_here('<a')

                # <Symbol value=<DEFAULT> at 7f4b9858d120> -> __default_139962602621680
                __default_139962602621680 = _DEFAULT_MARKER

                # <Substitution 'string:${context/aq_inner/aq_parent/absolute_url}/edit' (12:16)> -> __attr_href
                __token = 444
                try:
                    __zt_tmp = __attrs_139962602622208
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139962655709056('string', '${context/aq_inner/aq_parent/absolute_url}/edit', econtext=econtext)(_static_139962655708768(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append_139962602286752_go_here((' href="%s"' % __attr_href))
                __append_139962602286752_go_here(' >')
                __stream_139962602621104 = []
                __append_139962602621104 = __stream_139962602621104.append
                __append_139962602621104('go here')
                __msgid_139962602621104 = __re_whitespace(''.join(__stream_139962602621104)).strip()
                if 'label_edit_default_view_container_go_here':
                    __append_139962602286752_go_here(translate('label_edit_default_view_container_go_here', mapping=None, default=__msgid_139962602621104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_139962602286752_go_here('</a>')
                __append_139962602435872('${go_here}')
                __stream_139962602286752_go_here = ''.join(__stream_139962602286752_go_here)
                __append_139962602435872('.\n    ')
                __msgid_139962602435872 = __re_whitespace(''.join(__stream_139962602435872)).strip()
                if 'label_edit_default_view_container':
                    __append(translate('label_edit_default_view_container', mapping={'go_here': __stream_139962602286752_go_here, }, default=__msgid_139962602435872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n  </div>')
            __append('\n')
            __i18n_domain = __previous_i18n_domain_139962602503184
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }