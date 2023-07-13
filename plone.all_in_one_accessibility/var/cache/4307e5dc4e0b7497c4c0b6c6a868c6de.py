# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/plone-overview.pt'

__tokens = {581: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 16, 14), 583: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 16, 16), 727: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 19, 14), 729: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 19, 16), 830: ('view/sites', 23, 24), 864: (' python:len(sites) > ', 24, 22), 1087: ('string:${context/absolute_url}/++resource++plone-logo.svg', 29, 36), 1755: ('sites', 44, 28), 1802: ('sites', 45, 39), 1852: ('python: view.outdated(site)', 46, 42), 1910: ("mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", 47, 28), 1917: ("python: 'p-3 alert alert-warning' if outdated else ''", 47, 35), 2012: ('outdated', 48, 38), 2285: ('site/absolute_url', 50, 45), 2166: ("btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 49, 60), 2184: ("python:'btn-lg' if not many and not outdated  else ''", 49, 78), 2450: ('not: many', 53, 44), 2555: ('many', 54, 45), 2561: ('${python:site.title}', 54, 51), 2563: ('python:site.title', 54, 53), 2589: ('(${python:"/".join(site.getPhysicalPath())})', 54, 79), 2592: ('python:"/".join(site.getPhysicalPath())', 54, 82), 2851: ('outdated', 59, 43), 2912: ('python:view.upgrade_url(site)', 60, 51), 2990: ('not:view/can_manage', 61, 46), 3128: ('python:view.upgrade_url(site, can_manage=True)', 63, 54), 3620: ('sites', 74, 30), 3770: ('not:sites', 78, 30), 4017: ("python: '' if not sites else len(sites) + 1", 84, 44), 4100: (' string:${context/absolute_url}/@@plone-addsit', 85, 38), 4177: ('${action}', 86, 28), 4179: ('action', 86, 30), 4248: ('Plone${site_number}', 87, 59), 4255: ('site_number', 87, 66), 4341: ("btn btn-${python:'success' if sites else 'primary'}", 89, 31), 4351: ("python:'success' if sites else 'primary'", 89, 41), 4582: ('view/has_volto', 93, 35), 4624: ('${action}?site_id=Plone${site_number}&amp;classic=1', 94, 26), 4626: ('action', 94, 28), 4649: ('site_number', 94, 51), 4837: ('${action}?site_id=Plone${site_number}&amp;advanced=1', 98, 26), 4839: ('action', 98, 28), 4862: ('site_number', 98, 51), 6194: ('string:${context/absolute_url}/manage_main', 126, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139839123042416 = {'href': '#', 'title': 'Go to the ZMI', }
_static_139839123035936 = {'class': 'row', }
_static_139839123034688 = {'href': 'https://6.docs.plone.org/', 'title': 'Plone 6 developer documentation', }
_static_139839130428528 = {'class': 'btn btn-secondary', 'href': '${action}?site_id=Plone${site_number}&amp;advanced=1', }
_static_139839130428960 = {'class': 'btn btn-info', 'href': '${action}?site_id=Plone${site_number}&amp;classic=1', }
_static_139839130423488 = {'type': 'submit', 'class': "btn btn-${python:'success' if sites else 'primary'}", }
_static_139839130426272 = {'type': 'hidden', 'name': 'site_id', 'value': 'Plone${site_number}', }
_static_139839130430160 = {'id': 'add-plone-site', 'method': 'get', 'action': '${action}', }
_static_139839130427952 = {'class': 'alert alert-warning p-1', }
_static_139839092789920 = {'class': 'col-md-12', }
_static_139839130426224 = {'type': 'submit', 'class': 'btn btn-warning me-3', }
_static_139839117666928 = {'type': 'hidden', 'name': 'came_from', 'value': 'python:view.upgrade_url(site, can_manage=True)', }
_static_139839116414304 = {'action': '', 'style': 'display: inline;', 'method': 'get', }
_static_139839092794816 = {'href': '#', 'id': 'go-to-site-link', 'class': "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 'title': 'Go to your instance', }
_static_139839092791168 = {'class': "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", }
_static_139839092786368 = {'class': 'col-md-12 mb-4', }
_static_139839092791360 = {'class': 'row mb-5', }
_static_139839092792560 = {'href': 'http://plone.org', 'title': 'Plone Community Home', }
_static_139839092801392 = {'class': 'lead', }
_static_139839089957312 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_139839081899936 = {'class': 'row', }
_static_139839081897728 = {'class': 'container admin mt-5 mb-5 p-4', }
_static_139839081900368 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_139839140398752 = __C2ZContextWrapper
_static_139839140402352 = __compile_zt_expr
_static_139839116894720 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_139839116894960 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_139839116893328 = {'charset': 'utf-8', }
_static_139839134773072 = {}
_static_139839116886224 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')

            # <Static value=<ast.Dict object at 0x7f2ed4e340d0> name=None at 7f2ed4e340a0> -> __attrs_139839116887712
            __attrs_139839116887712 = _static_139839116886224
            __previous_i18n_domain_139839116891072 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839116888912
            __attrs_139839116888912 = _static_139839134773072

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed4e35c90> name=None at 7f2ed4e35900> -> __attrs_139839116891888
            __attrs_139839116891888 = _static_139839116893328

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8"/>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed4e362f0> name=None at 7f2ed4e36290> -> __attrs_139839116894912
            __attrs_139839116894912 = _static_139839116894960

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1"/>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839116899616
            __attrs_139839116899616 = _static_139839134773072

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>Plone</title>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed4e36200> name=None at 7f2ed4e361d0> -> __attrs_139839116896880
            __attrs_139839116896880 = _static_139839116894720

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839116894576
            __default_139839116894576 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (16:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed4e35b10> -> __attr_href
            __token = 581
            __token = 583
            try:
                __zt_tmp = __attrs_139839116896880
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

            # <Static value=<ast.Dict object at 0x7f2ed2cd6950> name=None at 7f2ed2cd6980> -> __attrs_139839081900848
            __attrs_139839081900848 = _static_139839081900368

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839081900512
            __default_139839081900512 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (19:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed2cd72e0> -> __attr_href
            __token = 727
            __token = 729
            try:
                __zt_tmp = __attrs_139839081900848
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
            __append(' />\n</head>\n\n\n')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839081904880
            __attrs_139839081904880 = _static_139839134773072
            __backup_sites_139839118833744 = get('sites', __marker)

            # <Value 'view/sites' (23:24)> -> __value
            __token = 830
            try:
                __zt_tmp = __attrs_139839081904880
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'view/sites', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['sites'] = __value
            __backup_many_139839118456528 = get('many', __marker)

            # <Value 'python:len(sites) > 1' (24:22)> -> __value
            __token = 864
            try:
                __zt_tmp = __attrs_139839081904880
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', 'len(sites) > 1', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['many'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed2cd5f00> name=None at 7f2ed2cd7c10> -> __attrs_139839081896048
            __attrs_139839081896048 = _static_139839081897728

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4">\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed2cd67a0> name=None at 7f2ed2cd7c70> -> __attrs_139839081905600
            __attrs_139839081905600 = _static_139839081899936

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839081898208
            __attrs_139839081898208 = _static_139839134773072

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x7f2ed34859c0> name=None at 7f2ed34868f0> -> __attrs_139839093666048
            __attrs_139839093666048 = _static_139839089957312

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839081905888
            __default_139839081905888 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (29:36)> -> __attr_src
            __token = 1087
            try:
                __zt_tmp = __attrs_139839093666048
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_139839140402352('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839081897248
            __default_139839081897248 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f2ed2cd7e50> at 7f2ed2cd7e20> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092796496
            __attrs_139839092796496 = _static_139839134773072

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_139839093666480 = []
            __append_139839093666480 = __stream_139839093666480.append
            __append_139839093666480('Plone is up and running.')
            __msgid_139839093666480 = __re_whitespace(''.join(__stream_139839093666480)).strip()
            if __msgid_139839093666480:
                __append(translate(__msgid_139839093666480, mapping=None, default=__msgid_139839093666480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed373bf70> name=None at 7f2ed373bf40> -> __attrs_139839092801008
            __attrs_139839092801008 = _static_139839092801392

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092799952
            __attrs_139839092799952 = _static_139839134773072

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_139839092800432 = []
            __append_139839092800432 = __stream_139839092800432.append
            __append_139839092800432(' For an introduction to Plone, documentation, demos, add-ons, support, and community, visit')
            __msgid_139839092800432 = __re_whitespace(''.join(__stream_139839092800432)).strip()
            if 'label_plone_org_description':
                __append(translate('label_plone_org_description', mapping=None, default=__msgid_139839092800432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed3739cf0> name=None at 7f2ed3739cc0> -> __attrs_139839092792032
            __attrs_139839092792032 = _static_139839092792560

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="http://plone.org"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839092799424
            __default_139839092799424 = _DEFAULT_MARKER

            # <Translate msgid='label_plone_org_title' node=<ast.Constant object at 0x7f2ed3739ed0> at 7f2ed3739f00> -> __attr_title
            __attr_title = 'Plone Community Home'
            __attr_title = translate('label_plone_org_title', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>plone.org</a>.\n          </p>\n\n    </header>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed3739840> name=None at 7f2ed3739810> -> __attrs_139839092785456
            __attrs_139839092785456 = _static_139839092791360

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row mb-5">\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed37384c0> name=None at 7f2ed37384f0> -> __attrs_139839092786800
            __attrs_139839092786800 = _static_139839092786368

            # <Value 'sites' (44:28)> -> __condition
            __token = 1755
            try:
                __zt_tmp = __attrs_139839092786800
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('path', 'sites', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-4">\n            ')

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092787856
                __attrs_139839092787856 = _static_139839134773072
                __backup_site_139839126166432 = get('site', __marker)

                # <Value 'sites' (45:39)> -> __iterator
                __token = 1802
                try:
                    __zt_tmp = __attrs_139839092787856
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139839140402352('path', 'sites', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                (__iterator, ____index_139839092798560, ) = getname('repeat')('site', __iterator)
                econtext['site'] = None
                for __item in __iterator:
                    econtext['site'] = __item
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed3739780> name=None at 7f2ed3739750> -> __attrs_139839092790304
                    __attrs_139839092790304 = _static_139839092791168
                    __backup_outdated_139839123015568 = get('outdated', __marker)

                    # <Value 'python: view.outdated(site)' (46:42)> -> __value
                    __token = 1852
                    try:
                        __zt_tmp = __attrs_139839092790304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139839140402352('python', ' view.outdated(site)', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    econtext['outdated'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839092790976
                    __default_139839092790976 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}" (47:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed373b6a0> -> __attr_class
                    __token = 1910
                    __token = 1917
                    try:
                        __zt_tmp = __attrs_139839092790304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139839140402352('python', " 'p-3 alert alert-warning' if outdated else ''", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('mb-3 ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append('>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092789200
                    __attrs_139839092789200 = _static_139839134773072

                    # <Value 'outdated' (48:38)> -> __condition
                    __token = 2012
                    try:
                        __zt_tmp = __attrs_139839092789200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139839140402352('path', 'outdated', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_139839092789680 = []
                        __append_139839092789680 = __stream_139839092789680.append
                        __append_139839092789680('This site configuration is outdated and needs to be upgraded:')
                        __msgid_139839092789680 = __re_whitespace(''.join(__stream_139839092789680)).strip()
                        if __msgid_139839092789680:
                            __append(translate(__msgid_139839092789680, mapping=None, default=__msgid_139839092789680, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>')
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x7f2ed373a5c0> name=None at 7f2ed373a5f0> -> __attrs_139839092793520
                    __attrs_139839092793520 = _static_139839092794816

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839092794336
                    __default_139839092794336 = _DEFAULT_MARKER

                    # <Substitution 'site/absolute_url' (50:45)> -> __attr_href
                    __token = 2285
                    try:
                        __zt_tmp = __attrs_139839092793520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139839140402352('path', 'site/absolute_url', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' id="go-to-site-link"')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839092793664
                    __default_139839092793664 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}" (49:60)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed373a1d0> -> __attr_class
                    __token = 2166
                    __token = 2184
                    try:
                        __zt_tmp = __attrs_139839092793520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139839140402352('python', "'btn-lg' if not many and not outdated  else ''", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('btn btn-primary ', (__attr_class if (__attr_class is not None) else ''), ))
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

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839092794912
                    __default_139839092794912 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f2ed3738c70> at 7f2ed3738ca0> -> __attr_title
                    __attr_title = 'Go to your instance'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839117541632
                    __attrs_139839117541632 = _static_139839134773072

                    # <Value 'not: many' (53:44)> -> __condition
                    __token = 2450
                    try:
                        __zt_tmp = __attrs_139839117541632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139839140402352('not', ' many', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    if __condition:
                        __stream_139839092788048 = []
                        __append_139839092788048 = __stream_139839092788048.append
                        __append_139839092788048('View your Plone site')
                        __msgid_139839092788048 = __re_whitespace(''.join(__stream_139839092788048)).strip()
                        if __msgid_139839092788048:
                            __append(translate(__msgid_139839092788048, mapping=None, default=__msgid_139839092788048, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092329296
                    __attrs_139839092329296 = _static_139839134773072

                    # <Value 'many' (54:45)> -> __condition
                    __token = 2555
                    try:
                        __zt_tmp = __attrs_139839092329296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139839140402352('path', 'many', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    if __condition:

                        # <Interpolation value=<Substitution '${python:site.title} ' (54:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed36cbdf0> -> __content_139839220113136
                        __token = 2561
                        __token = 2563
                        try:
                            __zt_tmp = __attrs_139839092329296
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139839220113136 = _static_139839140402352('python', 'site.title', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                        __content_139839220113136 = __quote(__content_139839220113136, '\x00', '&#0;', None, None)
                        __content_139839220113136 = ('%s%s' % ((__content_139839220113136 if (__content_139839220113136 is not None) else ''), ' ', ))
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

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839084167120
                        __attrs_139839084167120 = _static_139839134773072

                        # <small ... (0:0)
                        # --------------------------------------------------------
                        __append('<small>')

                        # <Interpolation value=<Substitution '(${python:"/".join(site.getPhysicalPath())})' (54:79)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed49f74f0> -> __content_139839220113136
                        __token = 2589
                        __token = 2592
                        try:
                            __zt_tmp = __attrs_139839084167120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139839220113136 = _static_139839140402352('python', '"/".join(site.getPhysicalPath())', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                        __content_139839220113136 = __quote(__content_139839220113136, '\x00', '&#0;', None, None)
                        __content_139839220113136 = ('%s%s%s' % ('(', (__content_139839220113136 if (__content_139839220113136 is not None) else ''), ')', ))
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
                        __append('</small>')
                    __append('\n                    </a>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f2ed4dc0d60> name=None at 7f2ed4dc1210> -> __attrs_139839093643856
                    __attrs_139839093643856 = _static_139839116414304

                    # <Value 'outdated' (59:43)> -> __condition
                    __token = 2851
                    try:
                        __zt_tmp = __attrs_139839093643856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139839140402352('path', 'outdated', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                    if __condition:

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form')

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839092334432
                        __default_139839092334432 = _DEFAULT_MARKER

                        # <Substitution 'python:view.upgrade_url(site)' (60:51)> -> __attr_action
                        __token = 2912
                        try:
                            __zt_tmp = __attrs_139839093643856
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_action = _static_139839140402352('python', 'view.upgrade_url(site)', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_action is not None):
                            __append((' action="%s"' % __attr_action))
                        __append(' style="display: inline;" method="get">\n                        ')

                        # <Static value=<ast.Dict object at 0x7f2ed4ef2a70> name=None at 7f2ed33e41f0> -> __attrs_139839130421760
                        __attrs_139839130421760 = _static_139839117666928

                        # <Value 'not:view/can_manage' (61:46)> -> __condition
                        __token = 2990
                        try:
                            __zt_tmp = __attrs_139839130421760
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139839140402352('not', 'view/can_manage', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="came_from"')

                            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839116747744
                            __default_139839116747744 = _DEFAULT_MARKER

                            # <Substitution 'python:view.upgrade_url(site, can_manage=True)' (63:54)> -> __attr_value
                            __token = 3128
                            try:
                                __zt_tmp = __attrs_139839130421760
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_139839140402352('python', 'view.upgrade_url(site, can_manage=True)', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append('/>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7f2ed5b1db70> name=None at 7f2ed5b1c670> -> __attrs_139839130420176
                        __attrs_139839130420176 = _static_139839130426224

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" class="btn btn-warning me-3">')
                        __stream_139839130430592 = []
                        __append_139839130430592 = __stream_139839130430592.append
                        __append_139839130430592('Upgrade&hellip;')
                        __msgid_139839130430592 = __re_whitespace(''.join(__stream_139839130430592)).strip()
                        if 'label_upgrade_hellip':
                            __append(translate('label_upgrade_hellip', mapping=None, default=__msgid_139839130430592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>\n                    </form>')
                    __append('\n                </div>')
                    if (__backup_outdated_139839123015568 is __marker):
                        del econtext['outdated']
                    else:
                        econtext['outdated'] = __backup_outdated_139839123015568
                    __append('\n            ')
                    ____index_139839092798560 -= 1
                    if (____index_139839092798560 > 0):
                        __append('')
                if (__backup_site_139839126166432 is __marker):
                    del econtext['site']
                else:
                    econtext['site'] = __backup_site_139839126166432
                __append('\n        </div>')
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed37392a0> name=None at 7f2ed33e5240> -> __attrs_139839130430832
            __attrs_139839130430832 = _static_139839092789920

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839130420944
            __attrs_139839130420944 = _static_139839134773072

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2 >')
            __stream_139839130428720 = []
            __append_139839130428720 = __stream_139839130428720.append
            __append_139839130428720('Add Plone site')
            __msgid_139839130428720 = __re_whitespace(''.join(__stream_139839130428720)).strip()
            if __msgid_139839130428720:
                __append(translate(__msgid_139839130428720, mapping=None, default=__msgid_139839130428720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h2>\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839130426608
            __attrs_139839130426608 = _static_139839134773072

            # <Value 'sites' (74:30)> -> __condition
            __token = 3620
            try:
                __zt_tmp = __attrs_139839130426608
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('path', 'sites', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_139839130426080 = []
                __append_139839130426080 = __stream_139839130426080.append
                __append_139839130426080('\n                You can add another Plone site to the server.\n            ')
                __msgid_139839130426080 = __re_whitespace(''.join(__stream_139839130426080)).strip()
                if __msgid_139839130426080:
                    __append(translate(__msgid_139839130426080, mapping=None, default=__msgid_139839130426080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5b1e230> name=None at 7f2ed5b1c250> -> __attrs_139839130432368
            __attrs_139839130432368 = _static_139839130427952

            # <Value 'not:sites' (78:30)> -> __condition
            __token = 3770
            try:
                __zt_tmp = __attrs_139839130432368
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('not', 'sites', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="alert alert-warning p-1">')
                __stream_139839130426752 = []
                __append_139839130426752 = __stream_139839130426752.append
                __append_139839130426752('\n                Your Plone site has not been added yet.\n            ')
                __msgid_139839130426752 = __re_whitespace(''.join(__stream_139839130426752)).strip()
                if __msgid_139839130426752:
                    __append(translate(__msgid_139839130426752, mapping=None, default=__msgid_139839130426752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5b1ead0> name=None at 7f2ed5b1eaa0> -> __attrs_139839130425600
            __attrs_139839130425600 = _static_139839130430160
            __backup_site_number_139839119722864 = get('site_number', __marker)

            # <Value "python: '' if not sites else len(sites) + 1" (84:44)> -> __value
            __token = 4017
            try:
                __zt_tmp = __attrs_139839130425600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', " '' if not sites else len(sites) + 1", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['site_number'] = __value
            __backup_action_139839119729728 = get('action', __marker)

            # <Value 'string:${context/absolute_url}/@@plone-addsite' (85:38)> -> __value
            __token = 4100
            try:
                __zt_tmp = __attrs_139839130425600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['action'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="add-plone-site" method="get"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839130430496
            __default_139839130430496 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}' (86:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed5b1f3d0> -> __attr_action
            __token = 4177
            __token = 4179
            try:
                __zt_tmp = __attrs_139839130425600
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_139839140402352('path', 'action', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_action = __attr_action
            if (__attr_action is None):
                pass
            else:
                if (__attr_action is _DEFAULT_MARKER):
                    __attr_action = None
                else:
                    __tt = type(__attr_action)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_action = str(__attr_action)
                    else:
                        if (__tt is bytes):
                            __attr_action = decode(__attr_action)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_action = __attr_action.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_action)
                                    __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                else:
                                    __attr_action = __attr_action()
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n                ')

            # <Static value=<ast.Dict object at 0x7f2ed5b1dba0> name=None at 7f2ed5b1faf0> -> __attrs_139839130434096
            __attrs_139839130434096 = _static_139839130426272

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="site_id"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839130423344
            __default_139839130423344 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'Plone${site_number}' (87:59)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed5b1caf0> -> __attr_value
            __token = 4248
            __token = 4255
            try:
                __zt_tmp = __attrs_139839130434096
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139839140402352('path', 'site_number', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_value = ('%s%s' % ('Plone', (__attr_value if (__attr_value is not None) else ''), ))
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

            # <Static value=<ast.Dict object at 0x7f2ed5b1d0c0> name=None at 7f2ed5b1d090> -> __attrs_139839130433904
            __attrs_139839130433904 = _static_139839130423488

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839130423584
            __default_139839130423584 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "btn btn-${python:'success' if sites else 'primary'}" (89:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed5b1fd60> -> __attr_class
            __token = 4341
            __token = 4351
            try:
                __zt_tmp = __attrs_139839130433904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139839140402352('python', "'success' if sites else 'primary'", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s' % ('btn btn-', (__attr_class if (__attr_class is not None) else ''), ))
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
            __append('>')
            __stream_139839130434192 = []
            __append_139839130434192 = __stream_139839130434192.append
            __append_139839130434192('Create a new Plone site')
            __msgid_139839130434192 = __re_whitespace(''.join(__stream_139839130434192)).strip()
            if __msgid_139839130434192:
                __append(translate(__msgid_139839130434192, mapping=None, default=__msgid_139839130434192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n                ')

            # <Static value=<ast.Dict object at 0x7f2ed5b1e620> name=None at 7f2ed5b1e890> -> __attrs_139839130429104
            __attrs_139839130429104 = _static_139839130428960

            # <Value 'view/has_volto' (93:35)> -> __condition
            __token = 4582
            try:
                __zt_tmp = __attrs_139839130429104
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('path', 'view/has_volto', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="btn btn-info"')

                # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839130428192
                __default_139839130428192 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;classic=1' (94:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed5b1d6c0> -> __attr_href
                __token = 4624
                __token = 4626
                try:
                    __zt_tmp = __attrs_139839130429104
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139839140402352('path', 'action', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __token = 4649
                try:
                    __zt_tmp = __attrs_139839130429104
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href_4647 = _static_139839140402352('path', 'site_number', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                __attr_href_4647 = __quote(__attr_href_4647, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4647 if (__attr_href_4647 is not None) else ''), '&amp;classic=1', ))
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
                __append(' >')
                __stream_139839130425984 = []
                __append_139839130425984 = __stream_139839130425984.append
                __append_139839130425984('Create Classic Plone site')
                __msgid_139839130425984 = __re_whitespace(''.join(__stream_139839130425984)).strip()
                if __msgid_139839130425984:
                    __append(translate(__msgid_139839130425984, mapping=None, default=__msgid_139839130425984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            __append('\n                ')

            # <Static value=<ast.Dict object at 0x7f2ed5b1e470> name=None at 7f2ed5b1d4e0> -> __attrs_139839123032096
            __attrs_139839123032096 = _static_139839130428528

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-secondary"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839130421664
            __default_139839130421664 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;advanced=1' (98:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed5b1d870> -> __attr_href
            __token = 4837
            __token = 4839
            try:
                __zt_tmp = __attrs_139839123032096
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139839140402352('path', 'action', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 4862
            try:
                __zt_tmp = __attrs_139839123032096
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href_4860 = _static_139839140402352('path', 'site_number', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_href_4860 = __quote(__attr_href_4860, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4860 if (__attr_href_4860 is not None) else ''), '&amp;advanced=1', ))
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
            __append(' >')
            __stream_139839130431696 = []
            __append_139839130431696 = __stream_139839130431696.append
            __append_139839130431696('Advanced')
            __msgid_139839130431696 = __re_whitespace(''.join(__stream_139839130431696)).strip()
            if __msgid_139839130431696:
                __append(translate(__msgid_139839130431696, mapping=None, default=__msgid_139839130431696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            </form>')
            if (__backup_action_139839119729728 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_139839119729728
            if (__backup_site_number_139839119722864 is __marker):
                del econtext['site_number']
            else:
                econtext['site_number'] = __backup_site_number_139839119722864
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839123042512
            __attrs_139839123042512 = _static_139839134773072

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br/>\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839123043520
            __attrs_139839123043520 = _static_139839134773072

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_139839123034400 = []
            __append_139839123034400 = __stream_139839123034400.append
            __append_139839123034400("\n                Starting with Plone 6, 'Create a new Plone site' applies a\n                profile and creates default content for the new React based\n                default frontend Volto. You are however required to set up and run\n                an additional frontend service to use this setup.\n            ")
            __msgid_139839123034400 = __re_whitespace(''.join(__stream_139839123034400)).strip()
            if 'help_create_plone_site_buttons_1':
                __append(translate('help_create_plone_site_buttons_1', mapping=None, default=__msgid_139839123034400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839123042368
            __attrs_139839123042368 = _static_139839134773072

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_139839117806720_docs_link = ''
            __stream_139839123046112 = []
            __append_139839123046112 = __stream_139839123046112.append
            __append_139839123046112("\n                The 'Create Classic Plone site' button creates a Plone site configured\n                for HTML based output, as was already supported by previous Plone versions.\n                Please consult our\n                ")
            __stream_139839117806720_docs_link = []
            __append_139839117806720_docs_link = __stream_139839117806720_docs_link.append

            # <Static value=<ast.Dict object at 0x7f2ed5411240> name=None at 7f2ed5411300> -> __attrs_139839123031856
            __attrs_139839123031856 = _static_139839123034688

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139839117806720_docs_link('<a href="https://6.docs.plone.org/"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839123035360
            __default_139839123035360 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f2ed5411360> at 7f2ed54112d0> -> __attr_title
            __attr_title = 'Plone 6 developer documentation'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_139839117806720_docs_link((' title="%s"' % __attr_title))
            __append_139839117806720_docs_link('>')
            __stream_139839123038864 = []
            __append_139839123038864 = __stream_139839123038864.append
            __append_139839123038864('developer documentation overview ')
            __msgid_139839123038864 = __re_whitespace(''.join(__stream_139839123038864)).strip()
            if __msgid_139839123038864:
                __append_139839117806720_docs_link(translate(__msgid_139839123038864, mapping=None, default=__msgid_139839123038864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_139839117806720_docs_link('</a>')
            __append_139839123046112('${docs_link}')
            __stream_139839117806720_docs_link = ''.join(__stream_139839117806720_docs_link)
            __append_139839123046112('\n                for more information about differences and requirements for\n                these frontends and possible upgrade paths from older Plone versions\n                to Plone 6.\n            ')
            __msgid_139839123046112 = __re_whitespace(''.join(__stream_139839123046112)).strip()
            if 'help_create_plone_site_buttons_2':
                __append(translate('help_create_plone_site_buttons_2', mapping={'docs_link': __stream_139839117806720_docs_link, }, default=__msgid_139839123046112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n    </article>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5411720> name=None at 7f2ed54137f0> -> __attrs_139839123041744
            __attrs_139839123041744 = _static_139839123035936

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer class="row">\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839123039392
            __attrs_139839123039392 = _static_139839134773072

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed5413070> name=None at 7f2ed54129b0> -> __attrs_139839123030080
            __attrs_139839123030080 = _static_139839123042416

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839123041504
            __default_139839123041504 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/manage_main' (126:29)> -> __attr_href
            __token = 6194
            try:
                __zt_tmp = __attrs_139839123030080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139839140402352('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839123038288
            __default_139839123038288 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f2ed5412da0> at 7f2ed5413760> -> __attr_title
            __attr_title = 'Go to the ZMI'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')
            __stream_139839123041216 = []
            __append_139839123041216 = __stream_139839123041216.append
            __append_139839123041216('Management Interface')
            __msgid_139839123041216 = __re_whitespace(''.join(__stream_139839123041216)).strip()
            if 'label_zmi_link':
                __append(translate('label_zmi_link', mapping=None, default=__msgid_139839123041216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839123035648
            __attrs_139839123035648 = _static_139839134773072

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_139839123032576 = []
            __append_139839123032576 = __stream_139839123032576.append
            __append_139839123032576(' &#151; low-level technical configuration.')
            __msgid_139839123032576 = __re_whitespace(''.join(__stream_139839123032576)).strip()
            if 'label_zmi_link_description':
                __append(translate('label_zmi_link_description', mapping=None, default=__msgid_139839123032576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n    </p>\n  </footer>\n</div>\n</body>')
            if (__backup_many_139839118456528 is __marker):
                del econtext['many']
            else:
                econtext['many'] = __backup_many_139839118456528
            if (__backup_sites_139839118833744 is __marker):
                del econtext['sites']
            else:
                econtext['sites'] = __backup_sites_139839118833744
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_139839116891072
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }