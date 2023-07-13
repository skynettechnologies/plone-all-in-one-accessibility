# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/login/templates/logged_out.pt'

__tokens = {402: ("python:request.set('disable_border',1)", 10, 35), 489: (" python:request.set('disable_plone.leftcolumn',1", 11, 47), 586: ("o python:request.set('disable_plone.rightcolumn',", 12, 46), 1204: ('string:${portal_url}/@@plone-root-logout', 30, 36), 255: ('context/@@main_template/macros/master', 5, 23), 255: ('context/@@main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_139856821593440 = {'href': 'string:${portal_url}/@@plone-root-logout', }
_static_139856821594496 = {'id': 'content-core', }
_static_139856821588208 = {'class': 'documentDescription', }
_static_139856821588784 = {'class': 'documentFirstHeading', }
_static_139856914195856 = __C2ZContextWrapper
_static_139856914196144 = __compile_zt_expr
_static_139856825689584 = 'master'
_static_139856913889840 = {}

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

            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820451648
            __attrs_139856820451648 = _static_139856913889840
            __previous_i18n_domain_139856820449392 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139856821304128 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f32f46a25f0> name=None at 7f32f4317070> -> __value
            __value = _static_139856825689584
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821595552
                __attrs_139856821595552 = _static_139856913889840
                __backup_dummy_139856820724224 = get('dummy', __marker)

                # <Value "python:request.set('disable_border',1)" (10:35)> -> __value
                __token = 402
                try:
                    __zt_tmp = __attrs_139856821595552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('python', "request.set('disable_border',1)", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_139856821791200 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (11:47)> -> __value
                __token = 489
                try:
                    __zt_tmp = __attrs_139856821595552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_139856820446896 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (12:46)> -> __value
                __token = 586
                try:
                    __zt_tmp = __attrs_139856821595552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_139856820446896 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_139856820446896
                if (__backup_disable_column_one_139856821791200 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_139856821791200
                if (__backup_dummy_139856820724224 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_139856820724224
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821600016
                __attrs_139856821600016 = _static_139856913889840
                __append('\n\n')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821589840
                __attrs_139856821589840 = _static_139856913889840
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f32f42b9330> name=None at 7f32f42b9ae0> -> __attrs_139856821589456
                __attrs_139856821589456 = _static_139856821588784

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_139856821589984 = []
                __append_139856821589984 = __stream_139856821589984.append
                __append_139856821589984('Still logged in as a Zope user')
                __msgid_139856821589984 = __re_whitespace(''.join(__stream_139856821589984)).strip()
                if 'heading_quit_to_log_out':
                    __append(translate('heading_quit_to_log_out', mapping=None, default=__msgid_139856821589984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f32f42b90f0> name=None at 7f32f42bace0> -> __attrs_139856821599056
                __attrs_139856821599056 = _static_139856821588208

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentDescription">')
                __stream_139856821595408 = []
                __append_139856821595408 = __stream_139856821595408.append
                __append_139856821595408('\n        You are logged in via HTTP authentication (i.e. the Zope Management\n        Interface). In order to log out, you must:\n    ')
                __msgid_139856821595408 = __re_whitespace(''.join(__stream_139856821595408)).strip()
                if 'description_quit_to_log_out':
                    __append(translate('description_quit_to_log_out', mapping=None, default=__msgid_139856821595408, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f32f42ba980> name=None at 7f32f42b9c60> -> __attrs_139856821584704
                __attrs_139856821584704 = _static_139856821594496

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n        ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821591664
                __attrs_139856821591664 = _static_139856913889840

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_139856820058848_text_logged_out_link = ''
                __stream_139856821593680 = []
                __append_139856821593680 = __stream_139856821593680.append
                __append_139856821593680('\n            ')
                __stream_139856820058848_text_logged_out_link = []
                __append_139856820058848_text_logged_out_link = __stream_139856820058848_text_logged_out_link.append

                # <Static value=<ast.Dict object at 0x7f32f42ba560> name=None at 7f32f42bae30> -> __attrs_139856821595936
                __attrs_139856821595936 = _static_139856821593440

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_139856820058848_text_logged_out_link('<a')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821594112
                __default_139856821594112 = _DEFAULT_MARKER

                # <Substitution 'string:${portal_url}/@@plone-root-logout' (30:36)> -> __attr_href
                __token = 1204
                try:
                    __zt_tmp = __attrs_139856821595936
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139856914196144('string', '${portal_url}/@@plone-root-logout', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append_139856820058848_text_logged_out_link((' href="%s"' % __attr_href))
                __append_139856820058848_text_logged_out_link('>')
                __stream_139856821589648 = []
                __append_139856821589648 = __stream_139856821589648.append
                __append_139856821589648('\n                Visit this link\n            ')
                __msgid_139856821589648 = __re_whitespace(''.join(__stream_139856821589648)).strip()
                if __msgid_139856821589648:
                    __append_139856820058848_text_logged_out_link(translate(__msgid_139856821589648, mapping=None, default=__msgid_139856821589648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_139856820058848_text_logged_out_link('</a>')
                __append_139856821593680('${text_logged_out_link}')
                __stream_139856820058848_text_logged_out_link = ''.join(__stream_139856820058848_text_logged_out_link)
                __append_139856821593680("\n            and click 'Cancel' when prompted with an authentication prompt.\n        ")
                __msgid_139856821593680 = __re_whitespace(''.join(__stream_139856821593680)).strip()
                if __msgid_139856821593680:
                    __append(translate(__msgid_139856821593680, mapping={'text_logged_out_link': __stream_139856820058848_text_logged_out_link, }, default=__msgid_139856821593680, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n    </div>\n\n\n')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'context/@@main_template/macros/master' (5:23)> -> __macro
            __token = 255
            try:
                __zt_tmp = __attrs_139856820451648
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139856914196144('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __token = 255
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139856821304128 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139856821304128
            __i18n_domain = __previous_i18n_domain_139856820449392
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }