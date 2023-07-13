# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/path_bar.pt'

__tokens = {96: ('python:view.breadcrumbs', 5, 19), 292: ('${python:view.navigation_root_url}', 12, 43), 294: ('python:view.navigation_root_url', 12, 45), 423: ('breadcrumbs', 15, 34), 500: ('not: repeat/crumb/end', 17, 27), 541: ("${python:crumb['absolute_url']}", 18, 18), 543: ("python:crumb['absolute_url']", 18, 20), 574: ("${python:crumb['Title']}", 18, 51), 576: ("python:crumb['Title']", 18, 53), 710: ('repeat/crumb/end', 21, 27), 737: ("${python:crumb['Title']}", 22, 9), 739: ("python:crumb['Title']", 22, 11)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310475817792 = {'class': 'breadcrumb-item active', 'aria-current': 'page', }
_static_140310272440688 = {'href': "${python:crumb['absolute_url']}", }
_static_140310272433728 = {'class': 'breadcrumb-item', }
_static_140310566789392 = {}
_static_140310272431952 = {'href': '${python:view.navigation_root_url}', }
_static_140310272428544 = {'class': 'breadcrumb-item', }
_static_140310272440016 = {'class': 'breadcrumb', }
_static_140310272430224 = {'class': 'container', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310272439584 = {'id': 'portal-breadcrumbs', 'aria-label': 'breadcrumb', 'label_breadcrumb': 'label_breadcrumb', }

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
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f9c87f27520> name=None at 7f9c87f25db0> -> __attrs_140310272436944
            __attrs_140310272436944 = _static_140310272439584
            __backup_breadcrumbs_140310272551728 = get('breadcrumbs', __marker)

            # <Value 'python:view.breadcrumbs' (5:19)> -> __value
            __token = 96
            try:
                __zt_tmp = __attrs_140310272436944
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', 'view.breadcrumbs', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['breadcrumbs'] = __value
            __previous_i18n_domain_140310272432576 = __i18n_domain
            __i18n_domain = 'plone'

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav id="portal-breadcrumbs" aria-label="breadcrumb"')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272434352
            __default_140310272434352 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f9c87f26590> at 7f9c87f27880> -> __attr_label_breadcrumb
            __attr_label_breadcrumb = 'label_breadcrumb'
            __attr_label_breadcrumb = translate(__attr_label_breadcrumb, default=__attr_label_breadcrumb, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_label_breadcrumb is not None):
                __append((' label_breadcrumb="%s"' % __attr_label_breadcrumb))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7f9c87f25090> name=None at 7f9c87f24c70> -> __attrs_140310272437664
            __attrs_140310272437664 = _static_140310272430224

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container">\n    ')

            # <Static value=<ast.Dict object at 0x7f9c87f276d0> name=None at 7f9c87f27d90> -> __attrs_140310272428880
            __attrs_140310272428880 = _static_140310272440016

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append('<ol class="breadcrumb">\n      ')

            # <Static value=<ast.Dict object at 0x7f9c87f24a00> name=None at 7f9c87f27d00> -> __attrs_140310272441312
            __attrs_140310272441312 = _static_140310272428544

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li class="breadcrumb-item">')

            # <Static value=<ast.Dict object at 0x7f9c87f25750> name=None at 7f9c87f27cd0> -> __attrs_140310272439872
            __attrs_140310272439872 = _static_140310272431952

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272427008
            __default_140310272427008 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python:view.navigation_root_url}' (12:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c87f27a00> -> __attr_href
            __token = 292
            __token = 294
            try:
                __zt_tmp = __attrs_140310272439872
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140310567013776('python', 'view.navigation_root_url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
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
            __append(' >')
            __stream_140310272440928 = []
            __append_140310272440928 = __stream_140310272440928.append
            __append_140310272440928('Home')
            __msgid_140310272440928 = __re_whitespace(''.join(__stream_140310272440928)).strip()
            if 'tabs_home':
                __append(translate('tabs_home', mapping=None, default=__msgid_140310272440928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a></li>\n      ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272441264
            __attrs_140310272441264 = _static_140310566789392
            __backup_crumb_140310475171840 = get('crumb', __marker)

            # <Value 'breadcrumbs' (15:34)> -> __iterator
            __token = 423
            try:
                __zt_tmp = __attrs_140310272441264
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140310567013776('path', 'breadcrumbs', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            (__iterator, ____index_140310272426480, ) = getname('repeat')('crumb', __iterator)
            econtext['crumb'] = None
            for __item in __iterator:
                econtext['crumb'] = __item
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f9c87f25e40> name=None at 7f9c87f261d0> -> __attrs_140310272427344
                __attrs_140310272427344 = _static_140310272433728

                # <Value 'not: repeat/crumb/end' (17:27)> -> __condition
                __token = 500
                try:
                    __zt_tmp = __attrs_140310272427344
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('not', ' repeat/crumb/end', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item" >')

                    # <Static value=<ast.Dict object at 0x7f9c87f27970> name=None at 7f9c87f24eb0> -> __attrs_140310475829408
                    __attrs_140310475829408 = _static_140310272440688

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272435120
                    __default_140310272435120 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:crumb['absolute_url']}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c87f244c0> -> __attr_href
                    __token = 541
                    __token = 543
                    try:
                        __zt_tmp = __attrs_140310475829408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140310567013776('python', "crumb['absolute_url']", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
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
                    __append('>')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (18:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9411ed40> -> __content_140310653968752
                    __token = 574
                    __token = 576
                    try:
                        __zt_tmp = __attrs_140310475829408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140310653968752 = _static_140310567013776('python', "crumb['Title']", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __content_140310653968752 = __quote(__content_140310653968752, '\x00', '&#0;', None, None)
                    __content_140310653968752 = __content_140310653968752
                    if (__content_140310653968752 is None):
                        pass
                    else:
                        if (__content_140310653968752 is None):
                            __content_140310653968752 = None
                        else:
                            __tt = type(__content_140310653968752)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140310653968752 = str(__content_140310653968752)
                            else:
                                if (__tt is bytes):
                                    __content_140310653968752 = decode(__content_140310653968752)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140310653968752 = __content_140310653968752.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140310653968752)
                                            __content_140310653968752 = (str(__content_140310653968752) if (__content_140310653968752 is __converted) else __converted)
                                        else:
                                            __content_140310653968752 = __content_140310653968752()
                    if (__content_140310653968752 is not None):
                        __append(__content_140310653968752)
                    __append('</a></li>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f9c9411c340> name=None at 7f9c9411da80> -> __attrs_140310475822208
                __attrs_140310475822208 = _static_140310475817792

                # <Value 'repeat/crumb/end' (21:27)> -> __condition
                __token = 710
                try:
                    __zt_tmp = __attrs_140310475822208
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'repeat/crumb/end', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item active" aria-current="page" >')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (22:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9411cfa0> -> __content_140310653968752
                    __token = 737
                    __token = 739
                    try:
                        __zt_tmp = __attrs_140310475822208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140310653968752 = _static_140310567013776('python', "crumb['Title']", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __content_140310653968752 = __quote(__content_140310653968752, '\x00', '&#0;', None, None)
                    __content_140310653968752 = __content_140310653968752
                    if (__content_140310653968752 is None):
                        pass
                    else:
                        if (__content_140310653968752 is None):
                            __content_140310653968752 = None
                        else:
                            __tt = type(__content_140310653968752)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140310653968752 = str(__content_140310653968752)
                            else:
                                if (__tt is bytes):
                                    __content_140310653968752 = decode(__content_140310653968752)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140310653968752 = __content_140310653968752.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140310653968752)
                                            __content_140310653968752 = (str(__content_140310653968752) if (__content_140310653968752 is __converted) else __converted)
                                        else:
                                            __content_140310653968752 = __content_140310653968752()
                    if (__content_140310653968752 is not None):
                        __append(__content_140310653968752)
                    __append('</li>')
                __append('\n      ')
                ____index_140310272426480 -= 1
                if (____index_140310272426480 > 0):
                    __append('')
            if (__backup_crumb_140310475171840 is __marker):
                del econtext['crumb']
            else:
                econtext['crumb'] = __backup_crumb_140310475171840
            __append('\n    </ol>\n  </div>\n</nav>')
            __i18n_domain = __previous_i18n_domain_140310272432576
            if (__backup_breadcrumbs_140310272551728 is __marker):
                del econtext['breadcrumbs']
            else:
                econtext['breadcrumbs'] = __backup_breadcrumbs_140310272551728
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }