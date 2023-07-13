# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.portlets-5.0.6-py3.10.egg/plone/app/portlets/portlets/actions.pt'

__tokens = {285: ('context/@@plone_portal_state/portal_url', 10, 20), 393: ('view/showTitle', 15, 24), 442: ('view/title', 17, 27), 479: ('view/title', 18, 25), 627: ('string:actions-${view/category}', 26, 18), 708: ('view/actionLinks', 28, 35), 842: ('nocall:link/icon', 31, 21), 748: ("portletItem action-item-${python:link['id']}", 29, 21), 774: ("python:link['id']", 29, 47), 963: ('link/modal|nothing', 36, 23), 1054: ('link/url', 39, 22), 1086: (" python:'pat-plone-modal' if modal else Non", 40, 22), 1168: ('l python:modal if modal else No', 41, 36), 1269: ('not:icon', 44, 35), 1312: ('link/title', 45, 33), 1447: ('icon/absolute_url|icon', 50, 31), 1528: ('icon', 52, 35), 1644: ('string:background-image:url($icon_url);', 55, 28), 1567: ('link/title', 53, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882206294224 = {'style': 'string:background-image:url($icon_url);', }
_static_139882215481328 = {'href': '#', 'class': "python:'pat-plone-modal' if modal else None", 'data-pat-plone-modal': 'python:modal if modal else None', }
_static_139882206287600 = {'class': "portletItem action-item-${python:link['id']}", }
_static_139882206292736 = {'class': 'string:actions-${view/category}', }
_static_139882206291056 = {'class': 'card-body portletContent', }
_static_139882337226896 = {}
_static_139882101359472 = {'class': 'card-header', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882101363408 = {'class': 'card portlet portletActions', }
_static_139882101359856 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f38d6f644f0> name=None at 7f38d6f65fc0> -> __attrs_139882101361200
            __attrs_139882101361200 = _static_139882101359856
            __previous_i18n_domain_139882101371136 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f38d6f652d0> name=None at 7f38d6f67910> -> __attrs_139882101367344
            __attrs_139882101367344 = _static_139882101363408
            __backup_portal_url_139882205639536 = get('portal_url', __marker)

            # <Value 'context/@@plone_portal_state/portal_url' (10:20)> -> __value
            __token = 285
            try:
                __zt_tmp = __attrs_139882101367344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'context/@@plone_portal_state/portal_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['portal_url'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card portlet portletActions" >\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38d6f64370> name=None at 7f38d6f66dd0> -> __attrs_139882101371280
            __attrs_139882101371280 = _static_139882101359472

            # <Value 'view/showTitle' (15:24)> -> __condition
            __token = 393
            try:
                __zt_tmp = __attrs_139882101371280
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('path', 'view/showTitle', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-header" >\n      ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101373920
                __attrs_139882101373920 = _static_139882337226896

                # <Value 'view/title' (17:27)> -> __condition
                __token = 442
                try:
                    __zt_tmp = __attrs_139882101373920
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'view/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101360144
                    __default_139882101360144 = _DEFAULT_MARKER

                    # <Value 'view/title' (18:25)> -> __cache_139882101374208
                    __token = 479
                    try:
                        __zt_tmp = __attrs_139882101373920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882101374208 = _static_139882257081264('path', 'view/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/title' (18:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6f65ff0> -> __condition
                    __expression = __cache_139882101374208

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n        Title\n      </span>')
                    else:
                        __content = __cache_139882101374208
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                __append('\n    </div>')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd376470> name=None at 7f38dd3765f0> -> __attrs_139882206282704
            __attrs_139882206282704 = _static_139882206291056

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body portletContent">\n      ')

            # <Static value=<ast.Dict object at 0x7f38dd376b00> name=None at 7f38dd3766b0> -> __attrs_139882206282176
            __attrs_139882206282176 = _static_139882206292736

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206294896
            __default_139882206294896 = _DEFAULT_MARKER

            # <Substitution 'string:actions-${view/category}' (26:18)> -> __attr_class
            __token = 627
            try:
                __zt_tmp = __attrs_139882206282176
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139882257081264('string', 'actions-${view/category}', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n        ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206283760
            __attrs_139882206283760 = _static_139882337226896
            __backup_link_139882101369888 = get('link', __marker)

            # <Value 'view/actionLinks' (28:35)> -> __iterator
            __token = 708
            try:
                __zt_tmp = __attrs_139882206283760
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139882257081264('path', 'view/actionLinks', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            (__iterator, ____index_139882206296624, ) = getname('repeat')('link', __iterator)
            econtext['link'] = None
            for __item in __iterator:
                econtext['link'] = __item
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f38dd3756f0> name=None at 7f38dd374ee0> -> __attrs_139882206284672
                __attrs_139882206284672 = _static_139882206287600
                __backup_icon_139882101373296 = get('icon', __marker)

                # <Value 'nocall:link/icon' (31:21)> -> __value
                __token = 842
                try:
                    __zt_tmp = __attrs_139882206284672
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('nocall', 'link/icon', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['icon'] = __value

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206291968
                __default_139882206291968 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution "portletItem action-item-${python:link['id']}" (29:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd376f80> -> __attr_class
                __token = 748
                __token = 774
                try:
                    __zt_tmp = __attrs_139882206284672
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_139882257081264('python', "link['id']", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_class = ('%s%s' % ('portletItem action-item-', (__attr_class if (__attr_class is not None) else ''), ))
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
                __append(' >\n            ')

                # <Static value=<ast.Dict object at 0x7f38ddc39ff0> name=None at 7f38ddf4cd60> -> __attrs_139882206290240
                __attrs_139882206290240 = _static_139882215481328
                __backup_modal_139882206286592 = get('modal', __marker)

                # <Value 'link/modal|nothing' (36:23)> -> __value
                __token = 963
                try:
                    __zt_tmp = __attrs_139882206290240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'link/modal|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['modal'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206296528
                __default_139882206296528 = _DEFAULT_MARKER

                # <Substitution 'link/url' (39:22)> -> __attr_href
                __token = 1054
                try:
                    __zt_tmp = __attrs_139882206290240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139882257081264('path', 'link/url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206281792
                __default_139882206281792 = _DEFAULT_MARKER

                # <Substitution "python:'pat-plone-modal' if modal else None" (40:22)> -> __attr_class
                __token = 1086
                try:
                    __zt_tmp = __attrs_139882206290240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_139882257081264('python', "'pat-plone-modal' if modal else None", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206294560
                __default_139882206294560 = _DEFAULT_MARKER

                # <Substitution 'python:modal if modal else None' (41:36)> -> __attr_data_pat_plone_modal
                __token = 1168
                try:
                    __zt_tmp = __attrs_139882206290240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_plone_modal = _static_139882257081264('python', 'modal if modal else None', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_pat_plone_modal is not None):
                    __append((' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                __append(' >\n              ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206296480
                __attrs_139882206296480 = _static_139882337226896

                # <Value 'not:icon' (44:35)> -> __condition
                __token = 1269
                try:
                    __zt_tmp = __attrs_139882206296480
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('not', 'icon', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206283904
                    __default_139882206283904 = _DEFAULT_MARKER

                    # <Value 'link/title' (45:33)> -> __cache_139882206297632
                    __token = 1312
                    try:
                        __zt_tmp = __attrs_139882206296480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882206297632 = _static_139882257081264('path', 'link/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'link/title' (45:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd3754e0> -> __condition
                    __expression = __cache_139882206297632

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              Action\n              ')
                    else:
                        __content = __cache_139882206297632
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7f38dd3770d0> name=None at 7f38dd375a80> -> __attrs_139882206284864
                __attrs_139882206284864 = _static_139882206294224
                __backup_icon_url_139882213180512 = get('icon_url', __marker)

                # <Value 'icon/absolute_url|icon' (50:31)> -> __value
                __token = 1447
                try:
                    __zt_tmp = __attrs_139882206284864
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'icon/absolute_url|icon', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['icon_url'] = __value

                # <Value 'icon' (52:35)> -> __condition
                __token = 1528
                try:
                    __zt_tmp = __attrs_139882206284864
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'icon', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206283616
                    __default_139882206283616 = _DEFAULT_MARKER

                    # <Substitution 'string:background-image:url($icon_url);' (55:28)> -> __attr_style
                    __token = 1644
                    try:
                        __zt_tmp = __attrs_139882206284864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_139882257081264('string', 'background-image:url($icon_url);', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((' style="%s"' % __attr_style))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206283664
                    __default_139882206283664 = _DEFAULT_MARKER

                    # <Value 'link/title' (53:33)> -> __cache_139882206297296
                    __token = 1567
                    try:
                        __zt_tmp = __attrs_139882206284864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882206297296 = _static_139882257081264('path', 'link/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'link/title' (53:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd375cc0> -> __condition
                    __expression = __cache_139882206297296

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              Action\n              ')
                    else:
                        __content = __cache_139882206297296
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')
                if (__backup_icon_url_139882213180512 is __marker):
                    del econtext['icon_url']
                else:
                    econtext['icon_url'] = __backup_icon_url_139882213180512
                __append('\n            </a>')
                if (__backup_modal_139882206286592 is __marker):
                    del econtext['modal']
                else:
                    econtext['modal'] = __backup_modal_139882206286592
                __append('\n          </li>')
                if (__backup_icon_139882101373296 is __marker):
                    del econtext['icon']
                else:
                    econtext['icon'] = __backup_icon_139882101373296
                __append('\n        ')
                ____index_139882206296624 -= 1
                if (____index_139882206296624 > 0):
                    __append('')
            if (__backup_link_139882101369888 is __marker):
                del econtext['link']
            else:
                econtext['link'] = __backup_link_139882101369888
            __append('\n      </ul>\n    </div>\n\n  </div>')
            if (__backup_portal_url_139882205639536 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_139882205639536
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_139882101371136
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }