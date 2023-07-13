# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/keywords.pt'

__tokens = {75: ('context/Subject|nothing', 3, 22), 120: (' nocall:modules/Products.PythonScripts.standard/url_quot', 4, 20), 214: ('categories', 6, 24), 481: ('categories', 18, 37), 627: ('python:url_quote(category)', 23, 21), 708: ('string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', 26, 16), 851: ('category', 29, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272290016 = {'class': 'btn btn-sm btn-outline-primary', 'href': '#', 'rel': 'nofollow', }
_static_140310566789392 = {}
_static_140310272282432 = {'class': 'card-title section-heading d-none', }
_static_140310272294528 = {'class': 'viewlet keywords-viewlet', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310272279408 = {'id': 'section-category', }

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

            # <Static value=<ast.Dict object at 0x7f9c87f00370> name=None at 7f9c87f009a0> -> __attrs_140310272291408
            __attrs_140310272291408 = _static_140310272279408
            __backup_categories_140310475916672 = get('categories', __marker)

            # <Value 'context/Subject|nothing' (3:22)> -> __value
            __token = 75
            try:
                __zt_tmp = __attrs_140310272291408
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'context/Subject|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['categories'] = __value
            __backup_url_quote_140310272482592 = get('url_quote', __marker)

            # <Value 'nocall:modules/Products.PythonScripts.standard/url_quote' (4:20)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_140310272291408
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('nocall', 'modules/Products.PythonScripts.standard/url_quote', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['url_quote'] = __value

            # <Value 'categories' (6:24)> -> __condition
            __token = 214
            try:
                __zt_tmp = __attrs_140310272291408
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'categories', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140310272289056 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-category" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c87f03e80> name=None at 7f9c87f02290> -> __attrs_140310272278880
                __attrs_140310272278880 = _static_140310272294528

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet keywords-viewlet">\n\n    ')

                # <Static value=<ast.Dict object at 0x7f9c87f00f40> name=None at 7f9c87f03280> -> __attrs_140310272294192
                __attrs_140310272294192 = _static_140310272282432

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-title section-heading d-none" >')
                __stream_140310272287952 = []
                __append_140310272287952 = __stream_140310272287952.append
                __append_140310272287952('\n      Keywords\n    ')
                __msgid_140310272287952 = __re_whitespace(''.join(__stream_140310272287952)).strip()
                if 'section_keywords_heading':
                    __append(translate('section_keywords_heading', mapping=None, default=__msgid_140310272287952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272281376
                __attrs_140310272281376 = _static_140310566789392
                __backup_category_140310476027792 = get('category', __marker)

                # <Value 'categories' (18:37)> -> __iterator
                __token = 481
                try:
                    __zt_tmp = __attrs_140310272281376
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140310567013776('path', 'categories', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                (__iterator, ____index_140310272290592, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f9c87f02ce0> name=None at 7f9c87f01720> -> __attrs_140310272281808
                    __attrs_140310272281808 = _static_140310272290016
                    __backup_quotedCat_140310272302704 = get('quotedCat', __marker)

                    # <Value 'python:url_quote(category)' (23:21)> -> __value
                    __token = 627
                    try:
                        __zt_tmp = __attrs_140310272281808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('python', 'url_quote(category)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['quotedCat'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="btn btn-sm btn-outline-primary"')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272286512
                    __default_140310272286512 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}' (26:16)> -> __attr_href
                    __token = 708
                    try:
                        __zt_tmp = __attrs_140310272281808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140310567013776('string', '${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="nofollow" >\n        ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272289920
                    __attrs_140310272289920 = _static_140310566789392

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272281328
                    __default_140310272281328 = _DEFAULT_MARKER

                    # <Value 'category' (29:27)> -> __cache_140310272289248
                    __token = 851
                    try:
                        __zt_tmp = __attrs_140310272289920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272289248 = _static_140310567013776('path', 'category', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'category' (29:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f01d80> -> __condition
                    __expression = __cache_140310272289248

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310272289248
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>')
                    if (__backup_quotedCat_140310272302704 is __marker):
                        del econtext['quotedCat']
                    else:
                        econtext['quotedCat'] = __backup_quotedCat_140310272302704
                    __append('\n    ')
                    ____index_140310272290592 -= 1
                    if (____index_140310272290592 > 0):
                        __append('')
                if (__backup_category_140310476027792 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_140310476027792
                __append('\n\n  </div>\n\n</section>')
                __i18n_domain = __previous_i18n_domain_140310272289056
            if (__backup_url_quote_140310272482592 is __marker):
                del econtext['url_quote']
            else:
                econtext['url_quote'] = __backup_url_quote_140310272482592
            if (__backup_categories_140310475916672 is __marker):
                del econtext['categories']
            else:
                econtext['categories'] = __backup_categories_140310475916672
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }