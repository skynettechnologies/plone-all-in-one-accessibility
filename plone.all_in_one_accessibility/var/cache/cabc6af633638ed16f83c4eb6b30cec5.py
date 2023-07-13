# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.locking-3.0.0-py3.10.egg/plone/locking/browser/info.pt'

__tokens = {60: ('view/info/is_locked_for_current_user', 3, 14), 114: (' view/lock_is_stealabl', 4, 16), 157: ('s view/lock_in', 5, 18), 185: ("ns python:context.restrictedTraverse('@@iconresolve", 6, 10), 299: ('locked', 10, 24), 401: ("python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", 12, 39), 574: ('lock_details/author_page', 14, 38), 819: ('lock_details/author_page', 20, 18), 750: ('lock_details/fullname', 18, 24), 929: ('lock_details/time_difference', 24, 27), 1087: ('not:lock_details/author_page', 29, 41), 1273: ('lock_details/fullname', 33, 27), 1373: ('lock_details/time_difference', 36, 27), 1546: ('stealable', 42, 27), 1607: ('string:${context/absolute_url}/@@plone_lock_operations/force_unlock', 44, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310475283408 = {'type': 'submit', 'value': 'Unlock', }
_static_140310272504688 = {'method': 'POST', 'action': 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', }
_static_140310272506896 = {'href': 'lock_details/author_page', }
_static_140310475463056 = {'class': 'portalMessage info alert alert-info', }
_static_140310566789392 = {}
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310475472032 = {'id': 'plone-lock-status', }

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

            # <Static value=<ast.Dict object at 0x7f9c940c7ca0> name=None at 7f9c940c4eb0> -> __attrs_140310475463440
            __attrs_140310475463440 = _static_140310475472032
            __backup_locked_140310475468192 = get('locked', __marker)

            # <Value 'view/info/is_locked_for_current_user' (3:14)> -> __value
            __token = 60
            try:
                __zt_tmp = __attrs_140310475463440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/info/is_locked_for_current_user', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_stealable_140310475456624 = get('stealable', __marker)

            # <Value 'view/lock_is_stealable' (4:16)> -> __value
            __token = 114
            try:
                __zt_tmp = __attrs_140310475463440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/lock_is_stealable', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['stealable'] = __value
            __backup_lock_details_140310475472416 = get('lock_details', __marker)

            # <Value 'view/lock_info' (5:18)> -> __value
            __token = 157
            try:
                __zt_tmp = __attrs_140310475463440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/lock_info', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['lock_details'] = __value
            __backup_icons_140310475459408 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (6:10)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_140310475463440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_140310475470304 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="plone-lock-status" >\n  ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475465360
            __attrs_140310475465360 = _static_140310566789392

            # <Value 'locked' (10:24)> -> __condition
            __token = 299
            try:
                __zt_tmp = __attrs_140310475465360
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'locked', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f9c940c5990> name=None at 7f9c940c4f10> -> __attrs_140310475466272
                __attrs_140310475466272 = _static_140310475463056

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portalMessage info alert alert-info">\n      ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272497488
                __attrs_140310272497488 = _static_140310566789392

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272499360
                __default_140310272499360 = _DEFAULT_MARKER

                # <Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> -> __cache_140310272494848
                __token = 401
                try:
                    __zt_tmp = __attrs_140310272497488
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310272494848 = _static_140310567013776('python', "icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f34b80> -> __condition
                __expression = __cache_140310272494848

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140310272494848
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272506608
                __attrs_140310272506608 = _static_140310566789392

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append('<strong>')
                __stream_140310272497920 = []
                __append_140310272497920 = __stream_140310272497920.append
                __append_140310272497920('Locked')
                __msgid_140310272497920 = __re_whitespace(''.join(__stream_140310272497920)).strip()
                if 'label_locked':
                    __append(translate('label_locked', mapping=None, default=__msgid_140310272497920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</strong>\n      ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272499552
                __attrs_140310272499552 = _static_140310566789392

                # <Value 'lock_details/author_page' (14:38)> -> __condition
                __token = 574
                try:
                    __zt_tmp = __attrs_140310272499552
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'lock_details/author_page', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:
                    __stream_140310476106304_time = ''
                    __stream_140310476106304_author = ''
                    __stream_140310272499408 = []
                    __append_140310272499408 = __stream_140310272499408.append
                    __append_140310272499408('\n          This item was locked by\n        ')
                    __stream_140310476106304_author = []
                    __append_140310476106304_author = __stream_140310476106304_author.append

                    # <Static value=<ast.Dict object at 0x7f9c87f37c10> name=None at 7f9c87f36da0> -> __attrs_140310272501472
                    __attrs_140310272501472 = _static_140310272506896

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140310476106304_author('<a')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272505504
                    __default_140310272505504 = _DEFAULT_MARKER

                    # <Substitution 'lock_details/author_page' (20:18)> -> __attr_href
                    __token = 819
                    try:
                        __zt_tmp = __attrs_140310272501472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140310567013776('path', 'lock_details/author_page', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140310476106304_author((' href="%s"' % __attr_href))
                    __append_140310476106304_author(' >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272504880
                    __default_140310272504880 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (18:24)> -> __cache_140310272497296
                    __token = 750
                    try:
                        __zt_tmp = __attrs_140310272501472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272497296 = _static_140310567013776('path', 'lock_details/fullname', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (18:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f373a0> -> __condition
                    __expression = __cache_140310272497296

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310272497296
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140310476106304_author(__content)
                    __append_140310476106304_author('</a>')
                    __append_140310272499408('${author}')
                    __stream_140310476106304_author = ''.join(__stream_140310476106304_author)
                    __append_140310272499408('\n        ')
                    __stream_140310476106304_time = []
                    __append_140310476106304_time = __stream_140310476106304_time.append

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272496816
                    __attrs_140310272496816 = _static_140310566789392

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140310476106304_time('<span >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272499840
                    __default_140310272499840 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (24:27)> -> __cache_140310272496672
                    __token = 929
                    try:
                        __zt_tmp = __attrs_140310272496816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272496672 = _static_140310567013776('path', 'lock_details/time_difference', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (24:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f35570> -> __condition
                    __expression = __cache_140310272496672

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310272496672
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140310476106304_time(__content)
                    __append_140310476106304_time('</span>')
                    __append_140310272499408('${time}')
                    __stream_140310476106304_time = ''.join(__stream_140310476106304_time)
                    __append_140310272499408('\n         ago.\n      ')
                    __msgid_140310272499408 = __re_whitespace(''.join(__stream_140310272499408)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'author': __stream_140310476106304_author, 'time': __stream_140310476106304_time, }, default=__msgid_140310272499408, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272496336
                __attrs_140310272496336 = _static_140310566789392

                # <Value 'not:lock_details/author_page' (29:41)> -> __condition
                __token = 1087
                try:
                    __zt_tmp = __attrs_140310272496336
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('not', 'lock_details/author_page', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:
                    __stream_140310476106304_time = ''
                    __stream_140310476106304_author = ''
                    __stream_140310272492208 = []
                    __append_140310272492208 = __stream_140310272492208.append
                    __append_140310272492208('\n          This item was locked by\n        ')
                    __stream_140310476106304_author = []
                    __append_140310476106304_author = __stream_140310476106304_author.append

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272502528
                    __attrs_140310272502528 = _static_140310566789392

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140310476106304_author('<span >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272507136
                    __default_140310272507136 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (33:27)> -> __cache_140310272506080
                    __token = 1273
                    try:
                        __zt_tmp = __attrs_140310272502528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272506080 = _static_140310567013776('path', 'lock_details/fullname', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (33:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f36a10> -> __condition
                    __expression = __cache_140310272506080

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310272506080
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140310476106304_author(__content)
                    __append_140310476106304_author('</span>')
                    __append_140310272492208('${author}')
                    __stream_140310476106304_author = ''.join(__stream_140310476106304_author)
                    __append_140310272492208('\n        ')
                    __stream_140310476106304_time = []
                    __append_140310476106304_time = __stream_140310476106304_time.append

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272497200
                    __attrs_140310272497200 = _static_140310566789392

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140310476106304_time('<span >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272496144
                    __default_140310272496144 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (36:27)> -> __cache_140310272500656
                    __token = 1373
                    try:
                        __zt_tmp = __attrs_140310272497200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272500656 = _static_140310567013776('path', 'lock_details/time_difference', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (36:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f36170> -> __condition
                    __expression = __cache_140310272500656

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310272500656
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140310476106304_time(__content)
                    __append_140310476106304_time('</span>')
                    __append_140310272492208('${time}')
                    __stream_140310476106304_time = ''.join(__stream_140310476106304_time)
                    __append_140310272492208('\n         ago.\n      ')
                    __msgid_140310272492208 = __re_whitespace(''.join(__stream_140310272492208)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'author': __stream_140310476106304_author, 'time': __stream_140310476106304_time, }, default=__msgid_140310272492208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f9c87f37370> name=None at 7f9c87f373d0> -> __attrs_140310272491680
                __attrs_140310272491680 = _static_140310272504688

                # <Value 'stealable' (42:27)> -> __condition
                __token = 1546
                try:
                    __zt_tmp = __attrs_140310272491680
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'stealable', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form method="POST"')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272506848
                    __default_140310272506848 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock' (44:21)> -> __attr_action
                    __token = 1607
                    try:
                        __zt_tmp = __attrs_140310272491680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140310567013776('string', '${context/absolute_url}/@@plone_lock_operations/force_unlock', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272498160
                    __attrs_140310272498160 = _static_140310566789392

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140310476107648_unlock_button = ''
                    __stream_140310272498688 = []
                    __append_140310272498688 = __stream_140310272498688.append
                    __append_140310272498688('\n            If you are certain this user has abandoned the object,\n            you may\n          ')
                    __stream_140310476107648_unlock_button = []
                    __append_140310476107648_unlock_button = __stream_140310476107648_unlock_button.append

                    # <Static value=<ast.Dict object at 0x7f9c94099bd0> name=None at 7f9c9409b370> -> __attrs_140310475279136
                    __attrs_140310475279136 = _static_140310475283408

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append_140310476107648_unlock_button('<input type="submit"')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475288448
                    __default_140310475288448 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f9c940993f0> at 7f9c940988e0> -> __attr_value
                    __attr_value = 'Unlock'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append_140310476107648_unlock_button((' value="%s"' % __attr_value))
                    __append_140310476107648_unlock_button(' />')
                    __append_140310272498688('${unlock_button}')
                    __stream_140310476107648_unlock_button = ''.join(__stream_140310476107648_unlock_button)
                    __append_140310272498688('\n            the object. You will then be able to edit it.\n        ')
                    __msgid_140310272498688 = __re_whitespace(''.join(__stream_140310272498688)).strip()
                    if 'description_webdav_locked_steal':
                        __append(translate('description_webdav_locked_steal', mapping={'unlock_button': __stream_140310476107648_unlock_button, }, default=__msgid_140310272498688, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      </form>')
                __append('\n    </div>\n  ')
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_140310475470304
            if (__backup_icons_140310475459408 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140310475459408
            if (__backup_lock_details_140310475472416 is __marker):
                del econtext['lock_details']
            else:
                econtext['lock_details'] = __backup_lock_details_140310475472416
            if (__backup_stealable_140310475456624 is __marker):
                del econtext['stealable']
            else:
                econtext['stealable'] = __backup_stealable_140310475456624
            if (__backup_locked_140310475468192 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_140310475468192
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }