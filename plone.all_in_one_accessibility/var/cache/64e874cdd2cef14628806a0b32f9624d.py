# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/toolbar.pt'

__tokens = {94: ('view/context_state', 4, 25), 130: (" python:context.restrictedTraverse('@@iconresolver'", 5, 16), 206: ('r python: view.get_personal_bar', 6, 22), 261: ('os view/toolbar_posit', 7, 20), 322: ('context_state/is_toolbar_visible', 9, 24), 680: ("python:icons.tag('arrow-bar-left')", 25, 41), 875: ("python:icons.tag('arrow-bar-right')", 31, 41), 1033: ('view/base_render', 37, 23), 1084: ('toolbar_main', 39, 23), 1137: ('toolbar_main', 41, 33), 1295: ('personal_bar/user_actions', 46, 24), 1191: ("personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", 45, 16), 1219: ("python:'dropend' if toolbar_pos == 'side' else ''", 45, 44), 1546: ('personal_bar/homelink_url', 55, 16), 1633: ("python:icons.tag('toolbar-action/personaltools', tag_class='')", 58, 41), 1763: ('personal_bar/user_name', 60, 27), 2000: ('${personal_bar/user_name}', 69, 38), 2002: ('personal_bar/user_name', 69, 40), 2076: ('personal_bar/user_actions', 71, 31), 2193: ('action', 74, 15), 2269: ("python:icons.tag(action.get('icon', 'dot'), tag_class='')", 77, 41), 2372: ('action/title', 78, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310475985568 = set([])
_static_140310475470448 = {'class': 'nav-link dropdown-item', }
_static_140310475462720 = {'class': 'dropdown-header', }
_static_140310475471504 = {'class': 'dropdown-menu', 'id': 'collapse-personaltools', 'aria-labelledby': 'personaltools-menulink', }
_static_140310475291808 = {'class': 'toolbar-label', }
_static_140310475288592 = {'class': 'nav-link dropdown-toggle', 'id': 'personaltools-menulink', 'aria-expanded': 'false', 'data-bs-offset': '0,0', 'data-bs-toggle': 'dropdown', 'href': 'personal_bar/homelink_url', }
_static_140310475288736 = {'class': "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", }
_static_140310475291712 = {'class': 'nav flex-column plone-toolbar-main', }
_static_140310475678544 = {'class': 'toolbar-expand', 'aria-label': 'Pin', }
_static_140310566789392 = {}
_static_140310475675808 = {'class': 'toolbar-collapse', 'aria-label': 'Unpin', }
_static_140310475674896 = {'class': 'toolbar-header nav', }
_static_140310475674272 = {'class': 'pat-toolbar', 'id': 'edit-zone', 'role': 'toolbar', 'data-bs-scroll': 'true', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310475684784 = {'id': 'edit-bar', 'role': 'toolbar', }

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

            # <Static value=<ast.Dict object at 0x7f9c940fbbb0> name=None at 7f9c940fa7a0> -> __attrs_140310475685216
            __attrs_140310475685216 = _static_140310475684784
            __backup_context_state_140310475254192 = get('context_state', __marker)

            # <Value 'view/context_state' (4:25)> -> __value
            __token = 94
            try:
                __zt_tmp = __attrs_140310475685216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/context_state', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_icons_140310476731728 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (5:16)> -> __value
            __token = 130
            try:
                __zt_tmp = __attrs_140310475685216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_personal_bar_140310564036352 = get('personal_bar', __marker)

            # <Value 'python: view.get_personal_bar()' (6:22)> -> __value
            __token = 206
            try:
                __zt_tmp = __attrs_140310475685216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', ' view.get_personal_bar()', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['personal_bar'] = __value
            __backup_toolbar_pos_140310513282368 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (7:20)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_140310475685216
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/toolbar_position', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'context_state/is_toolbar_visible' (9:24)> -> __condition
            __token = 322
            try:
                __zt_tmp = __attrs_140310475685216
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'context_state/is_toolbar_visible', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140310475671872 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="edit-bar" role="toolbar" >\n\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c940f92a0> name=None at 7f9c940f92d0> -> __attrs_140310475672928
                __attrs_140310475672928 = _static_140310475674272

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-toolbar" id="edit-zone" role="toolbar" data-bs-scroll="true" >\n\n    ')

                # <Static value=<ast.Dict object at 0x7f9c940f9510> name=None at 7f9c940f83d0> -> __attrs_140310475670048
                __attrs_140310475670048 = _static_140310475674896

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="toolbar-header nav">\n      ')

                # <Static value=<ast.Dict object at 0x7f9c940f98a0> name=None at 7f9c940f98d0> -> __attrs_140310475676288
                __attrs_140310475676288 = _static_140310475675808

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-collapse"')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475675136
                __default_140310475675136 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7f9c940f96c0> at 7f9c940f9690> -> __attr_aria_label
                __attr_aria_label = 'Unpin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475677872
                __attrs_140310475677872 = _static_140310566789392

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475677680
                __default_140310475677680 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-left')" (25:41)> -> __cache_140310475677152
                __token = 680
                try:
                    __zt_tmp = __attrs_140310475677872
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310475677152 = _static_140310567013776('python', "icons.tag('arrow-bar-left')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-left')" (25:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c940f9ed0> -> __condition
                __expression = __cache_140310475677152

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140310475677152
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n      ')

                # <Static value=<ast.Dict object at 0x7f9c940fa350> name=None at 7f9c940fa380> -> __attrs_140310475285280
                __attrs_140310475285280 = _static_140310475678544

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-expand"')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475279280
                __default_140310475279280 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7f9c940f9d50> at 7f9c940f9d20> -> __attr_aria_label
                __attr_aria_label = 'Pin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475290128
                __attrs_140310475290128 = _static_140310566789392

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475291088
                __default_140310475291088 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-right')" (31:41)> -> __cache_140310475291664
                __token = 875
                try:
                    __zt_tmp = __attrs_140310475290128
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310475291664 = _static_140310567013776('python', "icons.tag('arrow-bar-right')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-right')" (31:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94098a90> -> __condition
                __expression = __cache_140310475291664

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140310475291664
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n    </div>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f9c9409bc40> name=None at 7f9c94098820> -> __attrs_140310475282160
                __attrs_140310475282160 = _static_140310475291712
                __backup_toolbar_main_140310475408720 = get('toolbar_main', __marker)

                # <Value 'view/base_render' (37:23)> -> __value
                __token = 1033
                try:
                    __zt_tmp = __attrs_140310475282160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'view/base_render', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['toolbar_main'] = __value

                # <Value 'toolbar_main' (39:23)> -> __condition
                __token = 1084
                try:
                    __zt_tmp = __attrs_140310475282160
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'toolbar_main', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="nav flex-column plone-toolbar-main" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475291856
                    __attrs_140310475291856 = _static_140310566789392

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475286960
                    __default_140310475286960 = _DEFAULT_MARKER

                    # <Value 'toolbar_main' (41:33)> -> __cache_140310475284416
                    __token = 1137
                    try:
                        __zt_tmp = __attrs_140310475291856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475284416 = _static_140310567013776('path', 'toolbar_main', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'toolbar_main' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c940988b0> -> __condition
                    __expression = __cache_140310475284416

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n      </li>')
                    else:
                        __content = __cache_140310475284416
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </ul>')
                if (__backup_toolbar_main_140310475408720 is __marker):
                    del econtext['toolbar_main']
                else:
                    econtext['toolbar_main'] = __backup_toolbar_main_140310475408720
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f9c9409b0a0> name=None at 7f9c9409a650> -> __attrs_140310475282112
                __attrs_140310475282112 = _static_140310475288736

                # <Value 'personal_bar/user_actions' (46:24)> -> __condition
                __token = 1295
                try:
                    __zt_tmp = __attrs_140310475282112
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'personal_bar/user_actions', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475285616
                    __default_140310475285616 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}" (45:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9409a0b0> -> __attr_class
                    __token = 1191
                    __token = 1219
                    try:
                        __zt_tmp = __attrs_140310475282112
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140310567013776('python', "'dropend' if toolbar_pos == 'side' else ''", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
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

                    # <Static value=<ast.Dict object at 0x7f9c9409b010> name=None at 7f9c94098f10> -> __attrs_140310475277072
                    __attrs_140310475277072 = _static_140310475288592

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link dropdown-toggle" id="personaltools-menulink" aria-expanded="false" data-bs-offset="0,0" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475283600
                    __default_140310475283600 = _DEFAULT_MARKER

                    # <Substitution 'personal_bar/homelink_url' (55:16)> -> __attr_href
                    __token = 1546
                    try:
                        __zt_tmp = __attrs_140310475277072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140310567013776('path', 'personal_bar/homelink_url', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475291040
                    __attrs_140310475291040 = _static_140310566789392

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475280336
                    __default_140310475280336 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> -> __cache_140310475281680
                    __token = 1633
                    try:
                        __zt_tmp = __attrs_140310475291040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475281680 = _static_140310567013776('python', "icons.tag('toolbar-action/personaltools', tag_class='')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94098460> -> __condition
                    __expression = __cache_140310475281680

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310475281680
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f9c9409bca0> name=None at 7f9c9409baf0> -> __attrs_140310475284176
                    __attrs_140310475284176 = _static_140310475291808

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label" >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475288688
                    __default_140310475288688 = _DEFAULT_MARKER

                    # <Value 'personal_bar/user_name' (60:27)> -> __cache_140310475289984
                    __token = 1763
                    try:
                        __zt_tmp = __attrs_140310475284176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475289984 = _static_140310567013776('path', 'personal_bar/user_name', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'personal_bar/user_name' (60:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94099f00> -> __condition
                    __expression = __cache_140310475289984

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('User')
                    else:
                        __content = __cache_140310475289984
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f9c940c7a90> name=None at 7f9c940c50f0> -> __attrs_140310475461664
                    __attrs_140310475461664 = _static_140310475471504

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="dropdown-menu" id="collapse-personaltools" aria-labelledby="personaltools-menulink" >\n        ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475462672
                    __attrs_140310475462672 = _static_140310566789392

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>\n          ')

                    # <Static value=<ast.Dict object at 0x7f9c940c5840> name=None at 7f9c940c70d0> -> __attrs_140310475460944
                    __attrs_140310475460944 = _static_140310475462720

                    # <h6 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h6 class="dropdown-header">')

                    # <Interpolation value=<Substitution '${personal_bar/user_name}' (69:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c940c7fd0> -> __content_140310653968752
                    __token = 2000
                    __token = 2002
                    try:
                        __zt_tmp = __attrs_140310475460944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140310653968752 = _static_140310567013776('path', 'personal_bar/user_name', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
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
                    __append('</h6>\n        </li>\n        ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475466416
                    __attrs_140310475466416 = _static_140310566789392
                    __backup_action_140310475291568 = get('action', __marker)

                    # <Value 'personal_bar/user_actions' (71:31)> -> __iterator
                    __token = 2076
                    try:
                        __zt_tmp = __attrs_140310475466416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140310567013776('path', 'personal_bar/user_actions', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    (__iterator, ____index_140310475472608, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n          ')

                        # <Static value=<ast.Dict object at 0x7f9c940c7670> name=None at 7f9c940c7bb0> -> __attrs_140310475464352
                        __attrs_140310475464352 = _static_140310475470448

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Value 'action' (74:15)> -> __cache_140310475459840
                        __token = 2193
                        try:
                            __zt_tmp = __attrs_140310475464352
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140310475459840 = _static_140310567013776('path', 'action', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        if ('class' not in __chain(__cache_140310475459840)):
                            __append(' class="nav-link dropdown-item"')
                        __attr_140310475470976 = __cache_140310475459840
                        for (name, value, ) in __attr_140310475470976.items():
                            if ((name not in _static_140310475985568) and (value is not None)):
                                __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                        __append(' >\n            ')

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475515424
                        __attrs_140310475515424 = _static_140310566789392

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475517344
                        __default_140310475517344 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> -> __cache_140310475508320
                        __token = 2269
                        try:
                            __zt_tmp = __attrs_140310475515424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140310475508320 = _static_140310567013776('python', "icons.tag(action.get('icon', 'dot'), tag_class='')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c940d2d40> -> __condition
                        __expression = __cache_140310475508320

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140310475508320
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475511200
                        __attrs_140310475511200 = _static_140310566789392

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475512448
                        __default_140310475512448 = _DEFAULT_MARKER

                        # <Value 'action/title' (78:41)> -> __cache_140310475521664
                        __token = 2372
                        try:
                            __zt_tmp = __attrs_140310475511200
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140310475521664 = _static_140310567013776('path', 'action/title', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (78:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c940d0970> -> __condition
                        __expression = __cache_140310475521664

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              action title\n            ')
                        else:
                            __content = __cache_140310475521664
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          </a>\n        </li>')
                        ____index_140310475472608 -= 1
                        if (____index_140310475472608 > 0):
                            __append('\n        ')
                    if (__backup_action_140310475291568 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_140310475291568
                    __append('\n      </ul>\n\n    </div>')
                __append('\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_140310475671872
            if (__backup_toolbar_pos_140310513282368 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_140310513282368
            if (__backup_personal_bar_140310564036352 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_140310564036352
            if (__backup_icons_140310476731728 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140310476731728
            if (__backup_context_state_140310475254192 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140310475254192
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }