# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/toolbar.pt'

__tokens = {94: ('view/context_state', 4, 25), 130: (" python:context.restrictedTraverse('@@iconresolver'", 5, 16), 206: ('r python: view.get_personal_bar', 6, 22), 261: ('os view/toolbar_posit', 7, 20), 322: ('context_state/is_toolbar_visible', 9, 24), 680: ("python:icons.tag('arrow-bar-left')", 25, 41), 875: ("python:icons.tag('arrow-bar-right')", 31, 41), 1033: ('view/base_render', 37, 23), 1084: ('toolbar_main', 39, 23), 1137: ('toolbar_main', 41, 33), 1295: ('personal_bar/user_actions', 46, 24), 1191: ("personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", 45, 16), 1219: ("python:'dropend' if toolbar_pos == 'side' else ''", 45, 44), 1546: ('personal_bar/homelink_url', 55, 16), 1633: ("python:icons.tag('toolbar-action/personaltools', tag_class='')", 58, 41), 1763: ('personal_bar/user_name', 60, 27), 2000: ('${personal_bar/user_name}', 69, 38), 2002: ('personal_bar/user_name', 69, 40), 2076: ('personal_bar/user_actions', 71, 31), 2193: ('action', 74, 15), 2269: ("python:icons.tag(action.get('icon', 'dot'), tag_class='')", 77, 41), 2372: ('action/title', 78, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882205871888 = set([])
_static_139882205900192 = {'class': 'nav-link dropdown-item', }
_static_139882205904320 = {'class': 'dropdown-header', }
_static_139882205896064 = {'class': 'dropdown-menu', 'id': 'collapse-personaltools', 'aria-labelledby': 'personaltools-menulink', }
_static_139882205890928 = {'class': 'toolbar-label', }
_static_139882206154800 = {'class': 'nav-link dropdown-toggle', 'id': 'personaltools-menulink', 'aria-expanded': 'false', 'data-bs-offset': '0,0', 'data-bs-toggle': 'dropdown', 'href': 'personal_bar/homelink_url', }
_static_139882206159552 = {'class': "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", }
_static_139882206153696 = {'class': 'nav flex-column plone-toolbar-main', }
_static_139882206161952 = {'class': 'toolbar-expand', 'aria-label': 'Pin', }
_static_139882337226896 = {}
_static_139882205990672 = {'class': 'toolbar-collapse', 'aria-label': 'Unpin', }
_static_139882205994800 = {'class': 'toolbar-header nav', }
_static_139882206000464 = {'class': 'pat-toolbar', 'id': 'edit-zone', 'role': 'toolbar', 'data-bs-scroll': 'true', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882205990048 = {'id': 'edit-bar', 'role': 'toolbar', }

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

            # <Static value=<ast.Dict object at 0x7f38dd32cca0> name=None at 7f38dd32e7d0> -> __attrs_139882205993504
            __attrs_139882205993504 = _static_139882205990048
            __backup_context_state_139882205994992 = get('context_state', __marker)

            # <Value 'view/context_state' (4:25)> -> __value
            __token = 94
            try:
                __zt_tmp = __attrs_139882205993504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/context_state', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_icons_139882205987648 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (5:16)> -> __value
            __token = 130
            try:
                __zt_tmp = __attrs_139882205993504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_personal_bar_139882205998352 = get('personal_bar', __marker)

            # <Value 'python: view.get_personal_bar()' (6:22)> -> __value
            __token = 206
            try:
                __zt_tmp = __attrs_139882205993504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', ' view.get_personal_bar()', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['personal_bar'] = __value
            __backup_toolbar_pos_139882206001376 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (7:20)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_139882205993504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/toolbar_position', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'context_state/is_toolbar_visible' (9:24)> -> __condition
            __token = 322
            try:
                __zt_tmp = __attrs_139882205993504
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('path', 'context_state/is_toolbar_visible', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139882205988848 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="edit-bar" role="toolbar" >\n\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38dd32f550> name=None at 7f38dd32fc10> -> __attrs_139882206001280
                __attrs_139882206001280 = _static_139882206000464

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-toolbar" id="edit-zone" role="toolbar" data-bs-scroll="true" >\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd32df30> name=None at 7f38dd32ffa0> -> __attrs_139882205990576
                __attrs_139882205990576 = _static_139882205994800

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="toolbar-header nav">\n      ')

                # <Static value=<ast.Dict object at 0x7f38dd32cf10> name=None at 7f38dd32f100> -> __attrs_139882205989472
                __attrs_139882205989472 = _static_139882205990672

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-collapse"')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206001424
                __default_139882206001424 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7f38dd32d870> at 7f38dd32dc60> -> __attr_aria_label
                __attr_aria_label = 'Unpin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206162672
                __attrs_139882206162672 = _static_139882337226896

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206160800
                __default_139882206160800 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-left')" (25:41)> -> __cache_139882206156720
                __token = 680
                try:
                    __zt_tmp = __attrs_139882206162672
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882206156720 = _static_139882257081264('python', "icons.tag('arrow-bar-left')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-left')" (25:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd354310> -> __condition
                __expression = __cache_139882206156720

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139882206156720
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n      ')

                # <Static value=<ast.Dict object at 0x7f38dd356c20> name=None at 7f38dd356680> -> __attrs_139882206157008
                __attrs_139882206157008 = _static_139882206161952

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-expand"')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206162336
                __default_139882206162336 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7f38dd355ab0> at 7f38dd355630> -> __attr_aria_label
                __attr_aria_label = 'Pin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206164448
                __attrs_139882206164448 = _static_139882337226896

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206164784
                __default_139882206164784 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-right')" (31:41)> -> __cache_139882206162384
                __token = 875
                try:
                    __zt_tmp = __attrs_139882206164448
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882206162384 = _static_139882257081264('python', "icons.tag('arrow-bar-right')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-right')" (31:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd3549a0> -> __condition
                __expression = __cache_139882206162384

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139882206162384
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n    </div>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd354be0> name=None at 7f38dd355690> -> __attrs_139882206159216
                __attrs_139882206159216 = _static_139882206153696
                __backup_toolbar_main_139882205996480 = get('toolbar_main', __marker)

                # <Value 'view/base_render' (37:23)> -> __value
                __token = 1033
                try:
                    __zt_tmp = __attrs_139882206159216
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/base_render', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['toolbar_main'] = __value

                # <Value 'toolbar_main' (39:23)> -> __condition
                __token = 1084
                try:
                    __zt_tmp = __attrs_139882206159216
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'toolbar_main', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="nav flex-column plone-toolbar-main" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206158112
                    __attrs_139882206158112 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206154560
                    __default_139882206154560 = _DEFAULT_MARKER

                    # <Value 'toolbar_main' (41:33)> -> __cache_139882206161184
                    __token = 1137
                    try:
                        __zt_tmp = __attrs_139882206158112
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882206161184 = _static_139882257081264('path', 'toolbar_main', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'toolbar_main' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd356a70> -> __condition
                    __expression = __cache_139882206161184

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n      </li>')
                    else:
                        __content = __cache_139882206161184
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </ul>')
                if (__backup_toolbar_main_139882205996480 is __marker):
                    del econtext['toolbar_main']
                else:
                    econtext['toolbar_main'] = __backup_toolbar_main_139882205996480
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd3562c0> name=None at 7f38dd355a50> -> __attrs_139882206165024
                __attrs_139882206165024 = _static_139882206159552

                # <Value 'personal_bar/user_actions' (46:24)> -> __condition
                __token = 1295
                try:
                    __zt_tmp = __attrs_139882206165024
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'personal_bar/user_actions', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206155808
                    __default_139882206155808 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}" (45:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd356230> -> __attr_class
                    __token = 1191
                    __token = 1219
                    try:
                        __zt_tmp = __attrs_139882206165024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139882257081264('python', "'dropend' if toolbar_pos == 'side' else ''", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('personaltools-wrapper nav ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append(' >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f38dd355030> name=None at 7f38dd3573a0> -> __attrs_139882206151824
                    __attrs_139882206151824 = _static_139882206154800

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link dropdown-toggle" id="personaltools-menulink" aria-expanded="false" data-bs-offset="0,0" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206152304
                    __default_139882206152304 = _DEFAULT_MARKER

                    # <Substitution 'personal_bar/homelink_url' (55:16)> -> __attr_href
                    __token = 1546
                    try:
                        __zt_tmp = __attrs_139882206151824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('path', 'personal_bar/homelink_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205895632
                    __attrs_139882205895632 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205891792
                    __default_139882205891792 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> -> __cache_139882206152112
                    __token = 1633
                    try:
                        __zt_tmp = __attrs_139882205895632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882206152112 = _static_139882257081264('python', "icons.tag('toolbar-action/personaltools', tag_class='')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd3562f0> -> __condition
                    __expression = __cache_139882206152112

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882206152112
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f38dd314970> name=None at 7f38dd316ce0> -> __attrs_139882205891936
                    __attrs_139882205891936 = _static_139882205890928

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label" >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205891024
                    __default_139882205891024 = _DEFAULT_MARKER

                    # <Value 'personal_bar/user_name' (60:27)> -> __cache_139882205890784
                    __token = 1763
                    try:
                        __zt_tmp = __attrs_139882205891936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882205890784 = _static_139882257081264('path', 'personal_bar/user_name', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'personal_bar/user_name' (60:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd314a00> -> __condition
                    __expression = __cache_139882205890784

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('User')
                    else:
                        __content = __cache_139882205890784
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f38dd315d80> name=None at 7f38dd315c30> -> __attrs_139882205889728
                    __attrs_139882205889728 = _static_139882205896064

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="dropdown-menu" id="collapse-personaltools" aria-labelledby="personaltools-menulink" >\n        ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205903504
                    __attrs_139882205903504 = _static_139882337226896

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>\n          ')

                    # <Static value=<ast.Dict object at 0x7f38dd317dc0> name=None at 7f38dd317a00> -> __attrs_139882205893808
                    __attrs_139882205893808 = _static_139882205904320

                    # <h6 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h6 class="dropdown-header">')

                    # <Interpolation value=<Substitution '${personal_bar/user_name}' (69:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd314f70> -> __content_139882343851824
                    __token = 2000
                    __token = 2002
                    try:
                        __zt_tmp = __attrs_139882205893808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139882343851824 = _static_139882257081264('path', 'personal_bar/user_name', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
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
                    __append('</h6>\n        </li>\n        ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205892320
                    __attrs_139882205892320 = _static_139882337226896
                    __backup_action_139882206150864 = get('action', __marker)

                    # <Value 'personal_bar/user_actions' (71:31)> -> __iterator
                    __token = 2076
                    try:
                        __zt_tmp = __attrs_139882205892320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139882257081264('path', 'personal_bar/user_actions', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    (__iterator, ____index_139882205903456, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n          ')

                        # <Static value=<ast.Dict object at 0x7f38dd316da0> name=None at 7f38dd314f10> -> __attrs_139882205901344
                        __attrs_139882205901344 = _static_139882205900192

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Value 'action' (74:15)> -> __cache_139882205891696
                        __token = 2193
                        try:
                            __zt_tmp = __attrs_139882205901344
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882205891696 = _static_139882257081264('path', 'action', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if ('class' not in __chain(__cache_139882205891696)):
                            __append(' class="nav-link dropdown-item"')
                        __attr_139882205896880 = __cache_139882205891696
                        for (name, value, ) in __attr_139882205896880.items():
                            if ((name not in _static_139882205871888) and (value is not None)):
                                __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                        __append(' >\n            ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205902640
                        __attrs_139882205902640 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205897552
                        __default_139882205897552 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> -> __cache_139882205898080
                        __token = 2269
                        try:
                            __zt_tmp = __attrs_139882205902640
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882205898080 = _static_139882257081264('python', "icons.tag(action.get('icon', 'dot'), tag_class='')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd3168f0> -> __condition
                        __expression = __cache_139882205898080

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139882205898080
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205899328
                        __attrs_139882205899328 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205898800
                        __default_139882205898800 = _DEFAULT_MARKER

                        # <Value 'action/title' (78:41)> -> __cache_139882205897600
                        __token = 2372
                        try:
                            __zt_tmp = __attrs_139882205899328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882205897600 = _static_139882257081264('path', 'action/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (78:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd3179d0> -> __condition
                        __expression = __cache_139882205897600

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              action title\n            ')
                        else:
                            __content = __cache_139882205897600
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          </a>\n        </li>')
                        ____index_139882205903456 -= 1
                        if (____index_139882205903456 > 0):
                            __append('\n        ')
                    if (__backup_action_139882206150864 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_139882206150864
                    __append('\n      </ul>\n\n    </div>')
                __append('\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_139882205988848
            if (__backup_toolbar_pos_139882206001376 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_139882206001376
            if (__backup_personal_bar_139882205998352 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_139882205998352
            if (__backup_icons_139882205987648 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139882205987648
            if (__backup_context_state_139882205994992 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_139882205994992
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }