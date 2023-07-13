# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/login/templates/login.pt'

__tokens = {569: ('view/label | nothing', 18, 29), 1091: ('context/@@ploneform-macros/titlelessform', 31, 37), 1091: ('context/@@ploneform-macros/titlelessform', 31, 37), 1219: ('context/@@plone_portal_state', 34, 43), 1289: (' portal_state/portal_ur', 35, 40), 1503: ('string:${portal_url}/@@login-help', 38, 62), 1655: ('python:view.self_registration_enabled()', 40, 36), 1854: ('string:${portal_url}/@@register', 42, 60), 287: ('here/main_template/macros/master', 7, 23), 287: ('here/main_template/macros/master', 7, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140568710248048 = 'master'
_static_140568710484640 = {'href': '@@register', 'class': 'emph', }
_static_140568710480704 = {'href': '@@login-help', }
_static_140568710477040 = {'class': 'footer mt-4', }
_static_140568710475456 = 'titlelessform'
_static_140568710473440 = {'class': 'alert alert-danger pat-cookietrigger', 'style': 'display:none', }
_static_140568710471616 = {'id': 'login-form', }
_static_140568781877216 = __C2ZContextWrapper
_static_140568781877504 = __compile_zt_expr
_static_140568710470464 = {'class': 'card-title h5', }
_static_140568710468400 = {'class': 'card-body', }
_static_140568710467008 = {'class': 'card', }
_static_140568710465616 = {'class': 'login-wrapper', }
_static_140568781866176 = {}

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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710464512
            __attrs_140568710464512 = _static_140568781866176
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd8b40dc850> name=None at 7fd8b40dc880> -> __attrs_140568710466000
            __attrs_140568710466000 = _static_140568710465616

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="login-wrapper">\n\n        ')

            # <Static value=<ast.Dict object at 0x7fd8b40dcdc0> name=None at 7fd8b40dcdf0> -> __attrs_140568710467392
            __attrs_140568710467392 = _static_140568710467008

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card">\n          ')

            # <Static value=<ast.Dict object at 0x7fd8b40dd330> name=None at 7fd8b40dd360> -> __attrs_140568710468784
            __attrs_140568710468784 = _static_140568710468400

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n            ')

            # <Static value=<ast.Dict object at 0x7fd8b40ddb40> name=None at 7fd8b40ddb70> -> __attrs_140568710470848
            __attrs_140568710470848 = _static_140568710470464

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="card-title h5">')

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568710469888
            __default_140568710469888 = _DEFAULT_MARKER

            # <Value 'view/label | nothing' (18:29)> -> __cache_140568710469408
            __token = 569
            try:
                __zt_tmp = __attrs_140568710470848
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140568710469408 = _static_140568781877504('path', 'view/label | nothing', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/label | nothing' (18:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8b40dd7e0> -> __condition
            __expression = __cache_140568710469408

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140568710469408
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</h1>\n\n            ')

            # <Static value=<ast.Dict object at 0x7fd8b40ddfc0> name=None at 7fd8b40ddff0> -> __attrs_140568710472000
            __attrs_140568710472000 = _static_140568710471616

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="login-form">\n\n              ')

            # <Static value=<ast.Dict object at 0x7fd8b40de6e0> name=None at 7fd8b40de710> -> __attrs_140568710473632
            __attrs_140568710473632 = _static_140568710473440

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="alert alert-danger pat-cookietrigger" style="display:none">\n                ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710474736
            __attrs_140568710474736 = _static_140568781866176

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_140568710474256 = []
            __append_140568710474256 = __stream_140568710474256.append
            __append_140568710474256('\n                  Error\n                ')
            __msgid_140568710474256 = __re_whitespace(''.join(__stream_140568710474256)).strip()
            if __msgid_140568710474256:
                __append(translate(__msgid_140568710474256, mapping=None, default=__msgid_140568710474256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>\n                ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710475696
            __attrs_140568710475696 = _static_140568781866176
            __stream_140568710475312 = []
            __append_140568710475312 = __stream_140568710475312.append
            __append_140568710475312('\n                  Cookies are not enabled. You must enable cookies before you can log in.\n                ')
            __msgid_140568710475312 = __re_whitespace(''.join(__stream_140568710475312)).strip()
            if 'enable_cookies_message_before_login':
                __append(translate('enable_cookies_message_before_login', mapping=None, default=__msgid_140568710475312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n              </div>\n              ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710476272
            __attrs_140568710476272 = _static_140568781866176
            __backup_macroname_140568771355584 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd8b40deec0> name=None at 7fd8b40df010> -> __value
            __value = _static_140568710475456
            econtext['macroname'] = __value

            # <Value 'context/@@ploneform-macros/titlelessform' (31:37)> -> __macro
            __token = 1091
            try:
                __zt_tmp = __attrs_140568710476272
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140568781877504('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            __token = 1091
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140568771355584 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140568771355584
            __append('\n\n              ')

            # <Static value=<ast.Dict object at 0x7fd8b40df4f0> name=None at 7fd8b40df520> -> __attrs_140568710477424
            __attrs_140568710477424 = _static_140568710477040
            __backup_portal_state_140568710467728 = get('portal_state', __marker)

            # <Value 'context/@@plone_portal_state' (34:43)> -> __value
            __token = 1219
            try:
                __zt_tmp = __attrs_140568710477424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140568781877504('path', 'context/@@plone_portal_state', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_portal_url_140568710469120 = get('portal_url', __marker)

            # <Value 'portal_state/portal_url' (35:40)> -> __value
            __token = 1289
            try:
                __zt_tmp = __attrs_140568710477424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140568781877504('path', 'portal_state/portal_url', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            econtext['portal_url'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="footer mt-4">\n                ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710478816
            __attrs_140568710478816 = _static_140568781866176

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n                  ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710479824
            __attrs_140568710479824 = _static_140568781866176
            __stream_140568710479440 = []
            __append_140568710479440 = __stream_140568710479440.append
            __append_140568710479440('Trouble logging in?')
            __msgid_140568710479440 = __re_whitespace(''.join(__stream_140568710479440)).strip()
            if 'trouble_logging_in':
                __append(translate('trouble_logging_in', mapping=None, default=__msgid_140568710479440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n                  ')

            # <Static value=<ast.Dict object at 0x7fd8b40e0340> name=None at 7fd8b40e0370> -> __attrs_140568710481376
            __attrs_140568710481376 = _static_140568710480704

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568710480848
            __default_140568710480848 = _DEFAULT_MARKER

            # <Substitution 'string:${portal_url}/@@login-help' (38:62)> -> __attr_href
            __token = 1503
            try:
                __zt_tmp = __attrs_140568710481376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140568781877504('string', '${portal_url}/@@login-help', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '@@login-help', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')
            __stream_140568710479584 = []
            __append_140568710479584 = __stream_140568710479584.append
            __append_140568710479584('Get help')
            __msgid_140568710479584 = __re_whitespace(''.join(__stream_140568710479584)).strip()
            if 'footer_login_link_get_help':
                __append(translate('footer_login_link_get_help', mapping=None, default=__msgid_140568710479584, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>.\n                </div>\n                ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710482144
            __attrs_140568710482144 = _static_140568781866176

            # <Value 'python:view.self_registration_enabled()' (40:36)> -> __condition
            __token = 1655
            try:
                __zt_tmp = __attrs_140568710482144
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140568781877504('python', 'view.self_registration_enabled()', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n                  ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710483296
                __attrs_140568710483296 = _static_140568781866176
                __stream_140568710482912 = []
                __append_140568710482912 = __stream_140568710482912.append
                __append_140568710482912('Need an account?')
                __msgid_140568710482912 = __re_whitespace(''.join(__stream_140568710482912)).strip()
                if 'need_an_account':
                    __append(translate('need_an_account', mapping=None, default=__msgid_140568710482912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n                  ')

                # <Static value=<ast.Dict object at 0x7fd8b40e12a0> name=None at 7fd8b40e0f70> -> __attrs_140568710484928
                __attrs_140568710484928 = _static_140568710484640

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568710484304
                __default_140568710484304 = _DEFAULT_MARKER

                # <Substitution 'string:${portal_url}/@@register' (42:60)> -> __attr_href
                __token = 1854
                try:
                    __zt_tmp = __attrs_140568710484928
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140568781877504('string', '${portal_url}/@@register', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '@@register', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' class="emph">')
                __stream_140568710483056 = []
                __append_140568710483056 = __stream_140568710483056.append
                __append_140568710483056('Sign up here')
                __msgid_140568710483056 = __re_whitespace(''.join(__stream_140568710483056)).strip()
                if 'footer_login_link_signup':
                    __append(translate('footer_login_link_signup', mapping=None, default=__msgid_140568710483056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>.\n                </div>')
            __append('\n              </div>')
            if (__backup_portal_url_140568710469120 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140568710469120
            if (__backup_portal_state_140568710467728 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140568710467728
            __append('\n\n            </div>\n\n          </div>\n        </div>\n\n      </div>\n\n    ')
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

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710248384
            __attrs_140568710248384 = _static_140568781866176
            __previous_i18n_domain_140568710248528 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140568772834560 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd8b40a7670> name=None at 7fd8b40a76a0> -> __value
            __value = _static_140568710248048
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710250448
                __attrs_140568710250448 = _static_140568781866176
                __append('\n    ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n  ')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'here/main_template/macros/master' (7:23)> -> __macro
            __token = 287
            try:
                __zt_tmp = __attrs_140568710248384
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140568781877504('path', 'here/main_template/macros/master', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            __token = 287
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140568772834560 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140568772834560
            __i18n_domain = __previous_i18n_domain_140568710248528
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }