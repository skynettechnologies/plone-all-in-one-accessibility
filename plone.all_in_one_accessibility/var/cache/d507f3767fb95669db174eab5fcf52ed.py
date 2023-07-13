# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/plone-addsite.pt'

__tokens = {481: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 12, 14), 483: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 12, 16), 627: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 15, 14), 629: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 15, 16), 726: ('string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', 16, 30), 831: ('string:${context/absolute_url}/++resource++plone-admin-ui.js', 18, 30), 1117: ('string:${context/absolute_url}/++resource++plone-logo.svg', 28, 35), 1405: ('view/profiles', 35, 25), 1449: (' profiles/bas', 36, 29), 1495: ('e profiles/defau', 37, 30), 1547: ('es profiles/extensi', 38, 32), 1592: ('ced request/advanced|not', 39, 21), 1332: ('string:${context/absolute_url}/@@plone-addsite', 34, 27), 2255: ('request/site_id|nothing', 55, 40), 3261: ('view/browser_language', 78, 49), 3333: (' python:view.grouped_languages(browser_language', 79, 49), 3426: ('grouped_languages', 80, 42), 3491: ('group/label', 81, 46), 3582: ('group/languages', 84, 41), 3645: ("python:lang['langcode']", 85, 46), 3718: (" python:lang['langcode'] == browser_languag", 86, 48), 3801: ("python: lang['label']", 87, 37), 4403: ('view/timezones', 108, 40), 4462: ('tz_list', 109, 42), 4517: ('group', 110, 46), 4576: ('python:tz_list[group]', 111, 51), 4621: ('tz/value', 111, 96), 4662: ('tz/label', 112, 31), 5112: ('advanced', 124, 30), 5742: ('not:advanced', 140, 32), 5897: ('python: len(base_profiles) > 1', 144, 30), 6069: ('base_profiles', 148, 36), 6388: (' info/i', 155, 43), 6336: ('info/id', 154, 41), 6442: ("d python: default_profile==info['id'] and 'checked' or nothi", 156, 44), 6577: ('info/id', 157, 68), 6586: ('${info/title}', 157, 77), 6588: ('info/title', 157, 79), 6660: ('info/description', 158, 52), 6678: ('${info/description}', 158, 70), 6680: ('info/description', 158, 72), 7046: ("python:[p for p in extension_profiles if p.get('selected', None)]", 170, 40), 7143: ('python: extension_profiles or advanced', 171, 30), 7212: ('python: has_selected and not advanced', 172, 29), 7286: ('python: advanced', 173, 34), 7692: ('extension_profiles', 183, 39), 7757: ('info/selected|nothing', 184, 44), 7824: ('python: not selected or advanced', 185, 43), 7943: ('python: advanced', 187, 37), 8090: ('${info/id}', 190, 33), 8092: ('info/id', 190, 35), 8132: ('${info/id}', 191, 30), 8134: ('info/id', 191, 32), 8245: ('info/selected|nothing', 193, 50), 8329: ('${info/id}', 194, 57), 8331: ('info/id', 194, 59), 8342: ('${info/title}', 194, 70), 8344: ('info/title', 194, 72), 8446: ("python: advanced and info['description']", 196, 39), 8511: ('${info/description}', 197, 22), 8513: ('info/description', 197, 24), 8656: ('python: selected and not advanced', 201, 43), 8812: ('${info/id}', 204, 31), 8814: ('info/id', 204, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139839079511328 = {'class': 'btn btn-success mt-3', 'type': 'submit', 'name': 'submit', }
_static_139839079506192 = {'type': 'hidden', 'name': 'form.submitted:boolean', 'value': 'True', }
_static_139839079547040 = {'class': 'col-md-12 mt-3', }
_static_139839079557456 = {'type': 'hidden', 'name': 'extension_ids:list', 'value': '${info/id}', }
_static_139839079559376 = {'class': 'form-text', }
_static_139839079550736 = {'class': 'form-check-label', 'for': '${info/id}', }
_static_139839079560480 = {'type': 'checkbox', 'name': 'extension_ids:list', 'value': '${info/id}', 'id': '${info/id}', 'class': 'form-check-input', 'checked': 'info/selected|nothing', }
_static_139839079553232 = {'class': 'form-check mb-3', }
_static_139839079550112 = {'class': 'lead', }
_static_139839079622704 = {'class': 'col-md-12 mt-3', }
_static_139839079623472 = {'class': 'form-text', }
_static_139839079614112 = {'class': 'form-text', }
_static_139839079628752 = {'class': 'form-check-label', 'for': 'info/id', }
_static_139839079623232 = {'type': 'radio', 'name': 'profile_id:string', 'value': 'profile', 'class': 'form-check-input', 'id': 'info/id', 'checked': "python: default_profile==info['id'] and 'checked' or nothing", }
_static_139839079621360 = {'class': 'form-check mb-3', }
_static_139839079616896 = {'class': 'lead', }
_static_139839079615552 = {'class': 'mb-3', }
_static_139839079613968 = {'class': 'col-md-12', }
_static_139839082236608 = {'type': 'hidden', 'name': 'setup_content:boolean', 'value': 'true', }
_static_139839082236320 = {'class': 'form-text', }
_static_139839082238000 = {'class': 'form-check-label', 'for': 'example-content', }
_static_139839082240496 = {'class': 'form-check-input', 'id': 'example-content', 'type': 'checkbox', 'name': 'setup_content:boolean', 'checked': 'checked', }
_static_139839082241408 = {'class': 'form-check', }
_static_139839082247552 = {'class': 'col-md-12 mb-3', }
_static_139839082245488 = {'class': 'form-text', }
_static_139839082242464 = {'value': 'UTC', }
_static_139839082248944 = {'label': 'group', }
_static_139839082211664 = {'id': 'portal_timezone', 'name': 'portal_timezone', 'class': 'form-select', }
_static_139839082205568 = {'for': 'portal_timezone', 'class': 'form-label', }
_static_139839082208400 = {'class': 'col-md-12 mb-3 tzx', }
_static_139839082205328 = {'class': 'form-text', }
_static_139839082208016 = {'value': 'en', 'selected': "python:lang['langcode'] == browser_language", }
_static_139839082203696 = {'label': 'group/label', }
_static_139839082202928 = {'name': 'default_language', 'class': 'form-select', }
_static_139839082207248 = {'for': 'default_language', 'class': 'form-label', }
_static_139839082208352 = {'class': 'col-md-12 mb-3', }
_static_139839082211904 = {'class': 'form-text', }
_static_139839079661632 = {'type': 'text', 'name': 'title', 'size': '30', 'value': 'Site', 'class': 'form-control', }
_static_139839079665760 = {'for': 'title', 'class': 'form-label', }
_static_139839079666768 = {'class': 'col-md-12 mb-3', }
_static_139839079666432 = {'class': 'form-text', }
_static_139839079673776 = {'type': 'text', 'name': 'site_id', 'size': '20', 'id': 'site_id', 'class': 'form-control', 'value': 'request/site_id|nothing', }
_static_139839079674256 = {'for': 'site_id', 'class': 'form-label', }
_static_139839079671184 = {'class': 'col-md-12 mb-3 mb-3', }
_static_139839079677616 = {'class': 'lead', }
_static_139839079583072 = {'class': 'col-md-12', }
_static_139839079592528 = {'class': 'row', }
_static_139839079594784 = {'action': '#', 'method': 'post', }
_static_139839079585856 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_139839079586240 = {'class': 'row', }
_static_139839079590512 = {'class': 'container admin mt-5 mb-5 p-4 ', }
_static_139839079586816 = {'src': 'string:${context/absolute_url}/++resource++plone-admin-ui.js', }
_static_139839079592816 = {'src': 'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', }
_static_139839079464864 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_139839140398752 = __C2ZContextWrapper
_static_139839140402352 = __compile_zt_expr
_static_139839079461264 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_139839079458960 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_139839079457472 = {'charset': 'utf-8', }
_static_139839134773072 = {}
_static_139839079455024 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x7f2ed2a81930> name=None at 7f2ed2a81960> -> __attrs_139839079455456
            __attrs_139839079455456 = _static_139839079455024
            __previous_i18n_domain_139839079455600 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079456512
            __attrs_139839079456512 = _static_139839134773072

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed2a822c0> name=None at 7f2ed2a822f0> -> __attrs_139839079457760
            __attrs_139839079457760 = _static_139839079457472

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed2a82890> name=None at 7f2ed2a828c0> -> __attrs_139839079459056
            __attrs_139839079459056 = _static_139839079458960

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1" />\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079459920
            __attrs_139839079459920 = _static_139839134773072

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')
            __stream_139839079459440 = []
            __append_139839079459440 = __stream_139839079459440.append
            __append_139839079459440('Create a Plone site')
            __msgid_139839079459440 = __re_whitespace(''.join(__stream_139839079459440)).strip()
            if __msgid_139839079459440:
                __append(translate(__msgid_139839079459440, mapping=None, default=__msgid_139839079459440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</title>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed2a83190> name=None at 7f2ed2a831c0> -> __attrs_139839079461840
            __attrs_139839079461840 = _static_139839079461264

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079461408
            __default_139839079461408 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (12:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2a82ec0> -> __attr_href
            __token = 481
            __token = 483
            try:
                __zt_tmp = __attrs_139839079461840
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139839140402352('string', '${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
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
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed2a83fa0> name=None at 7f2ed2a83fd0> -> __attrs_139839079583264
            __attrs_139839079583264 = _static_139839079464864

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079583600
            __default_139839079583600 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2aa0eb0> -> __attr_href
            __token = 627
            __token = 629
            try:
                __zt_tmp = __attrs_139839079583264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139839140402352('string', '${context/absolute_url}/++resource++plone-admin-ui.css', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
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
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed2aa3370> name=None at 7f2ed2aa3310> -> __attrs_139839079588928
            __attrs_139839079588928 = _static_139839079592816

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079585568
            __default_139839079585568 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js' (16:30)> -> __attr_src
            __token = 726
            try:
                __zt_tmp = __attrs_139839079588928
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_139839140402352('string', '${context/absolute_url}/++resource++jstz-1.0.4.min.js', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append('>\n  </script>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed2aa1c00> name=None at 7f2ed2aa0940> -> __attrs_139839079585808
            __attrs_139839079585808 = _static_139839079586816

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079589504
            __default_139839079589504 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-admin-ui.js' (18:30)> -> __attr_src
            __token = 831
            try:
                __zt_tmp = __attrs_139839079585808
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_139839140402352('string', '${context/absolute_url}/++resource++plone-admin-ui.js', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append('>\n  </script>\n</head>\n\n')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079584032
            __attrs_139839079584032 = _static_139839134773072

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed2aa2a70> name=None at 7f2ed2aa11e0> -> __attrs_139839079580384
            __attrs_139839079580384 = _static_139839079590512

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4 ">\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed2aa19c0> name=None at 7f2ed2aa09a0> -> __attrs_139839079581152
            __attrs_139839079581152 = _static_139839079586240

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079586624
            __attrs_139839079586624 = _static_139839134773072

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x7f2ed2aa1840> name=None at 7f2ed2aa2740> -> __attrs_139839079592048
            __attrs_139839079592048 = _static_139839079585856

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079592192
            __default_139839079592192 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (28:35)> -> __attr_src
            __token = 1117
            try:
                __zt_tmp = __attrs_139839079592048
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_139839140402352('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079588160
            __default_139839079588160 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f2ed2aa2830> at 7f2ed2aa2dd0> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n    </header>\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed2aa3b20> name=None at 7f2ed2aa3f40> -> __attrs_139839079585424
            __attrs_139839079585424 = _static_139839079594784
            __backup_profiles_139839117258576 = get('profiles', __marker)

            # <Value 'view/profiles' (35:25)> -> __value
            __token = 1405
            try:
                __zt_tmp = __attrs_139839079585424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'view/profiles', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['profiles'] = __value
            __backup_base_profiles_139839117259104 = get('base_profiles', __marker)

            # <Value 'profiles/base' (36:29)> -> __value
            __token = 1449
            try:
                __zt_tmp = __attrs_139839079585424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'profiles/base', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['base_profiles'] = __value
            __backup_default_profile_139839115231392 = get('default_profile', __marker)

            # <Value 'profiles/default' (37:30)> -> __value
            __token = 1495
            try:
                __zt_tmp = __attrs_139839079585424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'profiles/default', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['default_profile'] = __value
            __backup_extension_profiles_139839115231584 = get('extension_profiles', __marker)

            # <Value 'profiles/extensions' (38:32)> -> __value
            __token = 1547
            try:
                __zt_tmp = __attrs_139839079585424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'profiles/extensions', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['extension_profiles'] = __value
            __backup_advanced_139839117251184 = get('advanced', __marker)

            # <Value 'request/advanced|nothing' (39:21)> -> __value
            __token = 1592
            try:
                __zt_tmp = __attrs_139839079585424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'request/advanced|nothing', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['advanced'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079595408
            __default_139839079595408 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/@@plone-addsite' (34:27)> -> __attr_action
            __token = 1332
            try:
                __zt_tmp = __attrs_139839079585424
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_139839140402352('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post">\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed2aa3250> name=None at 7f2ed2aa32b0> -> __attrs_139839079585088
            __attrs_139839079585088 = _static_139839079592528

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row">\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed2aa0d60> name=None at 7f2ed2aa0d30> -> __attrs_139839079666672
            __attrs_139839079666672 = _static_139839079583072

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079674928
            __attrs_139839079674928 = _static_139839134773072

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079676992
            __attrs_139839079676992 = _static_139839134773072

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_139839079670416 = []
            __append_139839079670416 = __stream_139839079670416.append
            __append_139839079670416('Create a Plone site')
            __msgid_139839079670416 = __re_whitespace(''.join(__stream_139839079670416)).strip()
            if __msgid_139839079670416:
                __append(translate(__msgid_139839079670416, mapping=None, default=__msgid_139839079670416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span></h1>\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2ab7eb0> name=None at 7f2ed2ab7fd0> -> __attrs_139839079677424
            __attrs_139839079677424 = _static_139839079677616

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">')
            __stream_139839079676704 = []
            __append_139839079676704 = __stream_139839079676704.append
            __append_139839079676704('Adds a new Plone content management system site to the underlying application server.')
            __msgid_139839079676704 = __re_whitespace(''.join(__stream_139839079676704)).strip()
            if __msgid_139839079676704:
                __append(translate(__msgid_139839079676704, mapping=None, default=__msgid_139839079676704, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2ab6590> name=None at 7f2ed2ab7be0> -> __attrs_139839079674880
            __attrs_139839079674880 = _static_139839079671184

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2ab7190> name=None at 7f2ed2ab73d0> -> __attrs_139839079670560
            __attrs_139839079670560 = _static_139839079674256

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="site_id" class="form-label">')
            __stream_139839079674736 = []
            __append_139839079674736 = __stream_139839079674736.append
            __append_139839079674736('\n              Path identifier\n            ')
            __msgid_139839079674736 = __re_whitespace(''.join(__stream_139839079674736)).strip()
            if __msgid_139839079674736:
                __append(translate(__msgid_139839079674736, mapping=None, default=__msgid_139839079674736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2ab6fb0> name=None at 7f2ed2ab7010> -> __attrs_139839079672240
            __attrs_139839079672240 = _static_139839079673776

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="site_id" size="20" id="site_id" class="form-control"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079672048
            __default_139839079672048 = _DEFAULT_MARKER

            # <Substitution 'request/site_id|nothing' (55:40)> -> __attr_value
            __token = 2255
            try:
                __zt_tmp = __attrs_139839079672240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139839140402352('path', 'request/site_id|nothing', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2ab5300> name=None at 7f2ed2ab5720> -> __attrs_139839079668928
            __attrs_139839079668928 = _static_139839079666432

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_139839079671328 = []
            __append_139839079671328 = __stream_139839079671328.append
            __append_139839079671328('\n              The ID of the site. No special characters or spaces are allowed. This ends up as part of the URL unless hidden by an upstream web server.\n            ')
            __msgid_139839079671328 = __re_whitespace(''.join(__stream_139839079671328)).strip()
            if __msgid_139839079671328:
                __append(translate(__msgid_139839079671328, mapping=None, default=__msgid_139839079671328, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2ab5450> name=None at 7f2ed2ab5ba0> -> __attrs_139839079669072
            __attrs_139839079669072 = _static_139839079666768

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2ab5060> name=None at 7f2ed2ab58a0> -> __attrs_139839079663552
            __attrs_139839079663552 = _static_139839079665760

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="title" class="form-label">')
            __stream_139839079667632 = []
            __append_139839079667632 = __stream_139839079667632.append
            __append_139839079667632('Title')
            __msgid_139839079667632 = __re_whitespace(''.join(__stream_139839079667632)).strip()
            if 'label_title':
                __append(translate('label_title', mapping=None, default=__msgid_139839079667632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2ab4040> name=None at 7f2ed2ab4070> -> __attrs_139839079662880
            __attrs_139839079662880 = _static_139839079661632

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="title" size="30"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079664416
            __default_139839079664416 = _DEFAULT_MARKER

            # <Translate msgid='text_default_site_title' node=<ast.Constant object at 0x7f2ed2ab4af0> at 7f2ed2ab4a90> -> __attr_value
            __attr_value = 'Site'
            __attr_value = translate('text_default_site_title', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' class="form-control" />\n\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2d22a40> name=None at 7f2ed2d20580> -> __attrs_139839082215744
            __attrs_139839082215744 = _static_139839082211904

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_139839082202736 = []
            __append_139839082202736 = __stream_139839082202736.append
            __append_139839082202736('\n              A short title for the site. This will be shown as part of the title of the browser window on each page.\n            ')
            __msgid_139839082202736 = __re_whitespace(''.join(__stream_139839082202736)).strip()
            if __msgid_139839082202736:
                __append(translate(__msgid_139839082202736, mapping=None, default=__msgid_139839082202736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2d21c60> name=None at 7f2ed2d22440> -> __attrs_139839082202064
            __attrs_139839082202064 = _static_139839082208352

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2d21810> name=None at 7f2ed2d218d0> -> __attrs_139839082207632
            __attrs_139839082207632 = _static_139839082207248

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="default_language" class="form-label">')
            __stream_139839082204080 = []
            __append_139839082204080 = __stream_139839082204080.append
            __append_139839082204080('Language')
            __msgid_139839082204080 = __re_whitespace(''.join(__stream_139839082204080)).strip()
            if __msgid_139839082204080:
                __append(translate(__msgid_139839082204080, mapping=None, default=__msgid_139839082204080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2d20730> name=None at 7f2ed2d23af0> -> __attrs_139839082216416
            __attrs_139839082216416 = _static_139839082202928
            __backup_browser_language_139839121291584 = get('browser_language', __marker)

            # <Value 'view/browser_language' (78:49)> -> __value
            __token = 3261
            try:
                __zt_tmp = __attrs_139839082216416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'view/browser_language', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['browser_language'] = __value
            __backup_grouped_languages_139839116413056 = get('grouped_languages', __marker)

            # <Value 'python:view.grouped_languages(browser_language)' (79:49)> -> __value
            __token = 3333
            try:
                __zt_tmp = __attrs_139839082216416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', 'view.grouped_languages(browser_language)', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['grouped_languages'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select name="default_language" class="form-select">\n              ')

            # <Static value=<ast.Dict object at 0x7f2ed2d20a30> name=None at 7f2ed2d20ac0> -> __attrs_139839082214064
            __attrs_139839082214064 = _static_139839082203696
            __backup_group_139839117077392 = get('group', __marker)

            # <Value 'grouped_languages' (80:42)> -> __iterator
            __token = 3426
            try:
                __zt_tmp = __attrs_139839082214064
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139839140402352('path', 'grouped_languages', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            (__iterator, ____index_139839082203360, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append('<optgroup')

                # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839082214880
                __default_139839082214880 = _DEFAULT_MARKER

                # <Substitution 'group/label' (81:46)> -> __attr_label
                __token = 3491
                try:
                    __zt_tmp = __attrs_139839082214064
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_139839140402352('path', 'group/label', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((' label="%s"' % __attr_label))
                __append('>\n\n                ')

                # <Static value=<ast.Dict object at 0x7f2ed2d21b10> name=None at 7f2ed2d21ae0> -> __attrs_139839082207488
                __attrs_139839082207488 = _static_139839082208016
                __backup_lang_139839117247152 = get('lang', __marker)

                # <Value 'group/languages' (84:41)> -> __iterator
                __token = 3582
                try:
                    __zt_tmp = __attrs_139839082207488
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139839140402352('path', 'group/languages', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                (__iterator, ____index_139839082207008, ) = getname('repeat')('lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839082201392
                    __default_139839082201392 = _DEFAULT_MARKER

                    # <Substitution "python:lang['langcode']" (85:46)> -> __attr_value
                    __token = 3645
                    try:
                        __zt_tmp = __attrs_139839082207488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139839140402352('python', "lang['langcode']", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'en', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839082216608
                    __default_139839082216608 = _DEFAULT_MARKER

                    # <Boolean "python:lang['langcode'] == browser_language" (86:48)> -> __attr_selected
                    __token = 3718
                    try:
                        __zt_tmp = __attrs_139839082207488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_139839140402352('python', "lang['langcode'] == browser_language", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = 'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((' selected="%s"' % __attr_selected))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839082203024
                    __default_139839082203024 = _DEFAULT_MARKER

                    # <Value "python: lang['label']" (87:37)> -> __cache_139839082215792
                    __token = 3801
                    try:
                        __zt_tmp = __attrs_139839082207488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139839082215792 = _static_139839140402352('python', " lang['label']", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                    # <BinOp left=<Value "python: lang['label']" (87:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed2d23070> -> __condition
                    __expression = __cache_139839082215792

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                  English\n                ')
                    else:
                        __content = __cache_139839082215792
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    ____index_139839082207008 -= 1
                    if (____index_139839082207008 > 0):
                        __append('\n                ')
                if (__backup_lang_139839117247152 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_139839117247152
                __append('\n\n              </optgroup>')
                ____index_139839082203360 -= 1
                if (____index_139839082203360 > 0):
                    __append('\n              ')
            if (__backup_group_139839117077392 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_139839117077392
            __append('\n            </select>')
            if (__backup_grouped_languages_139839116413056 is __marker):
                del econtext['grouped_languages']
            else:
                econtext['grouped_languages'] = __backup_grouped_languages_139839116413056
            if (__backup_browser_language_139839121291584 is __marker):
                del econtext['browser_language']
            else:
                econtext['browser_language'] = __backup_browser_language_139839121291584
            __append('\n\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2d21090> name=None at 7f2ed2d20f40> -> __attrs_139839082204608
            __attrs_139839082204608 = _static_139839082205328

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_139839082206912 = []
            __append_139839082206912 = __stream_139839082206912.append
            __append_139839082206912('\n              The main language of the site.\n            ')
            __msgid_139839082206912 = __re_whitespace(''.join(__stream_139839082206912)).strip()
            if __msgid_139839082206912:
                __append(translate(__msgid_139839082206912, mapping=None, default=__msgid_139839082206912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2d21c90> name=None at 7f2ed2d217b0> -> __attrs_139839082211472
            __attrs_139839082211472 = _static_139839082208400

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3 tzx">\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2d21180> name=None at 7f2ed2d211b0> -> __attrs_139839082206192
            __attrs_139839082206192 = _static_139839082205568

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="portal_timezone" class="form-label">')
            __stream_139839082206624 = []
            __append_139839082206624 = __stream_139839082206624.append
            __append_139839082206624('\n              Default timezone\n            ')
            __msgid_139839082206624 = __re_whitespace(''.join(__stream_139839082206624)).strip()
            if __msgid_139839082206624:
                __append(translate(__msgid_139839082206624, mapping=None, default=__msgid_139839082206624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2d22950> name=None at 7f2ed2d20700> -> __attrs_139839082247456
            __attrs_139839082247456 = _static_139839082211664
            __backup_tz_list_139839117255552 = get('tz_list', __marker)

            # <Value 'view/timezones' (108:40)> -> __value
            __token = 4403
            try:
                __zt_tmp = __attrs_139839082247456
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'view/timezones', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['tz_list'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select id="portal_timezone" name="portal_timezone" class="form-select">\n              ')

            # <Static value=<ast.Dict object at 0x7f2ed2d2baf0> name=None at 7f2ed2d29e10> -> __attrs_139839082242368
            __attrs_139839082242368 = _static_139839082248944
            __backup_group_139839116668896 = get('group', __marker)

            # <Value 'tz_list' (109:42)> -> __iterator
            __token = 4462
            try:
                __zt_tmp = __attrs_139839082242368
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139839140402352('path', 'tz_list', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            (__iterator, ____index_139839082245440, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append('<optgroup')

                # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839082249280
                __default_139839082249280 = _DEFAULT_MARKER

                # <Substitution 'group' (110:46)> -> __attr_label
                __token = 4517
                try:
                    __zt_tmp = __attrs_139839082242368
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_139839140402352('path', 'group', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((' label="%s"' % __attr_label))
                __append('>\n                ')

                # <Static value=<ast.Dict object at 0x7f2ed2d2a1a0> name=None at 7f2ed2d28df0> -> __attrs_139839082249952
                __attrs_139839082249952 = _static_139839082242464
                __backup_tz_139839190739856 = get('tz', __marker)

                # <Value 'python:tz_list[group]' (111:51)> -> __iterator
                __token = 4576
                try:
                    __zt_tmp = __attrs_139839082249952
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139839140402352('python', 'tz_list[group]', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                (__iterator, ____index_139839082247408, ) = getname('repeat')('tz', __iterator)
                econtext['tz'] = None
                for __item in __iterator:
                    econtext['tz'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839082249376
                    __default_139839082249376 = _DEFAULT_MARKER

                    # <Substitution 'tz/value' (111:96)> -> __attr_value
                    __token = 4621
                    try:
                        __zt_tmp = __attrs_139839082249952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139839140402352('path', 'tz/value', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'UTC', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839082241072
                    __default_139839082241072 = _DEFAULT_MARKER

                    # <Value 'tz/label' (112:31)> -> __cache_139839082239296
                    __token = 4662
                    try:
                        __zt_tmp = __attrs_139839082249952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139839082239296 = _static_139839140402352('path', 'tz/label', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                    # <BinOp left=<Value 'tz/label' (112:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed2d2afb0> -> __condition
                    __expression = __cache_139839082239296

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                  UTC\n                ')
                    else:
                        __content = __cache_139839082239296
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    ____index_139839082247408 -= 1
                    if (____index_139839082247408 > 0):
                        __append('\n                ')
                if (__backup_tz_139839190739856 is __marker):
                    del econtext['tz']
                else:
                    econtext['tz'] = __backup_tz_139839190739856
                __append('\n              </optgroup>')
                ____index_139839082245440 -= 1
                if (____index_139839082245440 > 0):
                    __append('\n              ')
            if (__backup_group_139839116668896 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_139839116668896
            __append('\n            </select>')
            if (__backup_tz_list_139839117255552 is __marker):
                del econtext['tz_list']
            else:
                econtext['tz_list'] = __backup_tz_list_139839117255552
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2d2ad70> name=None at 7f2ed2d281c0> -> __attrs_139839082234208
            __attrs_139839082234208 = _static_139839082245488

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_139839082247504 = []
            __append_139839082247504 = __stream_139839082247504.append
            __append_139839082247504('\n              The default timezone setting of the portal.\n              Users will be able to set their own timezone, if available timezones are defined in the date and time settings.\n            ')
            __msgid_139839082247504 = __re_whitespace(''.join(__stream_139839082247504)).strip()
            if __msgid_139839082247504:
                __append(translate(__msgid_139839082247504, mapping=None, default=__msgid_139839082247504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2d2b580> name=None at 7f2ed2d2b700> -> __attrs_139839082245248
            __attrs_139839082245248 = _static_139839082247552

            # <Value 'advanced' (124:30)> -> __condition
            __token = 5112
            try:
                __zt_tmp = __attrs_139839082245248
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('path', 'advanced', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-3">\n            ')

                # <Static value=<ast.Dict object at 0x7f2ed2d29d80> name=None at 7f2ed2d2a320> -> __attrs_139839082239920
                __attrs_139839082239920 = _static_139839082241408

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n              ')

                # <Static value=<ast.Dict object at 0x7f2ed2d299f0> name=None at 7f2ed2d29a20> -> __attrs_139839082243184
                __attrs_139839082243184 = _static_139839082240496

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-check-input" id="example-content" type="checkbox" name="setup_content:boolean" checked="checked" />\n              ')

                # <Static value=<ast.Dict object at 0x7f2ed2d29030> name=None at 7f2ed2d29330> -> __attrs_139839082234496
                __attrs_139839082234496 = _static_139839082238000

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label" for="example-content">')
                __stream_139839082244576 = []
                __append_139839082244576 = __stream_139839082244576.append
                __append_139839082244576('Example content')
                __msgid_139839082244576 = __re_whitespace(''.join(__stream_139839082244576)).strip()
                if __msgid_139839082244576:
                    __append(translate(__msgid_139839082244576, mapping=None, default=__msgid_139839082244576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n              ')

                # <Static value=<ast.Dict object at 0x7f2ed2d289a0> name=None at 7f2ed2d289d0> -> __attrs_139839082234976
                __attrs_139839082234976 = _static_139839082236320

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')
                __stream_139839082237904 = []
                __append_139839082237904 = __stream_139839082237904.append
                __append_139839082237904('\n                Should the default example content be added to the site?\n              ')
                __msgid_139839082237904 = __re_whitespace(''.join(__stream_139839082237904)).strip()
                if __msgid_139839082237904:
                    __append(translate(__msgid_139839082237904, mapping=None, default=__msgid_139839082237904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n            </div>\n          </div>')
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2d28ac0> name=None at 7f2ed2d28580> -> __attrs_139839082237616
            __attrs_139839082237616 = _static_139839082236608

            # <Value 'not:advanced' (140:32)> -> __condition
            __token = 5742
            try:
                __zt_tmp = __attrs_139839082237616
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('not', 'advanced', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="setup_content:boolean" value="true" />')
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2aa8610> name=None at 7f2ed2d290f0> -> __attrs_139839079614880
            __attrs_139839079614880 = _static_139839079613968

            # <Value 'python: len(base_profiles) > 1' (144:30)> -> __condition
            __token = 5897
            try:
                __zt_tmp = __attrs_139839079614880
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('python', ' len(base_profiles) > 1', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12">\n            ')

                # <Static value=<ast.Dict object at 0x7f2ed2aa8c40> name=None at 7f2ed2aa8280> -> __attrs_139839079615072
                __attrs_139839079615072 = _static_139839079615552

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n              ')

                # <Static value=<ast.Dict object at 0x7f2ed2aa9180> name=None at 7f2ed2aa91e0> -> __attrs_139839079618816
                __attrs_139839079618816 = _static_139839079616896

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_139839079613200 = []
                __append_139839079613200 = __stream_139839079613200.append
                __append_139839079613200('Base configuration')
                __msgid_139839079613200 = __re_whitespace(''.join(__stream_139839079613200)).strip()
                if __msgid_139839079613200:
                    __append(translate(__msgid_139839079613200, mapping=None, default=__msgid_139839079613200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n\n              ')

                # <Static value=<ast.Dict object at 0x7f2ed2aaa2f0> name=None at 7f2ed2aaa290> -> __attrs_139839079620544
                __attrs_139839079620544 = _static_139839079621360
                __backup_info_139839129177536 = get('info', __marker)

                # <Value 'base_profiles' (148:36)> -> __iterator
                __token = 6069
                try:
                    __zt_tmp = __attrs_139839079620544
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139839140402352('path', 'base_profiles', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                (__iterator, ____index_139839079620640, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check mb-3">\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed2aaaa40> name=None at 7f2ed2aab070> -> __attrs_139839079618864
                    __attrs_139839079618864 = _static_139839079623232

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="radio" name="profile_id:string"')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079619968
                    __default_139839079619968 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (155:43)> -> __attr_value
                    __token = 6388
                    try:
                        __zt_tmp = __attrs_139839079618864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139839140402352('path', 'info/id', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'profile', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' class="form-check-input"')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079621456
                    __default_139839079621456 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (154:41)> -> __attr_id
                    __token = 6336
                    try:
                        __zt_tmp = __attrs_139839079618864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139839140402352('path', 'info/id', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079624336
                    __default_139839079624336 = _DEFAULT_MARKER

                    # <Boolean "python: default_profile==info['id'] and 'checked' or nothing" (156:44)> -> __attr_checked
                    __token = 6442
                    try:
                        __zt_tmp = __attrs_139839079618864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_139839140402352('python', " default_profile==info['id'] and 'checked' or nothing", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed2aabfd0> name=None at 7f2ed2aa9750> -> __attrs_139839079628656
                    __attrs_139839079628656 = _static_139839079628752

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079619920
                    __default_139839079619920 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (157:68)> -> __attr_for
                    __token = 6577
                    try:
                        __zt_tmp = __attrs_139839079628656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_139839140402352('path', 'info/id', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append('>')

                    # <Interpolation value=<Substitution '${info/title}' (157:77)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2aabe50> -> __content_139839220113136
                    __token = 6586
                    __token = 6588
                    try:
                        __zt_tmp = __attrs_139839079628656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139839220113136 = _static_139839140402352('path', 'info/title', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __content_139839220113136 = __quote(__content_139839220113136, '\x00', '&#0;', None, None)
                    __content_139839220113136 = __content_139839220113136
                    if (__content_139839220113136 is None):
                        pass
                    else:
                        if (__content_139839220113136 is None):
                            __content_139839220113136 = None
                        else:
                            __tt = type(__content_139839220113136)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139839220113136 = str(__content_139839220113136)
                            else:
                                if (__tt is bytes):
                                    __content_139839220113136 = decode(__content_139839220113136)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139839220113136 = __content_139839220113136.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139839220113136)
                                            __content_139839220113136 = (str(__content_139839220113136) if (__content_139839220113136 is __converted) else __converted)
                                        else:
                                            __content_139839220113136 = __content_139839220113136()
                    if (__content_139839220113136 is not None):
                        __append(__content_139839220113136)
                    __append('</label>\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed2aa86a0> name=None at 7f2ed2aaba30> -> __attrs_139839079617232
                    __attrs_139839079617232 = _static_139839079614112

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-text">')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079627600
                    __default_139839079627600 = _DEFAULT_MARKER

                    # <Value 'info/description' (158:52)> -> __cache_139839079628464
                    __token = 6660
                    try:
                        __zt_tmp = __attrs_139839079617232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139839079628464 = _static_139839140402352('path', 'info/description', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                    # <BinOp left=<Value 'info/description' (158:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed2aa96f0> -> __condition
                    __expression = __cache_139839079628464

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <Interpolation value=<Substitution '${info/description}' (158:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2aa9330> -> __content_139839220113136
                        __token = 6678
                        __token = 6680
                        try:
                            __zt_tmp = __attrs_139839079617232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139839220113136 = _static_139839140402352('path', 'info/description', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                        __content_139839220113136 = __quote(__content_139839220113136, '\x00', '&#0;', None, None)
                        __content_139839220113136 = __content_139839220113136
                        if (__content_139839220113136 is None):
                            pass
                        else:
                            if (__content_139839220113136 is None):
                                __content_139839220113136 = None
                            else:
                                __tt = type(__content_139839220113136)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139839220113136 = str(__content_139839220113136)
                                else:
                                    if (__tt is bytes):
                                        __content_139839220113136 = decode(__content_139839220113136)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139839220113136 = __content_139839220113136.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139839220113136)
                                                __content_139839220113136 = (str(__content_139839220113136) if (__content_139839220113136 is __converted) else __converted)
                                            else:
                                                __content_139839220113136 = __content_139839220113136()
                        if (__content_139839220113136 is not None):
                            __append(__content_139839220113136)
                    else:
                        __content = __cache_139839079628464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n              </div>')
                    ____index_139839079620640 -= 1
                    if (____index_139839079620640 > 0):
                        __append('\n              ')
                if (__backup_info_139839129177536 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_139839129177536
                __append('\n\n              ')

                # <Static value=<ast.Dict object at 0x7f2ed2aaab30> name=None at 7f2ed2aaa500> -> __attrs_139839079623376
                __attrs_139839079623376 = _static_139839079623472

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')
                __stream_139839079625200 = []
                __append_139839079625200 = __stream_139839079625200.append
                __append_139839079625200("\n                You normally don't need to change anything here unless you have specific reasons and know what you are doing.\n              ")
                __msgid_139839079625200 = __re_whitespace(''.join(__stream_139839079625200)).strip()
                if __msgid_139839079625200:
                    __append(translate(__msgid_139839079625200, mapping=None, default=__msgid_139839079625200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n            </div>\n          </div>')
            __append('\n\n\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2aaa830> name=None at 7f2ed2aaa590> -> __attrs_139839079621504
            __attrs_139839079621504 = _static_139839079622704
            __backup_has_selected_139839117248832 = get('has_selected', __marker)

            # <Value "python:[p for p in extension_profiles if p.get('selected', None)]" (170:40)> -> __value
            __token = 7046
            try:
                __zt_tmp = __attrs_139839079621504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "[p for p in extension_profiles if p.get('selected', None)]", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['has_selected'] = __value

            # <Value 'python: extension_profiles or advanced' (171:30)> -> __condition
            __token = 7143
            try:
                __zt_tmp = __attrs_139839079621504
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('python', ' extension_profiles or advanced', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'python: has_selected and not advanced' (172:29)> at 7f2ed2aab370> -> __cache_139839079625584

                # <Value 'python: has_selected and not advanced' (172:29)> -> __cache_139839079625584
                __token = 7212
                try:
                    __zt_tmp = __attrs_139839079621504
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139839079625584 = _static_139839140402352('python', ' has_selected and not advanced', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                __cache_139839079625584 = not __cache_139839079625584
                __condition = __cache_139839079625584
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="col-md-12 mt-3">')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079554384
                __attrs_139839079554384 = _static_139839134773072

                # <Value 'python: advanced' (173:34)> -> __condition
                __token = 7286
                try:
                    __zt_tmp = __attrs_139839079554384
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139839140402352('python', ' advanced', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                if __condition:
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079553712
                    __attrs_139839079553712 = _static_139839134773072

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2>')
                    __stream_139839079552560 = []
                    __append_139839079552560 = __stream_139839079552560.append
                    __append_139839079552560('Add-ons')
                    __msgid_139839079552560 = __re_whitespace(''.join(__stream_139839079552560)).strip()
                    if __msgid_139839079552560:
                        __append(translate(__msgid_139839079552560, mapping=None, default=__msgid_139839079552560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h2>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f2ed2a98ca0> name=None at 7f2ed2a98d00> -> __attrs_139839079554624
                    __attrs_139839079554624 = _static_139839079550112

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="lead" >')
                    __stream_139839079552944 = []
                    __append_139839079552944 = __stream_139839079552944.append
                    __append_139839079552944('\n                Select any add-ons you want to activate immediately.\n                You can also activate add-ons after the site has been created using the Add-ons control panel.\n              ')
                    __msgid_139839079552944 = __re_whitespace(''.join(__stream_139839079552944)).strip()
                    if __msgid_139839079552944:
                        __append(translate(__msgid_139839079552944, mapping=None, default=__msgid_139839079552944, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div>\n            ')
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079554288
                __attrs_139839079554288 = _static_139839134773072
                __backup_info_139839116668944 = get('info', __marker)

                # <Value 'extension_profiles' (183:39)> -> __iterator
                __token = 7692
                try:
                    __zt_tmp = __attrs_139839079554288
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139839140402352('path', 'extension_profiles', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                (__iterator, ____index_139839079556304, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079550832
                    __attrs_139839079550832 = _static_139839134773072
                    __backup_selected_139839116659248 = get('selected', __marker)

                    # <Value 'info/selected|nothing' (184:44)> -> __value
                    __token = 7757
                    try:
                        __zt_tmp = __attrs_139839079550832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139839140402352('path', 'info/selected|nothing', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079557888
                    __attrs_139839079557888 = _static_139839134773072

                    # <Value 'python: not selected or advanced' (185:43)> -> __condition
                    __token = 7824
                    try:
                        __zt_tmp = __attrs_139839079557888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139839140402352('python', ' not selected or advanced', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f2ed2a998d0> name=None at 7f2ed2a98d90> -> __attrs_139839079562016
                        __attrs_139839079562016 = _static_139839079553232

                        # <Value 'python: advanced' (187:37)> -> __condition
                        __token = 7943
                        try:
                            __zt_tmp = __attrs_139839079562016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139839140402352('python', ' advanced', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="form-check mb-3">\n                    ')

                            # <Static value=<ast.Dict object at 0x7f2ed2a9b520> name=None at 7f2ed2a9b580> -> __attrs_139839079552512
                            __attrs_139839079552512 = _static_139839079560480

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="checkbox" name="extension_ids:list"')

                            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079560720
                            __default_139839079560720 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (190:33)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2a9b460> -> __attr_value
                            __token = 8090
                            __token = 8092
                            try:
                                __zt_tmp = __attrs_139839079552512
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_139839140402352('path', 'info/id', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_value = __attr_value
                            if (__attr_value is None):
                                pass
                            else:
                                if (__attr_value is _DEFAULT_MARKER):
                                    __attr_value = None
                                else:
                                    __tt = type(__attr_value)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_value = str(__attr_value)
                                    else:
                                        if (__tt is bytes):
                                            __attr_value = decode(__attr_value)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_value = __attr_value.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_value)
                                                    __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                                else:
                                                    __attr_value = __attr_value()
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079561296
                            __default_139839079561296 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (191:30)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2a9b880> -> __attr_id
                            __token = 8132
                            __token = 8134
                            try:
                                __zt_tmp = __attrs_139839079552512
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_139839140402352('path', 'info/id', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_id = __attr_id
                            if (__attr_id is None):
                                pass
                            else:
                                if (__attr_id is _DEFAULT_MARKER):
                                    __attr_id = None
                                else:
                                    __tt = type(__attr_id)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_id = str(__attr_id)
                                    else:
                                        if (__tt is bytes):
                                            __attr_id = decode(__attr_id)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_id = __attr_id.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_id)
                                                    __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                                else:
                                                    __attr_id = __attr_id()
                            if (__attr_id is not None):
                                __append((' id="%s"' % __attr_id))
                            __append(' class="form-check-input"')

                            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079562496
                            __default_139839079562496 = _DEFAULT_MARKER

                            # <Boolean 'info/selected|nothing' (193:50)> -> __attr_checked
                            __token = 8245
                            try:
                                __zt_tmp = __attrs_139839079552512
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_checked = _static_139839140402352('path', 'info/selected|nothing', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                            if (__attr_checked is _DEFAULT_MARKER):
                                __attr_checked = None
                            else:
                                if __attr_checked:
                                    __attr_checked = 'checked'
                                else:
                                    __attr_checked = None
                            if (__attr_checked is not None):
                                __append((' checked="%s"' % __attr_checked))
                            __append(' />\n                    ')

                            # <Static value=<ast.Dict object at 0x7f2ed2a98f10> name=None at 7f2ed2a98f40> -> __attrs_139839079551744
                            __attrs_139839079551744 = _static_139839079550736

                            # <label ... (0:0)
                            # --------------------------------------------------------
                            __append('<label class="form-check-label"')

                            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079547616
                            __default_139839079547616 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (194:57)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2a98280> -> __attr_for
                            __token = 8329
                            __token = 8331
                            try:
                                __zt_tmp = __attrs_139839079551744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_for = _static_139839140402352('path', 'info/id', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_for = __attr_for
                            if (__attr_for is None):
                                pass
                            else:
                                if (__attr_for is _DEFAULT_MARKER):
                                    __attr_for = None
                                else:
                                    __tt = type(__attr_for)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_for = str(__attr_for)
                                    else:
                                        if (__tt is bytes):
                                            __attr_for = decode(__attr_for)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_for = __attr_for.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_for)
                                                    __attr_for = (str(__attr_for) if (__attr_for is __converted) else __converted)
                                                else:
                                                    __attr_for = __attr_for()
                            if (__attr_for is not None):
                                __append((' for="%s"' % __attr_for))
                            __append(' >')

                            # <Interpolation value=<Substitution '${info/title}' (194:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2a99210> -> __content_139839220113136
                            __token = 8342
                            __token = 8344
                            try:
                                __zt_tmp = __attrs_139839079551744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_139839220113136 = _static_139839140402352('path', 'info/title', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                            __content_139839220113136 = __quote(__content_139839220113136, '\x00', '&#0;', None, None)
                            __content_139839220113136 = __content_139839220113136
                            if (__content_139839220113136 is None):
                                pass
                            else:
                                if (__content_139839220113136 is None):
                                    __content_139839220113136 = None
                                else:
                                    __tt = type(__content_139839220113136)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_139839220113136 = str(__content_139839220113136)
                                    else:
                                        if (__tt is bytes):
                                            __content_139839220113136 = decode(__content_139839220113136)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_139839220113136 = __content_139839220113136.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_139839220113136)
                                                    __content_139839220113136 = (str(__content_139839220113136) if (__content_139839220113136 is __converted) else __converted)
                                                else:
                                                    __content_139839220113136 = __content_139839220113136()
                            if (__content_139839220113136 is not None):
                                __append(__content_139839220113136)
                            __append('</label>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f2ed2a9b0d0> name=None at 7f2ed2a9b130> -> __attrs_139839079547808
                            __attrs_139839079547808 = _static_139839079559376

                            # <Value "python: advanced and info['description']" (196:39)> -> __condition
                            __token = 8446
                            try:
                                __zt_tmp = __attrs_139839079547808
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139839140402352('python', " advanced and info['description']", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="form-text">')

                                # <Interpolation value=<Substitution '\n                      ${info/description}\n                    ' (196:81)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2a989a0> -> __content_139839220113136
                                __token = 8511
                                __token = 8513
                                try:
                                    __zt_tmp = __attrs_139839079547808
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_139839220113136 = _static_139839140402352('path', 'info/description', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                                __content_139839220113136 = __quote(__content_139839220113136, '\x00', '&#0;', None, None)
                                __content_139839220113136 = ('%s%s%s' % ('\n                      ', (__content_139839220113136 if (__content_139839220113136 is not None) else ''), '\n                    ', ))
                                if (__content_139839220113136 is None):
                                    pass
                                else:
                                    if (__content_139839220113136 is None):
                                        __content_139839220113136 = None
                                    else:
                                        __tt = type(__content_139839220113136)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139839220113136 = str(__content_139839220113136)
                                        else:
                                            if (__tt is bytes):
                                                __content_139839220113136 = decode(__content_139839220113136)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139839220113136 = __content_139839220113136.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139839220113136)
                                                        __content_139839220113136 = (str(__content_139839220113136) if (__content_139839220113136 is __converted) else __converted)
                                                    else:
                                                        __content_139839220113136 = __content_139839220113136()
                                if (__content_139839220113136 is not None):
                                    __append(__content_139839220113136)
                                __append('</div>')
                            __append('\n                  </div>')
                        __append('\n                ')
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839079549200
                    __attrs_139839079549200 = _static_139839134773072

                    # <Value 'python: selected and not advanced' (201:43)> -> __condition
                    __token = 8656
                    try:
                        __zt_tmp = __attrs_139839079549200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139839140402352('python', ' selected and not advanced', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f2ed2a9a950> name=None at 7f2ed2a99c90> -> __attrs_139839079510128
                        __attrs_139839079510128 = _static_139839079557456

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="extension_ids:list"')

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839079497984
                        __default_139839079497984 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${info/id}' (204:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2a8c490> -> __attr_value
                        __token = 8812
                        __token = 8814
                        try:
                            __zt_tmp = __attrs_139839079510128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139839140402352('path', 'info/id', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_value = __attr_value
                        if (__attr_value is None):
                            pass
                        else:
                            if (__attr_value is _DEFAULT_MARKER):
                                __attr_value = None
                            else:
                                __tt = type(__attr_value)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __attr_value = str(__attr_value)
                                else:
                                    if (__tt is bytes):
                                        __attr_value = decode(__attr_value)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __attr_value = __attr_value.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__attr_value)
                                                __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                            else:
                                                __attr_value = __attr_value()
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n                ')
                    __append('\n              ')
                    if (__backup_selected_139839116659248 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_139839116659248
                    __append('\n            ')
                    ____index_139839079556304 -= 1
                    if (____index_139839079556304 > 0):
                        __append('')
                if (__backup_info_139839116668944 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_139839116668944
                __append('\n          ')
                __condition = __cache_139839079625584
                if __condition:
                    __append('</div>')
            if (__backup_has_selected_139839117248832 is __marker):
                del econtext['has_selected']
            else:
                econtext['has_selected'] = __backup_has_selected_139839117248832
            __append('\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2a980a0> name=None at 7f2ed2a9a560> -> __attrs_139839079557840
            __attrs_139839079557840 = _static_139839079547040

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mt-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2a8e110> name=None at 7f2ed2a8e380> -> __attrs_139839079506384
            __attrs_139839079506384 = _static_139839079506192

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="form.submitted:boolean" value="True" />\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2a8f520> name=None at 7f2ed2a8f550> -> __attrs_139839079501200
            __attrs_139839079501200 = _static_139839079511328

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-success mt-3" type="submit" name="submit">')
            __stream_139839079512864 = []
            __append_139839079512864 = __stream_139839079512864.append
            __append_139839079512864('Create Plone Site')
            __msgid_139839079512864 = __re_whitespace(''.join(__stream_139839079512864)).strip()
            if __msgid_139839079512864:
                __append(translate(__msgid_139839079512864, mapping=None, default=__msgid_139839079512864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n          </div>\n      </article>\n    </form>')
            if (__backup_advanced_139839117251184 is __marker):
                del econtext['advanced']
            else:
                econtext['advanced'] = __backup_advanced_139839117251184
            if (__backup_extension_profiles_139839115231584 is __marker):
                del econtext['extension_profiles']
            else:
                econtext['extension_profiles'] = __backup_extension_profiles_139839115231584
            if (__backup_default_profile_139839115231392 is __marker):
                del econtext['default_profile']
            else:
                econtext['default_profile'] = __backup_default_profile_139839115231392
            if (__backup_base_profiles_139839117259104 is __marker):
                del econtext['base_profiles']
            else:
                econtext['base_profiles'] = __backup_base_profiles_139839117259104
            if (__backup_profiles_139839117258576 is __marker):
                del econtext['profiles']
            else:
                econtext['profiles'] = __backup_profiles_139839117258576
            __append('\n  </div>\n</body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_139839079455600
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }