# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/basic_error_message.pt'

__tokens = {293: ('python:view.is_manager()', 8, 27), 352: ('not:isManager', 11, 24), 423: ('isManager', 12, 24), 434: ('${options/error_type}', 12, 35), 436: ('options/error_type', 12, 37), 694: ('isManager', 23, 21), 705: ('${options/error_type}', 23, 32), 707: ('options/error_type', 23, 34), 755: ('isManager', 25, 22), 786: ('options/error_tb', 26, 20), 834: ('not:isManager', 28, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139839041998128 = {'class': 'documentFirstHeading', }
_static_139839041995200 = {'class': 'documentFirstHeading', }
_static_139839140398752 = __C2ZContextWrapper
_static_139839140402352 = __compile_zt_expr
_static_139839134773072 = {}
_static_139839042005232 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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

            # <Static value=<ast.Dict object at 0x7f2ed06ca8f0> name=None at 7f2ed06c8400> -> __attrs_139839042006912
            __attrs_139839042006912 = _static_139839042005232
            __previous_i18n_domain_139839042004416 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042007488
            __attrs_139839042007488 = _static_139839134773072
            __backup_isManager_139839041905680 = get('isManager', __marker)

            # <Value 'python:view.is_manager()' (8:27)> -> __value
            __token = 293
            try:
                __zt_tmp = __attrs_139839042007488
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', 'view.is_manager()', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['isManager'] = __value
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042003120
            __attrs_139839042003120 = _static_139839134773072

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042003408
            __attrs_139839042003408 = _static_139839134773072

            # <Value 'not:isManager' (11:24)> -> __condition
            __token = 352
            try:
                __zt_tmp = __attrs_139839042003408
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('not', 'isManager', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <title ... (0:0)
                # --------------------------------------------------------
                __append('<title>')
                __stream_139839041998368 = []
                __append_139839041998368 = __stream_139839041998368.append
                __append_139839041998368('Error')
                __msgid_139839041998368 = __re_whitespace(''.join(__stream_139839041998368)).strip()
                if __msgid_139839041998368:
                    __append(translate(__msgid_139839041998368, mapping=None, default=__msgid_139839041998368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</title>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042003360
            __attrs_139839042003360 = _static_139839134773072

            # <Value 'isManager' (12:24)> -> __condition
            __token = 423
            try:
                __zt_tmp = __attrs_139839042003360
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('path', 'isManager', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <title ... (0:0)
                # --------------------------------------------------------
                __append('<title>')

                # <Interpolation value=<Substitution '${options/error_type}' (12:35)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed06ca950> -> __content_139839220113136
                __token = 434
                __token = 436
                try:
                    __zt_tmp = __attrs_139839042003360
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_139839220113136 = _static_139839140402352('path', 'options/error_type', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                __content_139839220113136 = __quote(__content_139839220113136, '\x00', '&#0;', None, None)
                __content_139839220113136 = __content_139839220113136
                if (__content_139839220113136 is None):
                    pass
                else:
                    if (__content_139839220113136 is None):
                        __content_139839220113136 = None
                    else:
                        __tt = type(__content_139839220113136)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139839220113136 = str(__content_139839220113136)
                        else:
                            if (__tt is bytes):
                                __content_139839220113136 = decode(__content_139839220113136)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139839220113136 = __content_139839220113136.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139839220113136)
                                        __content_139839220113136 = (str(__content_139839220113136) if (__content_139839220113136 is __converted) else __converted)
                                    else:
                                        __content_139839220113136 = __content_139839220113136()
                if (__content_139839220113136 is not None):
                    __append(__content_139839220113136)
                __append('</title>')
            __append('\n</head>\n\n')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042000672
            __attrs_139839042000672 = _static_139839134773072

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed06c81c0> name=None at 7f2ed06c9360> -> __attrs_139839042000336
            __attrs_139839042000336 = _static_139839041995200

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading">')
            __stream_139839041995920 = []
            __append_139839041995920 = __stream_139839041995920.append
            __append_139839041995920('\n      We&#8217;re sorry, but there seems to be an error&hellip;\n  ')
            __msgid_139839041995920 = __re_whitespace(''.join(__stream_139839041995920)).strip()
            if 'heading_site_error_sorry':
                __append(translate('heading_site_error_sorry', mapping=None, default=__msgid_139839041995920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed06c8d30> name=None at 7f2ed06c9090> -> __attrs_139839041996256
            __attrs_139839041996256 = _static_139839041998128

            # <Value 'isManager' (23:21)> -> __condition
            __token = 694
            try:
                __zt_tmp = __attrs_139839041996256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('path', 'isManager', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2 class="documentFirstHeading">')

                # <Interpolation value=<Substitution '${options/error_type}' (23:32)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2ed06c8670> -> __content_139839220113136
                __token = 705
                __token = 707
                try:
                    __zt_tmp = __attrs_139839041996256
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_139839220113136 = _static_139839140402352('path', 'options/error_type', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                __content_139839220113136 = __quote(__content_139839220113136, '\x00', '&#0;', None, None)
                __content_139839220113136 = __content_139839220113136
                if (__content_139839220113136 is None):
                    pass
                else:
                    if (__content_139839220113136 is None):
                        __content_139839220113136 = None
                    else:
                        __tt = type(__content_139839220113136)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139839220113136 = str(__content_139839220113136)
                        else:
                            if (__tt is bytes):
                                __content_139839220113136 = decode(__content_139839220113136)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139839220113136 = __content_139839220113136.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139839220113136)
                                        __content_139839220113136 = (str(__content_139839220113136) if (__content_139839220113136 is __converted) else __converted)
                                    else:
                                        __content_139839220113136 = __content_139839220113136()
                if (__content_139839220113136 is not None):
                    __append(__content_139839220113136)
                __append('</h2>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042632720
            __attrs_139839042632720 = _static_139839134773072

            # <Value 'isManager' (25:22)> -> __condition
            __token = 755
            try:
                __zt_tmp = __attrs_139839042632720
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('path', 'isManager', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:

                # <pre ... (0:0)
                # --------------------------------------------------------
                __append('<pre>')

                # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839041995248
                __default_139839041995248 = _DEFAULT_MARKER

                # <Value 'options/error_tb' (26:20)> -> __cache_139839042000384
                __token = 786
                try:
                    __zt_tmp = __attrs_139839042632720
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139839042000384 = _static_139839140402352('path', 'options/error_tb', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                # <BinOp left=<Value 'options/error_tb' (26:20)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed06ca530> -> __condition
                __expression = __cache_139839042000384

                # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139839042000384
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</pre>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042619088
            __attrs_139839042619088 = _static_139839134773072

            # <Value 'not:isManager' (28:26)> -> __condition
            __token = 834
            try:
                __zt_tmp = __attrs_139839042619088
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139839140402352('not', 'isManager', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042618704
                __attrs_139839042618704 = _static_139839134773072

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_139839041851616_site_admin = ''
                __stream_139839042620336 = []
                __append_139839042620336 = __stream_139839042620336.append
                __append_139839042620336('\n      If you are certain you have the correct web address but are encountering an error, please\n      contact the ')
                __stream_139839041851616_site_admin = []
                __append_139839041851616_site_admin = __stream_139839041851616_site_admin.append

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042621584
                __attrs_139839042621584 = _static_139839134773072

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_139839041851616_site_admin('<span>')
                __stream_139839042621440 = []
                __append_139839042621440 = __stream_139839042621440.append
                __append_139839042621440('site administration')
                __msgid_139839042621440 = __re_whitespace(''.join(__stream_139839042621440)).strip()
                if 'label_site_admin':
                    __append_139839041851616_site_admin(translate('label_site_admin', mapping=None, default=__msgid_139839042621440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_139839041851616_site_admin('</span>')
                __append_139839042620336('${site_admin}')
                __stream_139839041851616_site_admin = ''.join(__stream_139839041851616_site_admin)
                __append_139839042620336('.\n      ')
                __msgid_139839042620336 = __re_whitespace(''.join(__stream_139839042620336)).strip()
                if 'description_site_error_mail_site_admin':
                    __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_139839041851616_site_admin, }, default=__msgid_139839042620336, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  ')
            __append('\n\n</body>\n')
            if (__backup_isManager_139839041905680 is __marker):
                del econtext['isManager']
            else:
                econtext['isManager'] = __backup_isManager_139839041905680
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_139839042004416
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }