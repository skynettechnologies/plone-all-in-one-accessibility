# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/error_message.pt'

__tokens = {390: ('options/error_type|nothing', 11, 26), 441: (' options/error_tb|nothin', 12, 23), 494: ('d options/error_log_id|nothi', 13, 26), 567: ("python:err_type == 'NotFound'", 15, 39), 651: ('nocall:view/@@plone_redirector_view', 17, 51), 1699: ('string:${context/portal_url}/contact-info', 35, 48), 2055: ('redirection_view/find_first_parent', 43, 58), 2149: (' redirection_view/search_for_simila', 44, 58), 2241: ('w context/@@plo', 45, 54), 2311: ('ry context/portal_regis', 46, 51), 2396: ("ion python:registry['plone.types_use_view_action_in_listin", 47, 57), 2512: ("ngth python:registry['plone.search_results_description_len", 48, 52), 2632: ('tring nocall:plone_view/normalize', 49, 55), 2722: ('python:first_parent is not None or similar_items', 50, 48), 3031: ('first_parent/absolute_url | nothing', 56, 52), 3124: ('first_parent/absolute_url', 57, 55), 3206: (" python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId(", 58, 55), 3337: ("l python:result_url + '/view' if result_type in use_view_action else result_u", 59, 46), 3466: ('result_type', 60, 47), 3596: ("python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", 62, 67), 3521: ('${url}', 61, 41), 3523: ('url', 61, 43), 3743: ("python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 63, 57), 3819: ('${first_parent/Title}', 63, 133), 3821: ('first_parent/Title', 63, 135), 3896: ('python:plone_view.cropText(first_parent.Description(), desc_length)', 64, 51), 4134: ('similar_items', 68, 53), 4205: ('similar/getURL', 69, 55), 4276: (' similar/portal_typ', 70, 55), 4344: ("l python:result_url + '/view' if result_type in use_view_action else result_u", 71, 46), 4543: ('string: state-${similar/review_state}', 73, 67), 4468: ('${url}', 72, 41), 4470: ('url', 72, 43), 4640: ("python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 74, 57), 4716: ('${similar/pretty_title_or_id}', 74, 133), 4718: ('similar/pretty_title_or_id', 74, 135), 4801: ("python:plone_view.cropText(similar.Description or '', desc_length)", 75, 51), 5269: ('view/is_manager', 89, 35), 5202: ("python: err_type != 'NotFound'", 88, 41), 5557: ('isManager', 97, 36), 5756: ('err_tb', 102, 37), 5830: ('not:isManager', 105, 40), 6231: ('string:${context/portal_url}/contact-info', 111, 44), 261: ('context/@@main_template/macros/master', 6, 23), 261: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140524118688240 = {'href': '#', }
_static_140524118679968 = {'id': 'content-core', }
_static_140524118632592 = {'class': 'documentFirstHeading', }
_static_140524118678048 = {'class': 'discreet', }
_static_140524118675456 = {'href': '${url}', 'class': "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_140524118638448 = {'class': 'discreet', }
_static_140524118636240 = {'href': '${url}', 'class': "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_140524118631536 = {'id': 'page-not-found-list', }
_static_140524118624720 = {'href': '#', }
_static_140524158533488 = {'class': 'discreet', }
_static_140524158532144 = {'class': 'description', }
_static_140524158530704 = {'id': 'content-core', }
_static_140524158529504 = {'class': 'documentFirstHeading', }
_static_140524170096656 = __C2ZContextWrapper
_static_140524170096944 = __compile_zt_expr
_static_140524158523888 = 'master'
_static_140524250288176 = {}

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

            # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524158523360
            __attrs_140524158523360 = _static_140524250288176
            __previous_i18n_domain_140524158523504 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140524171492352 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fce548d19f0> name=None at 7fce548d1a20> -> __value
            __value = _static_140524158523888
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524158525328
                __attrs_140524158525328 = _static_140524250288176
                __backup_err_type_140524152461424 = get('err_type', __marker)

                # <Value 'options/error_type|nothing' (11:26)> -> __value
                __token = 390
                try:
                    __zt_tmp = __attrs_140524158525328
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140524170096944('path', 'options/error_type|nothing', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                econtext['err_type'] = __value
                __backup_err_tb_140524152458976 = get('err_tb', __marker)

                # <Value 'options/error_tb|nothing' (12:23)> -> __value
                __token = 441
                try:
                    __zt_tmp = __attrs_140524158525328
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140524170096944('path', 'options/error_tb|nothing', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                econtext['err_tb'] = __value
                __backup_err_log_id_140524152457776 = get('err_log_id', __marker)

                # <Value 'options/error_log_id|nothing' (13:26)> -> __value
                __token = 494
                try:
                    __zt_tmp = __attrs_140524158525328
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140524170096944('path', 'options/error_log_id|nothing', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                econtext['err_log_id'] = __value
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524158527152
                __attrs_140524158527152 = _static_140524250288176

                # <Value "python:err_type == 'NotFound'" (15:39)> -> __condition
                __token = 567
                try:
                    __zt_tmp = __attrs_140524158527152
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140524170096944('python', "err_type == 'NotFound'", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524158528160
                    __attrs_140524158528160 = _static_140524250288176
                    __backup_redirection_view_140524152461472 = get('redirection_view', __marker)

                    # <Value 'nocall:view/@@plone_redirector_view' (17:51)> -> __value
                    __token = 651
                    try:
                        __zt_tmp = __attrs_140524158528160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140524170096944('nocall', 'view/@@plone_redirector_view', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    econtext['redirection_view'] = __value
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7fce548d2fe0> name=None at 7fce548d2e60> -> __attrs_140524158529840
                    __attrs_140524158529840 = _static_140524158529504

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')
                    __stream_140524158528976 = []
                    __append_140524158528976 = __stream_140524158528976.append
                    __append_140524158528976('\n                    This page does not seem to exist&hellip;\n                ')
                    __msgid_140524158528976 = __re_whitespace(''.join(__stream_140524158528976)).strip()
                    if 'heading_site_there_seems_to_be_an_error':
                        __append(translate('heading_site_there_seems_to_be_an_error', mapping=None, default=__msgid_140524158528976, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h1>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7fce548d3490> name=None at 7fce548d34c0> -> __attrs_140524158531088
                    __attrs_140524158531088 = _static_140524158530704

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                    ')

                    # <Static value=<ast.Dict object at 0x7fce548d3a30> name=None at 7fce548d3a60> -> __attrs_140524158532528
                    __attrs_140524158532528 = _static_140524158532144

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="description">')
                    __stream_140524158531664 = []
                    __append_140524158531664 = __stream_140524158531664.append
                    __append_140524158531664('\n \t                    We apologize for the inconvenience, but the page you were trying to access is not at this address.\n                        You can use the links below to help you find what you are looking for.\n                     ')
                    __msgid_140524158531664 = __re_whitespace(''.join(__stream_140524158531664)).strip()
                    if 'description_site_error':
                        __append(translate('description_site_error', mapping=None, default=__msgid_140524158531664, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    ')

                    # <Static value=<ast.Dict object at 0x7fce548d3f70> name=None at 7fce548d3fa0> -> __attrs_140524118622512
                    __attrs_140524118622512 = _static_140524158533488

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')
                    __stream_140524150322368_site_admin = ''
                    __stream_140524158533008 = []
                    __append_140524158533008 = __stream_140524158533008.append
                    __append_140524158533008('\n                        If you are certain you have the correct web address but are encountering an error, please\n                        contact the ')
                    __stream_140524150322368_site_admin = []
                    __append_140524150322368_site_admin = __stream_140524150322368_site_admin.append

                    # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118623472
                    __attrs_140524118623472 = _static_140524250288176

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140524150322368_site_admin('<span>\n                        ')

                    # <Static value=<ast.Dict object at 0x7fce522c49d0> name=None at 7fce522c4a00> -> __attrs_140524118625392
                    __attrs_140524118625392 = _static_140524118624720

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140524150322368_site_admin('<a')

                    # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118624864
                    __default_140524118624864 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/portal_url}/contact-info' (35:48)> -> __attr_href
                    __token = 1699
                    try:
                        __zt_tmp = __attrs_140524118625392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140524170096944('string', '${context/portal_url}/contact-info', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140524150322368_site_admin((' href="%s"' % __attr_href))
                    __append_140524150322368_site_admin('>')
                    __stream_140524118624192 = []
                    __append_140524118624192 = __stream_140524118624192.append
                    __append_140524118624192('site administration')
                    __msgid_140524118624192 = __re_whitespace(''.join(__stream_140524118624192)).strip()
                    if 'label_site_administration':
                        __append_140524150322368_site_admin(translate('label_site_administration', mapping=None, default=__msgid_140524118624192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_140524150322368_site_admin('</a></span>')
                    __append_140524158533008('${site_admin}')
                    __stream_140524150322368_site_admin = ''.join(__stream_140524150322368_site_admin)
                    __append_140524158533008('.\n                    ')
                    __msgid_140524158533008 = __re_whitespace(''.join(__stream_140524158533008)).strip()
                    if 'description_site_error_mail_site_admin':
                        __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_140524150322368_site_admin, }, default=__msgid_140524158533008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    ')

                    # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118626016
                    __attrs_140524118626016 = _static_140524250288176

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')
                    __stream_140524118623952 = []
                    __append_140524118623952 = __stream_140524118623952.append
                    __append_140524118623952('\n                    Thank you.\n                    ')
                    __msgid_140524118623952 = __re_whitespace(''.join(__stream_140524118623952)).strip()
                    if 'description_site_error_thank_you':
                        __append(translate('description_site_error_thank_you', mapping=None, default=__msgid_140524118623952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    <!-- Offer search results for suggestions -->\n                    ')

                    # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118627024
                    __attrs_140524118627024 = _static_140524250288176
                    __backup_first_parent_140524152687200 = get('first_parent', __marker)

                    # <Value 'redirection_view/find_first_parent' (43:58)> -> __value
                    __token = 2055
                    try:
                        __zt_tmp = __attrs_140524118627024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140524170096944('path', 'redirection_view/find_first_parent', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    econtext['first_parent'] = __value
                    __backup_similar_items_140524152687104 = get('similar_items', __marker)

                    # <Value 'redirection_view/search_for_similar' (44:58)> -> __value
                    __token = 2149
                    try:
                        __zt_tmp = __attrs_140524118627024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140524170096944('path', 'redirection_view/search_for_similar', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    econtext['similar_items'] = __value
                    __backup_plone_view_140524152687152 = get('plone_view', __marker)

                    # <Value 'context/@@plone' (45:54)> -> __value
                    __token = 2241
                    try:
                        __zt_tmp = __attrs_140524118627024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140524170096944('path', 'context/@@plone', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    econtext['plone_view'] = __value
                    __backup_registry_140524152687536 = get('registry', __marker)

                    # <Value 'context/portal_registry' (46:51)> -> __value
                    __token = 2311
                    try:
                        __zt_tmp = __attrs_140524118627024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140524170096944('path', 'context/portal_registry', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    econtext['registry'] = __value
                    __backup_use_view_action_140524152687584 = get('use_view_action', __marker)

                    # <Value "python:registry['plone.types_use_view_action_in_listings']" (47:57)> -> __value
                    __token = 2396
                    try:
                        __zt_tmp = __attrs_140524118627024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140524170096944('python', "registry['plone.types_use_view_action_in_listings']", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    econtext['use_view_action'] = __value
                    __backup_desc_length_140524152687632 = get('desc_length', __marker)

                    # <Value "python:registry['plone.search_results_description_length']" (48:52)> -> __value
                    __token = 2512
                    try:
                        __zt_tmp = __attrs_140524118627024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140524170096944('python', "registry['plone.search_results_description_length']", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    econtext['desc_length'] = __value
                    __backup_normalizeString_140524152687680 = get('normalizeString', __marker)

                    # <Value 'nocall:plone_view/normalizeString' (49:55)> -> __value
                    __token = 2632
                    try:
                        __zt_tmp = __attrs_140524118627024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140524170096944('nocall', 'plone_view/normalizeString', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value

                    # <Value 'python:first_parent is not None or similar_items' (50:48)> -> __condition
                    __token = 2722
                    try:
                        __zt_tmp = __attrs_140524118627024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140524170096944('python', 'first_parent is not None or similar_items', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    if __condition:
                        __append('\n\n                        ')

                        # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118629712
                        __attrs_140524118629712 = _static_140524250288176

                        # <h2 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h2>')
                        __stream_140524118629232 = []
                        __append_140524118629232 = __stream_140524118629232.append
                        __append_140524118629232('You might have been looking for&hellip;')
                        __msgid_140524118629232 = __re_whitespace(''.join(__stream_140524118629232)).strip()
                        if 'heading_not_found_suggestions':
                            __append(translate('heading_not_found_suggestions', mapping=None, default=__msgid_140524118629232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</h2>\n                        ')

                        # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118630624
                        __attrs_140524118630624 = _static_140524250288176

                        # <nav ... (0:0)
                        # --------------------------------------------------------
                        __append('<nav>\n                        ')

                        # <Static value=<ast.Dict object at 0x7fce522c6470> name=None at 7fce522c64a0> -> __attrs_140524118631968
                        __attrs_140524118631968 = _static_140524118631536

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul id="page-not-found-list">\n\n                        ')

                        # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118632880
                        __attrs_140524118632880 = _static_140524250288176

                        # <Value 'first_parent/absolute_url | nothing' (56:52)> -> __condition
                        __token = 3031
                        try:
                            __zt_tmp = __attrs_140524118632880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140524170096944('path', 'first_parent/absolute_url | nothing', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                        if __condition:
                            __append('\n                            ')

                            # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118634080
                            __attrs_140524118634080 = _static_140524250288176
                            __backup_result_url_140524152695408 = get('result_url', __marker)

                            # <Value 'first_parent/absolute_url' (57:55)> -> __value
                            __token = 3124
                            try:
                                __zt_tmp = __attrs_140524118634080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140524170096944('path', 'first_parent/absolute_url', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_140524152695648 = get('result_type', __marker)

                            # <Value "python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()" (58:55)> -> __value
                            __token = 3206
                            try:
                                __zt_tmp = __attrs_140524118634080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140524170096944('python', "hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_140524152689264 = get('url', __marker)

                            # <Value "python:result_url + '/view' if result_type in use_view_action else result_url" (59:46)> -> __value
                            __token = 3337
                            try:
                                __zt_tmp = __attrs_140524118634080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140524170096944('python', "result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <Value 'result_type' (60:47)> -> __condition
                            __token = 3466
                            try:
                                __zt_tmp = __attrs_140524118634080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140524170096944('path', 'result_type', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append('<li>\n                                ')

                                # <Static value=<ast.Dict object at 0x7fce522c76d0> name=None at 7fce522c7700> -> __attrs_140524118636912
                                __attrs_140524118636912 = _static_140524118636240
                                __backup_item_wf_state_class_140524151063264 = get('item_wf_state_class', __marker)

                                # <Value "python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')" (62:67)> -> __value
                                __token = 3596
                                try:
                                    __zt_tmp = __attrs_140524118636912
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140524170096944('python', "' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                                econtext['item_wf_state_class'] = __value

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118635760
                                __default_140524118635760 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution '${url}' (61:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fce522c75b0> -> __attr_href
                                __token = 3521
                                __token = 3523
                                try:
                                    __zt_tmp = __attrs_140524118636912
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140524170096944('path', 'url', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_href = __attr_href
                                if (__attr_href is None):
                                    pass
                                else:
                                    if (__attr_href is _DEFAULT_MARKER):
                                        __attr_href = None
                                    else:
                                        __tt = type(__attr_href)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __attr_href = str(__attr_href)
                                        else:
                                            if (__tt is bytes):
                                                __attr_href = decode(__attr_href)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __attr_href = __attr_href.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__attr_href)
                                                        __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                                    else:
                                                        __attr_href = __attr_href()
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118636384
                                __default_140524118636384 = _DEFAULT_MARKER

                                # <Substitution "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (63:57)> -> __attr_class
                                __token = 3743
                                try:
                                    __zt_tmp = __attrs_140524118636912
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140524170096944('python', "'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((' class="%s"' % __attr_class))
                                __append('>')

                                # <Interpolation value=<Substitution '${first_parent/Title}' (63:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fce522c7b80> -> __content_140524256913200
                                __token = 3819
                                __token = 3821
                                try:
                                    __zt_tmp = __attrs_140524118636912
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_140524256913200 = _static_140524170096944('path', 'first_parent/Title', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                                __content_140524256913200 = __quote(__content_140524256913200, '\x00', '&#0;', None, None)
                                __content_140524256913200 = __content_140524256913200
                                if (__content_140524256913200 is None):
                                    pass
                                else:
                                    if (__content_140524256913200 is None):
                                        __content_140524256913200 = None
                                    else:
                                        __tt = type(__content_140524256913200)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_140524256913200 = str(__content_140524256913200)
                                        else:
                                            if (__tt is bytes):
                                                __content_140524256913200 = decode(__content_140524256913200)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_140524256913200 = __content_140524256913200.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_140524256913200)
                                                        __content_140524256913200 = (str(__content_140524256913200) if (__content_140524256913200 is __converted) else __converted)
                                                    else:
                                                        __content_140524256913200 = __content_140524256913200()
                                if (__content_140524256913200 is not None):
                                    __append(__content_140524256913200)
                                __append('</a>')
                                if (__backup_item_wf_state_class_140524151063264 is __marker):
                                    del econtext['item_wf_state_class']
                                else:
                                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_140524151063264
                                __append('\n                                ')

                                # <Static value=<ast.Dict object at 0x7fce522c7f70> name=None at 7fce522c7fd0> -> __attrs_140524118672000
                                __attrs_140524118672000 = _static_140524118638448

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span class="discreet">')

                                # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118638208
                                __default_140524118638208 = _DEFAULT_MARKER

                                # <Value 'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> -> __cache_140524118637728
                                __token = 3896
                                try:
                                    __zt_tmp = __attrs_140524118672000
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140524118637728 = _static_140524170096944('python', 'plone_view.cropText(first_parent.Description(), desc_length)', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))

                                # <BinOp left=<Value 'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fce55556a10> at 7fce522c7d60> -> __condition
                                __expression = __cache_140524118637728

                                # <Symbol value=<DEFAULT> at 7fce55556a10> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(' Description ')
                                else:
                                    __content = __cache_140524118637728
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</span>\n                            </li>')
                            if (__backup_url_140524152689264 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_140524152689264
                            if (__backup_result_type_140524152695648 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_140524152695648
                            if (__backup_result_url_140524152695408 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_140524152695408
                            __append('\n                        ')
                        __append('\n\n                        ')

                        # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118672096
                        __attrs_140524118672096 = _static_140524250288176
                        __backup_similar_140524152692672 = get('similar', __marker)

                        # <Value 'similar_items' (68:53)> -> __iterator
                        __token = 4134
                        try:
                            __zt_tmp = __attrs_140524118672096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140524170096944('path', 'similar_items', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                        (__iterator, ____index_140524118672528, ) = getname('repeat')('similar', __iterator)
                        econtext['similar'] = None
                        for __item in __iterator:
                            econtext['similar'] = __item
                            __append('\n                            ')

                            # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118673440
                            __attrs_140524118673440 = _static_140524250288176
                            __backup_result_url_140524152699728 = get('result_url', __marker)

                            # <Value 'similar/getURL' (69:55)> -> __value
                            __token = 4205
                            try:
                                __zt_tmp = __attrs_140524118673440
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140524170096944('path', 'similar/getURL', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_140524152699440 = get('result_type', __marker)

                            # <Value 'similar/portal_type' (70:55)> -> __value
                            __token = 4276
                            try:
                                __zt_tmp = __attrs_140524118673440
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140524170096944('path', 'similar/portal_type', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_140524151064224 = get('url', __marker)

                            # <Value "python:result_url + '/view' if result_type in use_view_action else result_url" (71:46)> -> __value
                            __token = 4344
                            try:
                                __zt_tmp = __attrs_140524118673440
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140524170096944('python', "result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li>\n                                ')

                            # <Static value=<ast.Dict object at 0x7fce522d1000> name=None at 7fce522d1030> -> __attrs_140524118676128
                            __attrs_140524118676128 = _static_140524118675456
                            __backup_item_wf_state_class_140524151064368 = get('item_wf_state_class', __marker)

                            # <Value 'string: state-${similar/review_state}' (73:67)> -> __value
                            __token = 4543
                            try:
                                __zt_tmp = __attrs_140524118676128
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140524170096944('string', ' state-${similar/review_state}', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            econtext['item_wf_state_class'] = __value

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118674976
                            __default_140524118674976 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${url}' (72:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fce522d0ee0> -> __attr_href
                            __token = 4468
                            __token = 4470
                            try:
                                __zt_tmp = __attrs_140524118676128
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_140524170096944('path', 'url', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = __attr_href
                            if (__attr_href is None):
                                pass
                            else:
                                if (__attr_href is _DEFAULT_MARKER):
                                    __attr_href = None
                                else:
                                    __tt = type(__attr_href)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_href = str(__attr_href)
                                    else:
                                        if (__tt is bytes):
                                            __attr_href = decode(__attr_href)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_href = __attr_href.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_href)
                                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                                else:
                                                    __attr_href = __attr_href()
                            if (__attr_href is not None):
                                __append((' href="%s"' % __attr_href))

                            # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118675600
                            __default_140524118675600 = _DEFAULT_MARKER

                            # <Substitution "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (74:57)> -> __attr_class
                            __token = 4640
                            try:
                                __zt_tmp = __attrs_140524118676128
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140524170096944('python', "'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))
                            __append('>')

                            # <Interpolation value=<Substitution '${similar/pretty_title_or_id}' (74:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fce522d14e0> -> __content_140524256913200
                            __token = 4716
                            __token = 4718
                            try:
                                __zt_tmp = __attrs_140524118676128
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_140524256913200 = _static_140524170096944('path', 'similar/pretty_title_or_id', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                            __content_140524256913200 = __quote(__content_140524256913200, '\x00', '&#0;', None, None)
                            __content_140524256913200 = __content_140524256913200
                            if (__content_140524256913200 is None):
                                pass
                            else:
                                if (__content_140524256913200 is None):
                                    __content_140524256913200 = None
                                else:
                                    __tt = type(__content_140524256913200)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_140524256913200 = str(__content_140524256913200)
                                    else:
                                        if (__tt is bytes):
                                            __content_140524256913200 = decode(__content_140524256913200)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_140524256913200 = __content_140524256913200.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_140524256913200)
                                                    __content_140524256913200 = (str(__content_140524256913200) if (__content_140524256913200 is __converted) else __converted)
                                                else:
                                                    __content_140524256913200 = __content_140524256913200()
                            if (__content_140524256913200 is not None):
                                __append(__content_140524256913200)
                            __append('</a>')
                            if (__backup_item_wf_state_class_140524151064368 is __marker):
                                del econtext['item_wf_state_class']
                            else:
                                econtext['item_wf_state_class'] = __backup_item_wf_state_class_140524151064368
                            __append('\n                                ')

                            # <Static value=<ast.Dict object at 0x7fce522d1a20> name=None at 7fce522d1a50> -> __attrs_140524118678432
                            __attrs_140524118678432 = _static_140524118678048

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="discreet">')

                            # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118677472
                            __default_140524118677472 = _DEFAULT_MARKER

                            # <Value "python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> -> __cache_140524118676992
                            __token = 4801
                            try:
                                __zt_tmp = __attrs_140524118678432
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140524118676992 = _static_140524170096944('python', "plone_view.cropText(similar.Description or '', desc_length)", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fce55556a10> at 7fce522d16c0> -> __condition
                            __expression = __cache_140524118676992

                            # <Symbol value=<DEFAULT> at 7fce55556a10> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(' Description ')
                            else:
                                __content = __cache_140524118676992
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</span>\n                            </li>')
                            if (__backup_url_140524151064224 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_140524151064224
                            if (__backup_result_type_140524152699440 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_140524152699440
                            if (__backup_result_url_140524152699728 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_140524152699728
                            __append('\n                        ')
                            ____index_140524118672528 -= 1
                            if (____index_140524118672528 > 0):
                                __append('')
                        if (__backup_similar_140524152692672 is __marker):
                            del econtext['similar']
                        else:
                            econtext['similar'] = __backup_similar_140524152692672
                        __append('\n\n                        </ul>\n                        </nav>\n\n                    ')
                    if (__backup_normalizeString_140524152687680 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_140524152687680
                    if (__backup_desc_length_140524152687632 is __marker):
                        del econtext['desc_length']
                    else:
                        econtext['desc_length'] = __backup_desc_length_140524152687632
                    if (__backup_use_view_action_140524152687584 is __marker):
                        del econtext['use_view_action']
                    else:
                        econtext['use_view_action'] = __backup_use_view_action_140524152687584
                    if (__backup_registry_140524152687536 is __marker):
                        del econtext['registry']
                    else:
                        econtext['registry'] = __backup_registry_140524152687536
                    if (__backup_plone_view_140524152687152 is __marker):
                        del econtext['plone_view']
                    else:
                        econtext['plone_view'] = __backup_plone_view_140524152687152
                    if (__backup_similar_items_140524152687104 is __marker):
                        del econtext['similar_items']
                    else:
                        econtext['similar_items'] = __backup_similar_items_140524152687104
                    if (__backup_first_parent_140524152687200 is __marker):
                        del econtext['first_parent']
                    else:
                        econtext['first_parent'] = __backup_first_parent_140524152687200
                    __append('\n                </div>\n            ')
                    if (__backup_redirection_view_140524152461472 is __marker):
                        del econtext['redirection_view']
                    else:
                        econtext['redirection_view'] = __backup_redirection_view_140524152461472
                    __append('\n\n        ')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524158527968
                __attrs_140524158527968 = _static_140524250288176
                __backup_isManager_140524152684608 = get('isManager', __marker)

                # <Value 'view/is_manager' (89:35)> -> __value
                __token = 5269
                try:
                    __zt_tmp = __attrs_140524158527968
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140524170096944('path', 'view/is_manager', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                econtext['isManager'] = __value

                # <Value "python: err_type != 'NotFound'" (88:41)> -> __condition
                __token = 5202
                try:
                    __zt_tmp = __attrs_140524158527968
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140524170096944('python', " err_type != 'NotFound'", econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7fce522c6890> name=None at 7fce522c6bc0> -> __attrs_140524118679104
                    __attrs_140524118679104 = _static_140524118632592

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')
                    __stream_140524118634800 = []
                    __append_140524118634800 = __stream_140524118634800.append
                    __append_140524118634800('\n                We&#8217;re sorry, but there seems to be an error&hellip;\n            ')
                    __msgid_140524118634800 = __re_whitespace(''.join(__stream_140524118634800)).strip()
                    if 'heading_site_error_sorry':
                        __append(translate('heading_site_error_sorry', mapping=None, default=__msgid_140524118634800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h1>\n\n            ')

                    # <Static value=<ast.Dict object at 0x7fce522d21a0> name=None at 7fce522d21d0> -> __attrs_140524118680352
                    __attrs_140524118680352 = _static_140524118679968

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')

                    # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118681312
                    __attrs_140524118681312 = _static_140524250288176

                    # <Value 'isManager' (97:36)> -> __condition
                    __token = 5557
                    try:
                        __zt_tmp = __attrs_140524118681312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140524170096944('path', 'isManager', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>\n                   ')

                        # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118682560
                        __attrs_140524118682560 = _static_140524250288176

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_140524118682080 = []
                        __append_140524118682080 = __stream_140524118682080.append
                        __append_140524118682080('\n                   Here is the full error message:\n                   ')
                        __msgid_140524118682080 = __re_whitespace(''.join(__stream_140524118682080)).strip()
                        if 'description_site_admin_full_error':
                            __append(translate('description_site_admin_full_error', mapping=None, default=__msgid_140524118682080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>\n\n                   ')

                        # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118684096
                        __attrs_140524118684096 = _static_140524250288176

                        # <pre ... (0:0)
                        # --------------------------------------------------------
                        __append('<pre>')

                        # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118683520
                        __default_140524118683520 = _DEFAULT_MARKER

                        # <Value 'err_tb' (102:37)> -> __cache_140524118683040
                        __token = 5756
                        try:
                            __zt_tmp = __attrs_140524118684096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140524118683040 = _static_140524170096944('path', 'err_tb', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))

                        # <BinOp left=<Value 'err_tb' (102:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fce55556a10> at 7fce522d2e60> -> __condition
                        __expression = __cache_140524118683040

                        # <Symbol value=<DEFAULT> at 7fce55556a10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140524118683040
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</pre>\n                </div>')
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118684672
                    __attrs_140524118684672 = _static_140524250288176

                    # <Value 'not:isManager' (105:40)> -> __condition
                    __token = 5830
                    try:
                        __zt_tmp = __attrs_140524118684672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140524170096944('not', 'isManager', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                    ')

                        # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118685920
                        __attrs_140524118685920 = _static_140524250288176

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_140524150321920_site_admin = ''
                        __stream_140524118685440 = []
                        __append_140524118685440 = __stream_140524118685440.append
                        __append_140524118685440('\n                    If you are certain you have the correct web address but are encountering an error, please\n                    contact the ')
                        __stream_140524150321920_site_admin = []
                        __append_140524150321920_site_admin = __stream_140524150321920_site_admin.append

                        # <Static value=<ast.Dict object at 0x7fce5a055030> name=None at 7fce5a055300> -> __attrs_140524118686880
                        __attrs_140524118686880 = _static_140524250288176

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_140524150321920_site_admin('<span>\n                    ')

                        # <Static value=<ast.Dict object at 0x7fce522d41f0> name=None at 7fce522d3fd0> -> __attrs_140524118688864
                        __attrs_140524118688864 = _static_140524118688240

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_140524150321920_site_admin('<a')

                        # <Symbol value=<DEFAULT> at 7fce55556a10> -> __default_140524118688336
                        __default_140524118688336 = _DEFAULT_MARKER

                        # <Substitution 'string:${context/portal_url}/contact-info' (111:44)> -> __attr_href
                        __token = 6231
                        try:
                            __zt_tmp = __attrs_140524118688864
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140524170096944('string', '${context/portal_url}/contact-info', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_140524150321920_site_admin((' href="%s"' % __attr_href))
                        __append_140524150321920_site_admin('>')
                        __stream_140524118687600 = []
                        __append_140524118687600 = __stream_140524118687600.append
                        __append_140524118687600('site administration')
                        __msgid_140524118687600 = __re_whitespace(''.join(__stream_140524118687600)).strip()
                        if 'label_site_admin':
                            __append_140524150321920_site_admin(translate('label_site_admin', mapping=None, default=__msgid_140524118687600, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append_140524150321920_site_admin('</a></span>')
                        __append_140524118685440('${site_admin}')
                        __stream_140524150321920_site_admin = ''.join(__stream_140524150321920_site_admin)
                        __append_140524118685440('.\n                    ')
                        __msgid_140524118685440 = __re_whitespace(''.join(__stream_140524118685440)).strip()
                        if 'description_site_error_mail_site_admin':
                            __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_140524150321920_site_admin, }, default=__msgid_140524118685440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>\n                ')
                    __append('\n            </div>\n\n        ')
                if (__backup_isManager_140524152684608 is __marker):
                    del econtext['isManager']
                else:
                    econtext['isManager'] = __backup_isManager_140524152684608
                __append('\n\n')
                if (__backup_err_log_id_140524152457776 is __marker):
                    del econtext['err_log_id']
                else:
                    econtext['err_log_id'] = __backup_err_log_id_140524152457776
                if (__backup_err_tb_140524152458976 is __marker):
                    del econtext['err_tb']
                else:
                    econtext['err_tb'] = __backup_err_tb_140524152458976
                if (__backup_err_type_140524152461424 is __marker):
                    del econtext['err_type']
                else:
                    econtext['err_type'] = __backup_err_type_140524152461424
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140524158523360
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140524170096944('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_140524170096656(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140524171492352 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140524171492352
            __i18n_domain = __previous_i18n_domain_140524158523504
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }