# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.protect-5.0.0-py3.10.egg/plone/protect/confirm.pt'

__tokens = {1381: ('request/original_url', 45, 23), 1467: ('python: request.form.keys()', 48, 38), 1592: ('key', 51, 26), 1623: (' python: request.form[key', 52, 26), 1807: ('request/original_url', 58, 29), 420: ("python:request.set('disable_border', 1)", 13, 23), 247: ('context/main_template/macros/master', 6, 23), 247: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140259638645456 = {'class': 'documentDescription', }
_static_140259638643488 = {'class': 'documentFirstHeading', }
_static_140259680495712 = 'master'
_static_140259638659920 = {'class': 'standalone', 'name': 'form.button.confirm', 'type': 'submit', 'value': 'Confirm action', }
_static_140259638656928 = {'class': 'formControls', }
_static_140259638652848 = {'type': 'hidden', 'name': 'key', 'value': 'python: request.form[key]', }
_static_140259692113696 = __C2ZContextWrapper
_static_140259692113984 = __compile_zt_expr
_static_140259638649968 = {'method': 'GET', 'action': 'request/original_url', }
_static_140259638648288 = {'class': 'discreet', }
_static_140259692102656 = {}

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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259638647136
            __attrs_140259638647136 = _static_140259692102656
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f90bdf01de0> name=None at 7f90bdf01e10> -> __attrs_140259638648672
            __attrs_140259638648672 = _static_140259638648288

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="discreet" >')
            __stream_140259638647808 = []
            __append_140259638647808 = __stream_140259638647808.append
            __append_140259638647808("\n        Careful, it's possible someone is executing an exploit against you.\n        Verify you just performed an action on this site and that you were\n        not referred here by a different website or email.\n        ")
            __msgid_140259638647808 = __re_whitespace(''.join(__stream_140259638647808)).strip()
            if __msgid_140259638647808:
                __append(translate(__msgid_140259638647808, mapping=None, default=__msgid_140259638647808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        ')

            # <Static value=<ast.Dict object at 0x7f90bdf02470> name=None at 7f90bdf024a0> -> __attrs_140259638650352
            __attrs_140259638650352 = _static_140259638649968

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form method="GET"')

            # <Symbol value=<DEFAULT> at 7f90c137a9e0> -> __default_140259638649440
            __default_140259638649440 = _DEFAULT_MARKER

            # <Substitution 'request/original_url' (45:23)> -> __attr_action
            __token = 1381
            try:
                __zt_tmp = __attrs_140259638650352
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140259692113984('path', 'request/original_url', econtext=econtext)(_static_140259692113696(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' >\n          ')

            # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259638651216
            __attrs_140259638651216 = _static_140259692102656
            __backup_key_140259672783216 = get('key', __marker)

            # <Value 'python: request.form.keys()' (48:38)> -> __iterator
            __token = 1467
            try:
                __zt_tmp = __attrs_140259638651216
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140259692113984('python', ' request.form.keys()', econtext=econtext)(_static_140259692113696(econtext, __zt_tmp))
            (__iterator, ____index_140259638651456, ) = getname('repeat')('key', __iterator)
            econtext['key'] = None
            for __item in __iterator:
                econtext['key'] = __item
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f90bdf02fb0> name=None at 7f90bdf02fe0> -> __attrs_140259638653520
                __attrs_140259638653520 = _static_140259638652848

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden"')

                # <Symbol value=<DEFAULT> at 7f90c137a9e0> -> __default_140259638652272
                __default_140259638652272 = _DEFAULT_MARKER

                # <Substitution 'key' (51:26)> -> __attr_name
                __token = 1592
                try:
                    __zt_tmp = __attrs_140259638653520
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140259692113984('path', 'key', econtext=econtext)(_static_140259692113696(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f90c137a9e0> -> __default_140259638653088
                __default_140259638653088 = _DEFAULT_MARKER

                # <Substitution 'python: request.form[key]' (52:26)> -> __attr_value
                __token = 1623
                try:
                    __zt_tmp = __attrs_140259638653520
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140259692113984('python', ' request.form[key]', econtext=econtext)(_static_140259692113696(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          ')
                ____index_140259638651456 -= 1
                if (____index_140259638651456 > 0):
                    __append('')
            if (__backup_key_140259672783216 is __marker):
                del econtext['key']
            else:
                econtext['key'] = __backup_key_140259672783216
            __append('\n          ')

            # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259638653904
            __attrs_140259638653904 = _static_140259692102656

            # <dl ... (0:0)
            # --------------------------------------------------------
            __append('<dl>\n            ')

            # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259638654960
            __attrs_140259638654960 = _static_140259692102656

            # <dt ... (0:0)
            # --------------------------------------------------------
            __append('<dt>')
            __stream_140259638654480 = []
            __append_140259638654480 = __stream_140259638654480.append
            __append_140259638654480('Original URL')
            __msgid_140259638654480 = __re_whitespace(''.join(__stream_140259638654480)).strip()
            if __msgid_140259638654480:
                __append(translate(__msgid_140259638654480, mapping=None, default=__msgid_140259638654480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</dt>\n            ')

            # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259638656496
            __attrs_140259638656496 = _static_140259692102656

            # <dd ... (0:0)
            # --------------------------------------------------------
            __append('<dd>')

            # <Symbol value=<DEFAULT> at 7f90c137a9e0> -> __default_140259638655920
            __default_140259638655920 = _DEFAULT_MARKER

            # <Value 'request/original_url' (58:29)> -> __cache_140259638655440
            __token = 1807
            try:
                __zt_tmp = __attrs_140259638656496
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140259638655440 = _static_140259692113984('path', 'request/original_url', econtext=econtext)(_static_140259692113696(econtext, __zt_tmp))

            # <BinOp left=<Value 'request/original_url' (58:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f90c137a9e0> at 7f90bdf03a90> -> __condition
            __expression = __cache_140259638655440

            # <Symbol value=<DEFAULT> at 7f90c137a9e0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140259638655440
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</dd>\n          </dl>\n          ')

            # <Static value=<ast.Dict object at 0x7f90bdf03fa0> name=None at 7f90bdf03fd0> -> __attrs_140259638657616
            __attrs_140259638657616 = _static_140259638656928

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formControls">\n            ')

            # <Static value=<ast.Dict object at 0x7f90bdf04b50> name=None at 7f90bdf04b80> -> __attrs_140259638658336
            __attrs_140259638658336 = _static_140259638659920

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="standalone" name="form.button.confirm" type="submit"')

            # <Symbol value=<DEFAULT> at 7f90c137a9e0> -> __default_140259638658864
            __default_140259638658864 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f90bdf047f0> at 7f90bdf047c0> -> __attr_value
            __attr_value = 'Confirm action'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n          </div>\n        </form>\n      ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259680500848
            __attrs_140259680500848 = _static_140259692102656
            __previous_i18n_domain_140259680500992 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140259690316672 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f90c06ea860> name=None at 7f90c06e9120> -> __value
            __value = _static_140259680495712
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259680501712
                __attrs_140259680501712 = _static_140259692102656
                __backup_dummy_140259672777264 = get('dummy', __marker)

                # <Value "python:request.set('disable_border', 1)" (13:23)> -> __value
                __token = 420
                try:
                    __zt_tmp = __attrs_140259680501712
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140259692113984('python', "request.set('disable_border', 1)", econtext=econtext)(_static_140259692113696(econtext, __zt_tmp))
                econtext['dummy'] = __value
                if (__backup_dummy_140259672777264 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_140259672777264
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259638642288
                __attrs_140259638642288 = _static_140259692102656
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f90bdf00b20> name=None at 7f90bdf009a0> -> __attrs_140259638643824
                __attrs_140259638643824 = _static_140259638643488

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading" >')
                __stream_140259638642960 = []
                __append_140259638642960 = __stream_140259638642960.append
                __append_140259638642960('\n         Confirming User Action.\n      ')
                __msgid_140259638642960 = __re_whitespace(''.join(__stream_140259638642960)).strip()
                if __msgid_140259638642960:
                    __append(translate(__msgid_140259638642960, mapping=None, default=__msgid_140259638642960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n    ')
            _slots = econtext['__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_description(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259638644256
                __attrs_140259638644256 = _static_140259692102656
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f90bdf012d0> name=None at 7f90bdf01150> -> __attrs_140259638645792
                __attrs_140259638645792 = _static_140259638645456

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentDescription" >')
                __stream_140259638644928 = []
                __append_140259638644928 = __stream_140259638644928.append
                __append_140259638644928("\n         Confirm that you'd like to perform this action.\n      ")
                __msgid_140259638644928 = __re_whitespace(''.join(__stream_140259638644928)).strip()
                if __msgid_140259638644928:
                    __append(translate(__msgid_140259638644928, mapping=None, default=__msgid_140259638644928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n    ')
            _slots = econtext['__slot_content_description'] = _deque((__fill_content_description, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f90c11fc400> name=None at 7f90c11fc730> -> __attrs_140259638646176
                __attrs_140259638646176 = _static_140259692102656
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140259680500848
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140259692113984('path', 'context/main_template/macros/master', econtext=econtext)(_static_140259692113696(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140259690316672 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140259690316672
            __i18n_domain = __previous_i18n_domain_140259680500992
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }