# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Zope-5.8.3-py3.10.egg/Products/Five/utilities/browser/edit_markers.pt'

__tokens = {803: ('request/ACTUAL_URL', 22, 33), 991: ('view/getInterfaceNames', 27, 34), 1141: ('interface/name', 30, 27), 1226: ('view/getDirectlyProvidedNames', 33, 34), 1416: ('interface/name', 36, 38), 1472: (' interface/nam', 37, 40), 1570: ('interface/name', 40, 27), 1648: ('view/getDirectlyProvidedNames', 43, 27), 2151: ('view/getAvailableInterfaceNames', 57, 34), 2340: ('interface/name', 60, 38), 2396: (' interface/nam', 61, 40), 2494: ('interface/name', 64, 27), 2629: ('view/getAvailableInterfaceNames', 67, 70), 23: ('context/@@standard_macros/page', 1, 23), 23: ('context/@@standard_macros/page', 1, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140568624058512 = 'page'
_static_140568624944112 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'SAVE', 'value': 'Add', }
_static_140568624945024 = {'class': 'zmi-controls form-group form-inline', }
_static_140568624944928 = {'class': 'zmi-object-id', }
_static_140568624943824 = {'type': 'checkbox', 'id': 'INTERFACE', 'name': 'add:list', 'value': 'interface/name', }
_static_140568624939744 = {'class': 'zmi-object-check text-right', }
_static_140568624950544 = {'class': 'table table-striped table-hover table-sm', }
_static_140568710484208 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'SAVE', 'value': 'Remove', }
_static_140568624044864 = {'class': 'zmi-controls', }
_static_140568624046496 = {'class': 'zmi-object-check text-right', }
_static_140568624043904 = {'class': 'zmi-object-id', }
_static_140568624044096 = {'type': 'checkbox', 'id': 'INTERFACE', 'name': 'remove:list', 'value': 'interface/name', }
_static_140568624053264 = {'class': 'zmi-object-check text-right', }
_static_140568624052304 = {'class': 'zmi-object-id', }
_static_140568624050864 = {'class': 'zmi-object-check text-right', }
_static_140568624065904 = {'class': 'table table-striped table-hover table-sm', }
_static_140568781877216 = __C2ZContextWrapper
_static_140568781877504 = __compile_zt_expr
_static_140568624059088 = {'action': '.', 'method': 'post', }
_static_140568624069696 = {'class': 'form-help formHelp', }
_static_140568781866176 = {}

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

    def render_heading(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624061872
            __attrs_140568624061872 = _static_140568781866176
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624070320
            __attrs_140568624070320 = _static_140568781866176

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_140568624060864 = []
            __append_140568624060864 = __stream_140568624060864.append
            __append_140568624060864('Assign Marker Interfaces')
            __msgid_140568624060864 = __re_whitespace(''.join(__stream_140568624060864)).strip()
            if 'heading_edit_marker':
                __append(translate('heading_edit_marker', mapping=None, default=__msgid_140568624060864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624070176
            __attrs_140568624070176 = _static_140568781866176
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7fd8aee77c40> name=None at 7fd8aee77c70> -> __attrs_140568624068880
            __attrs_140568624068880 = _static_140568624069696

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help formHelp">')
            __stream_140568624057984 = []
            __append_140568624057984 = __stream_140568624057984.append
            __append_140568624057984('\n      Change the behavior of this object by adding or removing marker\n      interfaces. You can choose one or more interfaces to be added to the\n      list of provided interfaces for this object.\n      ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624060576
            __attrs_140568624060576 = _static_140568781866176

            # <br ... (0:0)
            # --------------------------------------------------------
            __append_140568624057984('<br />\n      A marker interface is used to identify an instance of a piece of\n      content. This allows you to enable and disable views based on marker\n      interfaces for example.\n    ')
            __msgid_140568624057984 = __re_whitespace(''.join(__stream_140568624057984)).strip()
            if __msgid_140568624057984:
                __append(translate(__msgid_140568624057984, mapping=None, default=__msgid_140568624057984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n    \n    ')

            # <Static value=<ast.Dict object at 0x7fd8aee752d0> name=None at 7fd8aee75570> -> __attrs_140568624059184
            __attrs_140568624059184 = _static_140568624059088

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624062880
            __default_140568624062880 = _DEFAULT_MARKER

            # <Substitution 'request/ACTUAL_URL' (22:33)> -> __attr_action
            __token = 803
            try:
                __zt_tmp = __attrs_140568624059184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140568781877504('path', 'request/ACTUAL_URL', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post">\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624069264
            __attrs_140568624069264 = _static_140568781866176

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_140568624054528 = []
            __append_140568624054528 = __stream_140568624054528.append
            __append_140568624054528('Provided interfaces')
            __msgid_140568624054528 = __re_whitespace(''.join(__stream_140568624054528)).strip()
            if 'legend_provided':
                __append(translate('legend_provided', mapping=None, default=__msgid_140568624054528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd8aee76d70> name=None at 7fd8aee76dd0> -> __attrs_140568624065616
            __attrs_140568624065616 = _static_140568624065904

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-striped table-hover table-sm">\n        ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624054080
            __attrs_140568624054080 = _static_140568781866176
            __backup_interface_140568620248672 = get('interface', __marker)

            # <Value 'view/getInterfaceNames' (27:34)> -> __iterator
            __token = 991
            try:
                __zt_tmp = __attrs_140568624054080
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140568781877504('path', 'view/getInterfaceNames', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            (__iterator, ____index_140568624042224, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x7fd8aee732b0> name=None at 7fd8aee73460> -> __attrs_140568624051344
                __attrs_140568624051344 = _static_140568624050864

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">&nbsp;</td>\n          ')

                # <Static value=<ast.Dict object at 0x7fd8aee73850> name=None at 7fd8aee73820> -> __attrs_140568624052544
                __attrs_140568624052544 = _static_140568624052304

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624051008
                __default_140568624051008 = _DEFAULT_MARKER

                # <Value 'interface/name' (30:27)> -> __cache_140568624050336
                __token = 1141
                try:
                    __zt_tmp = __attrs_140568624052544
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140568624050336 = _static_140568781877504('path', 'interface/name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (30:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aee72f80> -> __condition
                __expression = __cache_140568624050336

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_140568624050336
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_140568624042224 -= 1
                if (____index_140568624042224 > 0):
                    __append('\n        ')
            if (__backup_interface_140568620248672 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140568620248672
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624051152
            __attrs_140568624051152 = _static_140568781866176
            __backup_interface_140568620249872 = get('interface', __marker)

            # <Value 'view/getDirectlyProvidedNames' (33:34)> -> __iterator
            __token = 1226
            try:
                __zt_tmp = __attrs_140568624051152
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140568781877504('path', 'view/getDirectlyProvidedNames', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            (__iterator, ____index_140568624053120, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x7fd8aee73c10> name=None at 7fd8aee73cd0> -> __attrs_140568624042992
                __attrs_140568624042992 = _static_140568624053264

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">\n            ')

                # <Static value=<ast.Dict object at 0x7fd8aee71840> name=None at 7fd8aee707f0> -> __attrs_140568624038480
                __attrs_140568624038480 = _static_140568624044096

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="checkbox"')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624041360
                __default_140568624041360 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (36:38)> -> __attr_id
                __token = 1416
                try:
                    __zt_tmp = __attrs_140568624038480
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140568781877504('path', 'interface/name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', 'INTERFACE', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' name="remove:list"')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624041936
                __default_140568624041936 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (37:40)> -> __attr_value
                __token = 1472
                try:
                    __zt_tmp = __attrs_140568624038480
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140568781877504('path', 'interface/name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n          ')

                # <Static value=<ast.Dict object at 0x7fd8aee71780> name=None at 7fd8aee71db0> -> __attrs_140568624044528
                __attrs_140568624044528 = _static_140568624043904

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624048032
                __default_140568624048032 = _DEFAULT_MARKER

                # <Value 'interface/name' (40:27)> -> __cache_140568624041168
                __token = 1570
                try:
                    __zt_tmp = __attrs_140568624044528
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140568624041168 = _static_140568781877504('path', 'interface/name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (40:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aee71d50> -> __condition
                __expression = __cache_140568624041168

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_140568624041168
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_140568624053120 -= 1
                if (____index_140568624053120 > 0):
                    __append('\n        ')
            if (__backup_interface_140568620249872 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140568620249872
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624053312
            __attrs_140568624053312 = _static_140568781866176

            # <Value 'view/getDirectlyProvidedNames' (43:27)> -> __condition
            __token = 1648
            try:
                __zt_tmp = __attrs_140568624053312
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140568781877504('path', 'view/getDirectlyProvidedNames', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            if __condition:

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x7fd8aee721a0> name=None at 7fd8aee72830> -> __attrs_140568624047504
                __attrs_140568624047504 = _static_140568624046496

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">&nbsp;</td>\n          ')

                # <Static value=<ast.Dict object at 0x7fd8aee71b40> name=None at 7fd8aee71ba0> -> __attrs_140568624044576
                __attrs_140568624044576 = _static_140568624044864

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-controls">\n            ')

                # <Static value=<ast.Dict object at 0x7fd8b40e10f0> name=None at 7fd8b40e0340> -> __attrs_140568624045152
                __attrs_140568624045152 = _static_140568710484208

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="SAVE"')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624046832
                __default_140568624046832 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fd8aee71c90> at 7fd8aee73d00> -> __attr_value
                __attr_value = 'Remove'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n        </tr>')
            __append('\n      </table>\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624941808
            __attrs_140568624941808 = _static_140568781866176

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_140568624046880 = []
            __append_140568624046880 = __stream_140568624046880.append
            __append_140568624046880('\n        Available Marker Interfaces\n      ')
            __msgid_140568624046880 = __re_whitespace(''.join(__stream_140568624046880)).strip()
            if 'legend_available_marker':
                __append(translate('legend_available_marker', mapping=None, default=__msgid_140568624046880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd8aef4ed10> name=None at 7fd8aef4fc70> -> __attrs_140568624942192
            __attrs_140568624942192 = _static_140568624950544

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-striped table-hover table-sm">\n        ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624939408
            __attrs_140568624939408 = _static_140568781866176
            __backup_interface_140568620249680 = get('interface', __marker)

            # <Value 'view/getAvailableInterfaceNames' (57:34)> -> __iterator
            __token = 2151
            try:
                __zt_tmp = __attrs_140568624939408
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140568781877504('path', 'view/getAvailableInterfaceNames', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            (__iterator, ____index_140568624953280, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x7fd8aef4c2e0> name=None at 7fd8aef4f0d0> -> __attrs_140568624939888
                __attrs_140568624939888 = _static_140568624939744

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">\n            ')

                # <Static value=<ast.Dict object at 0x7fd8aef4d2d0> name=None at 7fd8aef4d240> -> __attrs_140568624939840
                __attrs_140568624939840 = _static_140568624943824

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="checkbox"')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624940464
                __default_140568624940464 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (60:38)> -> __attr_id
                __token = 2340
                try:
                    __zt_tmp = __attrs_140568624939840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140568781877504('path', 'interface/name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', 'INTERFACE', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' name="add:list"')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624940704
                __default_140568624940704 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (61:40)> -> __attr_value
                __token = 2396
                try:
                    __zt_tmp = __attrs_140568624939840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140568781877504('path', 'interface/name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n          ')

                # <Static value=<ast.Dict object at 0x7fd8aef4d720> name=None at 7fd8aef4d6f0> -> __attrs_140568624952656
                __attrs_140568624952656 = _static_140568624944928

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624954720
                __default_140568624954720 = _DEFAULT_MARKER

                # <Value 'interface/name' (64:27)> -> __cache_140568624943632
                __token = 2494
                try:
                    __zt_tmp = __attrs_140568624952656
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140568624943632 = _static_140568781877504('path', 'interface/name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (64:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aef4fe20> -> __condition
                __expression = __cache_140568624943632

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_140568624943632
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_140568624953280 -= 1
                if (____index_140568624953280 > 0):
                    __append('\n        ')
            if (__backup_interface_140568620249680 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140568620249680
            __append('\n      </table>\n      ')

            # <Static value=<ast.Dict object at 0x7fd8aef4d780> name=None at 7fd8aef4ded0> -> __attrs_140568624945072
            __attrs_140568624945072 = _static_140568624945024

            # <Value 'view/getAvailableInterfaceNames' (67:70)> -> __condition
            __token = 2629
            try:
                __zt_tmp = __attrs_140568624945072
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140568781877504('path', 'view/getAvailableInterfaceNames', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="zmi-controls form-group form-inline">\n            ')

                # <Static value=<ast.Dict object at 0x7fd8aef4d3f0> name=None at 7fd8aef4d8d0> -> __attrs_140568624943248
                __attrs_140568624943248 = _static_140568624944112

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="SAVE"')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624951792
                __default_140568624951792 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fd8aef4f310> at 7fd8aef4f280> -> __attr_value
                __attr_value = 'Add'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n      </div>')
            __append('\n    </form>\n  ')
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

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624057504
            __attrs_140568624057504 = _static_140568781866176
            __backup_macroname_140568620373632 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd8aee75090> name=None at 7fd8aee74cd0> -> __value
            __value = _static_140568624058512
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624055776
                __attrs_140568624055776 = _static_140568781866176
                __append('\n\n  ')
                __token = None
                render_heading(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n  \n  ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'context/@@standard_macros/page' (1:23)> -> __macro
            __token = 23
            try:
                __zt_tmp = __attrs_140568624057504
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140568781877504('path', 'context/@@standard_macros/page', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            __token = 23
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140568620373632 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140568620373632
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_heading': render_heading, 'render_main': render_main, 'render': render, }