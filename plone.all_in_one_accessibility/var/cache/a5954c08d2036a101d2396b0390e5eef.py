# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.locking-3.0.0-py3.10.egg/plone/locking/browser/info.pt'

__tokens = {60: ('view/info/is_locked_for_current_user', 3, 14), 114: (' view/lock_is_stealabl', 4, 16), 157: ('s view/lock_in', 5, 18), 185: ("ns python:context.restrictedTraverse('@@iconresolve", 6, 10), 299: ('locked', 10, 24), 401: ("python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", 12, 39), 574: ('lock_details/author_page', 14, 38), 819: ('lock_details/author_page', 20, 18), 750: ('lock_details/fullname', 18, 24), 929: ('lock_details/time_difference', 24, 27), 1087: ('not:lock_details/author_page', 29, 41), 1273: ('lock_details/fullname', 33, 27), 1373: ('lock_details/time_difference', 36, 27), 1546: ('stealable', 42, 27), 1607: ('string:${context/absolute_url}/@@plone_lock_operations/force_unlock', 44, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882206108000 = {'type': 'submit', 'value': 'Unlock', }
_static_139882206108336 = {'method': 'POST', 'action': 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', }
_static_139882208493968 = {'href': 'lock_details/author_page', }
_static_139882101069840 = {'class': 'portalMessage info alert alert-info', }
_static_139882337226896 = {}
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882329965136 = {'id': 'plone-lock-status', }

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

            # <Static value=<ast.Dict object at 0x7f38e4968250> name=None at 7f38e4968130> -> __attrs_139882213725408
            __attrs_139882213725408 = _static_139882329965136
            __backup_locked_139882211073072 = get('locked', __marker)

            # <Value 'view/info/is_locked_for_current_user' (3:14)> -> __value
            __token = 60
            try:
                __zt_tmp = __attrs_139882213725408
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/info/is_locked_for_current_user', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_stealable_139882211079888 = get('stealable', __marker)

            # <Value 'view/lock_is_stealable' (4:16)> -> __value
            __token = 114
            try:
                __zt_tmp = __attrs_139882213725408
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/lock_is_stealable', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['stealable'] = __value
            __backup_lock_details_139882211070048 = get('lock_details', __marker)

            # <Value 'view/lock_info' (5:18)> -> __value
            __token = 157
            try:
                __zt_tmp = __attrs_139882213725408
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/lock_info', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['lock_details'] = __value
            __backup_icons_139882213721088 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (6:10)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_139882213725408
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_139882218701440 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="plone-lock-status" >\n  ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882337238800
            __attrs_139882337238800 = _static_139882337226896

            # <Value 'locked' (10:24)> -> __condition
            __token = 299
            try:
                __zt_tmp = __attrs_139882337238800
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('path', 'locked', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f38d6f1d810> name=None at 7f38d6f1ca30> -> __attrs_139882101069312
                __attrs_139882101069312 = _static_139882101069840

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portalMessage info alert alert-info">\n      ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101067920
                __attrs_139882101067920 = _static_139882337226896

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101073440
                __default_139882101073440 = _DEFAULT_MARKER

                # <Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> -> __cache_139882101064368
                __token = 401
                try:
                    __zt_tmp = __attrs_139882101067920
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882101064368 = _static_139882257081264('python', "icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6f1fbe0> -> __condition
                __expression = __cache_139882101064368

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139882101064368
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101078624
                __attrs_139882101078624 = _static_139882337226896

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append('<strong>')
                __stream_139882101077856 = []
                __append_139882101077856 = __stream_139882101077856.append
                __append_139882101077856('Locked')
                __msgid_139882101077856 = __re_whitespace(''.join(__stream_139882101077856)).strip()
                if 'label_locked':
                    __append(translate('label_locked', mapping=None, default=__msgid_139882101077856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</strong>\n      ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101078816
                __attrs_139882101078816 = _static_139882337226896

                # <Value 'lock_details/author_page' (14:38)> -> __condition
                __token = 574
                try:
                    __zt_tmp = __attrs_139882101078816
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'lock_details/author_page', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:
                    __stream_139882101600800_time = ''
                    __stream_139882101600800_author = ''
                    __stream_139882101069552 = []
                    __append_139882101069552 = __stream_139882101069552.append
                    __append_139882101069552('\n          This item was locked by\n        ')
                    __stream_139882101600800_author = []
                    __append_139882101600800_author = __stream_139882101600800_author.append

                    # <Static value=<ast.Dict object at 0x7f38dd590190> name=None at 7f38dd5939d0> -> __attrs_139882237469760
                    __attrs_139882237469760 = _static_139882208493968

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139882101600800_author('<a')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882238615440
                    __default_139882238615440 = _DEFAULT_MARKER

                    # <Substitution 'lock_details/author_page' (20:18)> -> __attr_href
                    __token = 819
                    try:
                        __zt_tmp = __attrs_139882237469760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('path', 'lock_details/author_page', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139882101600800_author((' href="%s"' % __attr_href))
                    __append_139882101600800_author(' >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882215131744
                    __default_139882215131744 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (18:24)> -> __cache_139882215139424
                    __token = 750
                    try:
                        __zt_tmp = __attrs_139882237469760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882215139424 = _static_139882257081264('path', 'lock_details/fullname', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (18:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38ddbe66b0> -> __condition
                    __expression = __cache_139882215139424

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882215139424
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139882101600800_author(__content)
                    __append_139882101600800_author('</a>')
                    __append_139882101069552('${author}')
                    __stream_139882101600800_author = ''.join(__stream_139882101600800_author)
                    __append_139882101069552('\n        ')
                    __stream_139882101600800_time = []
                    __append_139882101600800_time = __stream_139882101600800_time.append

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206105408
                    __attrs_139882206105408 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139882101600800_time('<span >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206112896
                    __default_139882206112896 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (24:27)> -> __cache_139882237472544
                    __token = 929
                    try:
                        __zt_tmp = __attrs_139882206105408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882237472544 = _static_139882257081264('path', 'lock_details/time_difference', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (24:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd34a170> -> __condition
                    __expression = __cache_139882237472544

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882237472544
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139882101600800_time(__content)
                    __append_139882101600800_time('</span>')
                    __append_139882101069552('${time}')
                    __stream_139882101600800_time = ''.join(__stream_139882101600800_time)
                    __append_139882101069552('\n         ago.\n      ')
                    __msgid_139882101069552 = __re_whitespace(''.join(__stream_139882101069552)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'author': __stream_139882101600800_author, 'time': __stream_139882101600800_time, }, default=__msgid_139882101069552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206113328
                __attrs_139882206113328 = _static_139882337226896

                # <Value 'not:lock_details/author_page' (29:41)> -> __condition
                __token = 1087
                try:
                    __zt_tmp = __attrs_139882206113328
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('not', 'lock_details/author_page', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:
                    __stream_139882101600800_time = ''
                    __stream_139882101600800_author = ''
                    __stream_139882101070608 = []
                    __append_139882101070608 = __stream_139882101070608.append
                    __append_139882101070608('\n          This item was locked by\n        ')
                    __stream_139882101600800_author = []
                    __append_139882101600800_author = __stream_139882101600800_author.append

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206112512
                    __attrs_139882206112512 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139882101600800_author('<span >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206113616
                    __default_139882206113616 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (33:27)> -> __cache_139882206113088
                    __token = 1273
                    try:
                        __zt_tmp = __attrs_139882206112512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882206113088 = _static_139882257081264('path', 'lock_details/fullname', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (33:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd34a1a0> -> __condition
                    __expression = __cache_139882206113088

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882206113088
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139882101600800_author(__content)
                    __append_139882101600800_author('</span>')
                    __append_139882101070608('${author}')
                    __stream_139882101600800_author = ''.join(__stream_139882101600800_author)
                    __append_139882101070608('\n        ')
                    __stream_139882101600800_time = []
                    __append_139882101600800_time = __stream_139882101600800_time.append

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206114672
                    __attrs_139882206114672 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139882101600800_time('<span >')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206109728
                    __default_139882206109728 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (36:27)> -> __cache_139882206114864
                    __token = 1373
                    try:
                        __zt_tmp = __attrs_139882206114672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882206114864 = _static_139882257081264('path', 'lock_details/time_difference', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (36:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd34aad0> -> __condition
                    __expression = __cache_139882206114864

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882206114864
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139882101600800_time(__content)
                    __append_139882101600800_time('</span>')
                    __append_139882101070608('${time}')
                    __stream_139882101600800_time = ''.join(__stream_139882101600800_time)
                    __append_139882101070608('\n         ago.\n      ')
                    __msgid_139882101070608 = __re_whitespace(''.join(__stream_139882101070608)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'author': __stream_139882101600800_author, 'time': __stream_139882101600800_time, }, default=__msgid_139882101070608, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f38dd349ab0> name=None at 7f38dd34afb0> -> __attrs_139882206109920
                __attrs_139882206109920 = _static_139882206108336

                # <Value 'stealable' (42:27)> -> __condition
                __token = 1546
                try:
                    __zt_tmp = __attrs_139882206109920
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'stealable', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form method="POST"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206113904
                    __default_139882206113904 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock' (44:21)> -> __attr_action
                    __token = 1607
                    try:
                        __zt_tmp = __attrs_139882206109920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_139882257081264('string', '${context/absolute_url}/@@plone_lock_operations/force_unlock', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206102768
                    __attrs_139882206102768 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139882101600352_unlock_button = ''
                    __stream_139882206113376 = []
                    __append_139882206113376 = __stream_139882206113376.append
                    __append_139882206113376('\n            If you are certain this user has abandoned the object,\n            you may\n          ')
                    __stream_139882101600352_unlock_button = []
                    __append_139882101600352_unlock_button = __stream_139882101600352_unlock_button.append

                    # <Static value=<ast.Dict object at 0x7f38dd349960> name=None at 7f38dd348ca0> -> __attrs_139882206103728
                    __attrs_139882206103728 = _static_139882206108000

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append_139882101600352_unlock_button('<input type="submit"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206107712
                    __default_139882206107712 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f38dd348490> at 7f38dd34a050> -> __attr_value
                    __attr_value = 'Unlock'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append_139882101600352_unlock_button((' value="%s"' % __attr_value))
                    __append_139882101600352_unlock_button(' />')
                    __append_139882206113376('${unlock_button}')
                    __stream_139882101600352_unlock_button = ''.join(__stream_139882101600352_unlock_button)
                    __append_139882206113376('\n            the object. You will then be able to edit it.\n        ')
                    __msgid_139882206113376 = __re_whitespace(''.join(__stream_139882206113376)).strip()
                    if 'description_webdav_locked_steal':
                        __append(translate('description_webdav_locked_steal', mapping={'unlock_button': __stream_139882101600352_unlock_button, }, default=__msgid_139882206113376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      </form>')
                __append('\n    </div>\n  ')
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_139882218701440
            if (__backup_icons_139882213721088 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139882213721088
            if (__backup_lock_details_139882211070048 is __marker):
                del econtext['lock_details']
            else:
                econtext['lock_details'] = __backup_lock_details_139882211070048
            if (__backup_stealable_139882211079888 is __marker):
                del econtext['stealable']
            else:
                econtext['stealable'] = __backup_stealable_139882211079888
            if (__backup_locked_139882211073072 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_139882211073072
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }