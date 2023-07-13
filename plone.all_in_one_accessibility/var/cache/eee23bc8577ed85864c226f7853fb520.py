# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.volto-4.0.9-py3.10.egg/plone/volto/browser/voltobackendwarning.pt'

__tokens = {33: ('nocall: context/@@iconresolver', 1, 33), 253: ("python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", 6, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882238269312 = {'href': 'https://6.docs.plone.org/volto/index.html', }
_static_139882205472576 = {'href': 'https://6.docs.plone.org/install/install-from-packages.html', }
_static_139882241554080 = {'class': 'content', }
_static_139882241553648 = {'class': 'portalMessage statusmessage statusmessage-warning alert alert-warning', 'role': 'alert', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882337226896 = {}

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

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241546544
            __attrs_139882241546544 = _static_139882337226896
            __backup_icons_139882101469152 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_139882241546544
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('nocall', ' context/@@iconresolver', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_139882241541840 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38df5174f0> name=None at 7f38df517730> -> __attrs_139882241552304
            __attrs_139882241552304 = _static_139882241553648

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="portalMessage statusmessage statusmessage-warning alert alert-warning" role="alert">\n        ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241550384
            __attrs_139882241550384 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882241540832
            __default_139882241540832 = _DEFAULT_MARKER

            # <Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> -> __cache_139882241543232
            __token = 253
            try:
                __zt_tmp = __attrs_139882241550384
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882241543232 = _static_139882257081264('python', "icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df516b30> -> __condition
            __expression = __cache_139882241543232

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139882241543232
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241543472
            __attrs_139882241543472 = _static_139882337226896

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_139882241555808 = []
            __append_139882241555808 = __stream_139882241555808.append
            __append_139882241555808('Warning')
            __msgid_139882241555808 = __re_whitespace(''.join(__stream_139882241555808)).strip()
            if __msgid_139882241555808:
                __append(translate(__msgid_139882241555808, mapping=None, default=__msgid_139882241555808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>:\n        ')

            # <Static value=<ast.Dict object at 0x7f38df5176a0> name=None at 7f38df516020> -> __attrs_139882241555952
            __attrs_139882241555952 = _static_139882241554080

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="content">\n            ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241547360
            __attrs_139882241547360 = _static_139882337226896
            __stream_139882241540736 = []
            __append_139882241540736 = __stream_139882241540736.append
            __append_139882241540736('You have accessed the Plone backend through its Classic UI frontend.')
            __msgid_139882241540736 = __re_whitespace(''.join(__stream_139882241540736)).strip()
            if 'volto_backend_warning':
                __append(translate('volto_backend_warning', mapping=None, default=__msgid_139882241540736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241551680
            __attrs_139882241551680 = _static_139882337226896

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241551968
            __attrs_139882241551968 = _static_139882337226896

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241553504
            __attrs_139882241553504 = _static_139882337226896
            __stream_139882241544624 = []
            __append_139882241544624 = __stream_139882241544624.append
            __append_139882241544624("If you want to use Plone's new frontend Volto instead:\n              ")

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241540544
            __attrs_139882241540544 = _static_139882337226896

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_139882241544624('<ul>\n                ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882208067440
            __attrs_139882208067440 = _static_139882337226896

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_139882241544624('<li>Install Volto, if not already installed.</li>\n                ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882210804112
            __attrs_139882210804112 = _static_139882337226896

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_139882241544624('<li>Start Volto, if not already started.</li>\n                ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206472096
            __attrs_139882206472096 = _static_139882337226896

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_139882241544624('<li>Visit the Volto frontend.</li>\n              </ul>\n              For more information, please read the documentation for how to\n              ')

            # <Static value=<ast.Dict object at 0x7f38dd2ae740> name=None at 7f38dd2ae2c0> -> __attrs_139882209747648
            __attrs_139882209747648 = _static_139882205472576

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139882241544624('<a href="https://6.docs.plone.org/install/install-from-packages.html">Install Plone from its packages</a>\n              and refer to the full Volto documentation\n              ')

            # <Static value=<ast.Dict object at 0x7f38df1f5780> name=None at 7f38df1f5360> -> __attrs_139882205849936
            __attrs_139882205849936 = _static_139882238269312

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139882241544624('<a href="https://6.docs.plone.org/volto/index.html">Frontend</a>.')
            __msgid_139882241544624 = __re_whitespace(''.join(__stream_139882241544624)).strip()
            if 'volto_backend_warning_link':
                __append(translate('volto_backend_warning_link', mapping=None, default=__msgid_139882241544624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n        </span>\n    </div>\n\n')
            __i18n_domain = __previous_i18n_domain_139882241541840
            if (__backup_icons_139882101469152 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139882101469152
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }