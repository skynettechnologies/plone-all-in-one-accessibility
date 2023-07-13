# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/searchbox.pt'

__tokens = {122: ('view/navigation_root_url', 4, 27), 198: ("d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'}", 9, 15), 207: ("python: view.livesearch and 'pat-livesearch'", 9, 24), 255: ("python: view.show_images and 'show_images'", 9, 72), 421: ('string:${navigation_root_url}/@@search', 14, 17), 490: (' string:ajaxUrl:${navigation_root_url}/@@ajax-searc', 15, 29), 980: ('request/form/SearchableText|nothing', 33, 19), 1439: ('string:${navigation_root_url}/@@search', 51, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310476961728 = {'href': '#', }
_static_140310476955680 = {'class': 'hiddenStructure', 'id': 'portal-advanced-search', }
_static_140310272575904 = {'class': 'searchButton btn btn-outline-light', 'type': 'submit', }
_static_140310272580656 = {'class': 'searchField form-control me-2', 'id': 'searchGadget', 'name': 'SearchableText', 'placeholder': 'Search Site', 'size': '18', 'title': 'Search Site', 'type': 'text', 'value': '', }
_static_140310272579840 = {'class': 'hiddenStructure', 'for': 'searchGadget', }
_static_140310272587424 = {'class': "d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'}", 'id': 'searchGadget_form', 'action': '@@search', 'role': 'search', 'data-pat-livesearch': 'string:ajaxUrl:${navigation_root_url}/@@ajax-search', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310272582624 = {'class': 'd-flex flex-column position-relative', 'id': 'portal-searchbox', }

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

            # <Static value=<ast.Dict object at 0x7f9c87f4a3e0> name=None at 7f9c87f4bdf0> -> __attrs_140310272576960
            __attrs_140310272576960 = _static_140310272582624
            __backup_navigation_root_url_140310272553168 = get('navigation_root_url', __marker)

            # <Value 'view/navigation_root_url' (4:27)> -> __value
            __token = 122
            try:
                __zt_tmp = __attrs_140310272576960
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/navigation_root_url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_140310272589632 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="d-flex flex-column position-relative" id="portal-searchbox" >\n\n  ')

            # <Static value=<ast.Dict object at 0x7f9c87f4b6a0> name=None at 7f9c87f4b610> -> __attrs_140310272574080
            __attrs_140310272574080 = _static_140310272587424

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272574320
            __default_140310272574320 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'}" (9:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c87f48ee0> -> __attr_class
            __token = 198
            __token = 207
            try:
                __zt_tmp = __attrs_140310272574080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140310567013776('python', " view.livesearch and 'pat-livesearch'", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 255
            try:
                __zt_tmp = __attrs_140310272574080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_253 = _static_140310567013776('python', " view.show_images and 'show_images'", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
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

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272588912
            __default_140310272588912 = _DEFAULT_MARKER

            # <Substitution 'string:${navigation_root_url}/@@search' (14:17)> -> __attr_action
            __token = 421
            try:
                __zt_tmp = __attrs_140310272574080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140310567013776('string', '${navigation_root_url}/@@search', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '@@search', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' role="search"')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272584400
            __default_140310272584400 = _DEFAULT_MARKER

            # <Substitution 'string:ajaxUrl:${navigation_root_url}/@@ajax-search' (15:29)> -> __attr_data_pat_livesearch
            __token = 490
            try:
                __zt_tmp = __attrs_140310272574080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_livesearch = _static_140310567013776('string', 'ajaxUrl:${navigation_root_url}/@@ajax-search', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_data_pat_livesearch = __quote(__attr_data_pat_livesearch, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_pat_livesearch is not None):
                __append((' data-pat-livesearch="%s"' % __attr_data_pat_livesearch))
            __append(' >\n\n    ')

            # <Static value=<ast.Dict object at 0x7f9c87f49900> name=None at 7f9c87f48fd0> -> __attrs_140310272577104
            __attrs_140310272577104 = _static_140310272579840

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="hiddenStructure" for="searchGadget" >')
            __stream_140310272588528 = []
            __append_140310272588528 = __stream_140310272588528.append
            __append_140310272588528('Search Site')
            __msgid_140310272588528 = __re_whitespace(''.join(__stream_140310272588528)).strip()
            if 'text_search':
                __append(translate('text_search', mapping=None, default=__msgid_140310272588528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f9c87f49c30> name=None at 7f9c87f49e40> -> __attrs_140310272583536
            __attrs_140310272583536 = _static_140310272580656

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="searchField form-control me-2" id="searchGadget" name="SearchableText"')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272583920
            __default_140310272583920 = _DEFAULT_MARKER

            # <Translate msgid='title_search_site' node=<ast.Constant object at 0x7f9c87f4afb0> at 7f9c87f49ed0> -> __attr_placeholder
            __attr_placeholder = 'Search Site'
            __attr_placeholder = translate('title_search_site', default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_placeholder is not None):
                __append((' placeholder="%s"' % __attr_placeholder))
            __append(' size="18"')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272583296
            __default_140310272583296 = _DEFAULT_MARKER

            # <Translate msgid='title_search_site' node=<ast.Constant object at 0x7f9c87f4a050> at 7f9c87f4a170> -> __attr_title
            __attr_title = 'Search Site'
            __attr_title = translate('title_search_site', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' type="text"')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272582768
            __default_140310272582768 = _DEFAULT_MARKER

            # <Substitution 'request/form/SearchableText|nothing' (33:19)> -> __attr_value
            __token = 980
            try:
                __zt_tmp = __attrs_140310272583536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140310567013776('path', 'request/form/SearchableText|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n    ')

            # <Static value=<ast.Dict object at 0x7f9c87f489a0> name=None at 7f9c87f49840> -> __attrs_140310476950208
            __attrs_140310476950208 = _static_140310272575904

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="searchButton btn btn-outline-light" type="submit" >')
            __stream_140310272582720 = []
            __append_140310272582720 = __stream_140310272582720.append
            __append_140310272582720('\n      Search\n    ')
            __msgid_140310272582720 = __re_whitespace(''.join(__stream_140310272582720)).strip()
            if 'label_search':
                __append(translate('label_search', mapping=None, default=__msgid_140310272582720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f9c94232020> name=None at 7f9c94232a40> -> __attrs_140310476962016
            __attrs_140310476962016 = _static_140310476955680

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="hiddenStructure" id="portal-advanced-search" >\n      ')

            # <Static value=<ast.Dict object at 0x7f9c942337c0> name=None at 7f9c94231180> -> __attrs_140310476963648
            __attrs_140310476963648 = _static_140310476961728

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476956976
            __default_140310476956976 = _DEFAULT_MARKER

            # <Substitution 'string:${navigation_root_url}/@@search' (51:16)> -> __attr_href
            __token = 1439
            try:
                __zt_tmp = __attrs_140310476963648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140310567013776('string', '${navigation_root_url}/@@search', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')
            __stream_140310476950256 = []
            __append_140310476950256 = __stream_140310476950256.append
            __append_140310476950256('\n          Advanced Search&hellip;\n      ')
            __msgid_140310476950256 = __re_whitespace(''.join(__stream_140310476950256)).strip()
            if 'label_advanced_search':
                __append(translate('label_advanced_search', mapping=None, default=__msgid_140310476950256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n    </div>\n\n  </form>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140310272589632
            if (__backup_navigation_root_url_140310272553168 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_140310272553168
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }