# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {73: ('view/enabled|nothing', 3, 19), 120: (' view/isViewTemplate|nothin', 4, 25), 185: ('python:enabled and isViewTemplate', 6, 24), 300: ('view/site_url', 11, 26), 422: ('view/next', 16, 16), 452: (' view/previou', 17, 19), 503: ('python:previous is not None or next is not None', 19, 24), 696: ('previous', 24, 24), 748: ('previous/url', 26, 16), 1012: ('previous/title', 35, 29), 1240: ('next', 43, 24), 1288: ('next/url', 45, 16), 1500: ('next/title', 53, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882206291872 = {'class': 'arrow', }
_static_139882206294176 = {'class': 'label', }
_static_139882206284816 = {'class': 'btn btn-sm btn-outline-secondary align-self-end next', 'title': 'Go to next item', 'href': 'next/url', }
_static_139882208508368 = {'class': 'label', }
_static_139882211073216 = {'class': 'arrow', }
_static_139882101369696 = {'class': 'btn btn-sm btn-outline-secondary align-self-start previous', 'title': 'Go to previous item', 'href': 'previous/url', }
_static_139882101363744 = {'class': 'pagination justify-content-between', }
_static_139882337226896 = {}
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882101364464 = {'id': 'section-next-prev', }

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

            # <Static value=<ast.Dict object at 0x7f38d6f656f0> name=None at 7f38d6f677f0> -> __attrs_139882101373248
            __attrs_139882101373248 = _static_139882101364464
            __backup_enabled_139882241829680 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (3:19)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_139882101373248
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/enabled|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_139882101362880 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (4:25)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_139882101373248
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (6:24)> -> __condition
            __token = 185
            try:
                __zt_tmp = __attrs_139882101373248
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('python', 'enabled and isViewTemplate', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139882101372672 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-next-prev" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101374256
                __attrs_139882101374256 = _static_139882337226896
                __backup_portal_url_139882101372432 = get('portal_url', __marker)

                # <Value 'view/site_url' (11:26)> -> __value
                __token = 300
                try:
                    __zt_tmp = __attrs_139882101374256
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/site_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38d6f65420> name=None at 7f38d6f674c0> -> __attrs_139882101361296
                __attrs_139882101361296 = _static_139882101363744
                __backup_next_139882101362784 = get('next', __marker)

                # <Value 'view/next' (16:16)> -> __value
                __token = 422
                try:
                    __zt_tmp = __attrs_139882101361296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/next', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_139882101366336 = get('previous', __marker)

                # <Value 'view/previous' (17:19)> -> __value
                __token = 452
                try:
                    __zt_tmp = __attrs_139882101361296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/previous', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'python:previous is not None or next is not None' (19:24)> -> __condition
                __token = 503
                try:
                    __zt_tmp = __attrs_139882101361296
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('python', 'previous is not None or next is not None', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="pagination justify-content-between" >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f38d6f66b60> name=None at 7f38d6f67c70> -> __attrs_139882101368400
                    __attrs_139882101368400 = _static_139882101369696

                    # <Value 'previous' (24:24)> -> __condition
                    __token = 696
                    try:
                        __zt_tmp = __attrs_139882101368400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('path', 'previous', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-start previous"')

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101374496
                        __default_139882101374496 = _DEFAULT_MARKER

                        # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x7f38d6f67220> at 7f38d6f67fa0> -> __attr_title
                        __attr_title = 'Go to previous item'
                        __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101361344
                        __default_139882101361344 = _DEFAULT_MARKER

                        # <Substitution 'previous/url' (26:16)> -> __attr_href
                        __token = 748
                        try:
                            __zt_tmp = __attrs_139882101368400
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139882257081264('path', 'previous/url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7f38dd805cc0> name=None at 7f38dd72b0a0> -> __attrs_139882208496800
                        __attrs_139882208496800 = _static_139882211073216

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n        ')

                        # <Static value=<ast.Dict object at 0x7f38dd5939d0> name=None at 7f38dd591630> -> __attrs_139882215136544
                        __attrs_139882215136544 = _static_139882208508368

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_139882101924448_itemtitle = ''
                        __stream_139882208498864 = []
                        __append_139882208498864 = __stream_139882208498864.append
                        __append_139882208498864('\n              Previous:\n          ')
                        __stream_139882101924448_itemtitle = []
                        __append_139882101924448_itemtitle = __stream_139882101924448_itemtitle.append

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882237476288
                        __attrs_139882237476288 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882237460544
                        __default_139882237460544 = _DEFAULT_MARKER

                        # <Value 'previous/title' (35:29)> -> __cache_139882237461504
                        __token = 1012
                        try:
                            __zt_tmp = __attrs_139882237476288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882237461504 = _static_139882257081264('path', 'previous/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'previous/title' (35:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df132e30> -> __condition
                        __expression = __cache_139882237461504

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_139882101924448_itemtitle('<span ></span>')
                        else:
                            __content = __cache_139882237461504
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_139882101924448_itemtitle(__content)
                        __append_139882208498864('${itemtitle}')
                        __stream_139882101924448_itemtitle = ''.join(__stream_139882101924448_itemtitle)
                        __append_139882208498864('\n        ')
                        __msgid_139882208498864 = __re_whitespace(''.join(__stream_139882208498864)).strip()
                        if 'label_previous_item':
                            __append(translate('label_previous_item', mapping={'itemtitle': __stream_139882101924448_itemtitle, }, default=__msgid_139882208498864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n      </a>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f38dd374c10> name=None at 7f38e5057f10> -> __attrs_139882206286400
                    __attrs_139882206286400 = _static_139882206284816

                    # <Value 'next' (43:24)> -> __condition
                    __token = 1240
                    try:
                        __zt_tmp = __attrs_139882206286400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('path', 'next', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-end next"')

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206297104
                        __default_139882206297104 = _DEFAULT_MARKER

                        # <Translate msgid='title_next_item' node=<ast.Constant object at 0x7f38dd3741c0> at 7f38dd375360> -> __attr_title
                        __attr_title = 'Go to next item'
                        __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206291392
                        __default_139882206291392 = _DEFAULT_MARKER

                        # <Substitution 'next/url' (45:16)> -> __attr_href
                        __token = 1288
                        try:
                            __zt_tmp = __attrs_139882206286400
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139882257081264('path', 'next/url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7f38dd3770a0> name=None at 7f38dd375660> -> __attrs_139882206286784
                        __attrs_139882206286784 = _static_139882206294176

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_139882101922656_itemtitle = ''
                        __stream_139882206292736 = []
                        __append_139882206292736 = __stream_139882206292736.append
                        __append_139882206292736('\n              Next:\n          ')
                        __stream_139882101922656_itemtitle = []
                        __append_139882101922656_itemtitle = __stream_139882101922656_itemtitle.append

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206296576
                        __attrs_139882206296576 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206296048
                        __default_139882206296048 = _DEFAULT_MARKER

                        # <Value 'next/title' (53:29)> -> __cache_139882206292016
                        __token = 1500
                        try:
                            __zt_tmp = __attrs_139882206296576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882206292016 = _static_139882257081264('path', 'next/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'next/title' (53:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd377250> -> __condition
                        __expression = __cache_139882206292016

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_139882101922656_itemtitle('<span ></span>')
                        else:
                            __content = __cache_139882206292016
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_139882101922656_itemtitle(__content)
                        __append_139882206292736('${itemtitle}')
                        __stream_139882101922656_itemtitle = ''.join(__stream_139882101922656_itemtitle)
                        __append_139882206292736('\n        ')
                        __msgid_139882206292736 = __re_whitespace(''.join(__stream_139882206292736)).strip()
                        if 'label_next_item':
                            __append(translate('label_next_item', mapping={'itemtitle': __stream_139882101922656_itemtitle, }, default=__msgid_139882206292736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n        ')

                        # <Static value=<ast.Dict object at 0x7f38dd3767a0> name=None at 7f38dd376aa0> -> __attrs_139882206287024
                        __attrs_139882206287024 = _static_139882206291872

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n      </a>')
                    __append('\n\n\n    </nav>')
                if (__backup_previous_139882101366336 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_139882101366336
                if (__backup_next_139882101362784 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_139882101362784
                __append('\n\n  ')
                if (__backup_portal_url_139882101372432 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_139882101372432
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_139882101372672
            if (__backup_isViewTemplate_139882101362880 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_139882101362880
            if (__backup_enabled_139882241829680 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_139882241829680
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }