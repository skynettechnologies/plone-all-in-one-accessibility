# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/document_actions.pt'

__tokens = {63: ('view/actions', 2, 24), 393: ('nocall: context/@@plone/normalizeString', 17, 28), 451: (" python:context.restrictedTraverse('@@iconresolver'", 18, 17), 557: ('view/actions', 21, 32), 617: ("python:'document-action-' + normalizeString(daction['id'])", 23, 17), 772: ('daction/url', 28, 20), 806: (' daction/link_target|nothin', 29, 21), 855: ('e daction/description|nothi', 30, 19), 958: ("python:icons.tag(daction.get('icon'))", 33, 45), 1031: ('daction/title', 34, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882245436992 = {'href': '', 'target': 'daction/link_target|nothing', 'title': 'daction/description|nothing', }
_static_139882241828240 = {'id': "python:'document-action-' + normalizeString(daction['id'])", }
_static_139882241829008 = {'class': 'list-inline', }
_static_139882241824352 = {'class': 'd-none', }
_static_139882337226896 = {}
_static_139882241827328 = {'class': 'viewlet viewlet-document-actions', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882241821328 = {'id': 'section-document-actions', }

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

            # <Static value=<ast.Dict object at 0x7f38df558a90> name=None at 7f38df55a6b0> -> __attrs_139882241833568
            __attrs_139882241833568 = _static_139882241821328

            # <Value 'view/actions' (2:24)> -> __condition
            __token = 63
            try:
                __zt_tmp = __attrs_139882241833568
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('path', 'view/actions', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139882241820224 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-document-actions" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38df55a200> name=None at 7f38df55b820> -> __attrs_139882241820368
                __attrs_139882241820368 = _static_139882241827328

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet viewlet-document-actions">\n    ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241819168
                __attrs_139882241819168 = _static_139882337226896
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f38df559660> name=None at 7f38df5597e0> -> __attrs_139882241829728
                __attrs_139882241829728 = _static_139882241824352

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="d-none" >')
                __stream_139882241821520 = []
                __append_139882241821520 = __stream_139882241821520.append
                __append_139882241821520('\n              Document Actions\n      ')
                __msgid_139882241821520 = __re_whitespace(''.join(__stream_139882241821520)).strip()
                if 'heading_document_actions':
                    __append(translate('heading_document_actions', mapping=None, default=__msgid_139882241821520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n      ')

                # <Static value=<ast.Dict object at 0x7f38df55a890> name=None at 7f38df55be20> -> __attrs_139882206467488
                __attrs_139882206467488 = _static_139882241829008
                __backup_normalizeString_139882241829680 = get('normalizeString', __marker)

                # <Value 'nocall: context/@@plone/normalizeString' (17:28)> -> __value
                __token = 393
                try:
                    __zt_tmp = __attrs_139882206467488
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('nocall', ' context/@@plone/normalizeString', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['normalizeString'] = __value
                __backup_icons_139882241826176 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (18:17)> -> __value
                __token = 451
                try:
                    __zt_tmp = __attrs_139882206467488
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['icons'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="list-inline" >\n        ')

                # <Static value=<ast.Dict object at 0x7f38df55a590> name=None at 7f38df55b0a0> -> __attrs_139882245430512
                __attrs_139882245430512 = _static_139882241828240
                __backup_daction_139882241549280 = get('daction', __marker)

                # <Value 'view/actions' (21:32)> -> __iterator
                __token = 557
                try:
                    __zt_tmp = __attrs_139882245430512
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139882257081264('path', 'view/actions', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                (__iterator, ____index_139882245429696, ) = getname('repeat')('daction', __iterator)
                econtext['daction'] = None
                for __item in __iterator:
                    econtext['daction'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245425712
                    __default_139882245425712 = _DEFAULT_MARKER

                    # <Substitution "python:'document-action-' + normalizeString(daction['id'])" (23:17)> -> __attr_id
                    __token = 617
                    try:
                        __zt_tmp = __attrs_139882245430512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139882257081264('python', "'document-action-' + normalizeString(daction['id'])", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7f38df8cb640> name=None at 7f38df8ca8c0> -> __attrs_139882245435024
                    __attrs_139882245435024 = _static_139882245436992

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245438240
                    __default_139882245438240 = _DEFAULT_MARKER

                    # <Substitution 'daction/url' (28:20)> -> __attr_href
                    __token = 772
                    try:
                        __zt_tmp = __attrs_139882245435024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('path', 'daction/url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245435936
                    __default_139882245435936 = _DEFAULT_MARKER

                    # <Substitution 'daction/link_target|nothing' (29:21)> -> __attr_target
                    __token = 806
                    try:
                        __zt_tmp = __attrs_139882245435024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_139882257081264('path', 'daction/link_target|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((' target="%s"' % __attr_target))

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245435552
                    __default_139882245435552 = _DEFAULT_MARKER

                    # <Substitution 'daction/description|nothing' (30:19)> -> __attr_title
                    __token = 855
                    try:
                        __zt_tmp = __attrs_139882245435024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_139882257081264('path', 'daction/description|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n            ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245436416
                    __attrs_139882245436416 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245436656
                    __default_139882245436656 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(daction.get('icon'))" (33:45)> -> __cache_139882245423648
                    __token = 958
                    try:
                        __zt_tmp = __attrs_139882245436416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882245423648 = _static_139882257081264('python', "icons.tag(daction.get('icon'))", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(daction.get('icon'))" (33:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df8c9db0> -> __condition
                    __expression = __cache_139882245423648

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882245423648
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245432240
                    __attrs_139882245432240 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245436176
                    __default_139882245436176 = _DEFAULT_MARKER

                    # <Value 'daction/title' (34:31)> -> __cache_139882245437232
                    __token = 1031
                    try:
                        __zt_tmp = __attrs_139882245432240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882245437232 = _static_139882257081264('path', 'daction/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'daction/title' (34:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df8cb5e0> -> __condition
                    __expression = __cache_139882245437232

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n                            Menu Title\n            </span>')
                    else:
                        __content = __cache_139882245437232
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          </a>\n        </li>')
                    ____index_139882245429696 -= 1
                    if (____index_139882245429696 > 0):
                        __append('\n        ')
                if (__backup_daction_139882241549280 is __marker):
                    del econtext['daction']
                else:
                    econtext['daction'] = __backup_daction_139882241549280
                __append('\n      </ul>')
                if (__backup_icons_139882241826176 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_139882241826176
                if (__backup_normalizeString_139882241829680 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_139882241829680
                __append('\n    \n\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_139882241820224
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }