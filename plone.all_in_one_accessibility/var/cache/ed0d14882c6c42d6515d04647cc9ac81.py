# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {73: ('view/enabled|nothing', 3, 19), 120: (' view/isViewTemplate|nothin', 4, 25), 185: ('python:enabled and isViewTemplate', 6, 24), 300: ('view/site_url', 11, 26), 422: ('view/next', 16, 16), 452: (' view/previou', 17, 19), 503: ('python:previous is not None or next is not None', 19, 24), 696: ('previous', 24, 24), 748: ('previous/url', 26, 16), 1012: ('previous/title', 35, 29), 1240: ('next', 43, 24), 1288: ('next/url', 45, 16), 1500: ('next/title', 53, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272494368 = {'class': 'arrow', }
_static_140310272491680 = {'class': 'label', }
_static_140310272502864 = {'class': 'btn btn-sm btn-outline-secondary align-self-end next', 'title': 'Go to next item', 'href': 'next/url', }
_static_140310272497248 = {'class': 'label', }
_static_140310272499792 = {'class': 'arrow', }
_static_140310272294624 = {'class': 'btn btn-sm btn-outline-secondary align-self-start previous', 'title': 'Go to previous item', 'href': 'previous/url', }
_static_140310272278592 = {'class': 'pagination justify-content-between', }
_static_140310566789392 = {}
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310272281136 = {'id': 'section-next-prev', }

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

            # <Static value=<ast.Dict object at 0x7f9c87f00a30> name=None at 7f9c87f03a90> -> __attrs_140310272279216
            __attrs_140310272279216 = _static_140310272281136
            __backup_enabled_140310272708320 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (3:19)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_140310272279216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/enabled|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_140310272286896 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (4:25)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_140310272279216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (6:24)> -> __condition
            __token = 185
            try:
                __zt_tmp = __attrs_140310272279216
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('python', 'enabled and isViewTemplate', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140310272287760 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-next-prev" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272292512
                __attrs_140310272292512 = _static_140310566789392
                __backup_portal_url_140310272279888 = get('portal_url', __marker)

                # <Value 'view/site_url' (11:26)> -> __value
                __token = 300
                try:
                    __zt_tmp = __attrs_140310272292512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'view/site_url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f9c87f00040> name=None at 7f9c87f001c0> -> __attrs_140310272286944
                __attrs_140310272286944 = _static_140310272278592
                __backup_next_140310272280992 = get('next', __marker)

                # <Value 'view/next' (16:16)> -> __value
                __token = 422
                try:
                    __zt_tmp = __attrs_140310272286944
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'view/next', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_140310272292944 = get('previous', __marker)

                # <Value 'view/previous' (17:19)> -> __value
                __token = 452
                try:
                    __zt_tmp = __attrs_140310272286944
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'view/previous', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'python:previous is not None or next is not None' (19:24)> -> __condition
                __token = 503
                try:
                    __zt_tmp = __attrs_140310272286944
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('python', 'previous is not None or next is not None', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="pagination justify-content-between" >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f9c87f03ee0> name=None at 7f9c87f026b0> -> __attrs_140310272498304
                    __attrs_140310272498304 = _static_140310272294624

                    # <Value 'previous' (24:24)> -> __condition
                    __token = 696
                    try:
                        __zt_tmp = __attrs_140310272498304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140310567013776('path', 'previous', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-start previous"')

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272286512
                        __default_140310272286512 = _DEFAULT_MARKER

                        # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x7f9c87f00d90> at 7f9c87f02380> -> __attr_title
                        __attr_title = 'Go to previous item'
                        __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272293280
                        __default_140310272293280 = _DEFAULT_MARKER

                        # <Substitution 'previous/url' (26:16)> -> __attr_href
                        __token = 748
                        try:
                            __zt_tmp = __attrs_140310272498304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140310567013776('path', 'previous/url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7f9c87f36050> name=None at 7f9c87f357b0> -> __attrs_140310272506704
                        __attrs_140310272506704 = _static_140310272499792

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n        ')

                        # <Static value=<ast.Dict object at 0x7f9c87f35660> name=None at 7f9c87f37ee0> -> __attrs_140310272498496
                        __attrs_140310272498496 = _static_140310272497248

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_140310476097344_itemtitle = ''
                        __stream_140310272501280 = []
                        __append_140310272501280 = __stream_140310272501280.append
                        __append_140310272501280('\n              Previous:\n          ')
                        __stream_140310476097344_itemtitle = []
                        __append_140310476097344_itemtitle = __stream_140310476097344_itemtitle.append

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272506944
                        __attrs_140310272506944 = _static_140310566789392

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272493888
                        __default_140310272493888 = _DEFAULT_MARKER

                        # <Value 'previous/title' (35:29)> -> __cache_140310272494224
                        __token = 1012
                        try:
                            __zt_tmp = __attrs_140310272506944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140310272494224 = _static_140310567013776('path', 'previous/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                        # <BinOp left=<Value 'previous/title' (35:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f35fc0> -> __condition
                        __expression = __cache_140310272494224

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140310476097344_itemtitle('<span ></span>')
                        else:
                            __content = __cache_140310272494224
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140310476097344_itemtitle(__content)
                        __append_140310272501280('${itemtitle}')
                        __stream_140310476097344_itemtitle = ''.join(__stream_140310476097344_itemtitle)
                        __append_140310272501280('\n        ')
                        __msgid_140310272501280 = __re_whitespace(''.join(__stream_140310272501280)).strip()
                        if 'label_previous_item':
                            __append(translate('label_previous_item', mapping={'itemtitle': __stream_140310476097344_itemtitle, }, default=__msgid_140310272501280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n      </a>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f9c87f36c50> name=None at 7f9c87f349d0> -> __attrs_140310272497872
                    __attrs_140310272497872 = _static_140310272502864

                    # <Value 'next' (43:24)> -> __condition
                    __token = 1240
                    try:
                        __zt_tmp = __attrs_140310272497872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140310567013776('path', 'next', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-end next"')

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272505984
                        __default_140310272505984 = _DEFAULT_MARKER

                        # <Translate msgid='title_next_item' node=<ast.Constant object at 0x7f9c87f37a60> at 7f9c87f35570> -> __attr_title
                        __attr_title = 'Go to next item'
                        __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272502528
                        __default_140310272502528 = _DEFAULT_MARKER

                        # <Substitution 'next/url' (45:16)> -> __attr_href
                        __token = 1288
                        try:
                            __zt_tmp = __attrs_140310272497872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140310567013776('path', 'next/url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7f9c87f340a0> name=None at 7f9c87f36590> -> __attrs_140310272500416
                        __attrs_140310272500416 = _static_140310272491680

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_140310476098688_itemtitle = ''
                        __stream_140310272505264 = []
                        __append_140310272505264 = __stream_140310272505264.append
                        __append_140310272505264('\n              Next:\n          ')
                        __stream_140310476098688_itemtitle = []
                        __append_140310476098688_itemtitle = __stream_140310476098688_itemtitle.append

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272499600
                        __attrs_140310272499600 = _static_140310566789392

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272500464
                        __default_140310272500464 = _DEFAULT_MARKER

                        # <Value 'next/title' (53:29)> -> __cache_140310272507136
                        __token = 1500
                        try:
                            __zt_tmp = __attrs_140310272499600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140310272507136 = _static_140310567013776('path', 'next/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                        # <BinOp left=<Value 'next/title' (53:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f35540> -> __condition
                        __expression = __cache_140310272507136

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140310476098688_itemtitle('<span ></span>')
                        else:
                            __content = __cache_140310272507136
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140310476098688_itemtitle(__content)
                        __append_140310272505264('${itemtitle}')
                        __stream_140310476098688_itemtitle = ''.join(__stream_140310476098688_itemtitle)
                        __append_140310272505264('\n        ')
                        __msgid_140310272505264 = __re_whitespace(''.join(__stream_140310272505264)).strip()
                        if 'label_next_item':
                            __append(translate('label_next_item', mapping={'itemtitle': __stream_140310476098688_itemtitle, }, default=__msgid_140310272505264, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n        ')

                        # <Static value=<ast.Dict object at 0x7f9c87f34b20> name=None at 7f9c87f34a00> -> __attrs_140310272505936
                        __attrs_140310272505936 = _static_140310272494368

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n      </a>')
                    __append('\n\n\n    </nav>')
                if (__backup_previous_140310272292944 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_140310272292944
                if (__backup_next_140310272280992 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_140310272280992
                __append('\n\n  ')
                if (__backup_portal_url_140310272279888 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140310272279888
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_140310272287760
            if (__backup_isViewTemplate_140310272286896 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_140310272286896
            if (__backup_enabled_140310272708320 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_140310272708320
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }