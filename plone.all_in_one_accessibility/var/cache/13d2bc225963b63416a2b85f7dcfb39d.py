# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/document_actions.pt'

__tokens = {63: ('view/actions', 2, 24), 393: ('nocall: context/@@plone/normalizeString', 17, 28), 451: (" python:context.restrictedTraverse('@@iconresolver'", 18, 17), 557: ('view/actions', 21, 32), 617: ("python:'document-action-' + normalizeString(daction['id'])", 23, 17), 772: ('daction/url', 28, 20), 806: (' daction/link_target|nothin', 29, 21), 855: ('e daction/description|nothi', 30, 19), 958: ("python:icons.tag(daction.get('icon'))", 33, 45), 1031: ('daction/title', 34, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310475281296 = {'href': '', 'target': 'daction/link_target|nothing', 'title': 'daction/description|nothing', }
_static_140310272716336 = {'id': "python:'document-action-' + normalizeString(daction['id'])", }
_static_140310272710720 = {'class': 'list-inline', }
_static_140310272718928 = {'class': 'd-none', }
_static_140310566789392 = {}
_static_140310272706688 = {'class': 'viewlet viewlet-document-actions', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310272719984 = {'id': 'section-document-actions', }

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

            # <Static value=<ast.Dict object at 0x7f9c87f6bc70> name=None at 7f9c87f6bc40> -> __attrs_140310272718112
            __attrs_140310272718112 = _static_140310272719984

            # <Value 'view/actions' (2:24)> -> __condition
            __token = 63
            try:
                __zt_tmp = __attrs_140310272718112
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'view/actions', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140310272716672 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-document-actions" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c87f68880> name=None at 7f9c87f6bf70> -> __attrs_140310272714176
                __attrs_140310272714176 = _static_140310272706688

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet viewlet-document-actions">\n    ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272717056
                __attrs_140310272717056 = _static_140310566789392
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f9c87f6b850> name=None at 7f9c87f69120> -> __attrs_140310272713120
                __attrs_140310272713120 = _static_140310272718928

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="d-none" >')
                __stream_140310272714704 = []
                __append_140310272714704 = __stream_140310272714704.append
                __append_140310272714704('\n              Document Actions\n      ')
                __msgid_140310272714704 = __re_whitespace(''.join(__stream_140310272714704)).strip()
                if 'heading_document_actions':
                    __append(translate('heading_document_actions', mapping=None, default=__msgid_140310272714704, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n      ')

                # <Static value=<ast.Dict object at 0x7f9c87f69840> name=None at 7f9c87f688b0> -> __attrs_140310272710288
                __attrs_140310272710288 = _static_140310272710720
                __backup_normalizeString_140310272708320 = get('normalizeString', __marker)

                # <Value 'nocall: context/@@plone/normalizeString' (17:28)> -> __value
                __token = 393
                try:
                    __zt_tmp = __attrs_140310272710288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('nocall', ' context/@@plone/normalizeString', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['normalizeString'] = __value
                __backup_icons_140310272707408 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (18:17)> -> __value
                __token = 451
                try:
                    __zt_tmp = __attrs_140310272710288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['icons'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="list-inline" >\n        ')

                # <Static value=<ast.Dict object at 0x7f9c87f6ae30> name=None at 7f9c87f6ad40> -> __attrs_140310475411072
                __attrs_140310475411072 = _static_140310272716336
                __backup_daction_140310272716480 = get('daction', __marker)

                # <Value 'view/actions' (21:32)> -> __iterator
                __token = 557
                try:
                    __zt_tmp = __attrs_140310475411072
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140310567013776('path', 'view/actions', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                (__iterator, ____index_140310475408480, ) = getname('repeat')('daction', __iterator)
                econtext['daction'] = None
                for __item in __iterator:
                    econtext['daction'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272709568
                    __default_140310272709568 = _DEFAULT_MARKER

                    # <Substitution "python:'document-action-' + normalizeString(daction['id'])" (23:17)> -> __attr_id
                    __token = 617
                    try:
                        __zt_tmp = __attrs_140310475411072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140310567013776('python', "'document-action-' + normalizeString(daction['id'])", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7f9c94099390> name=None at 7f9c940ba140> -> __attrs_140310475282688
                    __attrs_140310475282688 = _static_140310475281296

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475290656
                    __default_140310475290656 = _DEFAULT_MARKER

                    # <Substitution 'daction/url' (28:20)> -> __attr_href
                    __token = 772
                    try:
                        __zt_tmp = __attrs_140310475282688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140310567013776('path', 'daction/url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475277984
                    __default_140310475277984 = _DEFAULT_MARKER

                    # <Substitution 'daction/link_target|nothing' (29:21)> -> __attr_target
                    __token = 806
                    try:
                        __zt_tmp = __attrs_140310475282688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_140310567013776('path', 'daction/link_target|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((' target="%s"' % __attr_target))

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475277312
                    __default_140310475277312 = _DEFAULT_MARKER

                    # <Substitution 'daction/description|nothing' (30:19)> -> __attr_title
                    __token = 855
                    try:
                        __zt_tmp = __attrs_140310475282688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140310567013776('path', 'daction/description|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475288880
                    __attrs_140310475288880 = _static_140310566789392

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475281776
                    __default_140310475281776 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(daction.get('icon'))" (33:45)> -> __cache_140310475281632
                    __token = 958
                    try:
                        __zt_tmp = __attrs_140310475288880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475281632 = _static_140310567013776('python', "icons.tag(daction.get('icon'))", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(daction.get('icon'))" (33:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9409b9d0> -> __condition
                    __expression = __cache_140310475281632

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310475281632
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475283792
                    __attrs_140310475283792 = _static_140310566789392

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475280336
                    __default_140310475280336 = _DEFAULT_MARKER

                    # <Value 'daction/title' (34:31)> -> __cache_140310475287776
                    __token = 1031
                    try:
                        __zt_tmp = __attrs_140310475283792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475287776 = _static_140310567013776('path', 'daction/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'daction/title' (34:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94098970> -> __condition
                    __expression = __cache_140310475287776

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n                            Menu Title\n            </span>')
                    else:
                        __content = __cache_140310475287776
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          </a>\n        </li>')
                    ____index_140310475408480 -= 1
                    if (____index_140310475408480 > 0):
                        __append('\n        ')
                if (__backup_daction_140310272716480 is __marker):
                    del econtext['daction']
                else:
                    econtext['daction'] = __backup_daction_140310272716480
                __append('\n      </ul>')
                if (__backup_icons_140310272707408 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_140310272707408
                if (__backup_normalizeString_140310272708320 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_140310272708320
                __append('\n    \n\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_140310272716672
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }