# -*- coding: utf-8 -*-
__filename = 'login_form'

__tokens = {166: ('string:${here/absolute_url}/login', 11, 33), 291: ('request/came_from | string:', 14, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139839082472512 = {'type': 'submit', 'value': ' Log In ', }
_static_139839082478032 = {'colspan': '2', }
_static_139839082476256 = {'type': 'password', 'name': '__ac_password', 'size': '30', }
_static_139839082472272 = {'type': 'text', 'name': '__ac_name', 'size': '30', }
_static_139839082473184 = {'cellpadding': '2', }
_static_139839092818272 = {'type': 'hidden', 'name': 'came_from', 'value': '', }
_static_139839140398752 = __C2ZContextWrapper
_static_139839140402352 = __compile_zt_expr
_static_139839092826336 = {'method': 'post', 'action': '', }
_static_139839134773072 = {}

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

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092833584
            __attrs_139839092833584 = _static_139839134773072

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092818896
            __attrs_139839092818896 = _static_139839134773072

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092824176
            __attrs_139839092824176 = _static_139839134773072

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title> Login Form </title>\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092823264
            __attrs_139839092823264 = _static_139839134773072

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839092825712
            __attrs_139839092825712 = _static_139839134773072

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3> Please log in </h3>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed37420e0> name=None at 7f2ed37404c0> -> __attrs_139839092830704
            __attrs_139839092830704 = _static_139839092826336

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form method="post"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839092834208
            __default_139839092834208 = _DEFAULT_MARKER

            # <Substitution 'string:${here/absolute_url}/login' (11:33)> -> __attr_action
            __token = 166
            try:
                __zt_tmp = __attrs_139839092830704
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_139839140402352('string', '${here/absolute_url}/login', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed3740160> name=None at 7f2ed37428f0> -> __attrs_139839082471264
            __attrs_139839082471264 = _static_139839092818272

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="came_from"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839082469584
            __default_139839082469584 = _DEFAULT_MARKER

            # <Substitution 'request/came_from | string:' (14:35)> -> __attr_value
            __token = 291
            try:
                __zt_tmp = __attrs_139839082471264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139839140402352('path', 'request/came_from | string:', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append('/>\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed2d626e0> name=None at 7f2ed2d62b30> -> __attrs_139839082477744
            __attrs_139839082477744 = _static_139839082473184

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table cellpadding="2">\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082477504
            __attrs_139839082477504 = _static_139839134773072

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082470880
            __attrs_139839082470880 = _static_139839134773072

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082471600
            __attrs_139839082471600 = _static_139839134773072

            # <b ... (0:0)
            # --------------------------------------------------------
            __append('<b>Login:</b> </td>\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082468576
            __attrs_139839082468576 = _static_139839134773072

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x7f2ed2d62350> name=None at 7f2ed2d61cc0> -> __attrs_139839082464112
            __attrs_139839082464112 = _static_139839082472272

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="__ac_name" size="30" /></td>\n        </tr>\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082471648
            __attrs_139839082471648 = _static_139839134773072

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082469344
            __attrs_139839082469344 = _static_139839134773072

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082470544
            __attrs_139839082470544 = _static_139839134773072

            # <b ... (0:0)
            # --------------------------------------------------------
            __append('<b>Password:</b></td>\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082474432
            __attrs_139839082474432 = _static_139839134773072

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x7f2ed2d632e0> name=None at 7f2ed2d63220> -> __attrs_139839082474912
            __attrs_139839082474912 = _static_139839082476256

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="password" name="__ac_password" size="30" /></td>\n        </tr>\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082475488
            __attrs_139839082475488 = _static_139839134773072

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x7f2ed2d639d0> name=None at 7f2ed2d63190> -> __attrs_139839082476880
            __attrs_139839082476880 = _static_139839082478032

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td colspan="2">\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839082467808
            __attrs_139839082467808 = _static_139839134773072

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7f2ed2d62440> name=None at 7f2ed2d61870> -> __attrs_139839082567168
            __attrs_139839082567168 = _static_139839082472512

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" value=" Log In " />\n          </td>\n        </tr>\n      </table>\n\n    </form>\n\n  </body>\n\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }