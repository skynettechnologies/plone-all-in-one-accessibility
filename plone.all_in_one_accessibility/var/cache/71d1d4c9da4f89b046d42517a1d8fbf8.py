# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/searchbox.pt'

__tokens = {122: ('view/navigation_root_url', 4, 27), 198: ("d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'}", 9, 15), 207: ("python: view.livesearch and 'pat-livesearch'", 9, 24), 255: ("python: view.show_images and 'show_images'", 9, 72), 421: ('string:${navigation_root_url}/@@search', 14, 17), 490: (' string:ajaxUrl:${navigation_root_url}/@@ajax-searc', 15, 29), 980: ('request/form/SearchableText|nothing', 33, 19), 1439: ('string:${navigation_root_url}/@@search', 51, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882206240608 = {'href': '#', }
_static_139882206248768 = {'class': 'hiddenStructure', 'id': 'portal-advanced-search', }
_static_139882206235184 = {'class': 'searchButton btn btn-outline-light', 'type': 'submit', }
_static_139882206236288 = {'class': 'searchField form-control me-2', 'id': 'searchGadget', 'name': 'SearchableText', 'placeholder': 'Search Site', 'size': '18', 'title': 'Search Site', 'type': 'text', 'value': '', }
_static_139882206232832 = {'class': 'hiddenStructure', 'for': 'searchGadget', }
_static_139882206244544 = {'class': "d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'}", 'id': 'searchGadget_form', 'action': '@@search', 'role': 'search', 'data-pat-livesearch': 'string:ajaxUrl:${navigation_root_url}/@@ajax-search', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882205864544 = {'class': 'd-flex flex-column position-relative', 'id': 'portal-searchbox', }

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

            # <Static value=<ast.Dict object at 0x7f38dd30e260> name=None at 7f38dd30dc90> -> __attrs_139882205859504
            __attrs_139882205859504 = _static_139882205864544
            __backup_navigation_root_url_139882206240080 = get('navigation_root_url', __marker)

            # <Value 'view/navigation_root_url' (4:27)> -> __value
            __token = 122
            try:
                __zt_tmp = __attrs_139882205859504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/navigation_root_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_139882205859840 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="d-flex flex-column position-relative" id="portal-searchbox" >\n\n  ')

            # <Static value=<ast.Dict object at 0x7f38dd36aec0> name=None at 7f38dd3680d0> -> __attrs_139882206245456
            __attrs_139882206245456 = _static_139882206244544

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206235376
            __default_139882206235376 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'}" (9:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd36a950> -> __attr_class
            __token = 198
            __token = 207
            try:
                __zt_tmp = __attrs_139882206245456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139882257081264('python', " view.livesearch and 'pat-livesearch'", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 255
            try:
                __zt_tmp = __attrs_139882206245456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_253 = _static_139882257081264('python', " view.show_images and 'show_images'", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class_253 = __quote(__attr_class_253, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s%s%s' % ('d-flex ', (__attr_class if (__attr_class is not None) else ''), ' ', (__attr_class_253 if (__attr_class_253 is not None) else ''), ))
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append(' id="searchGadget_form"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206240176
            __default_139882206240176 = _DEFAULT_MARKER

            # <Substitution 'string:${navigation_root_url}/@@search' (14:17)> -> __attr_action
            __token = 421
            try:
                __zt_tmp = __attrs_139882206245456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_139882257081264('string', '${navigation_root_url}/@@search', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '@@search', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' role="search"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206246224
            __default_139882206246224 = _DEFAULT_MARKER

            # <Substitution 'string:ajaxUrl:${navigation_root_url}/@@ajax-search' (15:29)> -> __attr_data_pat_livesearch
            __token = 490
            try:
                __zt_tmp = __attrs_139882206245456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_livesearch = _static_139882257081264('string', 'ajaxUrl:${navigation_root_url}/@@ajax-search', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_data_pat_livesearch = __quote(__attr_data_pat_livesearch, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_pat_livesearch is not None):
                __append((' data-pat-livesearch="%s"' % __attr_data_pat_livesearch))
            __append(' >\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd368100> name=None at 7f38dd36a1d0> -> __attrs_139882206243920
            __attrs_139882206243920 = _static_139882206232832

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="hiddenStructure" for="searchGadget" >')
            __stream_139882206234656 = []
            __append_139882206234656 = __stream_139882206234656.append
            __append_139882206234656('Search Site')
            __msgid_139882206234656 = __re_whitespace(''.join(__stream_139882206234656)).strip()
            if 'text_search':
                __append(translate('text_search', mapping=None, default=__msgid_139882206234656, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd368e80> name=None at 7f38dd36add0> -> __attrs_139882206246896
            __attrs_139882206246896 = _static_139882206236288

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="searchField form-control me-2" id="searchGadget" name="SearchableText"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206240800
            __default_139882206240800 = _DEFAULT_MARKER

            # <Translate msgid='title_search_site' node=<ast.Constant object at 0x7f38dd369c60> at 7f38dd36b880> -> __attr_placeholder
            __attr_placeholder = 'Search Site'
            __attr_placeholder = translate('title_search_site', default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_placeholder is not None):
                __append((' placeholder="%s"' % __attr_placeholder))
            __append(' size="18"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206242096
            __default_139882206242096 = _DEFAULT_MARKER

            # <Translate msgid='title_search_site' node=<ast.Constant object at 0x7f38dd369c00> at 7f38dd368280> -> __attr_title
            __attr_title = 'Search Site'
            __attr_title = translate('title_search_site', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' type="text"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206238928
            __default_139882206238928 = _DEFAULT_MARKER

            # <Substitution 'request/form/SearchableText|nothing' (33:19)> -> __attr_value
            __token = 980
            try:
                __zt_tmp = __attrs_139882206246896
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139882257081264('path', 'request/form/SearchableText|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd368a30> name=None at 7f38dd3686d0> -> __attrs_139882206242720
            __attrs_139882206242720 = _static_139882206235184

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="searchButton btn btn-outline-light" type="submit" >')
            __stream_139882206239456 = []
            __append_139882206239456 = __stream_139882206239456.append
            __append_139882206239456('\n      Search\n    ')
            __msgid_139882206239456 = __re_whitespace(''.join(__stream_139882206239456)).strip()
            if 'label_search':
                __append(translate('label_search', mapping=None, default=__msgid_139882206239456, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd36bf40> name=None at 7f38dd369210> -> __attrs_139882206235472
            __attrs_139882206235472 = _static_139882206248768

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="hiddenStructure" id="portal-advanced-search" >\n      ')

            # <Static value=<ast.Dict object at 0x7f38dd369f60> name=None at 7f38dd36b6a0> -> __attrs_139882206246176
            __attrs_139882206246176 = _static_139882206240608

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206234704
            __default_139882206234704 = _DEFAULT_MARKER

            # <Substitution 'string:${navigation_root_url}/@@search' (51:16)> -> __attr_href
            __token = 1439
            try:
                __zt_tmp = __attrs_139882206246176
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139882257081264('string', '${navigation_root_url}/@@search', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')
            __stream_139882206233696 = []
            __append_139882206233696 = __stream_139882206233696.append
            __append_139882206233696('\n          Advanced Search&hellip;\n      ')
            __msgid_139882206233696 = __re_whitespace(''.join(__stream_139882206233696)).strip()
            if 'label_advanced_search':
                __append(translate('label_advanced_search', mapping=None, default=__msgid_139882206233696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n    </div>\n\n  </form>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_139882205859840
            if (__backup_navigation_root_url_139882206240080 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_139882206240080
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }