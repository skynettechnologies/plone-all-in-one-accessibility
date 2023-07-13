# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/controlpanel/browser/maintenance.pt'

__tokens = {454: ('view/available', 14, 51), 1008: ('view/label', 33, 31), 1049: ('view/label', 34, 29), 1248: ('view/description', 40, 31), 1295: ('view/description', 41, 29), 1483: ('request/URL', 49, 41), 2355: ('view/isRestartable', 69, 51), 2903: ('context/@@authenticator/authenticator', 83, 46), 5385: ('view/extra_script | nothing', 143, 41), 5445: ('extra_script', 144, 31), 5498: ('extra_script', 145, 39), 555: ('view/status', 18, 37), 600: ('status', 19, 32), 815: ('view/status', 25, 36), 3083: ('request/URL', 89, 41), 3323: ('nothing', 95, 65), 3447: ('view/form_name|nothing', 99, 50), 3514: ('form_name', 100, 43), 3566: ('form_name', 101, 41), 3737: ('view/dbName', 104, 116), 3944: ('view/dbSize', 108, 100), 5260: ('context/@@authenticator/authenticator', 138, 46), 4105: ('view/widgets/values', 112, 52), 4332: ('widget/@@ploneform-render-widget', 115, 71), 5602: ('not: view/available', 151, 32), 5725: ('view/label', 154, 28), 5763: ('view/label', 155, 26), 5935: ('view/description', 160, 27), 6161: ('string:$portal_url/@@overview-controlpanel', 167, 37), 277: ('context/prefs_main_template/macros/master', 7, 23), 277: ('context/prefs_main_template/macros/master', 7, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140568625063648 = {'href': '', 'class': 'link-parent', }
_static_140568625066432 = {'id': 'content-core', }
_static_140568625059616 = {'class': 'documentDescription', }
_static_140568625055824 = {'class': 'documentFirstHeading', }
_static_140568711027328 = 'master'
_static_140568625330256 = {'type': 'submit', 'id': 'form.buttons.pack', 'name': 'form.buttons.pack', 'value': 'Pack', 'class': 'btn btn-danger', }
_static_140568625316000 = {'class': 'actionButtons', }
_static_140568625331744 = {'id': 'actionsView', 'class': 'formControls', }
_static_140568625328768 = {'class': 'visualClear', }
_static_140568861882592 = {'class': 'mb-4', }
_static_140568625353808 = {'action': '.', 'method': 'post', 'class': 'edit-form', 'enctype': 'multipart/form-data', 'id': 'zc.page.browser_form', }
_static_140568624962848 = {'role': 'status', 'class': 'alert alert-info', }
_static_140568625364464 = {'type': 'submit', 'id': 'form.buttons.restart', 'name': 'form.buttons.restart', 'value': 'Restart', 'class': 'btn btn-danger', }
_static_140568625361536 = {'type': 'submit', 'id': 'form.buttons.shutdown', 'name': 'form.buttons.shutdown', 'value': 'Shut down', 'class': 'btn btn-danger', }
_static_140568625352656 = {'class': 'actionButtons', }
_static_140568625362928 = {'id': 'actionsView', 'class': 'formControls', }
_static_140568710247520 = {'class': 'mb-4', }
_static_140568710247616 = {'action': '.', 'method': 'post', 'class': 'edit-form', 'enctype': 'multipart/form-data', }
_static_140568710241808 = {'id': 'content-core', }
_static_140568710699504 = {'class': 'documentDescription', }
_static_140568624966448 = {'class': 'documentFirstHeading', }
_static_140568781877216 = __C2ZContextWrapper
_static_140568781877504 = __compile_zt_expr
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

    def render_form(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_heading = econtext['__slot_heading'].pop()
        except:
            __slot_heading = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624958720
            __attrs_140568624958720 = _static_140568781866176

            # <Value 'view/available' (14:51)> -> __condition
            __token = 454
            try:
                __zt_tmp = __attrs_140568624958720
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140568781877504('path', 'view/available', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            if __condition:
                __append('\n\n         ')
                __token = None
                render_header(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n         ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624967648
                __attrs_140568624967648 = _static_140568781866176

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n            ')
                if (__slot_heading is None):

                    # <Static value=<ast.Dict object at 0x7fd8aef52b30> name=None at 7fd8aef529b0> -> __attrs_140568624966784
                    __attrs_140568624966784 = _static_140568624966448

                    # <Value 'view/label' (33:31)> -> __condition
                    __token = 1008
                    try:
                        __zt_tmp = __attrs_140568624966784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140568781877504('path', 'view/label', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                    if __condition:

                        # <h1 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h1 class="documentFirstHeading">')

                        # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624960928
                        __default_140568624960928 = _DEFAULT_MARKER

                        # <Value 'view/label' (34:29)> -> __cache_140568624960304
                        __token = 1049
                        try:
                            __zt_tmp = __attrs_140568624966784
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140568624960304 = _static_140568781877504('path', 'view/label', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                        # <BinOp left=<Value 'view/label' (34:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aef517b0> -> __condition
                        __expression = __cache_140568624960304

                        # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                Do something\n            ')
                        else:
                            __content = __cache_140568624960304
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</h1>')
                else:
                    __slot_heading(__stream, econtext.copy(), rcontext)
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7fd8b41159f0> name=None at 7fd8b4114910> -> __attrs_140568710702576
                __attrs_140568710702576 = _static_140568710699504

                # <Value 'view/description' (40:31)> -> __condition
                __token = 1248
                try:
                    __zt_tmp = __attrs_140568710702576
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140568781877504('path', 'view/description', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="documentDescription">')

                    # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568710693648
                    __default_140568710693648 = _DEFAULT_MARKER

                    # <Value 'view/description' (41:29)> -> __cache_140568624968272
                    __token = 1295
                    try:
                        __zt_tmp = __attrs_140568710702576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140568624968272 = _static_140568781877504('path', 'view/description', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/description' (41:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aef53c10> -> __condition
                    __expression = __cache_140568624968272

                    # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                Description\n            ')
                    else:
                        __content = __cache_140568624968272
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>')
                __append('\n        </header>\n\n        ')

                # <Static value=<ast.Dict object at 0x7fd8b40a5e10> name=None at 7fd8b40a75b0> -> __attrs_140568710246848
                __attrs_140568710246848 = _static_140568710241808

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n\n            ')

                # <Static value=<ast.Dict object at 0x7fd8b40a74c0> name=None at 7fd8b40a7a90> -> __attrs_140568710248240
                __attrs_140568710248240 = _static_140568710247616

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568710242048
                __default_140568710242048 = _DEFAULT_MARKER

                # <Substitution 'request/URL' (49:41)> -> __attr_action
                __token = 1483
                try:
                    __zt_tmp = __attrs_140568710248240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140568781877504('path', 'request/URL', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' method="post" class="edit-form" enctype="multipart/form-data">\n\n                ')

                # <Static value=<ast.Dict object at 0x7fd8b40a7460> name=None at 7fd8b40a7c40> -> __attrs_140568625355584
                __attrs_140568625355584 = _static_140568710247520

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset class="mb-4">\n                    ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625359472
                __attrs_140568625359472 = _static_140568781866176

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')
                __stream_140568625356160 = []
                __append_140568625356160 = __stream_140568625356160.append
                __append_140568625356160('\n                        Zope Server\n                    ')
                __msgid_140568625356160 = __re_whitespace(''.join(__stream_140568625356160)).strip()
                if 'heading_zope_server':
                    __append(translate('heading_zope_server', mapping=None, default=__msgid_140568625356160, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</legend>\n\n                    ')

                # <Static value=<ast.Dict object at 0x7fd8aefb37f0> name=None at 7fd8aefb20b0> -> __attrs_140568625362880
                __attrs_140568625362880 = _static_140568625362928

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="actionsView" class="formControls">\n                        ')

                # <Static value=<ast.Dict object at 0x7fd8aefb0fd0> name=None at 7fd8aefb2560> -> __attrs_140568625357936
                __attrs_140568625357936 = _static_140568625352656

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="actionButtons">\n                            ')

                # <Static value=<ast.Dict object at 0x7fd8aefb3280> name=None at 7fd8aefb30d0> -> __attrs_140568625358608
                __attrs_140568625358608 = _static_140568625361536

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button type="submit" id="form.buttons.shutdown" name="form.buttons.shutdown" value="Shut down" class="btn btn-danger">\n                                ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625349872
                __attrs_140568625349872 = _static_140568781866176

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_140568625362304 = []
                __append_140568625362304 = __stream_140568625362304.append
                __append_140568625362304('Shut down')
                __msgid_140568625362304 = __re_whitespace(''.join(__stream_140568625362304)).strip()
                if __msgid_140568625362304:
                    __append(translate(__msgid_140568625362304, mapping=None, default=__msgid_140568625362304, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n                            </button>\n\n                            ')

                # <Static value=<ast.Dict object at 0x7fd8aefb3df0> name=None at 7fd8aefb0340> -> __attrs_140568625349824
                __attrs_140568625349824 = _static_140568625364464

                # <Value 'view/isRestartable' (69:51)> -> __condition
                __token = 2355
                try:
                    __zt_tmp = __attrs_140568625349824
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140568781877504('path', 'view/isRestartable', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                if __condition:

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button type="submit" id="form.buttons.restart" name="form.buttons.restart" value="Restart" class="btn btn-danger">\n                                ')

                    # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625349248
                    __attrs_140568625349248 = _static_140568781866176

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140568625351936 = []
                    __append_140568625351936 = __stream_140568625351936.append
                    __append_140568625351936('Restart')
                    __msgid_140568625351936 = __re_whitespace(''.join(__stream_140568625351936)).strip()
                    if __msgid_140568625351936:
                        __append(translate(__msgid_140568625351936, mapping=None, default=__msgid_140568625351936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n                            </button>')
                __append('\n\n                        </span>\n                    </div>\n\n                </fieldset>\n\n                ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625351168
                __attrs_140568625351168 = _static_140568781866176

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568625351072
                __default_140568625351072 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (83:46)> -> __cache_140568625348912
                __token = 2903
                try:
                    __zt_tmp = __attrs_140568625351168
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140568625348912 = _static_140568781877504('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (83:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aefb0400> -> __condition
                __expression = __cache_140568625348912

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input />')
                else:
                    __content = __cache_140568625348912
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n            </form>\n\n            ')
                __token = None
                render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624993120
                __attrs_140568624993120 = _static_140568781866176
                __backup_extra_script_140568625364800 = get('extra_script', __marker)

                # <Value 'view/extra_script | nothing' (143:41)> -> __value
                __token = 5385
                try:
                    __zt_tmp = __attrs_140568624993120
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140568781877504('path', 'view/extra_script | nothing', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                econtext['extra_script'] = __value

                # <Value 'extra_script' (144:31)> -> __condition
                __token = 5445
                try:
                    __zt_tmp = __attrs_140568624993120
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140568781877504('path', 'extra_script', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                if __condition:

                    # <script ... (0:0)
                    # --------------------------------------------------------
                    __append('<script>')

                    # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624991776
                    __default_140568624991776 = _DEFAULT_MARKER

                    # <Value 'extra_script' (145:39)> -> __cache_140568625323104
                    __token = 5498
                    try:
                        __zt_tmp = __attrs_140568624993120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140568625323104 = _static_140568781877504('path', 'extra_script', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                    # <BinOp left=<Value 'extra_script' (145:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aefa9b70> -> __condition
                    __expression = __cache_140568625323104

                    # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n            ')
                    else:
                        __content = __cache_140568625323104
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</script>')
                if (__backup_extra_script_140568625364800 is __marker):
                    del econtext['extra_script']
                else:
                    econtext['extra_script'] = __backup_extra_script_140568625364800
                __append('\n        </div>\n\n    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_header(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624970480
            __attrs_140568624970480 = _static_140568781866176
            __append('\n\n             ')

            # <Static value=<ast.Dict object at 0x7fd8aef51d20> name=None at 7fd8aef51660> -> __attrs_140568624971488
            __attrs_140568624971488 = _static_140568624962848
            __backup_status_140568625364368 = get('status', __marker)

            # <Value 'view/status' (18:37)> -> __value
            __token = 555
            try:
                __zt_tmp = __attrs_140568624971488
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140568781877504('path', 'view/status', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            econtext['status'] = __value

            # <Value 'status' (19:32)> -> __condition
            __token = 600
            try:
                __zt_tmp = __attrs_140568624971488
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140568781877504('path', 'status', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div role="status" class="alert alert-info">\n                 ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624965440
                __attrs_140568624965440 = _static_140568781866176

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append('<strong>')
                __stream_140568624971056 = []
                __append_140568624971056 = __stream_140568624971056.append
                __append_140568624971056('\n                     Info\n                 ')
                __msgid_140568624971056 = __re_whitespace(''.join(__stream_140568624971056)).strip()
                if __msgid_140568624971056:
                    __append(translate(__msgid_140568624971056, mapping=None, default=__msgid_140568624971056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</strong>\n                 ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624968416
                __attrs_140568624968416 = _static_140568781866176

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568624965248
                __default_140568624965248 = _DEFAULT_MARKER

                # <Value 'view/status' (25:36)> -> __cache_140568624963520
                __token = 815
                try:
                    __zt_tmp = __attrs_140568624968416
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140568624963520 = _static_140568781877504('path', 'view/status', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/status' (25:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aef50ee0> -> __condition
                __expression = __cache_140568624963520

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140568624963520
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n                </div>')
            if (__backup_status_140568625364368 is __marker):
                del econtext['status']
            else:
                econtext['status'] = __backup_status_140568625364368
            __append('\n\n         ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_above_buttons = econtext['__slot_above_buttons'].pop()
        except:
            __slot_above_buttons = None

        try:
            __slot_extra_info = econtext['__slot_extra_info'].pop()
        except:
            __slot_extra_info = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd8aefb1450> name=None at 7fd8aefb14b0> -> __attrs_140568710588272
            __attrs_140568710588272 = _static_140568625353808

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568625355008
            __default_140568625355008 = _DEFAULT_MARKER

            # <Substitution 'request/URL' (89:41)> -> __attr_action
            __token = 3083
            try:
                __zt_tmp = __attrs_140568710588272
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140568781877504('path', 'request/URL', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post" class="edit-form" enctype="multipart/form-data" id="zc.page.browser_form">\n\n                ')
            if (__slot_extra_info is None):

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568710584912
                __attrs_140568710584912 = _static_140568781866176

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568710581984
                __default_140568710581984 = _DEFAULT_MARKER

                # <Value 'nothing' (95:65)> -> __cache_140568710582752
                __token = 3323
                try:
                    __zt_tmp = __attrs_140568710584912
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140568710582752 = _static_140568781877504('path', 'nothing', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                # <BinOp left=<Value 'nothing' (95:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8b40f95d0> -> __condition
                __expression = __cache_140568710582752

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>\n                </div>')
                else:
                    __content = __cache_140568710582752
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            else:
                __slot_extra_info(__stream, econtext.copy(), rcontext)
            __append('\n\n                ')

            # <Static value=<ast.Dict object at 0x7fd8bd1438e0> name=None at 7fd8bd143fd0> -> __attrs_140568623730928
            __attrs_140568623730928 = _static_140568861882592

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset class="mb-4">\n                    ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623728336
            __attrs_140568623728336 = _static_140568781866176
            __backup_form_name_140568625351792 = get('form_name', __marker)

            # <Value 'view/form_name|nothing' (99:50)> -> __value
            __token = 3447
            try:
                __zt_tmp = __attrs_140568623728336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140568781877504('path', 'view/form_name|nothing', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            econtext['form_name'] = __value

            # <Value 'form_name' (100:43)> -> __condition
            __token = 3514
            try:
                __zt_tmp = __attrs_140568623728336
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140568781877504('path', 'form_name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            if __condition:

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568623727520
                __default_140568623727520 = _DEFAULT_MARKER

                # <Value 'form_name' (101:41)> -> __cache_140568623726944
                __token = 3566
                try:
                    __zt_tmp = __attrs_140568623728336
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140568623726944 = _static_140568781877504('path', 'form_name', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                # <BinOp left=<Value 'form_name' (101:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aee241c0> -> __condition
                __expression = __cache_140568623726944

                # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Form name')
                else:
                    __content = __cache_140568623726944
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</legend>')
            if (__backup_form_name_140568625351792 is __marker):
                del econtext['form_name']
            else:
                econtext['form_name'] = __backup_form_name_140568625351792
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623729536
            __attrs_140568623729536 = _static_140568781866176

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n                        ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623732224
            __attrs_140568623732224 = _static_140568781866176

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_140568623731744 = []
            __append_140568623731744 = __stream_140568623731744.append
            __append_140568623731744('Database name:')
            __msgid_140568623731744 = __re_whitespace(''.join(__stream_140568623731744)).strip()
            if 'text_zope_database_name':
                __append(translate('text_zope_database_name', mapping=None, default=__msgid_140568623731744, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong> ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623733328
            __attrs_140568623733328 = _static_140568781866176

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568623740768
            __default_140568623740768 = _DEFAULT_MARKER

            # <Value 'view/dbName' (104:116)> -> __cache_140568623742208
            __token = 3737
            try:
                __zt_tmp = __attrs_140568623733328
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140568623742208 = _static_140568781877504('path', 'view/dbName', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/dbName' (104:116)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aee27850> -> __condition
            __expression = __cache_140568623742208

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span />')
            else:
                __content = __cache_140568623742208
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n                    </p>\n\n                    ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623740480
            __attrs_140568623740480 = _static_140568781866176

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_140568623584352_size = ''
            __stream_140568623737744 = []
            __append_140568623737744 = __stream_140568623737744.append
            __append_140568623737744('\n                        ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623737312
            __attrs_140568623737312 = _static_140568781866176

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append_140568623737744('<strong>Current database size:</strong> ')
            __stream_140568623584352_size = []
            __append_140568623584352_size = __stream_140568623584352_size.append

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623739856
            __attrs_140568623739856 = _static_140568781866176

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568623742304
            __default_140568623742304 = _DEFAULT_MARKER

            # <Value 'view/dbSize' (108:100)> -> __cache_140568623738800
            __token = 3944
            try:
                __zt_tmp = __attrs_140568623739856
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140568623738800 = _static_140568781877504('path', 'view/dbSize', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/dbSize' (108:100)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aee27b80> -> __condition
            __expression = __cache_140568623738800

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140568623584352_size('<span />')
            else:
                __content = __cache_140568623738800
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_140568623584352_size(__content)
            __append_140568623737744('${size}')
            __stream_140568623584352_size = ''.join(__stream_140568623584352_size)
            __append_140568623737744('\n                    ')
            __msgid_140568623737744 = __re_whitespace(''.join(__stream_140568623737744)).strip()
            if 'text_zope_database_size':
                __append(translate('text_zope_database_size', mapping={'size': __stream_140568623584352_size, }, default=__msgid_140568623737744, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n                    ')
            __token = None
            render_widget_rendering(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n                    ')
            if (__slot_above_buttons is None):

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623738128
                __attrs_140568623738128 = _static_140568781866176
            else:
                __slot_above_buttons(__stream, econtext.copy(), rcontext)
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x7fd8aefab280> name=None at 7fd8aee26e60> -> __attrs_140568625328672
            __attrs_140568625328672 = _static_140568625328768

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="visualClear"><!-- --></div>\n\n                    ')

            # <Static value=<ast.Dict object at 0x7fd8aefabe20> name=None at 7fd8aefa9a50> -> __attrs_140568625330400
            __attrs_140568625330400 = _static_140568625331744

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="actionsView" class="formControls">\n                        ')

            # <Static value=<ast.Dict object at 0x7fd8aefa80a0> name=None at 7fd8aefa8070> -> __attrs_140568625316288
            __attrs_140568625316288 = _static_140568625316000

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="actionButtons">\n                            ')

            # <Static value=<ast.Dict object at 0x7fd8aefab850> name=None at 7fd8aefab3d0> -> __attrs_140568625325360
            __attrs_140568625325360 = _static_140568625330256

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit" id="form.buttons.pack" name="form.buttons.pack" value="Pack" class="btn btn-danger">\n                                ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625329968
            __attrs_140568625329968 = _static_140568781866176

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_140568625329488 = []
            __append_140568625329488 = __stream_140568625329488.append
            __append_140568625329488('Pack')
            __msgid_140568625329488 = __re_whitespace(''.join(__stream_140568625329488)).strip()
            if __msgid_140568625329488:
                __append(translate(__msgid_140568625329488, mapping=None, default=__msgid_140568625329488, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n                        </span>\n                    </div>\n\n                </fieldset>\n\n                ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625323440
            __attrs_140568625323440 = _static_140568781866176

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568625323536
            __default_140568625323536 = _DEFAULT_MARKER

            # <Value 'context/@@authenticator/authenticator' (138:46)> -> __cache_140568625324112
            __token = 5260
            try:
                __zt_tmp = __attrs_140568625323440
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140568625324112 = _static_140568781877504('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/@@authenticator/authenticator' (138:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aefa9f90> -> __condition
            __expression = __cache_140568625324112

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input />')
            else:
                __content = __cache_140568625324112
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n            </form>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_widget_rendering(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_field = econtext['__slot_field'].pop()
        except:
            __slot_field = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623729920
            __attrs_140568623729920 = _static_140568781866176
            __append('\n                        ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568623737984
            __attrs_140568623737984 = _static_140568781866176
            __backup_widget_140568625348864 = get('widget', __marker)

            # <Value 'view/widgets/values' (112:52)> -> __iterator
            __token = 4105
            try:
                __zt_tmp = __attrs_140568623737984
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140568781877504('path', 'view/widgets/values', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            (__iterator, ____index_140568625324880, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n                            ')
                if (__slot_field is None):

                    # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625325072
                    __attrs_140568625325072 = _static_140568781866176
                    __append('\n                                ')
                    __token = None
                    render_field(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n                            ')
                else:
                    __slot_field(__stream, econtext.copy(), rcontext)
                __append('\n                        ')
                ____index_140568625324880 -= 1
                if (____index_140568625324880 > 0):
                    __append('')
            if (__backup_widget_140568625348864 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140568625348864
            __append('\n                    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_field(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625322336
            __attrs_140568625322336 = _static_140568781866176
            __append('\n                                    ')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568625326128
            __attrs_140568625326128 = _static_140568781866176

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568625326416
            __default_140568625326416 = _DEFAULT_MARKER

            # <Value 'widget/@@ploneform-render-widget' (115:71)> -> __cache_140568625327280
            __token = 4332
            try:
                __zt_tmp = __attrs_140568625326128
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140568625327280 = _static_140568781877504('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

            # <BinOp left=<Value 'widget/@@ploneform-render-widget' (115:71)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aefaaa10> -> __condition
            __expression = __cache_140568625327280

            # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140568625327280
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n                                ')
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
            __append('<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568711027088
            __attrs_140568711027088 = _static_140568781866176
            __previous_i18n_domain_140568711031072 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140568621252288 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd8b4165a80> name=None at 7fd8b4166620> -> __value
            __value = _static_140568711027328
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568711021184
                __attrs_140568711021184 = _static_140568781866176
                __append('\n\n    ')
                __token = None
                render_form(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7fd8b84f44c0> name=None at 7fd8b84f47f0> -> __attrs_140568624994944
                __attrs_140568624994944 = _static_140568781866176

                # <Value 'not: view/available' (151:32)> -> __condition
                __token = 5602
                try:
                    __zt_tmp = __attrs_140568624994944
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140568781877504('not', ' view/available', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                if __condition:
                    __append('\n         ')

                    # <Static value=<ast.Dict object at 0x7fd8aef68850> name=None at 7fd8aef699c0> -> __attrs_140568625056832
                    __attrs_140568625056832 = _static_140568625055824

                    # <Value 'view/label' (154:28)> -> __condition
                    __token = 5725
                    try:
                        __zt_tmp = __attrs_140568625056832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140568781877504('path', 'view/label', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                    if __condition:

                        # <h1 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h1 class="documentFirstHeading">')

                        # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568625060000
                        __default_140568625060000 = _DEFAULT_MARKER

                        # <Value 'view/label' (155:26)> -> __cache_140568625002720
                        __token = 5763
                        try:
                            __zt_tmp = __attrs_140568625056832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140568625002720 = _static_140568781877504('path', 'view/label', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))

                        # <BinOp left=<Value 'view/label' (155:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd8b8676aa0> at 7fd8aef5bd00> -> __condition
                        __expression = __cache_140568625002720

                        # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n             Do something\n         ')
                        else:
                            __content = __cache_140568625002720
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</h1>')
                    __append('\n\n         ')

                    # <Static value=<ast.Dict object at 0x7fd8aef69720> name=None at 7fd8aef69b70> -> __attrs_140568625059328
                    __attrs_140568625059328 = _static_140568625059616

                    # <Value 'view/description' (160:27)> -> __condition
                    __token = 5935
                    try:
                        __zt_tmp = __attrs_140568625059328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140568781877504('path', 'view/description', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="documentDescription">')
                        __stream_140568625060624 = []
                        __append_140568625060624 = __stream_140568625060624.append
                        __append_140568625060624('\n             You are not allowed to manage the Zope server.\n         ')
                        __msgid_140568625060624 = __re_whitespace(''.join(__stream_140568625060624)).strip()
                        if 'text_not_allowed_manage_server':
                            __append(translate('text_not_allowed_manage_server', mapping=None, default=__msgid_140568625060624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>')
                    __append('\n\n         ')

                    # <Static value=<ast.Dict object at 0x7fd8aef6b1c0> name=None at 7fd8aef6b190> -> __attrs_140568625069696
                    __attrs_140568625069696 = _static_140568625066432

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n             ')

                    # <Static value=<ast.Dict object at 0x7fd8aef6a6e0> name=None at 7fd8aef6aaa0> -> __attrs_140568625063264
                    __attrs_140568625063264 = _static_140568625063648

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fd8b8676aa0> -> __default_140568625064176
                    __default_140568625064176 = _DEFAULT_MARKER

                    # <Substitution 'string:$portal_url/@@overview-controlpanel' (167:37)> -> __attr_href
                    __token = 6161
                    try:
                        __zt_tmp = __attrs_140568625063264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140568781877504('string', '$portal_url/@@overview-controlpanel', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' class="link-parent">')
                    __stream_140568625064896 = []
                    __append_140568625064896 = __stream_140568625064896.append
                    __append_140568625064896('\n                 Up to Site Setup\n             ')
                    __msgid_140568625064896 = __re_whitespace(''.join(__stream_140568625064896)).strip()
                    if 'label_up_to_plone_setup':
                        __append(translate('label_up_to_plone_setup', mapping=None, default=__msgid_140568625064896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n         </div>\n    ')
                __append('\n\n\n')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (7:23)> -> __macro
            __token = 277
            try:
                __zt_tmp = __attrs_140568711027088
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140568781877504('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_140568781877216(econtext, __zt_tmp))
            __token = 277
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140568621252288 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140568621252288
            __i18n_domain = __previous_i18n_domain_140568711031072
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_form': render_form, 'render_header': render_header, 'render_master': render_master, 'render_widget_rendering': render_widget_rendering, 'render_field': render_field, 'render': render, }