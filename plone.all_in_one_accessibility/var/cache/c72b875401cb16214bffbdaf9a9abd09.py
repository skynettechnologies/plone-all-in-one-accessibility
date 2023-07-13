# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.volto-4.0.9-py3.10.egg/plone/volto/browser/voltobackendwarning.pt'

__tokens = {33: ('nocall: context/@@iconresolver', 1, 33), 253: ("python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", 6, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272719216 = {'href': 'https://6.docs.plone.org/volto/index.html', }
_static_140310272301312 = {'href': 'https://6.docs.plone.org/install/install-from-packages.html', }
_static_140310272306688 = {'class': 'content', }
_static_140310475412464 = {'class': 'portalMessage statusmessage statusmessage-warning alert alert-warning', 'role': 'alert', }
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475407952
            __attrs_140310475407952 = _static_140310566789392
            __backup_icons_140310272280656 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_140310475407952
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('nocall', ' context/@@iconresolver', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_140310475412176 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f9c940b93f0> name=None at 7f9c940b94e0> -> __attrs_140310272296608
            __attrs_140310272296608 = _static_140310475412464

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="portalMessage statusmessage statusmessage-warning alert alert-warning" role="alert">\n        ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272307936
            __attrs_140310272307936 = _static_140310566789392

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272305392
            __default_140310272305392 = _DEFAULT_MARKER

            # <Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> -> __cache_140310272301840
            __token = 253
            try:
                __zt_tmp = __attrs_140310272307936
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140310272301840 = _static_140310567013776('python', "icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

            # <BinOp left=<Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f04fd0> -> __condition
            __expression = __cache_140310272301840

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140310272301840
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272310576
            __attrs_140310272310576 = _static_140310566789392

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_140310272304192 = []
            __append_140310272304192 = __stream_140310272304192.append
            __append_140310272304192('Warning')
            __msgid_140310272304192 = __re_whitespace(''.join(__stream_140310272304192)).strip()
            if __msgid_140310272304192:
                __append(translate(__msgid_140310272304192, mapping=None, default=__msgid_140310272304192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>:\n        ')

            # <Static value=<ast.Dict object at 0x7f9c87f06e00> name=None at 7f9c87f047f0> -> __attrs_140310272299632
            __attrs_140310272299632 = _static_140310272306688

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="content">\n            ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272300208
            __attrs_140310272300208 = _static_140310566789392
            __stream_140310272302656 = []
            __append_140310272302656 = __stream_140310272302656.append
            __append_140310272302656('You have accessed the Plone backend through its Classic UI frontend.')
            __msgid_140310272302656 = __re_whitespace(''.join(__stream_140310272302656)).strip()
            if 'volto_backend_warning':
                __append(translate('volto_backend_warning', mapping=None, default=__msgid_140310272302656, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272308608
            __attrs_140310272308608 = _static_140310566789392

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272305872
            __attrs_140310272305872 = _static_140310566789392

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272304768
            __attrs_140310272304768 = _static_140310566789392
            __stream_140310272299968 = []
            __append_140310272299968 = __stream_140310272299968.append
            __append_140310272299968("If you want to use Plone's new frontend Volto instead:\n              ")

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272307216
            __attrs_140310272307216 = _static_140310566789392

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_140310272299968('<ul>\n                ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272297280
            __attrs_140310272297280 = _static_140310566789392

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140310272299968('<li>Install Volto, if not already installed.</li>\n                ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272298048
            __attrs_140310272298048 = _static_140310566789392

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140310272299968('<li>Start Volto, if not already started.</li>\n                ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272299824
            __attrs_140310272299824 = _static_140310566789392

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140310272299968('<li>Visit the Volto frontend.</li>\n              </ul>\n              For more information, please read the documentation for how to\n              ')

            # <Static value=<ast.Dict object at 0x7f9c87f05900> name=None at 7f9c87f045e0> -> __attrs_140310272298432
            __attrs_140310272298432 = _static_140310272301312

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140310272299968('<a href="https://6.docs.plone.org/install/install-from-packages.html">Install Plone from its packages</a>\n              and refer to the full Volto documentation\n              ')

            # <Static value=<ast.Dict object at 0x7f9c87f6b970> name=None at 7f9c87f687c0> -> __attrs_140310272713648
            __attrs_140310272713648 = _static_140310272719216

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140310272299968('<a href="https://6.docs.plone.org/volto/index.html">Frontend</a>.')
            __msgid_140310272299968 = __re_whitespace(''.join(__stream_140310272299968)).strip()
            if 'volto_backend_warning_link':
                __append(translate('volto_backend_warning_link', mapping=None, default=__msgid_140310272299968, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n        </span>\n    </div>\n\n')
            __i18n_domain = __previous_i18n_domain_140310475412176
            if (__backup_icons_140310272280656 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140310272280656
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }