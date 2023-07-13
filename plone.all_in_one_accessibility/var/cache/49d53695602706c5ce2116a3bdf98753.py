# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/globalstatusmessage.pt'

__tokens = {51: ('nocall: context/@@iconresolver', 2, 23), 135: ('python:view.messages', 4, 35), 279: ('message/type | nothing', 10, 15), 324: (' python:view.display_info_for_mtype(mtype', 11, 21), 399: ('mtype', 13, 22), 174: ("portalMessage ${python:display_info['cssclass']}", 7, 14), 190: ("python:display_info['cssclass']", 7, 30), 447: ("python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')", 15, 37), 573: ("${python:display_info['msg']}", 16, 12), 575: ("python:display_info['msg']", 16, 14), 661: ('message/message | nothing', 18, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310475277696 = {'class': 'content', }
_static_140310475288688 = {'class': "portalMessage ${python:display_info['cssclass']}", 'role': 'alert', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310566789392 = {}

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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475286144
            __attrs_140310475286144 = _static_140310566789392
            __backup_icons_140310272303808 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (2:23)> -> __value
            __token = 51
            try:
                __zt_tmp = __attrs_140310475286144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('nocall', ' context/@@iconresolver', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_message_140310272551056 = get('message', __marker)

            # <Value 'python:view.messages' (4:35)> -> __iterator
            __token = 135
            try:
                __zt_tmp = __attrs_140310475286144
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140310567013776('python', 'view.messages', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            (__iterator, ____index_140310475291472, ) = getname('repeat')('message', __iterator)
            econtext['message'] = None
            for __item in __iterator:
                econtext['message'] = __item
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f9c9409b070> name=None at 7f9c9409abc0> -> __attrs_140310475287728
                __attrs_140310475287728 = _static_140310475288688
                __backup_mtype_140310272302368 = get('mtype', __marker)

                # <Value 'message/type | nothing' (10:15)> -> __value
                __token = 279
                try:
                    __zt_tmp = __attrs_140310475287728
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'message/type | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['mtype'] = __value
                __backup_display_info_140310475290224 = get('display_info', __marker)

                # <Value 'python:view.display_info_for_mtype(mtype)' (11:21)> -> __value
                __token = 324
                try:
                    __zt_tmp = __attrs_140310475287728
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('python', 'view.display_info_for_mtype(mtype)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['display_info'] = __value

                # <Value 'mtype' (13:22)> -> __condition
                __token = 399
                try:
                    __zt_tmp = __attrs_140310475287728
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'mtype', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475283216
                    __default_140310475283216 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "portalMessage ${python:display_info['cssclass']}" (7:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c9409b820> -> __attr_class
                    __token = 174
                    __token = 190
                    try:
                        __zt_tmp = __attrs_140310475287728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140310567013776('python', "display_info['cssclass']", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('portalMessage ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append(' role="alert" >\n    ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475276592
                    __attrs_140310475276592 = _static_140310566789392

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475290560
                    __default_140310475290560 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')" (15:37)> -> __cache_140310475282352
                    __token = 447
                    try:
                        __zt_tmp = __attrs_140310475276592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475282352 = _static_140310567013776('python', "icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')" (15:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9409a8f0> -> __condition
                    __expression = __cache_140310475282352

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310475282352
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475286864
                    __attrs_140310475286864 = _static_140310566789392

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')

                    # <Interpolation value=<Substitution "${python:display_info['msg']}" (16:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9c940989a0> -> __content_140310653968752
                    __token = 573
                    __token = 575
                    try:
                        __zt_tmp = __attrs_140310475286864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140310653968752 = _static_140310567013776('python', "display_info['msg']", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
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
                    __append('</strong>\n    ')

                    # <Static value=<ast.Dict object at 0x7f9c94098580> name=None at 7f9c9409aa70> -> __attrs_140310475284464
                    __attrs_140310475284464 = _static_140310475277696

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475282208
                    __default_140310475282208 = _DEFAULT_MARKER

                    # <Value 'message/message | nothing' (18:23)> -> __cache_140310475292096
                    __token = 661
                    try:
                        __zt_tmp = __attrs_140310475284464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310475292096 = _static_140310567013776('path', 'message/message | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'message/message | nothing' (18:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94098340> -> __condition
                    __expression = __cache_140310475292096

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content" >\n            The status message.\n    </span>')
                    else:
                        __content = __cache_140310475292096
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n  </div>')
                if (__backup_display_info_140310475290224 is __marker):
                    del econtext['display_info']
                else:
                    econtext['display_info'] = __backup_display_info_140310475290224
                if (__backup_mtype_140310272302368 is __marker):
                    del econtext['mtype']
                else:
                    econtext['mtype'] = __backup_mtype_140310272302368
                __append('\n\n')
                ____index_140310475291472 -= 1
                if (____index_140310475291472 > 0):
                    __append('')
            if (__backup_message_140310272551056 is __marker):
                del econtext['message']
            else:
                econtext['message'] = __backup_message_140310272551056
            if (__backup_icons_140310272303808 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140310272303808
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }