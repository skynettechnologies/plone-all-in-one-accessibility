# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/main_template.pt'

__tokens = {71: ('string:&lt;!DOCTYPE ht', 2, 36), 344: ("python:context.restrictedTraverse('@@plone_portal_state')", 8, 31), 426: (" python:context.restrictedTraverse('@@plone_context_state'", 9, 23), 506: ("w python:context.restrictedTraverse('@@plone", 10, 19), 567: ("ns python:context.restrictedTraverse('@@iconresolve", 11, 13), 642: ("out python:context.restrictedTraverse('@@plone_layo", 12, 19), 709: ('lang python:portal_state.langu', 13, 10), 755: (' view nocall:view | nocall: plon', 14, 9), 804: (' dummy python: plone_layout.mark_vie', 15, 9), 862: ('tal_url python:portal_state.port', 16, 13), 921: ("rmission python:context.restrictedTraverse('portal_membership').checkP", 17, 17), 1018: ("roperties python:context.restrictedTraverse('portal_properties').site_", 18, 16), 1117: ("clude_head python:request.get('ajax_include_he", 19, 17), 1184: ('  ajax_load ', 20, 8), 1264: ('lang', 22, 27), 1313: ('provider:plone.httpheaders', 24, 40), 1416: ('provider:plone.htmlhead', 29, 32), 1471: ('nothing', 31, 26), 1757: ('provider:plone.scripts', 38, 32), 1882: ('provider:plone.htmlhead.links', 41, 33), 2021: ('portal_state/is_rtl', 46, 26), 2064: (" python:plone_layout.have_portlets('plone.leftcolumn', view", 47, 22), 2147: ("r python:plone_layout.have_portlets('plone.rightcolumn', vie", 48, 21), 2239: ('ss python:plone_layout.bodyClass(template, vi', 49, 28), 2415: ("  python:context.restrictedTraverse('@@plone_patterns_settings')", 52, 22), 2320: ('body_class', 50, 30), 2359: (" python:isRTL and 'rtl' or 'ltr", 51, 27), 2553: ('provider:plone.toolbar', 55, 32), 2664: ('provider:plone.portaltop', 58, 34), 2760: ('provider:plone.portalheader', 60, 36), 2880: ('provider:plone.mainnavigation', 65, 59), 3032: ('provider:plone.globalstatusmessage', 70, 42), 3211: ('provider:plone.abovecontent', 75, 59), 5052: ('sl', 130, 26), 5150: ('provider:plone.leftcolumn', 132, 38), 5325: ('sr', 138, 26), 5423: ('provider:plone.rightcolumn', 140, 38), 5586: ('provider:plone.portalfooter', 145, 34), 3606: ('provider:plone.abovecontenttitle', 91, 77), 3747: ('context/@@title', 94, 45), 3876: ('provider:plone.belowcontenttitle', 97, 77), 4028: ('context/@@description', 100, 44), 4175: ('provider:plone.belowcontentdescription', 103, 83), 4318: ('provider:plone.abovecontentbody', 107, 74), 4461: ('nothing', 110, 68), 4630: ('provider:plone.belowcontentbody', 115, 74), 4787: ('provider:plone.belowcontent', 119, 69)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139839042148464 = {'id': 'viewlet-below-content', }
_static_139839042153984 = {'id': 'viewlet-below-content-body', }
_static_139839042367744 = {'id': 'content-core', }
_static_139839042370240 = {'id': 'viewlet-above-content-body', }
_static_139839042368800 = {'id': 'viewlet-below-content-description', }
_static_139839042359104 = {'id': 'viewlet-below-content-title', }
_static_139839042357520 = {'id': 'viewlet-above-content-title', }
_static_139839042279488 = {'id': 'content', }
_static_139839042157248 = {'id': 'portal-footer-wrapper', }
_static_139839042157920 = {'id': 'portal-column-two', }
_static_139839042277328 = {'id': 'portal-column-one', }
_static_139839042277280 = {'id': 'portal-column-content', }
_static_139839042284240 = {'id': 'viewlet-above-content', }
_static_139839042289568 = {'id': 'global_statusmessage', }
_static_139839042289280 = {'id': 'portal-mainnavigation', }
_static_139839042372752 = {'id': 'portal-header', }
_static_139839042378896 = {'id': 'portal-top', }
_static_139839042186224 = set([])
_static_139839042380096 = {'id': 'visual-portal-wrapper', 'class': 'body_class', 'dir': "python:isRTL and 'rtl' or 'ltr'", }
_static_139839042381296 = {'name': 'generator', 'content': 'Plone - https://plone.org/', }
_static_139839042103248 = {'charset': 'utf-8', }
_static_139839042105264 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'lang', }
_static_139839140398752 = __C2ZContextWrapper
_static_139839140402352 = __compile_zt_expr
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
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_column_two_slot = econtext['__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_javascript_head_slot = econtext['__slot_javascript_head_slot'].pop()
        except:
            __slot_javascript_head_slot = None

        try:
            __slot_portlets_one_slot = econtext['__slot_portlets_one_slot'].pop()
        except:
            __slot_portlets_one_slot = None

        try:
            __slot_global_statusmessage = econtext['__slot_global_statusmessage'].pop()
        except:
            __slot_global_statusmessage = None

        try:
            __slot_portlets_two_slot = econtext['__slot_portlets_two_slot'].pop()
        except:
            __slot_portlets_two_slot = None

        try:
            __slot_content = econtext['__slot_content'].pop()
        except:
            __slot_content = None

        try:
            __slot_column_one_slot = econtext['__slot_column_one_slot'].pop()
        except:
            __slot_column_one_slot = None

        try:
            __slot_head_slot = econtext['__slot_head_slot'].pop()
        except:
            __slot_head_slot = None

        try:
            __slot_style_slot = econtext['__slot_style_slot'].pop()
        except:
            __slot_style_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042099888
            __attrs_139839042099888 = _static_139839134773072
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042109344
            __attrs_139839042109344 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042099168
            __default_139839042099168 = _DEFAULT_MARKER

            # <Value 'string:<!DOCTYPE html>' (2:36)> -> __cache_139839042095184
            __token = 71
            try:
                __zt_tmp = __attrs_139839042109344
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042095184 = _static_139839140402352('string', '<!DOCTYPE html>', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'string:<!DOCTYPE html>' (2:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed06e15a0> -> __condition
            __expression = __cache_139839042095184

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139839042095184
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f2ed06e2fb0> name=None at 7f2ed06e3010> -> __attrs_139839042106272
            __attrs_139839042106272 = _static_139839042105264
            __backup_portal_state_139839042236576 = get('portal_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_portal_state')" (8:31)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_139839042232640 = get('context_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_context_state')" (9:23)> -> __value
            __token = 426
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_139839042359824 = get('plone_view', __marker)

            # <Value "python:context.restrictedTraverse('@@plone')" (10:19)> -> __value
            __token = 506
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "context.restrictedTraverse('@@plone')", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_icons_139839042232496 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (11:13)> -> __value
            __token = 567
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_plone_layout_139839041962912 = get('plone_layout', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_layout')" (12:19)> -> __value
            __token = 642
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_139839041808144 = get('lang', __marker)

            # <Value 'python:portal_state.language()' (13:10)> -> __value
            __token = 709
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', 'portal_state.language()', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_139839042232064 = get('view', __marker)

            # <Value 'nocall:view | nocall: plone_view' (14:9)> -> __value
            __token = 755
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('nocall', 'view | nocall: plone_view', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_139839043380960 = get('dummy', __marker)

            # <Value 'python: plone_layout.mark_view(view)' (15:9)> -> __value
            __token = 804
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', ' plone_layout.mark_view(view)', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_139839041717392 = get('portal_url', __marker)

            # <Value 'python:portal_state.portal_url()' (16:13)> -> __value
            __token = 862
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', 'portal_state.portal_url()', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_139839042105024 = get('checkPermission', __marker)

            # <Value "python:context.restrictedTraverse('portal_membership').checkPermission" (17:17)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_139839042107472 = get('site_properties', __marker)

            # <Value "python:context.restrictedTraverse('portal_properties').site_properties" (18:16)> -> __value
            __token = 1018
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_139839042106320 = get('ajax_include_head', __marker)

            # <Value "python:request.get('ajax_include_head', False)" (19:17)> -> __value
            __token = 1117
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "request.get('ajax_include_head', False)", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_139839042107376 = get('ajax_load', __marker)

            # <Value 'python:False' (20:8)> -> __value
            __token = 1184
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', 'False', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_139839042104352 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042108480
            __default_139839042108480 = _DEFAULT_MARKER

            # <Substitution 'lang' (22:27)> -> __attr_lang
            __token = 1264
            try:
                __zt_tmp = __attrs_139839042106272
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_139839140402352('path', 'lang', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042103968
            __attrs_139839042103968 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042101376
            __default_139839042101376 = _DEFAULT_MARKER

            # <Value 'provider:plone.httpheaders' (24:40)> -> __cache_139839042101712
            __token = 1313
            try:
                __zt_tmp = __attrs_139839042103968
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042101712 = _static_139839140402352('provider', 'plone.httpheaders', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.httpheaders' (24:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed06e20b0> -> __condition
            __expression = __cache_139839042101712

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139839042101712
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042104112
            __attrs_139839042104112 = _static_139839134773072

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed06e27d0> name=None at 7f2ed06e2860> -> __attrs_139839042100656
            __attrs_139839042100656 = _static_139839042103248

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042098400
            __attrs_139839042098400 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042106464
            __default_139839042106464 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead' (29:32)> -> __cache_139839042101040
            __token = 1416
            try:
                __zt_tmp = __attrs_139839042098400
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042101040 = _static_139839140402352('provider', 'plone.htmlhead', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead' (29:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed06e10f0> -> __condition
            __expression = __cache_139839042101040

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139839042101040
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042387056
            __attrs_139839042387056 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042387248
            __default_139839042387248 = _DEFAULT_MARKER

            # <Value 'nothing' (31:26)> -> __cache_139839042387728
            __token = 1471
            try:
                __zt_tmp = __attrs_139839042387056
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042387728 = _static_139839140402352('path', 'nothing', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'nothing' (31:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0727e50> -> __condition
            __expression = __cache_139839042387728

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_139839042387728
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_top_slot is None):

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042386624
                __attrs_139839042386624 = _static_139839134773072
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_head_slot is None):

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042386144
                __attrs_139839042386144 = _static_139839134773072
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_style_slot is None):

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042385664
                __attrs_139839042385664 = _static_139839134773072
            else:
                __slot_style_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042384368
            __attrs_139839042384368 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042384560
            __default_139839042384560 = _DEFAULT_MARKER

            # <Value 'provider:plone.scripts' (38:32)> -> __cache_139839042385040
            __token = 1757
            try:
                __zt_tmp = __attrs_139839042384368
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042385040 = _static_139839140402352('provider', 'plone.scripts', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.scripts' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed07273d0> -> __condition
            __expression = __cache_139839042385040

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139839042385040
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_javascript_head_slot is None):

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042383792
                __attrs_139839042383792 = _static_139839134773072
            else:
                __slot_javascript_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042382496
            __attrs_139839042382496 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042382688
            __default_139839042382688 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead.links' (41:33)> -> __cache_139839042383168
            __token = 1882
            try:
                __zt_tmp = __attrs_139839042382496
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042383168 = _static_139839140402352('provider', 'plone.htmlhead.links', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead.links' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0726c80> -> __condition
            __expression = __cache_139839042383168

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link />')
            else:
                __content = __cache_139839042383168
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed07265f0> name=None at 7f2ed07265c0> -> __attrs_139839042381200
            __attrs_139839042381200 = _static_139839042381296

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="generator" content="Plone - https://plone.org/" />\n\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f2ed0726140> name=None at 7f2ed0726110> -> __attrs_139839042377552
            __attrs_139839042377552 = _static_139839042380096
            __backup_isRTL_139839042105696 = get('isRTL', __marker)

            # <Value 'portal_state/is_rtl' (46:26)> -> __value
            __token = 2021
            try:
                __zt_tmp = __attrs_139839042377552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('path', 'portal_state/is_rtl', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_139839042106416 = get('sl', __marker)

            # <Value "python:plone_layout.have_portlets('plone.leftcolumn', view)" (47:22)> -> __value
            __token = 2064
            try:
                __zt_tmp = __attrs_139839042377552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_139839042106992 = get('sr', __marker)

            # <Value "python:plone_layout.have_portlets('plone.rightcolumn', view)" (48:21)> -> __value
            __token = 2147
            try:
                __zt_tmp = __attrs_139839042377552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', "plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_139839042097824 = get('body_class', __marker)

            # <Value 'python:plone_layout.bodyClass(template, view)' (49:28)> -> __value
            __token = 2239
            try:
                __zt_tmp = __attrs_139839042377552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139839140402352('python', 'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')

            # <Value "python:context.restrictedTraverse('@@plone_patterns_settings')()" (52:22)> -> __cache_139839042379616
            __token = 2415
            try:
                __zt_tmp = __attrs_139839042377552
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042379616 = _static_139839140402352('python', "context.restrictedTraverse('@@plone_patterns_settings')()", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            if ('id' not in __chain(__cache_139839042379616)):
                __append(' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042380720
            __default_139839042380720 = _DEFAULT_MARKER

            # <Substitution 'body_class' (50:30)> -> __attr_class
            __token = 2320
            try:
                __zt_tmp = __attrs_139839042377552
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139839140402352('path', 'body_class', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and ('class' not in __chain(__cache_139839042379616))):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042379808
            __default_139839042379808 = _DEFAULT_MARKER

            # <Substitution "python:isRTL and 'rtl' or 'ltr'" (51:27)> -> __attr_dir
            __token = 2359
            try:
                __zt_tmp = __attrs_139839042377552
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_139839140402352('python', "isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and ('dir' not in __chain(__cache_139839042379616))):
                __append((' dir="%s"' % __attr_dir))
            __attr_139839042379472 = __cache_139839042379616
            for (name, value, ) in __attr_139839042379472.items():
                if ((name not in _static_139839042186224) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042376208
            __attrs_139839042376208 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042376640
            __default_139839042376640 = _DEFAULT_MARKER

            # <Value 'provider:plone.toolbar' (55:32)> -> __cache_139839042376784
            __token = 2553
            try:
                __zt_tmp = __attrs_139839042376208
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042376784 = _static_139839140402352('provider', 'plone.toolbar', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.toolbar' (55:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0725b40> -> __condition
            __expression = __cache_139839042376784

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139839042376784
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed0725c90> name=None at 7f2ed0725690> -> __attrs_139839042374192
            __attrs_139839042374192 = _static_139839042378896
            __previous_i18n_domain_139839042374432 = __i18n_domain
            __i18n_domain = 'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header id="portal-top">\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042373376
            __attrs_139839042373376 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042371936
            __default_139839042371936 = _DEFAULT_MARKER

            # <Value 'provider:plone.portaltop' (58:34)> -> __cache_139839042373712
            __token = 2664
            try:
                __zt_tmp = __attrs_139839042373376
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042373712 = _static_139839140402352('provider', 'plone.portaltop', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portaltop' (58:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0724220> -> __condition
            __expression = __cache_139839042373712

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139839042373712
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed0724490> name=None at 7f2ed0724400> -> __attrs_139839042372176
            __attrs_139839042372176 = _static_139839042372752

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-header">\n        ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042281504
            __attrs_139839042281504 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042288896
            __default_139839042288896 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalheader' (60:36)> -> __cache_139839042278528
            __token = 2760
            try:
                __zt_tmp = __attrs_139839042281504
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042278528 = _static_139839140402352('provider', 'plone.portalheader', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalheader' (60:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed070e050> -> __condition
            __expression = __cache_139839042278528

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139839042278528
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      </div>\n\n    </header>')
            __i18n_domain = __previous_i18n_domain_139839042374432
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed070fe80> name=None at 7f2ed070d390> -> __attrs_139839042288608
            __attrs_139839042288608 = _static_139839042289280

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042285296
            __default_139839042285296 = _DEFAULT_MARKER

            # <Value 'provider:plone.mainnavigation' (65:59)> -> __cache_139839042288464
            __token = 2880
            try:
                __zt_tmp = __attrs_139839042288608
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042288464 = _static_139839140402352('provider', 'plone.mainnavigation', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.mainnavigation' (65:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed070e3b0> -> __condition
            __expression = __cache_139839042288464

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n      The main navigation\n    ')
            else:
                __content = __cache_139839042288464
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed070ffa0> name=None at 7f2ed070edd0> -> __attrs_139839042284528
            __attrs_139839042284528 = _static_139839042289568

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="global_statusmessage">\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042283616
            __attrs_139839042283616 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042284912
            __default_139839042284912 = _DEFAULT_MARKER

            # <Value 'provider:plone.globalstatusmessage' (70:42)> -> __cache_139839042286208
            __token = 3032
            try:
                __zt_tmp = __attrs_139839042283616
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042286208 = _static_139839140402352('provider', 'plone.globalstatusmessage', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.globalstatusmessage' (70:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed070f580> -> __condition
            __expression = __cache_139839042286208

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139839042286208
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')
            if (__slot_global_statusmessage is None):

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042287408
                __attrs_139839042287408 = _static_139839134773072

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append('\n    </section>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed070ead0> name=None at 7f2ed070ef80> -> __attrs_139839042282800
            __attrs_139839042282800 = _static_139839042284240

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042283664
            __default_139839042283664 = _DEFAULT_MARKER

            # <Value 'provider:plone.abovecontent' (75:59)> -> __cache_139839042283232
            __token = 3211
            try:
                __zt_tmp = __attrs_139839042282800
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042283232 = _static_139839140402352('provider', 'plone.abovecontent', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.abovecontent' (75:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed070f940> -> __condition
            __expression = __cache_139839042283232

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139839042283232
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed070cfa0> name=None at 7f2ed070e200> -> __attrs_139839042281408
            __attrs_139839042281408 = _static_139839042277280

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="portal-column-content">\n\n      ')
            if (__slot_content is None):

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042280592
                __attrs_139839042280592 = _static_139839134773072
                __append('\n\n      ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n      ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append('\n    </article>\n\n    ')
            if (__slot_column_one_slot is None):

                # <Static value=<ast.Dict object at 0x7f2ed070cfd0> name=None at 7f2ed070d420> -> __attrs_139839042273824
                __attrs_139839042273824 = _static_139839042277328

                # <Value 'sl' (130:26)> -> __condition
                __token = 5052
                try:
                    __zt_tmp = __attrs_139839042273824
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139839140402352('path', 'sl', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-one">\n      ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042155952
                        __attrs_139839042155952 = _static_139839134773072
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042148944
                        __attrs_139839042148944 = _static_139839134773072

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042158400
                        __default_139839042158400 = _DEFAULT_MARKER

                        # <Value 'provider:plone.leftcolumn' (132:38)> -> __cache_139839042154272
                        __token = 5150
                        try:
                            __zt_tmp = __attrs_139839042148944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139839042154272 = _static_139839140402352('provider', 'plone.leftcolumn', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.leftcolumn' (132:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed06efdf0> -> __condition
                        __expression = __cache_139839042154272

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139839042154272
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_one_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_one_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')
            if (__slot_column_two_slot is None):

                # <Static value=<ast.Dict object at 0x7f2ed06efd60> name=None at 7f2ed06ef820> -> __attrs_139839042148992
                __attrs_139839042148992 = _static_139839042157920

                # <Value 'sr' (138:26)> -> __condition
                __token = 5325
                try:
                    __zt_tmp = __attrs_139839042148992
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139839140402352('path', 'sr', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-two">\n      ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042151728
                        __attrs_139839042151728 = _static_139839134773072
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042156672
                        __attrs_139839042156672 = _static_139839134773072

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042152256
                        __default_139839042152256 = _DEFAULT_MARKER

                        # <Value 'provider:plone.rightcolumn' (140:38)> -> __cache_139839042155280
                        __token = 5423
                        try:
                            __zt_tmp = __attrs_139839042156672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139839042155280 = _static_139839140402352('provider', 'plone.rightcolumn', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.rightcolumn' (140:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed06ef340> -> __condition
                        __expression = __cache_139839042155280

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139839042155280
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_two_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_two_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f2ed06efac0> name=None at 7f2ed06efa00> -> __attrs_139839042150192
            __attrs_139839042150192 = _static_139839042157248
            __previous_i18n_domain_139839042145152 = __i18n_domain
            __i18n_domain = 'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer id="portal-footer-wrapper">\n      ')

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042149856
            __attrs_139839042149856 = _static_139839134773072

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042147408
            __default_139839042147408 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalfooter' (145:34)> -> __cache_139839042150912
            __token = 5586
            try:
                __zt_tmp = __attrs_139839042149856
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139839042150912 = _static_139839140402352('provider', 'plone.portalfooter', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalfooter' (145:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed06ee0e0> -> __condition
            __expression = __cache_139839042150912

            # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139839042150912
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    </footer>')
            __i18n_domain = __previous_i18n_domain_139839042145152
            __append('\n\n  </body>')
            if (__backup_body_class_139839042097824 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_139839042097824
            if (__backup_sr_139839042106992 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_139839042106992
            if (__backup_sl_139839042106416 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_139839042106416
            if (__backup_isRTL_139839042105696 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_139839042105696
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_139839042104352
            if (__backup_ajax_load_139839042107376 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_139839042107376
            if (__backup_ajax_include_head_139839042106320 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_139839042106320
            if (__backup_site_properties_139839042107472 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_139839042107472
            if (__backup_checkPermission_139839042105024 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_139839042105024
            if (__backup_portal_url_139839041717392 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_139839041717392
            if (__backup_dummy_139839043380960 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_139839043380960
            if (__backup_view_139839042232064 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_139839042232064
            if (__backup_lang_139839041808144 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_139839041808144
            if (__backup_plone_layout_139839041962912 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_139839041962912
            if (__backup_icons_139839042232496 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139839042232496
            if (__backup_plone_view_139839042359824 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_139839042359824
            if (__backup_context_state_139839042232640 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_139839042232640
            if (__backup_portal_state_139839042236576 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_139839042236576
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_content(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_content_core = econtext['__slot_content_core'].pop()
        except:
            __slot_content_core = None

        try:
            __slot_body = econtext['__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_content_description = econtext['__slot_content_description'].pop()
        except:
            __slot_content_description = None

        try:
            __slot_content_title = econtext['__slot_content_title'].pop()
        except:
            __slot_content_title = None

        try:
            __slot_main = econtext['__slot_main'].pop()
        except:
            __slot_main = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042274112
            __attrs_139839042274112 = _static_139839134773072
            __append('\n\n        ')
            if (__slot_body is None):

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042278384
                __attrs_139839042278384 = _static_139839134773072
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7f2ed070d840> name=None at 7f2ed070d8a0> -> __attrs_139839042278048
                __attrs_139839042278048 = _static_139839042279488

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n            ')
                if (__slot_main is None):

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042276224
                    __attrs_139839042276224 = _static_139839134773072
                    __append('\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042366592
                    __attrs_139839042366592 = _static_139839134773072

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed0720910> name=None at 7f2ed07203a0> -> __attrs_139839042357760
                    __attrs_139839042357760 = _static_139839042357520

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042355504
                    __default_139839042355504 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontenttitle' (91:77)> -> __cache_139839042355936
                    __token = 3606
                    try:
                        __zt_tmp = __attrs_139839042357760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139839042355936 = _static_139839140402352('provider', 'plone.abovecontenttitle', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontenttitle' (91:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0720640> -> __condition
                    __expression = __cache_139839042355936

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139839042355936
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_title is None):

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042358432
                        __attrs_139839042358432 = _static_139839134773072
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042360448
                        __attrs_139839042360448 = _static_139839134773072

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042360400
                        __default_139839042360400 = _DEFAULT_MARKER

                        # <Value 'context/@@title' (94:45)> -> __cache_139839042356752
                        __token = 3747
                        try:
                            __zt_tmp = __attrs_139839042360448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139839042356752 = _static_139839140402352('path', 'context/@@title', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@title' (94:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0720c10> -> __condition
                        __expression = __cache_139839042356752

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append('<h1 />')
                        else:
                            __content = __cache_139839042356752
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed0720f40> name=None at 7f2ed0721b40> -> __attrs_139839042362656
                    __attrs_139839042362656 = _static_139839042359104

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042362224
                    __default_139839042362224 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontenttitle' (97:77)> -> __cache_139839042358576
                    __token = 3876
                    try:
                        __zt_tmp = __attrs_139839042362656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139839042358576 = _static_139839140402352('provider', 'plone.belowcontenttitle', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontenttitle' (97:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0721cf0> -> __condition
                    __expression = __cache_139839042358576

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139839042358576
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_description is None):

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042361072
                        __attrs_139839042361072 = _static_139839134773072
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042366928
                        __attrs_139839042366928 = _static_139839134773072

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042367312
                        __default_139839042367312 = _DEFAULT_MARKER

                        # <Value 'context/@@description' (100:44)> -> __cache_139839042361360
                        __token = 4028
                        try:
                            __zt_tmp = __attrs_139839042366928
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139839042361360 = _static_139839140402352('path', 'context/@@description', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@description' (100:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0722d70> -> __condition
                        __expression = __cache_139839042361360

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append('<p />')
                        else:
                            __content = __cache_139839042361360
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f2ed0723520> name=None at 7f2ed0723ca0> -> __attrs_139839042368176
                    __attrs_139839042368176 = _static_139839042368800

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-description">')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042370960
                    __default_139839042370960 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentdescription' (103:83)> -> __cache_139839042361552
                    __token = 4175
                    try:
                        __zt_tmp = __attrs_139839042368176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139839042361552 = _static_139839140402352('provider', 'plone.belowcontentdescription', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentdescription' (103:83)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0723f70> -> __condition
                    __expression = __cache_139839042361552

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139839042361552
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              </header>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f2ed0723ac0> name=None at 7f2ed07237f0> -> __attrs_139839042368704
                    __attrs_139839042368704 = _static_139839042370240

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042366208
                    __default_139839042366208 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontentbody' (107:74)> -> __cache_139839042368848
                    __token = 4318
                    try:
                        __zt_tmp = __attrs_139839042368704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139839042368848 = _static_139839140402352('provider', 'plone.abovecontentbody', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontentbody' (107:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0723b50> -> __condition
                    __expression = __cache_139839042368848

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139839042368848
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f2ed0723100> name=None at 7f2ed0723460> -> __attrs_139839042365968
                    __attrs_139839042365968 = _static_139839042367744

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')
                    if (__slot_content_core is None):

                        # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042364480
                        __attrs_139839042364480 = _static_139839134773072

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042365104
                        __default_139839042365104 = _DEFAULT_MARKER

                        # <Value 'nothing' (110:68)> -> __cache_139839042365296
                        __token = 4461
                        try:
                            __zt_tmp = __attrs_139839042364480
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139839042365296 = _static_139839140402352('path', 'nothing', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                        # <BinOp left=<Value 'nothing' (110:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed07223e0> -> __condition
                        __expression = __cache_139839042365296

                        # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  Page body text\n                ')
                        else:
                            __content = __cache_139839042365296
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append('\n              </div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f2ed06eee00> name=None at 7f2ed06ed660> -> __attrs_139839042153744
                    __attrs_139839042153744 = _static_139839042153984

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042363808
                    __default_139839042363808 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentbody' (115:74)> -> __cache_139839042364720
                    __token = 4630
                    try:
                        __zt_tmp = __attrs_139839042153744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139839042364720 = _static_139839140402352('provider', 'plone.belowcontentbody', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentbody' (115:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed0722380> -> __condition
                    __expression = __cache_139839042364720

                    # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139839042364720
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n            ')
                else:
                    __slot_main(__stream, econtext.copy(), rcontext)
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f2ed5f42f50> name=None at 7f2ed5f411b0> -> __attrs_139839042157872
                __attrs_139839042157872 = _static_139839134773072

                # <footer ... (0:0)
                # --------------------------------------------------------
                __append('<footer>\n              ')

                # <Static value=<ast.Dict object at 0x7f2ed06ed870> name=None at 7f2ed06ed5a0> -> __attrs_139839042152400
                __attrs_139839042152400 = _static_139839042148464

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="viewlet-below-content">')

                # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __default_139839042154128
                __default_139839042154128 = _DEFAULT_MARKER

                # <Value 'provider:plone.belowcontent' (119:69)> -> __cache_139839042154512
                __token = 4787
                try:
                    __zt_tmp = __attrs_139839042152400
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139839042154512 = _static_139839140402352('provider', 'plone.belowcontent', econtext=econtext)(_static_139839140398752(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.belowcontent' (119:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f2ed6350d60> at 7f2ed06eeb00> -> __condition
                __expression = __cache_139839042154512

                # <Symbol value=<DEFAULT> at 7f2ed6350d60> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139839042154512
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n            </footer>\n          </article>\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append('\n      ')
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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_master': render_master, 'render_content': render_content, 'render': render, }