# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/main_template.pt'

__tokens = {71: ('string:&lt;!DOCTYPE ht', 2, 36), 344: ("python:context.restrictedTraverse('@@plone_portal_state')", 8, 31), 426: (" python:context.restrictedTraverse('@@plone_context_state'", 9, 23), 506: ("w python:context.restrictedTraverse('@@plone", 10, 19), 567: ("ns python:context.restrictedTraverse('@@iconresolve", 11, 13), 642: ("out python:context.restrictedTraverse('@@plone_layo", 12, 19), 709: ('lang python:portal_state.langu', 13, 10), 755: (' view nocall:view | nocall: plon', 14, 9), 804: (' dummy python: plone_layout.mark_vie', 15, 9), 862: ('tal_url python:portal_state.port', 16, 13), 921: ("rmission python:context.restrictedTraverse('portal_membership').checkP", 17, 17), 1018: ("roperties python:context.restrictedTraverse('portal_properties').site_", 18, 16), 1117: ("clude_head python:request.get('ajax_include_he", 19, 17), 1184: ('  ajax_load ', 20, 8), 1264: ('lang', 22, 27), 1313: ('provider:plone.httpheaders', 24, 40), 1416: ('provider:plone.htmlhead', 29, 32), 1471: ('nothing', 31, 26), 1757: ('provider:plone.scripts', 38, 32), 1882: ('provider:plone.htmlhead.links', 41, 33), 2021: ('portal_state/is_rtl', 46, 26), 2064: (" python:plone_layout.have_portlets('plone.leftcolumn', view", 47, 22), 2147: ("r python:plone_layout.have_portlets('plone.rightcolumn', vie", 48, 21), 2239: ('ss python:plone_layout.bodyClass(template, vi', 49, 28), 2415: ("  python:context.restrictedTraverse('@@plone_patterns_settings')", 52, 22), 2320: ('body_class', 50, 30), 2359: (" python:isRTL and 'rtl' or 'ltr", 51, 27), 2553: ('provider:plone.toolbar', 55, 32), 2664: ('provider:plone.portaltop', 58, 34), 2760: ('provider:plone.portalheader', 60, 36), 2880: ('provider:plone.mainnavigation', 65, 59), 3032: ('provider:plone.globalstatusmessage', 70, 42), 3211: ('provider:plone.abovecontent', 75, 59), 5052: ('sl', 130, 26), 5150: ('provider:plone.leftcolumn', 132, 38), 5325: ('sr', 138, 26), 5423: ('provider:plone.rightcolumn', 140, 38), 5586: ('provider:plone.portalfooter', 145, 34), 3606: ('provider:plone.abovecontenttitle', 91, 77), 3747: ('context/@@title', 94, 45), 3876: ('provider:plone.belowcontenttitle', 97, 77), 4028: ('context/@@description', 100, 44), 4175: ('provider:plone.belowcontentdescription', 103, 83), 4318: ('provider:plone.abovecontentbody', 107, 74), 4461: ('nothing', 110, 68), 4630: ('provider:plone.belowcontentbody', 115, 74), 4787: ('provider:plone.belowcontent', 119, 69)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882241826032 = {'id': 'viewlet-below-content', }
_static_139882241822816 = {'id': 'viewlet-below-content-body', }
_static_139882241834240 = {'id': 'content-core', }
_static_139882205622432 = {'id': 'viewlet-above-content-body', }
_static_139882205625552 = {'id': 'viewlet-below-content-description', }
_static_139882205620176 = {'id': 'viewlet-below-content-title', }
_static_139882205611968 = {'id': 'viewlet-above-content-title', }
_static_139882205616960 = {'id': 'content', }
_static_139882241823632 = {'id': 'portal-footer-wrapper', }
_static_139882241822672 = {'id': 'portal-column-two', }
_static_139882205642272 = {'id': 'portal-column-one', }
_static_139882205636560 = {'id': 'portal-column-content', }
_static_139882205634880 = {'id': 'viewlet-above-content', }
_static_139882205642560 = {'id': 'global_statusmessage', }
_static_139882205630656 = {'id': 'portal-mainnavigation', }
_static_139882205632576 = {'id': 'portal-header', }
_static_139882205629024 = {'id': 'portal-top', }
_static_139882206046880 = set([])
_static_139882245432384 = {'id': 'visual-portal-wrapper', 'class': 'body_class', 'dir': "python:isRTL and 'rtl' or 'ltr'", }
_static_139882245429696 = {'name': 'generator', 'content': 'Plone - https://plone.org/', }
_static_139882205649584 = {'charset': 'utf-8', }
_static_139882205643488 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'lang', }
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
            __slot_style_slot = econtext['__slot_style_slot'].pop()
        except:
            __slot_style_slot = None

        try:
            __slot_column_two_slot = econtext['__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_column_one_slot = econtext['__slot_column_one_slot'].pop()
        except:
            __slot_column_one_slot = None

        try:
            __slot_javascript_head_slot = econtext['__slot_javascript_head_slot'].pop()
        except:
            __slot_javascript_head_slot = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_head_slot = econtext['__slot_head_slot'].pop()
        except:
            __slot_head_slot = None

        try:
            __slot_global_statusmessage = econtext['__slot_global_statusmessage'].pop()
        except:
            __slot_global_statusmessage = None

        try:
            __slot_portlets_one_slot = econtext['__slot_portlets_one_slot'].pop()
        except:
            __slot_portlets_one_slot = None

        try:
            __slot_portlets_two_slot = econtext['__slot_portlets_two_slot'].pop()
        except:
            __slot_portlets_two_slot = None

        try:
            __slot_content = econtext['__slot_content'].pop()
        except:
            __slot_content = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205654480
            __attrs_139882205654480 = _static_139882337226896
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205652896
            __attrs_139882205652896 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205653088
            __default_139882205653088 = _DEFAULT_MARKER

            # <Value 'string:<!DOCTYPE html>' (2:36)> -> __cache_139882205653568
            __token = 71
            try:
                __zt_tmp = __attrs_139882205652896
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205653568 = _static_139882257081264('string', '<!DOCTYPE html>', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'string:<!DOCTYPE html>' (2:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2da980> -> __condition
            __expression = __cache_139882205653568

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139882205653568
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f38dd2d82e0> name=None at 7f38dd2d8310> -> __attrs_139882205644064
            __attrs_139882205644064 = _static_139882205643488
            __backup_portal_state_139882238269504 = get('portal_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_portal_state')" (8:31)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_139882238269648 = get('context_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_context_state')" (9:23)> -> __value
            __token = 426
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_139882238610016 = get('plone_view', __marker)

            # <Value "python:context.restrictedTraverse('@@plone')" (10:19)> -> __value
            __token = 506
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('@@plone')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_icons_139882238609968 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (11:13)> -> __value
            __token = 567
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_plone_layout_139882238609104 = get('plone_layout', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_layout')" (12:19)> -> __value
            __token = 642
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_139882238609392 = get('lang', __marker)

            # <Value 'python:portal_state.language()' (13:10)> -> __value
            __token = 709
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', 'portal_state.language()', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_139882238611216 = get('view', __marker)

            # <Value 'nocall:view | nocall: plone_view' (14:9)> -> __value
            __token = 755
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('nocall', 'view | nocall: plone_view', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_139882238610784 = get('dummy', __marker)

            # <Value 'python: plone_layout.mark_view(view)' (15:9)> -> __value
            __token = 804
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', ' plone_layout.mark_view(view)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_139882238610640 = get('portal_url', __marker)

            # <Value 'python:portal_state.portal_url()' (16:13)> -> __value
            __token = 862
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', 'portal_state.portal_url()', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_139882238610304 = get('checkPermission', __marker)

            # <Value "python:context.restrictedTraverse('portal_membership').checkPermission" (17:17)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_139882238610832 = get('site_properties', __marker)

            # <Value "python:context.restrictedTraverse('portal_properties').site_properties" (18:16)> -> __value
            __token = 1018
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_139882238611312 = get('ajax_include_head', __marker)

            # <Value "python:request.get('ajax_include_head', False)" (19:17)> -> __value
            __token = 1117
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "request.get('ajax_include_head', False)", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_139882238611072 = get('ajax_load', __marker)

            # <Value 'python:False' (20:8)> -> __value
            __token = 1184
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', 'False', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_139882205646752 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205642912
            __default_139882205642912 = _DEFAULT_MARKER

            # <Substitution 'lang' (22:27)> -> __attr_lang
            __token = 1264
            try:
                __zt_tmp = __attrs_139882205644064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_139882257081264('path', 'lang', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205648192
            __attrs_139882205648192 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205648000
            __default_139882205648000 = _DEFAULT_MARKER

            # <Value 'provider:plone.httpheaders' (24:40)> -> __cache_139882205647520
            __token = 1313
            try:
                __zt_tmp = __attrs_139882205648192
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205647520 = _static_139882257081264('provider', 'plone.httpheaders', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.httpheaders' (24:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d9360> -> __condition
            __expression = __cache_139882205647520

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139882205647520
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205648768
            __attrs_139882205648768 = _static_139882337226896

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd2d9ab0> name=None at 7f38dd2d9ae0> -> __attrs_139882205652560
            __attrs_139882205652560 = _static_139882205649584

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205650544
            __attrs_139882205650544 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205650640
            __default_139882205650640 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead' (29:32)> -> __cache_139882205651312
            __token = 1416
            try:
                __zt_tmp = __attrs_139882205650544
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205651312 = _static_139882257081264('provider', 'plone.htmlhead', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead' (29:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2da5f0> -> __condition
            __expression = __cache_139882205651312

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139882205651312
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245425712
            __attrs_139882245425712 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245424176
            __default_139882245424176 = _DEFAULT_MARKER

            # <Value 'nothing' (31:26)> -> __cache_139882205650880
            __token = 1471
            try:
                __zt_tmp = __attrs_139882245425712
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205650880 = _static_139882257081264('path', 'nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'nothing' (31:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d9de0> -> __condition
            __expression = __cache_139882205650880

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_139882205650880
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_top_slot is None):

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245432528
                __attrs_139882245432528 = _static_139882337226896
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_head_slot is None):

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245431136
                __attrs_139882245431136 = _static_139882337226896
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_style_slot is None):

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245433152
                __attrs_139882245433152 = _static_139882337226896
            else:
                __slot_style_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245435456
            __attrs_139882245435456 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245434208
            __default_139882245434208 = _DEFAULT_MARKER

            # <Value 'provider:plone.scripts' (38:32)> -> __cache_139882245429744
            __token = 1757
            try:
                __zt_tmp = __attrs_139882245435456
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882245429744 = _static_139882257081264('provider', 'plone.scripts', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.scripts' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df8c9e40> -> __condition
            __expression = __cache_139882245429744

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139882245429744
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_javascript_head_slot is None):

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245436704
                __attrs_139882245436704 = _static_139882337226896
            else:
                __slot_javascript_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882245437184
            __attrs_139882245437184 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245436800
            __default_139882245436800 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead.links' (41:33)> -> __cache_139882245436320
            __token = 1882
            try:
                __zt_tmp = __attrs_139882245437184
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882245436320 = _static_139882257081264('provider', 'plone.htmlhead.links', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead.links' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df8cb9d0> -> __condition
            __expression = __cache_139882245436320

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link />')
            else:
                __content = __cache_139882245436320
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7f38df8c99c0> name=None at 7f38df8c9ae0> -> __attrs_139882245423648
            __attrs_139882245423648 = _static_139882245429696

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="generator" content="Plone - https://plone.org/" />\n\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f38df8ca440> name=None at 7f38df8cbb20> -> __attrs_139882245431808
            __attrs_139882245431808 = _static_139882245432384
            __backup_isRTL_139882237892336 = get('isRTL', __marker)

            # <Value 'portal_state/is_rtl' (46:26)> -> __value
            __token = 2021
            try:
                __zt_tmp = __attrs_139882245431808
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'portal_state/is_rtl', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_139882238613328 = get('sl', __marker)

            # <Value "python:plone_layout.have_portlets('plone.leftcolumn', view)" (47:22)> -> __value
            __token = 2064
            try:
                __zt_tmp = __attrs_139882245431808
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_139882238615008 = get('sr', __marker)

            # <Value "python:plone_layout.have_portlets('plone.rightcolumn', view)" (48:21)> -> __value
            __token = 2147
            try:
                __zt_tmp = __attrs_139882245431808
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_139882263900896 = get('body_class', __marker)

            # <Value 'python:plone_layout.bodyClass(template, view)' (49:28)> -> __value
            __token = 2239
            try:
                __zt_tmp = __attrs_139882245431808
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', 'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')

            # <Value "python:context.restrictedTraverse('@@plone_patterns_settings')()" (52:22)> -> __cache_139882245438960
            __token = 2415
            try:
                __zt_tmp = __attrs_139882245431808
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882245438960 = _static_139882257081264('python', "context.restrictedTraverse('@@plone_patterns_settings')()", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if ('id' not in __chain(__cache_139882245438960)):
                __append(' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245430944
            __default_139882245430944 = _DEFAULT_MARKER

            # <Substitution 'body_class' (50:30)> -> __attr_class
            __token = 2320
            try:
                __zt_tmp = __attrs_139882245431808
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139882257081264('path', 'body_class', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and ('class' not in __chain(__cache_139882245438960))):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882245433488
            __default_139882245433488 = _DEFAULT_MARKER

            # <Substitution "python:isRTL and 'rtl' or 'ltr'" (51:27)> -> __attr_dir
            __token = 2359
            try:
                __zt_tmp = __attrs_139882245431808
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_139882257081264('python', "isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and ('dir' not in __chain(__cache_139882245438960))):
                __append((' dir="%s"' % __attr_dir))
            __attr_139882245438768 = __cache_139882245438960
            for (name, value, ) in __attr_139882245438768.items():
                if ((name not in _static_139882206046880) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205638672
            __attrs_139882205638672 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205639344
            __default_139882205639344 = _DEFAULT_MARKER

            # <Value 'provider:plone.toolbar' (55:32)> -> __cache_139882245434400
            __token = 2553
            try:
                __zt_tmp = __attrs_139882205638672
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882245434400 = _static_139882257081264('provider', 'plone.toolbar', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.toolbar' (55:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d54e0> -> __condition
            __expression = __cache_139882245434400

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139882245434400
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd2d4a60> name=None at 7f38dd2d4a90> -> __attrs_139882205628928
            __attrs_139882205628928 = _static_139882205629024
            __previous_i18n_domain_139882205637568 = __i18n_domain
            __i18n_domain = 'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header id="portal-top">\n      ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205628064
            __attrs_139882205628064 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205627056
            __default_139882205627056 = _DEFAULT_MARKER

            # <Value 'provider:plone.portaltop' (58:34)> -> __cache_139882205626960
            __token = 2664
            try:
                __zt_tmp = __attrs_139882205628064
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205626960 = _static_139882257081264('provider', 'plone.portaltop', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portaltop' (58:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d45e0> -> __condition
            __expression = __cache_139882205626960

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139882205626960
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x7f38dd2d5840> name=None at 7f38dd2d5750> -> __attrs_139882205626864
            __attrs_139882205626864 = _static_139882205632576

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-header">\n        ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205630992
            __attrs_139882205630992 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205638240
            __default_139882205638240 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalheader' (60:36)> -> __cache_139882205639872
            __token = 2760
            try:
                __zt_tmp = __attrs_139882205630992
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205639872 = _static_139882257081264('provider', 'plone.portalheader', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalheader' (60:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d7310> -> __condition
            __expression = __cache_139882205639872

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139882205639872
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      </div>\n\n    </header>')
            __i18n_domain = __previous_i18n_domain_139882205637568
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd2d50c0> name=None at 7f38dd2d4d60> -> __attrs_139882205629744
            __attrs_139882205629744 = _static_139882205630656

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205638384
            __default_139882205638384 = _DEFAULT_MARKER

            # <Value 'provider:plone.mainnavigation' (65:59)> -> __cache_139882205638528
            __token = 2880
            try:
                __zt_tmp = __attrs_139882205629744
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205638528 = _static_139882257081264('provider', 'plone.mainnavigation', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.mainnavigation' (65:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d4490> -> __condition
            __expression = __cache_139882205638528

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n      The main navigation\n    ')
            else:
                __content = __cache_139882205638528
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd2d7f40> name=None at 7f38dd2d7f70> -> __attrs_139882205640976
            __attrs_139882205640976 = _static_139882205642560

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="global_statusmessage">\n      ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205633296
            __attrs_139882205633296 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205635696
            __default_139882205635696 = _DEFAULT_MARKER

            # <Value 'provider:plone.globalstatusmessage' (70:42)> -> __cache_139882205640736
            __token = 3032
            try:
                __zt_tmp = __attrs_139882205633296
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205640736 = _static_139882257081264('provider', 'plone.globalstatusmessage', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.globalstatusmessage' (70:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d6440> -> __condition
            __expression = __cache_139882205640736

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139882205640736
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')
            if (__slot_global_statusmessage is None):

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205633488
                __attrs_139882205633488 = _static_139882337226896

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append('\n    </section>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd2d6140> name=None at 7f38dd2d6200> -> __attrs_139882205640544
            __attrs_139882205640544 = _static_139882205634880

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205634352
            __default_139882205634352 = _DEFAULT_MARKER

            # <Value 'provider:plone.abovecontent' (75:59)> -> __cache_139882205634016
            __token = 3211
            try:
                __zt_tmp = __attrs_139882205640544
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882205634016 = _static_139882257081264('provider', 'plone.abovecontent', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.abovecontent' (75:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d5f00> -> __condition
            __expression = __cache_139882205634016

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139882205634016
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd2d67d0> name=None at 7f38dd2d6740> -> __attrs_139882205636176
            __attrs_139882205636176 = _static_139882205636560

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="portal-column-content">\n\n      ')
            if (__slot_content is None):

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205629888
                __attrs_139882205629888 = _static_139882337226896
                __append('\n\n      ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n      ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append('\n    </article>\n\n    ')
            if (__slot_column_one_slot is None):

                # <Static value=<ast.Dict object at 0x7f38dd2d7e20> name=None at 7f38dd2d7d00> -> __attrs_139882205617248
                __attrs_139882205617248 = _static_139882205642272

                # <Value 'sl' (130:26)> -> __condition
                __token = 5052
                try:
                    __zt_tmp = __attrs_139882205617248
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'sl', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-one">\n      ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241823152
                        __attrs_139882241823152 = _static_139882337226896
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241823968
                        __attrs_139882241823968 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882241825840
                        __default_139882241825840 = _DEFAULT_MARKER

                        # <Value 'provider:plone.leftcolumn' (132:38)> -> __cache_139882241822192
                        __token = 5150
                        try:
                            __zt_tmp = __attrs_139882241823968
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882241822192 = _static_139882257081264('provider', 'plone.leftcolumn', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.leftcolumn' (132:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df5599c0> -> __condition
                        __expression = __cache_139882241822192

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139882241822192
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

                # <Static value=<ast.Dict object at 0x7f38df558fd0> name=None at 7f38df55a530> -> __attrs_139882241825168
                __attrs_139882241825168 = _static_139882241822672

                # <Value 'sr' (138:26)> -> __condition
                __token = 5325
                try:
                    __zt_tmp = __attrs_139882241825168
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'sr', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-two">\n      ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241834864
                        __attrs_139882241834864 = _static_139882337226896
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241830832
                        __attrs_139882241830832 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882241831072
                        __default_139882241831072 = _DEFAULT_MARKER

                        # <Value 'provider:plone.rightcolumn' (140:38)> -> __cache_139882241832944
                        __token = 5423
                        try:
                            __zt_tmp = __attrs_139882241830832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882241832944 = _static_139882257081264('provider', 'plone.rightcolumn', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.rightcolumn' (140:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df55b1c0> -> __condition
                        __expression = __cache_139882241832944

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139882241832944
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

            # <Static value=<ast.Dict object at 0x7f38df559390> name=None at 7f38df55ba60> -> __attrs_139882241828912
            __attrs_139882241828912 = _static_139882241823632
            __previous_i18n_domain_139882241828432 = __i18n_domain
            __i18n_domain = 'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer id="portal-footer-wrapper">\n      ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241830352
            __attrs_139882241830352 = _static_139882337226896

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882241830064
            __default_139882241830064 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalfooter' (145:34)> -> __cache_139882241829968
            __token = 5586
            try:
                __zt_tmp = __attrs_139882241830352
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882241829968 = _static_139882257081264('provider', 'plone.portalfooter', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalfooter' (145:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df55ab30> -> __condition
            __expression = __cache_139882241829968

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139882241829968
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    </footer>')
            __i18n_domain = __previous_i18n_domain_139882241828432
            __append('\n\n  </body>')
            if (__backup_body_class_139882263900896 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_139882263900896
            if (__backup_sr_139882238615008 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_139882238615008
            if (__backup_sl_139882238613328 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_139882238613328
            if (__backup_isRTL_139882237892336 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_139882237892336
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_139882205646752
            if (__backup_ajax_load_139882238611072 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_139882238611072
            if (__backup_ajax_include_head_139882238611312 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_139882238611312
            if (__backup_site_properties_139882238610832 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_139882238610832
            if (__backup_checkPermission_139882238610304 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_139882238610304
            if (__backup_portal_url_139882238610640 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_139882238610640
            if (__backup_dummy_139882238610784 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_139882238610784
            if (__backup_view_139882238611216 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_139882238611216
            if (__backup_lang_139882238609392 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_139882238609392
            if (__backup_plone_layout_139882238609104 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_139882238609104
            if (__backup_icons_139882238609968 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139882238609968
            if (__backup_plone_view_139882238610016 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_139882238610016
            if (__backup_context_state_139882238269648 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_139882238269648
            if (__backup_portal_state_139882238269504 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_139882238269504
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
            __slot_body = econtext['__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_content_title = econtext['__slot_content_title'].pop()
        except:
            __slot_content_title = None

        try:
            __slot_content_core = econtext['__slot_content_core'].pop()
        except:
            __slot_content_core = None

        try:
            __slot_main = econtext['__slot_main'].pop()
        except:
            __slot_main = None

        try:
            __slot_content_description = econtext['__slot_content_description'].pop()
        except:
            __slot_content_description = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205642656
            __attrs_139882205642656 = _static_139882337226896
            __append('\n\n        ')
            if (__slot_body is None):

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205617344
                __attrs_139882205617344 = _static_139882337226896
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7f38dd2d1b40> name=None at 7f38dd2d04c0> -> __attrs_139882205616144
                __attrs_139882205616144 = _static_139882205616960

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n            ')
                if (__slot_main is None):

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205619360
                    __attrs_139882205619360 = _static_139882337226896
                    __append('\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205615280
                    __attrs_139882205615280 = _static_139882337226896

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f38dd2d07c0> name=None at 7f38dd2d0a90> -> __attrs_139882205614032
                    __attrs_139882205614032 = _static_139882205611968

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205610816
                    __default_139882205610816 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontenttitle' (91:77)> -> __cache_139882205611680
                    __token = 3606
                    try:
                        __zt_tmp = __attrs_139882205614032
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882205611680 = _static_139882257081264('provider', 'plone.abovecontenttitle', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontenttitle' (91:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d06d0> -> __condition
                    __expression = __cache_139882205611680

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882205611680
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_title is None):

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205614560
                        __attrs_139882205614560 = _static_139882337226896
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205616576
                        __attrs_139882205616576 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205616672
                        __default_139882205616672 = _DEFAULT_MARKER

                        # <Value 'context/@@title' (94:45)> -> __cache_139882205612064
                        __token = 3747
                        try:
                            __zt_tmp = __attrs_139882205616576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882205612064 = _static_139882257081264('path', 'context/@@title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@title' (94:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d0b50> -> __condition
                        __expression = __cache_139882205612064

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append('<h1 />')
                        else:
                            __content = __cache_139882205612064
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f38dd2d27d0> name=None at 7f38dd2d2680> -> __attrs_139882205611584
                    __attrs_139882205611584 = _static_139882205620176

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205615616
                    __default_139882205615616 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontenttitle' (97:77)> -> __cache_139882205613648
                    __token = 3876
                    try:
                        __zt_tmp = __attrs_139882205611584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882205613648 = _static_139882257081264('provider', 'plone.belowcontenttitle', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontenttitle' (97:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d17b0> -> __condition
                    __expression = __cache_139882205613648

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882205613648
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_description is None):

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205621760
                        __attrs_139882205621760 = _static_139882337226896
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205621232
                        __attrs_139882205621232 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205621280
                        __default_139882205621280 = _DEFAULT_MARKER

                        # <Value 'context/@@description' (100:44)> -> __cache_139882205623248
                        __token = 4028
                        try:
                            __zt_tmp = __attrs_139882205621232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882205623248 = _static_139882257081264('path', 'context/@@description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@description' (100:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d2e30> -> __condition
                        __expression = __cache_139882205623248

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append('<p />')
                        else:
                            __content = __cache_139882205623248
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f38dd2d3cd0> name=None at 7f38dd2d26b0> -> __attrs_139882205625072
                    __attrs_139882205625072 = _static_139882205625552

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-description">')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205626176
                    __default_139882205626176 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentdescription' (103:83)> -> __cache_139882205620656
                    __token = 4175
                    try:
                        __zt_tmp = __attrs_139882205625072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882205620656 = _static_139882257081264('provider', 'plone.belowcontentdescription', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentdescription' (103:83)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d2890> -> __condition
                    __expression = __cache_139882205620656

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882205620656
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              </header>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f38dd2d30a0> name=None at 7f38dd2d3220> -> __attrs_139882205623872
                    __attrs_139882205623872 = _static_139882205622432

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205624016
                    __default_139882205624016 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontentbody' (107:74)> -> __cache_139882205624496
                    __token = 4318
                    try:
                        __zt_tmp = __attrs_139882205623872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882205624496 = _static_139882257081264('provider', 'plone.abovecontentbody', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontentbody' (107:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d37f0> -> __condition
                    __expression = __cache_139882205624496

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882205624496
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f38df55bd00> name=None at 7f38dd2d3d00> -> __attrs_139882241833952
                    __attrs_139882241833952 = _static_139882241834240

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')
                    if (__slot_content_core is None):

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241822624
                        __attrs_139882241822624 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882241821712
                        __default_139882241821712 = _DEFAULT_MARKER

                        # <Value 'nothing' (110:68)> -> __cache_139882241832848
                        __token = 4461
                        try:
                            __zt_tmp = __attrs_139882241822624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882241832848 = _static_139882257081264('path', 'nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'nothing' (110:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df55b250> -> __condition
                        __expression = __cache_139882241832848

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  Page body text\n                ')
                        else:
                            __content = __cache_139882241832848
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append('\n              </div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f38df559060> name=None at 7f38df559630> -> __attrs_139882241822048
                    __attrs_139882241822048 = _static_139882241822816

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882241826848
                    __default_139882241826848 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentbody' (115:74)> -> __cache_139882241819168
                    __token = 4630
                    try:
                        __zt_tmp = __attrs_139882241822048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882241819168 = _static_139882257081264('provider', 'plone.belowcontentbody', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentbody' (115:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df558160> -> __condition
                    __expression = __cache_139882241819168

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139882241819168
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n            ')
                else:
                    __slot_main(__stream, econtext.copy(), rcontext)
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882241827568
                __attrs_139882241827568 = _static_139882337226896

                # <footer ... (0:0)
                # --------------------------------------------------------
                __append('<footer>\n              ')

                # <Static value=<ast.Dict object at 0x7f38df559cf0> name=None at 7f38df558f40> -> __attrs_139882241819504
                __attrs_139882241819504 = _static_139882241826032

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="viewlet-below-content">')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882241819840
                __default_139882241819840 = _DEFAULT_MARKER

                # <Value 'provider:plone.belowcontent' (119:69)> -> __cache_139882241820032
                __token = 4787
                try:
                    __zt_tmp = __attrs_139882241819504
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882241820032 = _static_139882257081264('provider', 'plone.belowcontent', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.belowcontent' (119:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38df5585b0> -> __condition
                __expression = __cache_139882241820032

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139882241820032
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