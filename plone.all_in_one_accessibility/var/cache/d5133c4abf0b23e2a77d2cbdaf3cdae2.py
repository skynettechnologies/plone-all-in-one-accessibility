# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/path_bar.pt'

__tokens = {96: ('python:view.breadcrumbs', 5, 19), 292: ('${python:view.navigation_root_url}', 12, 43), 294: ('python:view.navigation_root_url', 12, 45), 423: ('breadcrumbs', 15, 34), 500: ('not: repeat/crumb/end', 17, 27), 541: ("${python:crumb['absolute_url']}", 18, 18), 543: ("python:crumb['absolute_url']", 18, 20), 574: ("${python:crumb['Title']}", 18, 51), 576: ("python:crumb['Title']", 18, 53), 710: ('repeat/crumb/end', 21, 27), 737: ("${python:crumb['Title']}", 22, 9), 739: ("python:crumb['Title']", 22, 11)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882241821664 = {'class': 'breadcrumb-item active', 'aria-current': 'page', }
_static_139882241830208 = {'href': "${python:crumb['absolute_url']}", }
_static_139882206157488 = {'class': 'breadcrumb-item', }
_static_139882337226896 = {}
_static_139882206165312 = {'href': '${python:view.navigation_root_url}', }
_static_139882206159360 = {'class': 'breadcrumb-item', }
_static_139882206153504 = {'class': 'breadcrumb', }
_static_139882206156480 = {'class': 'container', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882206154464 = {'id': 'portal-breadcrumbs', 'aria-label': 'breadcrumb', 'label_breadcrumb': 'label_breadcrumb', }

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

            # <Static value=<ast.Dict object at 0x7f38dd354ee0> name=None at 7f38dd354fa0> -> __attrs_139882206162288
            __attrs_139882206162288 = _static_139882206154464
            __backup_breadcrumbs_139882205848928 = get('breadcrumbs', __marker)

            # <Value 'python:view.breadcrumbs' (5:19)> -> __value
            __token = 96
            try:
                __zt_tmp = __attrs_139882206162288
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', 'view.breadcrumbs', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['breadcrumbs'] = __value
            __previous_i18n_domain_139882206159072 = __i18n_domain
            __i18n_domain = 'plone'

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav id="portal-breadcrumbs" aria-label="breadcrumb"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206156672
            __default_139882206156672 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f38dd3568c0> at 7f38dd356230> -> __attr_label_breadcrumb
            __attr_label_breadcrumb = 'label_breadcrumb'
            __attr_label_breadcrumb = translate(__attr_label_breadcrumb, default=__attr_label_breadcrumb, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_label_breadcrumb is not None):
                __append((' label_breadcrumb="%s"' % __attr_label_breadcrumb))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7f38dd3556c0> name=None at 7f38dd357250> -> __attrs_139882206156624
            __attrs_139882206156624 = _static_139882206156480

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container">\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd354b20> name=None at 7f38dd3551b0> -> __attrs_139882206159312
            __attrs_139882206159312 = _static_139882206153504

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append('<ol class="breadcrumb">\n      ')

            # <Static value=<ast.Dict object at 0x7f38dd356200> name=None at 7f38dd3555d0> -> __attrs_139882206162912
            __attrs_139882206162912 = _static_139882206159360

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li class="breadcrumb-item">')

            # <Static value=<ast.Dict object at 0x7f38dd357940> name=None at 7f38dd357880> -> __attrs_139882206160224
            __attrs_139882206160224 = _static_139882206165312

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206153984
            __default_139882206153984 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python:view.navigation_root_url}' (12:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd357490> -> __attr_href
            __token = 292
            __token = 294
            try:
                __zt_tmp = __attrs_139882206160224
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139882257081264('python', 'view.navigation_root_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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
            __stream_139882206153360 = []
            __append_139882206153360 = __stream_139882206153360.append
            __append_139882206153360('Home')
            __msgid_139882206153360 = __re_whitespace(''.join(__stream_139882206153360)).strip()
            if 'tabs_home':
                __append(translate('tabs_home', mapping=None, default=__msgid_139882206153360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a></li>\n      ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206164160
            __attrs_139882206164160 = _static_139882337226896
            __backup_crumb_139882242313856 = get('crumb', __marker)

            # <Value 'breadcrumbs' (15:34)> -> __iterator
            __token = 423
            try:
                __zt_tmp = __attrs_139882206164160
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139882257081264('path', 'breadcrumbs', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            (__iterator, ____index_139882206161952, ) = getname('repeat')('crumb', __iterator)
            econtext['crumb'] = None
            for __item in __iterator:
                econtext['crumb'] = __item
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f38dd355ab0> name=None at 7f38dd3576d0> -> __attrs_139882241831168
                __attrs_139882241831168 = _static_139882206157488

                # <Value 'not: repeat/crumb/end' (17:27)> -> __condition
                __token = 500
                try:
                    __zt_tmp = __attrs_139882241831168
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('not', ' repeat/crumb/end', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item" >')

                    # <Static value=<ast.Dict object at 0x7f38df55ad40> name=None at 7f38df55bb20> -> __attrs_139882241834864
                    __attrs_139882241834864 = _static_139882241830208

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882241820560
                    __default_139882241820560 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:crumb['absolute_url']}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38df5585e0> -> __attr_href
                    __token = 541
                    __token = 543
                    try:
                        __zt_tmp = __attrs_139882241834864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('python', "crumb['absolute_url']", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (18:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38df5586d0> -> __content_139882343851824
                    __token = 574
                    __token = 576
                    try:
                        __zt_tmp = __attrs_139882241834864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139882343851824 = _static_139882257081264('python', "crumb['Title']", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __content_139882343851824 = __quote(__content_139882343851824, '\x00', '&#0;', None, None)
                    __content_139882343851824 = __content_139882343851824
                    if (__content_139882343851824 is None):
                        pass
                    else:
                        if (__content_139882343851824 is None):
                            __content_139882343851824 = None
                        else:
                            __tt = type(__content_139882343851824)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139882343851824 = str(__content_139882343851824)
                            else:
                                if (__tt is bytes):
                                    __content_139882343851824 = decode(__content_139882343851824)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139882343851824 = __content_139882343851824.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139882343851824)
                                            __content_139882343851824 = (str(__content_139882343851824) if (__content_139882343851824 is __converted) else __converted)
                                        else:
                                            __content_139882343851824 = __content_139882343851824()
                    if (__content_139882343851824 is not None):
                        __append(__content_139882343851824)
                    __append('</a></li>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f38df558be0> name=None at 7f38df558f70> -> __attrs_139882241823968
                __attrs_139882241823968 = _static_139882241821664

                # <Value 'repeat/crumb/end' (21:27)> -> __condition
                __token = 710
                try:
                    __zt_tmp = __attrs_139882241823968
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'repeat/crumb/end', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item active" aria-current="page" >')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (22:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38df5590c0> -> __content_139882343851824
                    __token = 737
                    __token = 739
                    try:
                        __zt_tmp = __attrs_139882241823968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139882343851824 = _static_139882257081264('python', "crumb['Title']", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __content_139882343851824 = __quote(__content_139882343851824, '\x00', '&#0;', None, None)
                    __content_139882343851824 = __content_139882343851824
                    if (__content_139882343851824 is None):
                        pass
                    else:
                        if (__content_139882343851824 is None):
                            __content_139882343851824 = None
                        else:
                            __tt = type(__content_139882343851824)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139882343851824 = str(__content_139882343851824)
                            else:
                                if (__tt is bytes):
                                    __content_139882343851824 = decode(__content_139882343851824)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139882343851824 = __content_139882343851824.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139882343851824)
                                            __content_139882343851824 = (str(__content_139882343851824) if (__content_139882343851824 is __converted) else __converted)
                                        else:
                                            __content_139882343851824 = __content_139882343851824()
                    if (__content_139882343851824 is not None):
                        __append(__content_139882343851824)
                    __append('</li>')
                __append('\n      ')
                ____index_139882206161952 -= 1
                if (____index_139882206161952 > 0):
                    __append('')
            if (__backup_crumb_139882242313856 is __marker):
                del econtext['crumb']
            else:
                econtext['crumb'] = __backup_crumb_139882242313856
            __append('\n    </ol>\n  </div>\n</nav>')
            __i18n_domain = __previous_i18n_domain_139882206159072
            if (__backup_breadcrumbs_139882205848928 is __marker):
                del econtext['breadcrumbs']
            else:
                econtext['breadcrumbs'] = __backup_breadcrumbs_139882205848928
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }