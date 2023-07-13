# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.portlets-5.0.6-py3.10.egg/plone/app/portlets/browser/templates/column.pt'

__tokens = {27: ('options/portlets', 1, 27), 188: ('string:portletwrapper-${portlet/hash}', 5, 12), 252: (' portlet/has', 6, 25), 106: ("python:view.safe_render(portlet['renderer'])", 3, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272337248 = {'class': 'portletWrapper', 'id': 'string:portletwrapper-${portlet/hash}', 'data-portlethash': 'portlet/hash', }
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272327744
            __attrs_140310272327744 = _static_140310566789392
            __backup_portlet_140310272343632 = get('portlet', __marker)

            # <Value 'options/portlets' (1:27)> -> __iterator
            __token = 27
            try:
                __zt_tmp = __attrs_140310272327744
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140310567013776('path', 'options/portlets', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            (__iterator, ____index_140310272339456, ) = getname('repeat')('portlet', __iterator)
            econtext['portlet'] = None
            for __item in __iterator:
                econtext['portlet'] = __item
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f9c87f0e560> name=None at 7f9c87f0db70> -> __attrs_140310272331248
                __attrs_140310272331248 = _static_140310272337248

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portletWrapper"')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272343200
                __default_140310272343200 = _DEFAULT_MARKER

                # <Substitution 'string:portletwrapper-${portlet/hash}' (5:12)> -> __attr_id
                __token = 188
                try:
                    __zt_tmp = __attrs_140310272331248
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140310567013776('string', 'portletwrapper-${portlet/hash}', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272341808
                __default_140310272341808 = _DEFAULT_MARKER

                # <Substitution 'portlet/hash' (6:25)> -> __attr_data_portlethash
                __token = 252
                try:
                    __zt_tmp = __attrs_140310272331248
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_portlethash = _static_140310567013776('path', 'portlet/hash', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                __attr_data_portlethash = __quote(__attr_data_portlethash, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_portlethash is not None):
                    __append((' data-portlethash="%s"' % __attr_data_portlethash))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272330144
                __default_140310272330144 = _DEFAULT_MARKER

                # <Value "python:view.safe_render(portlet['renderer'])" (3:30)> -> __cache_140310272329520
                __token = 106
                try:
                    __zt_tmp = __attrs_140310272331248
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310272329520 = _static_140310567013776('python', "view.safe_render(portlet['renderer'])", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value "python:view.safe_render(portlet['renderer'])" (3:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f0d600> -> __condition
                __expression = __cache_140310272329520

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140310272329520
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n')
                ____index_140310272339456 -= 1
                if (____index_140310272339456 > 0):
                    __append('')
            if (__backup_portlet_140310272343632 is __marker):
                del econtext['portlet']
            else:
                econtext['portlet'] = __backup_portlet_140310272343632
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }