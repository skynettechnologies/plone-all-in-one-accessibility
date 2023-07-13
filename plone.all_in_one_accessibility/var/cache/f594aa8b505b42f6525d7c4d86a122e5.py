# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.portlets-5.0.6-py3.10.egg/plone/app/portlets/portlets/actions.pt'

__tokens = {285: ('context/@@plone_portal_state/portal_url', 10, 20), 393: ('view/showTitle', 15, 24), 442: ('view/title', 17, 27), 479: ('view/title', 18, 25), 627: ('string:actions-${view/category}', 26, 18), 708: ('view/actionLinks', 28, 35), 842: ('nocall:link/icon', 31, 21), 748: ("portletItem action-item-${python:link['id']}", 29, 21), 774: ("python:link['id']", 29, 47), 963: ('link/modal|nothing', 36, 23), 1054: ('link/url', 39, 22), 1086: (" python:'pat-plone-modal' if modal else Non", 40, 22), 1168: ('l python:modal if modal else No', 41, 36), 1269: ('not:icon', 44, 35), 1312: ('link/title', 45, 33), 1447: ('icon/absolute_url|icon', 50, 31), 1528: ('icon', 52, 35), 1644: ('string:background-image:url($icon_url);', 55, 28), 1567: ('link/title', 53, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272495712 = {'style': 'string:background-image:url($icon_url);', }
_static_140310475986288 = {'href': '#', 'class': "python:'pat-plone-modal' if modal else None", 'data-pat-plone-modal': 'python:modal if modal else None', }
_static_140310475995600 = {'class': "portletItem action-item-${python:link['id']}", }
_static_140310475994160 = {'class': 'string:actions-${view/category}', }
_static_140310475990272 = {'class': 'card-body portletContent', }
_static_140310566789392 = {}
_static_140310475991376 = {'class': 'card-header', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310475991088 = {'class': 'card portlet portletActions', }
_static_140310475988160 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f9c94145cc0> name=None at 7f9c94144070> -> __attrs_140310475991040
            __attrs_140310475991040 = _static_140310475988160
            __previous_i18n_domain_140310475981488 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f9c94146830> name=None at 7f9c94145c00> -> __attrs_140310475983504
            __attrs_140310475983504 = _static_140310475991088
            __backup_portal_url_140310272578880 = get('portal_url', __marker)

            # <Value 'context/@@plone_portal_state/portal_url' (10:20)> -> __value
            __token = 285
            try:
                __zt_tmp = __attrs_140310475983504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'context/@@plone_portal_state/portal_url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['portal_url'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card portlet portletActions" >\n\n    ')

            # <Static value=<ast.Dict object at 0x7f9c94146950> name=None at 7f9c941479a0> -> __attrs_140310475982640
            __attrs_140310475982640 = _static_140310475991376

            # <Value 'view/showTitle' (15:24)> -> __condition
            __token = 393
            try:
                __zt_tmp = __attrs_140310475982640
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'view/showTitle', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-header" >\n      ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475994736
                __attrs_140310475994736 = _static_140310566789392

                # <Value 'view/title' (17:27)> -> __condition
                __token = 442
                try:
                    __zt_tmp = __attrs_140310475994736
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'view/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475983696
                    __default_140310475983696 = _DEFAULT_MARKER

                    # <Value 'view/title' (18:25)> -> __cache_140310475986096
                    __token = 479
                    try:
                        __zt_tmp = __attrs_140310475994736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475986096 = _static_140310567013776('path', 'view/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/title' (18:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94144880> -> __condition
                    __expression = __cache_140310475986096

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n        Title\n      </span>')
                    else:
                        __content = __cache_140310475986096
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                __append('\n    </div>')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f9c94146500> name=None at 7f9c94145780> -> __attrs_140310475983984
            __attrs_140310475983984 = _static_140310475990272

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body portletContent">\n      ')

            # <Static value=<ast.Dict object at 0x7f9c94147430> name=None at 7f9c94146230> -> __attrs_140310475992912
            __attrs_140310475992912 = _static_140310475994160

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475992000
            __default_140310475992000 = _DEFAULT_MARKER

            # <Substitution 'string:actions-${view/category}' (26:18)> -> __attr_class
            __token = 627
            try:
                __zt_tmp = __attrs_140310475992912
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140310567013776('string', 'actions-${view/category}', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n        ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475988400
            __attrs_140310475988400 = _static_140310566789392
            __backup_link_140310272712400 = get('link', __marker)

            # <Value 'view/actionLinks' (28:35)> -> __iterator
            __token = 708
            try:
                __zt_tmp = __attrs_140310475988400
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140310567013776('path', 'view/actionLinks', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            (__iterator, ____index_140310475993968, ) = getname('repeat')('link', __iterator)
            econtext['link'] = None
            for __item in __iterator:
                econtext['link'] = __item
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f9c941479d0> name=None at 7f9c94146aa0> -> __attrs_140310475995168
                __attrs_140310475995168 = _static_140310475995600
                __backup_icon_140310272498160 = get('icon', __marker)

                # <Value 'nocall:link/icon' (31:21)> -> __value
                __token = 842
                try:
                    __zt_tmp = __attrs_140310475995168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('nocall', 'link/icon', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['icon'] = __value

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475996272
                __default_140310475996272 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution "portletItem action-item-${python:link['id']}" (29:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c941448e0> -> __attr_class
                __token = 748
                __token = 774
                try:
                    __zt_tmp = __attrs_140310475995168
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140310567013776('python', "link['id']", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
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

                # <Static value=<ast.Dict object at 0x7f9c94145570> name=None at 7f9c94146530> -> __attrs_140310272507376
                __attrs_140310272507376 = _static_140310475986288
                __backup_modal_140310475985616 = get('modal', __marker)

                # <Value 'link/modal|nothing' (36:23)> -> __value
                __token = 963
                try:
                    __zt_tmp = __attrs_140310272507376
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'link/modal|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['modal'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272500080
                __default_140310272500080 = _DEFAULT_MARKER

                # <Substitution 'link/url' (39:22)> -> __attr_href
                __token = 1054
                try:
                    __zt_tmp = __attrs_140310272507376
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140310567013776('path', 'link/url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272496864
                __default_140310272496864 = _DEFAULT_MARKER

                # <Substitution "python:'pat-plone-modal' if modal else None" (40:22)> -> __attr_class
                __token = 1086
                try:
                    __zt_tmp = __attrs_140310272507376
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140310567013776('python', "'pat-plone-modal' if modal else None", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272504400
                __default_140310272504400 = _DEFAULT_MARKER

                # <Substitution 'python:modal if modal else None' (41:36)> -> __attr_data_pat_plone_modal
                __token = 1168
                try:
                    __zt_tmp = __attrs_140310272507376
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_plone_modal = _static_140310567013776('python', 'modal if modal else None', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_pat_plone_modal is not None):
                    __append((' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                __append(' >\n              ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272494176
                __attrs_140310272494176 = _static_140310566789392

                # <Value 'not:icon' (44:35)> -> __condition
                __token = 1269
                try:
                    __zt_tmp = __attrs_140310272494176
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('not', 'icon', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272501856
                    __default_140310272501856 = _DEFAULT_MARKER

                    # <Value 'link/title' (45:33)> -> __cache_140310272493888
                    __token = 1312
                    try:
                        __zt_tmp = __attrs_140310272494176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272493888 = _static_140310567013776('path', 'link/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'link/title' (45:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f363e0> -> __condition
                    __expression = __cache_140310272493888

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              Action\n              ')
                    else:
                        __content = __cache_140310272493888
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7f9c87f35060> name=None at 7f9c87f366b0> -> __attrs_140310272496240
                __attrs_140310272496240 = _static_140310272495712
                __backup_icon_url_140310272704960 = get('icon_url', __marker)

                # <Value 'icon/absolute_url|icon' (50:31)> -> __value
                __token = 1447
                try:
                    __zt_tmp = __attrs_140310272496240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'icon/absolute_url|icon', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['icon_url'] = __value

                # <Value 'icon' (52:35)> -> __condition
                __token = 1528
                try:
                    __zt_tmp = __attrs_140310272496240
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'icon', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272507664
                    __default_140310272507664 = _DEFAULT_MARKER

                    # <Substitution 'string:background-image:url($icon_url);' (55:28)> -> __attr_style
                    __token = 1644
                    try:
                        __zt_tmp = __attrs_140310272496240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_140310567013776('string', 'background-image:url($icon_url);', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((' style="%s"' % __attr_style))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272501232
                    __default_140310272501232 = _DEFAULT_MARKER

                    # <Value 'link/title' (53:33)> -> __cache_140310272492352
                    __token = 1567
                    try:
                        __zt_tmp = __attrs_140310272496240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272492352 = _static_140310567013776('path', 'link/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'link/title' (53:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f37ac0> -> __condition
                    __expression = __cache_140310272492352

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              Action\n              ')
                    else:
                        __content = __cache_140310272492352
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')
                if (__backup_icon_url_140310272704960 is __marker):
                    del econtext['icon_url']
                else:
                    econtext['icon_url'] = __backup_icon_url_140310272704960
                __append('\n            </a>')
                if (__backup_modal_140310475985616 is __marker):
                    del econtext['modal']
                else:
                    econtext['modal'] = __backup_modal_140310475985616
                __append('\n          </li>')
                if (__backup_icon_140310272498160 is __marker):
                    del econtext['icon']
                else:
                    econtext['icon'] = __backup_icon_140310272498160
                __append('\n        ')
                ____index_140310475993968 -= 1
                if (____index_140310475993968 > 0):
                    __append('')
            if (__backup_link_140310272712400 is __marker):
                del econtext['link']
            else:
                econtext['link'] = __backup_link_140310272712400
            __append('\n      </ul>\n    </div>\n\n  </div>')
            if (__backup_portal_url_140310272578880 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140310272578880
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_140310475981488
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }