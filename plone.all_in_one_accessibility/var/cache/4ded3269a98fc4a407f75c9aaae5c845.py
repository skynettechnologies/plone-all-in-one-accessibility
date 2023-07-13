# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/plone-overview.pt'

__tokens = {581: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 16, 14), 583: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 16, 16), 727: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 19, 14), 729: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 19, 16), 830: ('view/sites', 23, 24), 864: (' python:len(sites) > ', 24, 22), 1087: ('string:${context/absolute_url}/++resource++plone-logo.svg', 29, 36), 1755: ('sites', 44, 28), 1802: ('sites', 45, 39), 1852: ('python: view.outdated(site)', 46, 42), 1910: ("mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", 47, 28), 1917: ("python: 'p-3 alert alert-warning' if outdated else ''", 47, 35), 2012: ('outdated', 48, 38), 2285: ('site/absolute_url', 50, 45), 2166: ("btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 49, 60), 2184: ("python:'btn-lg' if not many and not outdated  else ''", 49, 78), 2450: ('not: many', 53, 44), 2555: ('many', 54, 45), 2561: ('${python:site.title}', 54, 51), 2563: ('python:site.title', 54, 53), 2589: ('(${python:"/".join(site.getPhysicalPath())})', 54, 79), 2592: ('python:"/".join(site.getPhysicalPath())', 54, 82), 2851: ('outdated', 59, 43), 2912: ('python:view.upgrade_url(site)', 60, 51), 2990: ('not:view/can_manage', 61, 46), 3128: ('python:view.upgrade_url(site, can_manage=True)', 63, 54), 3620: ('sites', 74, 30), 3770: ('not:sites', 78, 30), 4017: ("python: '' if not sites else len(sites) + 1", 84, 44), 4100: (' string:${context/absolute_url}/@@plone-addsit', 85, 38), 4177: ('${action}', 86, 28), 4179: ('action', 86, 30), 4248: ('Plone${site_number}', 87, 59), 4255: ('site_number', 87, 66), 4341: ("btn btn-${python:'success' if sites else 'primary'}", 89, 31), 4351: ("python:'success' if sites else 'primary'", 89, 41), 4582: ('view/has_volto', 93, 35), 4624: ('${action}?site_id=Plone${site_number}&amp;classic=1', 94, 26), 4626: ('action', 94, 28), 4649: ('site_number', 94, 51), 4837: ('${action}?site_id=Plone${site_number}&amp;advanced=1', 98, 26), 4839: ('action', 98, 28), 4862: ('site_number', 98, 51), 6194: ('string:${context/absolute_url}/manage_main', 126, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140416200484240 = {'href': '#', 'title': 'Go to the ZMI', }
_static_140416200481168 = {'class': 'row', }
_static_140416200479920 = {'href': 'https://6.docs.plone.org/', 'title': 'Plone 6 developer documentation', }
_static_140416200475456 = {'class': 'btn btn-secondary', 'href': '${action}?site_id=Plone${site_number}&amp;advanced=1', }
_static_140416200456992 = {'class': 'btn btn-info', 'href': '${action}?site_id=Plone${site_number}&amp;classic=1', }
_static_140416200455120 = {'type': 'submit', 'class': "btn btn-${python:'success' if sites else 'primary'}", }
_static_140416200453248 = {'type': 'hidden', 'name': 'site_id', 'value': 'Plone${site_number}', }
_static_140416200450608 = {'id': 'add-plone-site', 'method': 'get', 'action': '${action}', }
_static_140416200448784 = {'class': 'alert alert-warning p-1', }
_static_140416200400064 = {'class': 'col-md-12', }
_static_140416200444800 = {'type': 'submit', 'class': 'btn btn-warning me-3', }
_static_140416200442832 = {'type': 'hidden', 'name': 'came_from', 'value': 'python:view.upgrade_url(site, can_manage=True)', }
_static_140416200407648 = {'action': '', 'style': 'display: inline;', 'method': 'get', }
_static_140416200403232 = {'href': '#', 'id': 'go-to-site-link', 'class': "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 'title': 'Go to your instance', }
_static_140416200398720 = {'class': "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", }
_static_140416200395984 = {'class': 'col-md-12 mb-4', }
_static_140416200394688 = {'class': 'row mb-5', }
_static_140416200393536 = {'href': 'http://plone.org', 'title': 'Plone Community Home', }
_static_140416200390688 = {'class': 'lead', }
_static_140416200389008 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_140416200385312 = {'class': 'row', }
_static_140416200383968 = {'class': 'container admin mt-5 mb-5 p-4', }
_static_140416200381280 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_140416288627712 = __C2ZContextWrapper
_static_140416288628000 = __compile_zt_expr
_static_140416200379456 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_140416200377200 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_140416200129888 = {'charset': 'utf-8', }
_static_140416369266208 = {}
_static_140416276950384 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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

            # <Static value=<ast.Dict object at 0x7fb5364eed70> name=None at 7fb5364ede10> -> __attrs_140416237144960
            __attrs_140416237144960 = _static_140416276950384
            __previous_i18n_domain_140416237148800 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200128880
            __attrs_140416200128880 = _static_140416369266208

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7fb531babd60> name=None at 7fb531babd90> -> __attrs_140416200130176
            __attrs_140416200130176 = _static_140416200129888

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8"/>\n  ')

            # <Static value=<ast.Dict object at 0x7fb531be8370> name=None at 7fb531be83a0> -> __attrs_140416200377296
            __attrs_140416200377296 = _static_140416200377200

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1"/>\n  ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200378064
            __attrs_140416200378064 = _static_140416369266208

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>Plone</title>\n  ')

            # <Static value=<ast.Dict object at 0x7fb531be8c40> name=None at 7fb531be8c70> -> __attrs_140416200380032
            __attrs_140416200380032 = _static_140416200379456

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200379600
            __default_140416200379600 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (16:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531be8970> -> __attr_href
            __token = 581
            __token = 583
            try:
                __zt_tmp = __attrs_140416200380032
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140416288628000('string', '${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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

            # <Static value=<ast.Dict object at 0x7fb531be9360> name=None at 7fb531be9390> -> __attrs_140416200381856
            __attrs_140416200381856 = _static_140416200381280

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200381424
            __default_140416200381424 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (19:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531be9090> -> __attr_href
            __token = 727
            __token = 729
            try:
                __zt_tmp = __attrs_140416200381856
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140416288628000('string', '${context/absolute_url}/++resource++plone-admin-ui.css', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200382624
            __attrs_140416200382624 = _static_140416369266208
            __backup_sites_140416276948944 = get('sites', __marker)

            # <Value 'view/sites' (23:24)> -> __value
            __token = 830
            try:
                __zt_tmp = __attrs_140416200382624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140416288628000('path', 'view/sites', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            econtext['sites'] = __value
            __backup_many_140416237148512 = get('many', __marker)

            # <Value 'python:len(sites) > 1' (24:22)> -> __value
            __token = 864
            try:
                __zt_tmp = __attrs_140416200382624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140416288628000('python', 'len(sites) > 1', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            econtext['many'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n  ')

            # <Static value=<ast.Dict object at 0x7fb531be9de0> name=None at 7fb531be9c30> -> __attrs_140416200384304
            __attrs_140416200384304 = _static_140416200383968

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4">\n    ')

            # <Static value=<ast.Dict object at 0x7fb531bea320> name=None at 7fb531bea350> -> __attrs_140416200385696
            __attrs_140416200385696 = _static_140416200385312

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n        ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200386704
            __attrs_140416200386704 = _static_140416369266208

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x7fb531beb190> name=None at 7fb531beb1c0> -> __attrs_140416200389152
            __attrs_140416200389152 = _static_140416200389008

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200388240
            __default_140416200388240 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (29:36)> -> __attr_src
            __token = 1087
            try:
                __zt_tmp = __attrs_140416200389152
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140416288628000('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200387616
            __default_140416200387616 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7fb531bead40> at 7fb531bead10> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n        ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200389824
            __attrs_140416200389824 = _static_140416369266208

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_140416200389248 = []
            __append_140416200389248 = __stream_140416200389248.append
            __append_140416200389248('Plone is up and running.')
            __msgid_140416200389248 = __re_whitespace(''.join(__stream_140416200389248)).strip()
            if __msgid_140416200389248:
                __append(translate(__msgid_140416200389248, mapping=None, default=__msgid_140416200389248, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n        ')

            # <Static value=<ast.Dict object at 0x7fb531beb820> name=None at 7fb531beb850> -> __attrs_140416200391072
            __attrs_140416200391072 = _static_140416200390688

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">\n            ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200392128
            __attrs_140416200392128 = _static_140416369266208

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_140416200391648 = []
            __append_140416200391648 = __stream_140416200391648.append
            __append_140416200391648(' For an introduction to Plone, documentation, demos, add-ons, support, and community, visit')
            __msgid_140416200391648 = __re_whitespace(''.join(__stream_140416200391648)).strip()
            if 'label_plone_org_description':
                __append(translate('label_plone_org_description', mapping=None, default=__msgid_140416200391648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n            ')

            # <Static value=<ast.Dict object at 0x7fb531bec340> name=None at 7fb531bebfd0> -> __attrs_140416200394016
            __attrs_140416200394016 = _static_140416200393536

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="http://plone.org"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200392864
            __default_140416200392864 = _DEFAULT_MARKER

            # <Translate msgid='label_plone_org_title' node=<ast.Constant object at 0x7fb531bec160> at 7fb531bec130> -> __attr_title
            __attr_title = 'Plone Community Home'
            __attr_title = translate('label_plone_org_title', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>plone.org</a>.\n          </p>\n\n    </header>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fb531bec7c0> name=None at 7fb531bec7f0> -> __attrs_140416200395072
            __attrs_140416200395072 = _static_140416200394688

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row mb-5">\n        ')

            # <Static value=<ast.Dict object at 0x7fb531beccd0> name=None at 7fb531becd00> -> __attrs_140416200396416
            __attrs_140416200396416 = _static_140416200395984

            # <Value 'sites' (44:28)> -> __condition
            __token = 1755
            try:
                __zt_tmp = __attrs_140416200396416
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140416288628000('path', 'sites', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-4">\n            ')

                # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200397472
                __attrs_140416200397472 = _static_140416369266208
                __backup_site_140416200387184 = get('site', __marker)

                # <Value 'sites' (45:39)> -> __iterator
                __token = 1802
                try:
                    __zt_tmp = __attrs_140416200397472
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140416288628000('path', 'sites', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                (__iterator, ____index_140416200397808, ) = getname('repeat')('site', __iterator)
                econtext['site'] = None
                for __item in __iterator:
                    econtext['site'] = __item
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7fb531bed780> name=None at 7fb531bed7b0> -> __attrs_140416200399584
                    __attrs_140416200399584 = _static_140416200398720
                    __backup_outdated_140416200392464 = get('outdated', __marker)

                    # <Value 'python: view.outdated(site)' (46:42)> -> __value
                    __token = 1852
                    try:
                        __zt_tmp = __attrs_140416200399584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140416288628000('python', ' view.outdated(site)', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                    econtext['outdated'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200398912
                    __default_140416200398912 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}" (47:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531bed630> -> __attr_class
                    __token = 1910
                    __token = 1917
                    try:
                        __zt_tmp = __attrs_140416200399584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140416288628000('python', " 'p-3 alert alert-warning' if outdated else ''", econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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

                    # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200400784
                    __attrs_140416200400784 = _static_140416369266208

                    # <Value 'outdated' (48:38)> -> __condition
                    __token = 2012
                    try:
                        __zt_tmp = __attrs_140416200400784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140416288628000('path', 'outdated', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_140416200400304 = []
                        __append_140416200400304 = __stream_140416200400304.append
                        __append_140416200400304('This site configuration is outdated and needs to be upgraded:')
                        __msgid_140416200400304 = __re_whitespace(''.join(__stream_140416200400304)).strip()
                        if __msgid_140416200400304:
                            __append(translate(__msgid_140416200400304, mapping=None, default=__msgid_140416200400304, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>')
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x7fb531bee920> name=None at 7fb531bee950> -> __attrs_140416200403856
                    __attrs_140416200403856 = _static_140416200403232

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200402752
                    __default_140416200402752 = _DEFAULT_MARKER

                    # <Substitution 'site/absolute_url' (50:45)> -> __attr_href
                    __token = 2285
                    try:
                        __zt_tmp = __attrs_140416200403856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140416288628000('path', 'site/absolute_url', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' id="go-to-site-link"')

                    # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200402080
                    __default_140416200402080 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}" (49:60)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531bee530> -> __attr_class
                    __token = 2166
                    __token = 2184
                    try:
                        __zt_tmp = __attrs_140416200403856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140416288628000('python', "'btn-lg' if not many and not outdated  else ''", econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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

                    # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200403328
                    __default_140416200403328 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7fb531bee350> at 7fb531bee320> -> __attr_title
                    __attr_title = 'Go to your instance'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>\n                        ')

                    # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200404816
                    __attrs_140416200404816 = _static_140416369266208

                    # <Value 'not: many' (53:44)> -> __condition
                    __token = 2450
                    try:
                        __zt_tmp = __attrs_140416200404816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140416288628000('not', ' many', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                    if __condition:
                        __stream_140416200404432 = []
                        __append_140416200404432 = __stream_140416200404432.append
                        __append_140416200404432('View your Plone site')
                        __msgid_140416200404432 = __re_whitespace(''.join(__stream_140416200404432)).strip()
                        if __msgid_140416200404432:
                            __append(translate(__msgid_140416200404432, mapping=None, default=__msgid_140416200404432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200405536
                    __attrs_140416200405536 = _static_140416369266208

                    # <Value 'many' (54:45)> -> __condition
                    __token = 2555
                    try:
                        __zt_tmp = __attrs_140416200405536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140416288628000('path', 'many', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                    if __condition:

                        # <Interpolation value=<Substitution '${python:site.title} ' (54:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531bef430> -> __content_140416375842224
                        __token = 2561
                        __token = 2563
                        try:
                            __zt_tmp = __attrs_140416200405536
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_140416375842224 = _static_140416288628000('python', 'site.title', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                        __content_140416375842224 = __quote(__content_140416375842224, '\x00', '&#0;', None, None)
                        __content_140416375842224 = ('%s%s' % ((__content_140416375842224 if (__content_140416375842224 is not None) else ''), ' ', ))
                        if (__content_140416375842224 is None):
                            pass
                        else:
                            if (__content_140416375842224 is None):
                                __content_140416375842224 = None
                            else:
                                __tt = type(__content_140416375842224)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_140416375842224 = str(__content_140416375842224)
                                else:
                                    if (__tt is bytes):
                                        __content_140416375842224 = decode(__content_140416375842224)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_140416375842224 = __content_140416375842224.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_140416375842224)
                                                __content_140416375842224 = (str(__content_140416375842224) if (__content_140416375842224 is __converted) else __converted)
                                            else:
                                                __content_140416375842224 = __content_140416375842224()
                        if (__content_140416375842224 is not None):
                            __append(__content_140416375842224)

                        # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200406784
                        __attrs_140416200406784 = _static_140416369266208

                        # <small ... (0:0)
                        # --------------------------------------------------------
                        __append('<small>')

                        # <Interpolation value=<Substitution '(${python:"/".join(site.getPhysicalPath())})' (54:79)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531bef850> -> __content_140416375842224
                        __token = 2589
                        __token = 2592
                        try:
                            __zt_tmp = __attrs_140416200406784
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_140416375842224 = _static_140416288628000('python', '"/".join(site.getPhysicalPath())', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                        __content_140416375842224 = __quote(__content_140416375842224, '\x00', '&#0;', None, None)
                        __content_140416375842224 = ('%s%s%s' % ('(', (__content_140416375842224 if (__content_140416375842224 is not None) else ''), ')', ))
                        if (__content_140416375842224 is None):
                            pass
                        else:
                            if (__content_140416375842224 is None):
                                __content_140416375842224 = None
                            else:
                                __tt = type(__content_140416375842224)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_140416375842224 = str(__content_140416375842224)
                                else:
                                    if (__tt is bytes):
                                        __content_140416375842224 = decode(__content_140416375842224)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_140416375842224 = __content_140416375842224.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_140416375842224)
                                                __content_140416375842224 = (str(__content_140416375842224) if (__content_140416375842224 is __converted) else __converted)
                                            else:
                                                __content_140416375842224 = __content_140416375842224()
                        if (__content_140416375842224 is not None):
                            __append(__content_140416375842224)
                        __append('</small>')
                    __append('\n                    </a>\n                    ')

                    # <Static value=<ast.Dict object at 0x7fb531befa60> name=None at 7fb531befa90> -> __attrs_140416200408320
                    __attrs_140416200408320 = _static_140416200407648

                    # <Value 'outdated' (59:43)> -> __condition
                    __token = 2851
                    try:
                        __zt_tmp = __attrs_140416200408320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140416288628000('path', 'outdated', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                    if __condition:

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form')

                        # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200407216
                        __default_140416200407216 = _DEFAULT_MARKER

                        # <Substitution 'python:view.upgrade_url(site)' (60:51)> -> __attr_action
                        __token = 2912
                        try:
                            __zt_tmp = __attrs_140416200408320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_action = _static_140416288628000('python', 'view.upgrade_url(site)', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_action is not None):
                            __append((' action="%s"' % __attr_action))
                        __append(' style="display: inline;" method="get">\n                        ')

                        # <Static value=<ast.Dict object at 0x7fb531bf83d0> name=None at 7fb531bf8400> -> __attrs_140416200443360
                        __attrs_140416200443360 = _static_140416200442832

                        # <Value 'not:view/can_manage' (61:46)> -> __condition
                        __token = 2990
                        try:
                            __zt_tmp = __attrs_140416200443360
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140416288628000('not', 'view/can_manage', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="came_from"')

                            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200441920
                            __default_140416200441920 = _DEFAULT_MARKER

                            # <Substitution 'python:view.upgrade_url(site, can_manage=True)' (63:54)> -> __attr_value
                            __token = 3128
                            try:
                                __zt_tmp = __attrs_140416200443360
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140416288628000('python', 'view.upgrade_url(site, can_manage=True)', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append('/>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7fb531bf8b80> name=None at 7fb531bf8bb0> -> __attrs_140416200444992
                        __attrs_140416200444992 = _static_140416200444800

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" class="btn btn-warning me-3">')
                        __stream_140416200443888 = []
                        __append_140416200443888 = __stream_140416200443888.append
                        __append_140416200443888('Upgrade&hellip;')
                        __msgid_140416200443888 = __re_whitespace(''.join(__stream_140416200443888)).strip()
                        if 'label_upgrade_hellip':
                            __append(translate('label_upgrade_hellip', mapping=None, default=__msgid_140416200443888, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>\n                    </form>')
                    __append('\n                </div>')
                    if (__backup_outdated_140416200392464 is __marker):
                        del econtext['outdated']
                    else:
                        econtext['outdated'] = __backup_outdated_140416200392464
                    __append('\n            ')
                    ____index_140416200397808 -= 1
                    if (____index_140416200397808 > 0):
                        __append('')
                if (__backup_site_140416200387184 is __marker):
                    del econtext['site']
                else:
                    econtext['site'] = __backup_site_140416200387184
                __append('\n        </div>')
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7fb531bedcc0> name=None at 7fb531befdc0> -> __attrs_140416200445568
            __attrs_140416200445568 = _static_140416200400064

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n            ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200446624
            __attrs_140416200446624 = _static_140416369266208

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2 >')
            __stream_140416200446144 = []
            __append_140416200446144 = __stream_140416200446144.append
            __append_140416200446144('Add Plone site')
            __msgid_140416200446144 = __re_whitespace(''.join(__stream_140416200446144)).strip()
            if __msgid_140416200446144:
                __append(translate(__msgid_140416200446144, mapping=None, default=__msgid_140416200446144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h2>\n            ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200447584
            __attrs_140416200447584 = _static_140416369266208

            # <Value 'sites' (74:30)> -> __condition
            __token = 3620
            try:
                __zt_tmp = __attrs_140416200447584
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140416288628000('path', 'sites', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_140416200447104 = []
                __append_140416200447104 = __stream_140416200447104.append
                __append_140416200447104('\n                You can add another Plone site to the server.\n            ')
                __msgid_140416200447104 = __re_whitespace(''.join(__stream_140416200447104)).strip()
                if __msgid_140416200447104:
                    __append(translate(__msgid_140416200447104, mapping=None, default=__msgid_140416200447104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fb531bf9b10> name=None at 7fb531bf9960> -> __attrs_140416200449120
            __attrs_140416200449120 = _static_140416200448784

            # <Value 'not:sites' (78:30)> -> __condition
            __token = 3770
            try:
                __zt_tmp = __attrs_140416200449120
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140416288628000('not', 'sites', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="alert alert-warning p-1">')
                __stream_140416200448256 = []
                __append_140416200448256 = __stream_140416200448256.append
                __append_140416200448256('\n                Your Plone site has not been added yet.\n            ')
                __msgid_140416200448256 = __re_whitespace(''.join(__stream_140416200448256)).strip()
                if __msgid_140416200448256:
                    __append(translate(__msgid_140416200448256, mapping=None, default=__msgid_140416200448256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fb531bfa230> name=None at 7fb531bfa260> -> __attrs_140416200451328
            __attrs_140416200451328 = _static_140416200450608
            __backup_site_number_140416200383248 = get('site_number', __marker)

            # <Value "python: '' if not sites else len(sites) + 1" (84:44)> -> __value
            __token = 4017
            try:
                __zt_tmp = __attrs_140416200451328
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140416288628000('python', " '' if not sites else len(sites) + 1", econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            econtext['site_number'] = __value
            __backup_action_140416200386032 = get('action', __marker)

            # <Value 'string:${context/absolute_url}/@@plone-addsite' (85:38)> -> __value
            __token = 4100
            try:
                __zt_tmp = __attrs_140416200451328
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140416288628000('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            econtext['action'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="add-plone-site" method="get"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200450800
            __default_140416200450800 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}' (86:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531bf9f90> -> __attr_action
            __token = 4177
            __token = 4179
            try:
                __zt_tmp = __attrs_140416200451328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140416288628000('path', 'action', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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

            # <Static value=<ast.Dict object at 0x7fb531bfac80> name=None at 7fb531bfacb0> -> __attrs_140416200453824
            __attrs_140416200453824 = _static_140416200453248

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="site_id"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200453392
            __default_140416200453392 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'Plone${site_number}' (87:59)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531bfa9b0> -> __attr_value
            __token = 4248
            __token = 4255
            try:
                __zt_tmp = __attrs_140416200453824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140416288628000('path', 'site_number', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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

            # <Static value=<ast.Dict object at 0x7fb531bfb3d0> name=None at 7fb531bfb400> -> __attrs_140416200455600
            __attrs_140416200455600 = _static_140416200455120

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200454448
            __default_140416200454448 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "btn btn-${python:'success' if sites else 'primary'}" (89:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531bfb1f0> -> __attr_class
            __token = 4341
            __token = 4351
            try:
                __zt_tmp = __attrs_140416200455600
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140416288628000('python', "'success' if sites else 'primary'", econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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
            __stream_140416200454208 = []
            __append_140416200454208 = __stream_140416200454208.append
            __append_140416200454208('Create a new Plone site')
            __msgid_140416200454208 = __re_whitespace(''.join(__stream_140416200454208)).strip()
            if __msgid_140416200454208:
                __append(translate(__msgid_140416200454208, mapping=None, default=__msgid_140416200454208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n                ')

            # <Static value=<ast.Dict object at 0x7fb531bfbb20> name=None at 7fb531bfbb50> -> __attrs_140416200457472
            __attrs_140416200457472 = _static_140416200456992

            # <Value 'view/has_volto' (93:35)> -> __condition
            __token = 4582
            try:
                __zt_tmp = __attrs_140416200457472
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140416288628000('path', 'view/has_volto', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="btn btn-info"')

                # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200456320
                __default_140416200456320 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;classic=1' (94:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531bfb940> -> __attr_href
                __token = 4624
                __token = 4626
                try:
                    __zt_tmp = __attrs_140416200457472
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140416288628000('path', 'action', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __token = 4649
                try:
                    __zt_tmp = __attrs_140416200457472
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href_4647 = _static_140416288628000('path', 'site_number', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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
                __stream_140416200456080 = []
                __append_140416200456080 = __stream_140416200456080.append
                __append_140416200456080('Create Classic Plone site')
                __msgid_140416200456080 = __re_whitespace(''.join(__stream_140416200456080)).strip()
                if __msgid_140416200456080:
                    __append(translate(__msgid_140416200456080, mapping=None, default=__msgid_140416200456080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            __append('\n                ')

            # <Static value=<ast.Dict object at 0x7fb531c00340> name=None at 7fb531c00370> -> __attrs_140416200475984
            __attrs_140416200475984 = _static_140416200475456

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-secondary"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200474736
            __default_140416200474736 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;advanced=1' (98:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fb531c00130> -> __attr_href
            __token = 4837
            __token = 4839
            try:
                __zt_tmp = __attrs_140416200475984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140416288628000('path', 'action', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 4862
            try:
                __zt_tmp = __attrs_140416200475984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href_4860 = _static_140416288628000('path', 'site_number', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
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
            __stream_140416200458144 = []
            __append_140416200458144 = __stream_140416200458144.append
            __append_140416200458144('Advanced')
            __msgid_140416200458144 = __re_whitespace(''.join(__stream_140416200458144)).strip()
            if __msgid_140416200458144:
                __append(translate(__msgid_140416200458144, mapping=None, default=__msgid_140416200458144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            </form>')
            if (__backup_action_140416200386032 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_140416200386032
            if (__backup_site_number_140416200383248 is __marker):
                del econtext['site_number']
            else:
                econtext['site_number'] = __backup_site_number_140416200383248
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200476656
            __attrs_140416200476656 = _static_140416369266208

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br/>\n            ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200477520
            __attrs_140416200477520 = _static_140416369266208

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_140416200477040 = []
            __append_140416200477040 = __stream_140416200477040.append
            __append_140416200477040("\n                Starting with Plone 6, 'Create a new Plone site' applies a\n                profile and creates default content for the new React based\n                default frontend Volto. You are however required to set up and run\n                an additional frontend service to use this setup.\n            ")
            __msgid_140416200477040 = __re_whitespace(''.join(__stream_140416200477040)).strip()
            if 'help_create_plone_site_buttons_1':
                __append(translate('help_create_plone_site_buttons_1', mapping=None, default=__msgid_140416200477040, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n            ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200478480
            __attrs_140416200478480 = _static_140416369266208

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_140416237581728_docs_link = ''
            __stream_140416200478000 = []
            __append_140416200478000 = __stream_140416200478000.append
            __append_140416200478000("\n                The 'Create Classic Plone site' button creates a Plone site configured\n                for HTML based output, as was already supported by previous Plone versions.\n                Please consult our\n                ")
            __stream_140416237581728_docs_link = []
            __append_140416237581728_docs_link = __stream_140416237581728_docs_link.append

            # <Static value=<ast.Dict object at 0x7fb531c014b0> name=None at 7fb531c014e0> -> __attrs_140416200480448
            __attrs_140416200480448 = _static_140416200479920

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140416237581728_docs_link('<a href="https://6.docs.plone.org/"')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200479200
            __default_140416200479200 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7fb531c012d0> at 7fb531c012a0> -> __attr_title
            __attr_title = 'Plone 6 developer documentation'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_140416237581728_docs_link((' title="%s"' % __attr_title))
            __append_140416237581728_docs_link('>')
            __stream_140416200479056 = []
            __append_140416200479056 = __stream_140416200479056.append
            __append_140416200479056('developer documentation overview ')
            __msgid_140416200479056 = __re_whitespace(''.join(__stream_140416200479056)).strip()
            if __msgid_140416200479056:
                __append_140416237581728_docs_link(translate(__msgid_140416200479056, mapping=None, default=__msgid_140416200479056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_140416237581728_docs_link('</a>')
            __append_140416200478000('${docs_link}')
            __stream_140416237581728_docs_link = ''.join(__stream_140416237581728_docs_link)
            __append_140416200478000('\n                for more information about differences and requirements for\n                these frontends and possible upgrade paths from older Plone versions\n                to Plone 6.\n            ')
            __msgid_140416200478000 = __re_whitespace(''.join(__stream_140416200478000)).strip()
            if 'help_create_plone_site_buttons_2':
                __append(translate('help_create_plone_site_buttons_2', mapping={'docs_link': __stream_140416237581728_docs_link, }, default=__msgid_140416200478000, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n    </article>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fb531c01990> name=None at 7fb531c019c0> -> __attrs_140416200481552
            __attrs_140416200481552 = _static_140416200481168

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer class="row">\n    ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200482512
            __attrs_140416200482512 = _static_140416369266208

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      ')

            # <Static value=<ast.Dict object at 0x7fb531c02590> name=None at 7fb531c02230> -> __attrs_140416200484864
            __attrs_140416200484864 = _static_140416200484240

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200483760
            __default_140416200483760 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/manage_main' (126:29)> -> __attr_href
            __token = 6194
            try:
                __zt_tmp = __attrs_140416200484864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140416288628000('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_140416288627712(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7fb536f95d20> -> __default_140416200484336
            __default_140416200484336 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7fb531c02290> at 7fb531c021a0> -> __attr_title
            __attr_title = 'Go to the ZMI'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')
            __stream_140416200483136 = []
            __append_140416200483136 = __stream_140416200483136.append
            __append_140416200483136('Management Interface')
            __msgid_140416200483136 = __re_whitespace(''.join(__stream_140416200483136)).strip()
            if 'label_zmi_link':
                __append(translate('label_zmi_link', mapping=None, default=__msgid_140416200483136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n      ')

            # <Static value=<ast.Dict object at 0x7fb53bcf8e20> name=None at 7fb53bcf90f0> -> __attrs_140416200485776
            __attrs_140416200485776 = _static_140416369266208

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_140416200485296 = []
            __append_140416200485296 = __stream_140416200485296.append
            __append_140416200485296(' &#151; low-level technical configuration.')
            __msgid_140416200485296 = __re_whitespace(''.join(__stream_140416200485296)).strip()
            if 'label_zmi_link_description':
                __append(translate('label_zmi_link_description', mapping=None, default=__msgid_140416200485296, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n    </p>\n  </footer>\n</div>\n</body>')
            if (__backup_many_140416237148512 is __marker):
                del econtext['many']
            else:
                econtext['many'] = __backup_many_140416237148512
            if (__backup_sites_140416276948944 is __marker):
                del econtext['sites']
            else:
                econtext['sites'] = __backup_sites_140416276948944
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_140416237148800
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }