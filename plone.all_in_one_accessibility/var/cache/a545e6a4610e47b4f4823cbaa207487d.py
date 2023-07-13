# -*- coding: utf-8 -*-
__filename = 'manage_main'

__tokens = {31: ('here/manage_page_header', 1, 31), 89: ('here/manage_tabs', 3, 29), 238: ("python:getattr(here.aq_explicit, 'has_order_support', 0)", 7, 38), 318: (' modules/AccessControl/getSecurityManage', 8, 22), 392: ("t python: 'position' if has_order_support else 'i", 9, 31), 467: ("ey python:request.get('skey',default_so", 10, 22), 532: ("key python:request.get('rkey','a", 11, 21), 594: ("_alt python:'desc' if rkey=='asc' else ", 12, 24), 666: ('lt_up rkey_alt', 13, 26), 705: ('   obs python: here.manage_get_sortedObjects(sortkey = skey, revkey ', 14, 17), 801: (' my_url string:${context/absolute_url}/man', 15, 19), 905: ('string:${request/URL1}/', 17, 31), 962: ('obs', 19, 30), 1057: ('obs', 20, 89), 1120: ("python:'thead-light sorted_%s'%(request.get('rkey',''))", 21, 57), 1550: ('string:Sort ${rkey_alt_up} by meta-type', 29, 39), 1628: (' string:${my_url}?skey=meta_type&rkey=${rkey_alt', 30, 37), 1716: ("s python:skey=='meta_type' and 'zmi-sort_key' or No", 31, 37), 2066: ('string:Sort ${rkey_alt_up} by name', 39, 39), 2139: (' string:${my_url}?skey=id&rkey=${rkey_alt', 40, 37), 2220: ("s python:skey=='id' and 'zmi-sort_key' or No", 41, 37), 2879: ('string:Sort ${rkey_alt_up} by size', 52, 39), 2952: (' string:${my_url}?skey=get_size&rkey=${rkey_alt', 53, 37), 3039: ("s python:skey=='get_size' and 'zmi-sort_key' or No", 54, 37), 3451: ('string:Sort ${rkey_alt_up} by modification date', 63, 39), 3537: (' string:${my_url}?skey=_p_mtime&rkey=${rkey_alt', 64, 37), 3624: ("s python:skey=='_p_mtime' and 'zmi-sort_key' or No", 65, 37), 3906: ('obs', 74, 34), 3944: ('nocall:ob_dict/obj', 75, 32), 4178: ('ob_dict/id', 77, 104), 4519: (' ob/meta_type | defaul', 81, 122), 4491: ('ob/zmi_icon | default', 81, 94), 4598: ('ob/meta_type | default', 82, 53), 4765: ("python:'%s/manage_workspace'%(ob_dict['quoted_id'])", 86, 40), 4856: ('ob_dict/id', 87, 37), 4989: ('ob/wl_isLocked | nothing', 88, 111), 5163: ('ob/title|nothing', 91, 74), 5228: ('ob/title', 92, 46), 5390: ('python:here.compute_size(ob)', 96, 76), 5522: ('python:here.last_modified(ob)', 98, 81), 5737: ("python:sm.checkPermission('Delete objects', context)", 106, 23), 5806: ('obs', 106, 92), 5883: ('not:context/dontAllowCopyAndPaste|nothing', 108, 37), 6160: ('delete_allowed', 110, 121), 6415: ('here/cb_dataValid', 112, 125), 6587: ('delete_allowed', 114, 122), 6741: ("python:sm.checkPermission('Import/Export objects', context)", 115, 135), 6856: ("python: has_order_support and sm.checkPermission('Manage properties', context)", 117, 50), 7050: ('python:range(1,min(5,len(obs)))', 119, 38), 7096: ('val', 119, 84), 7142: ('python:range(5,len(obs),5)', 120, 38), 7183: ('val', 120, 79), 8444: ('not:obs', 146, 26), 8558: ('here/title_or_id', 148, 57), 8662: ('not:context/dontAllowCopyAndPaste|nothing', 151, 35), 8824: ('here/cb_dataValid', 152, 118), 9000: ("python:sm.checkPermission('Import/Export objects', context)", 154, 128), 12921: ('here/manage_page_footer', 281, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139922408324592 = {'class': 'zmi-typename_show', }
_static_139922408312016 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_139922408310576 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_139922408315472 = {'class': 'form-group', }
_static_139922408312928 = {'class': 'alert alert-info mt-4 mb-4', }
_static_139922408318112 = {'class': 'fas fa-arrow-down', 'style': 'border-bottom: 0.2rem solid silver;', }
_static_139922406807520 = {'type': 'submit', 'name': 'manage_move_objects_to_bottom:method', 'value': 'Move to bottom', 'title': 'Move selected items to bottom', 'class': 'btn btn-primary', }
_static_139922406801712 = {'class': 'fas fa-arrow-up', 'style': 'border-top: 0.2rem solid silver;', }
_static_139922406817600 = {'type': 'submit', 'name': 'manage_move_objects_to_top:method', 'value': 'Move to top', 'title': 'Move selected items to top', 'class': 'btn btn-primary ml-2 mr-2', }
_static_139922406813520 = {'class': 'fas fa-arrow-down', }
_static_139922406808192 = {'type': 'submit', 'name': 'manage_move_objects_down:method', 'value': 'Move down', 'title': 'Move selected items down', 'class': 'btn btn-primary rounded-right', }
_static_139922406806944 = {'class': 'fas fa-arrow-up', }
_static_139922406806560 = {'type': 'submit', 'name': 'manage_move_objects_up:method', 'value': 'Move up', 'title': 'Move selected items up', 'class': 'btn btn-primary', }
_static_139922406815056 = {'class': 'input-group-append', }
_static_139922407279296 = {'class': 'form-control btn btn-primary', 'name': 'delta:int', }
_static_139922406898704 = {'class': 'input-group', }
_static_139922406895488 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_139922406899232 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_delObjects:method', 'value': 'Delete', }
_static_139922406898320 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_139922406899328 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_copyObjects:method', 'value': 'Copy', }
_static_139922406894144 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_cutObjects:method', 'value': 'Cut', }
_static_139922406893760 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_renameForm:method', 'value': 'Rename', }
_static_139922406886464 = {'class': 'input-group', }
_static_139922406703216 = {'class': 'form-group form-inline zmi-controls', }
_static_139922407062880 = {'class': 'text-right zmi-object-date hidden-xs pl-3', }
_static_139922407050496 = {'class': 'text-right zmi-object-size hidden-xs', }
_static_139922407053472 = {'class': 'zmi-object-title hidden-xs', }
_static_139922407056016 = {'class': 'fa fa-lock', }
_static_139922407055200 = {'class': 'badge badge-warning', 'title': 'This item has been locked by WebDAV', }
_static_139922407052992 = {'href': "python:'%s/manage_workspace'%(ob_dict['quoted_id'])", }
_static_139922407056784 = {'class': 'zmi-object-id', }
_static_139922406706576 = {'class': 'sr-only', }
_static_139922406713344 = {'title': 'Broken object', 'class': 'fas fa-ban text-danger', }
_static_139922406712768 = {'class': 'zmi-object-type', 'onclick': "$(this).prev().children('input').trigger('click')", }
_static_139922406711904 = {'type': 'checkbox', 'class': 'checkbox-list-item', 'name': 'ids:list', 'onclick': 'event.stopPropagation();select_objectitem($(this));', 'value': 'ob_dict/id', }
_static_139922406705376 = {'class': 'zmi-object-check text-right', 'onclick': "$(this).children('input').trigger('click');", }
_static_139922406707488 = {'class': 'fa fa-sort', }
_static_139922407186848 = {'title': 'Sort Ascending by Modification Date', 'href': '?skey=_p_mtime&rkey=asc', 'class': "python:skey=='_p_mtime' and 'zmi-sort_key' or None", }
_static_139922408286208 = {'scope': 'col', 'class': 'zmi-object-date text-right hidden-xs', }
_static_139922408281552 = {'class': 'fa fa-sort', }
_static_139922408278336 = {'title': 'Sort Ascending by File-Size', 'href': '?skey=get_size&rkey=asc', 'class': "python:skey=='get_size' and 'zmi-sort_key' or None", }
_static_139922408285920 = {'scope': 'col', 'class': 'zmi-object-size text-right hidden-xs', }
_static_139922408288080 = {'id': 'tablefilter', 'name': 'obj_ids:tokens', 'type': 'text', 'title': 'Filter object list by entering a name. Pressing the Enter key starts recursive search.', }
_static_139922408277760 = {'class': 'fa fa-search tablefilter', 'onclick': "$('#tablefilter').focus()", }
_static_139922408291872 = {'class': 'fa fa-sort', }
_static_139922408286544 = {'title': 'Sort Ascending by Name', 'href': '?skey=id&rkey=asc', 'class': "python:skey=='id' and 'zmi-sort_key' or None", }
_static_139922407036848 = {'scope': 'col', 'class': 'zmi-object-id', }
_static_139922407042896 = {'class': 'fa fa-sort', }
_static_139922407044576 = {'title': 'Sort Ascending by Meta-Type', 'href': '?skey=meta_type&rkey=asc', 'class': "python:skey=='meta_type' and 'zmi-sort_key' or None", }
_static_139922407043424 = {'scope': 'col', 'class': 'zmi-object-type', }
_static_139922407045056 = {'type': 'checkbox', 'id': 'checkAll', 'onclick': 'checkbox_all();', }
_static_139922407046736 = {'scope': 'col', 'class': 'zmi-object-check text-right', }
_static_139922407045152 = {'class': 'thead-light', }
_static_139922407039248 = {'class': 'table table-striped table-hover table-sm objectItems', }
_static_139922406676448 = {'id': 'objectItems', 'name': 'objectItems', 'method': 'post', 'action': 'string:${request/URL1}/', }
_static_139922407152112 = {'class': 'container-fluid', }
_static_139922496189968 = __C2ZContextWrapper
_static_139922496190256 = __compile_zt_expr
_static_139922496178928 = {}

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

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407147888
            __attrs_139922407147888 = _static_139922496178928

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407158112
            __default_139922407158112 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:31)> -> __cache_139922407156288
            __token = 31
            try:
                __zt_tmp = __attrs_139922407147888
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139922407156288 = _static_139922496190256('path', 'here/manage_page_header', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42395ffdc0> -> __condition
            __expression = __cache_139922407156288

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139922407156288
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407156816
            __attrs_139922407156816 = _static_139922496178928

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407160128
            __default_139922407160128 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (3:29)> -> __cache_139922407147552
            __token = 89
            try:
                __zt_tmp = __attrs_139922407156816
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139922407147552 = _static_139922496190256('path', 'here/manage_tabs', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (3:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42395ffa90> -> __condition
            __expression = __cache_139922407147552

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139922407147552
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f42395fd9f0> name=None at 7f42395fdf30> -> __attrs_139922407159744
            __attrs_139922407159744 = _static_139922407152112

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n  ')

            # <Static value=<ast.Dict object at 0x7f42395897e0> name=None at 7f4239589600> -> __attrs_139922406685616
            __attrs_139922406685616 = _static_139922406676448
            __backup_has_order_support_139922406814816 = get('has_order_support', __marker)

            # <Value "python:getattr(here.aq_explicit, 'has_order_support', 0)" (7:38)> -> __value
            __token = 238
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('python', "getattr(here.aq_explicit, 'has_order_support', 0)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['has_order_support'] = __value
            __backup_sm_139922406809008 = get('sm', __marker)

            # <Value 'modules/AccessControl/getSecurityManager' (8:22)> -> __value
            __token = 318
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'modules/AccessControl/getSecurityManager', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['sm'] = __value
            __backup_default_sort_139922406682928 = get('default_sort', __marker)

            # <Value "python: 'position' if has_order_support else 'id'" (9:31)> -> __value
            __token = 392
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('python', " 'position' if has_order_support else 'id'", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['default_sort'] = __value
            __backup_skey_139922406673712 = get('skey', __marker)

            # <Value "python:request.get('skey',default_sort)" (10:22)> -> __value
            __token = 467
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('python', "request.get('skey',default_sort)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['skey'] = __value
            __backup_rkey_139922406675728 = get('rkey', __marker)

            # <Value "python:request.get('rkey','asc')" (11:21)> -> __value
            __token = 532
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('python', "request.get('rkey','asc')", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['rkey'] = __value
            __backup_rkey_alt_139922406676208 = get('rkey_alt', __marker)

            # <Value "python:'desc' if rkey=='asc' else 'asc'" (12:24)> -> __value
            __token = 594
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('python', "'desc' if rkey=='asc' else 'asc'", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['rkey_alt'] = __value
            __backup_rkey_alt_up_139922406670496 = get('rkey_alt_up', __marker)

            # <Value 'rkey_alt/upper' (13:26)> -> __value
            __token = 666
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'rkey_alt/upper', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['rkey_alt_up'] = __value
            __backup_obs_139922406676304 = get('obs', __marker)

            # <Value 'python: here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)' (14:17)> -> __value
            __token = 705
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('python', ' here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['obs'] = __value
            __backup_my_url_139922406676544 = get('my_url', __marker)

            # <Value 'string:${context/absolute_url}/manage_main' (15:19)> -> __value
            __token = 801
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['my_url'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="objectItems" name="objectItems" method="post"')

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406681776
            __default_139922406681776 = _DEFAULT_MARKER

            # <Substitution 'string:${request/URL1}/' (17:31)> -> __attr_action
            __token = 905
            try:
                __zt_tmp = __attrs_139922406685616
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_139922496190256('string', '${request/URL1}/', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406671648
            __attrs_139922406671648 = _static_139922496178928

            # <Value 'obs' (19:30)> -> __condition
            __token = 962
            try:
                __zt_tmp = __attrs_139922406671648
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139922496190256('path', 'obs', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f42395e2110> name=None at 7f42395e1e70> -> __attrs_139922407039200
                __attrs_139922407039200 = _static_139922407039248

                # <Value 'obs' (20:89)> -> __condition
                __token = 1057
                try:
                    __zt_tmp = __attrs_139922407039200
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('path', 'obs', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table class="table table-striped table-hover table-sm objectItems">\n        ')

                    # <Static value=<ast.Dict object at 0x7f42395e3820> name=None at 7f42395e2ef0> -> __attrs_139922407039440
                    __attrs_139922407039440 = _static_139922407045152

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407031808
                    __default_139922407031808 = _DEFAULT_MARKER

                    # <Substitution "python:'thead-light sorted_%s'%(request.get('rkey',''))" (21:57)> -> __attr_class
                    __token = 1120
                    try:
                        __zt_tmp = __attrs_139922407039440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139922496190256('python', "'thead-light sorted_%s'%(request.get('rkey',''))", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'thead-light', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n          ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407046304
                    __attrs_139922407046304 = _static_139922496178928

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n            ')

                    # <Static value=<ast.Dict object at 0x7f42395e3e50> name=None at 7f42395e3ee0> -> __attrs_139922407046784
                    __attrs_139922407046784 = _static_139922407046736

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-check text-right">\n              ')

                    # <Static value=<ast.Dict object at 0x7f42395e37c0> name=None at 7f42395e1750> -> __attrs_139922407042320
                    __attrs_139922407042320 = _static_139922407045056

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" id="checkAll" onclick="checkbox_all();" />\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f42395e3160> name=None at 7f42395e36a0> -> __attrs_139922407045104
                    __attrs_139922407045104 = _static_139922407043424

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-type">\n              ')

                    # <Static value=<ast.Dict object at 0x7f42395e35e0> name=None at 7f42395e1ae0> -> __attrs_139922407037568
                    __attrs_139922407037568 = _static_139922407044576

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407044480
                    __default_139922407044480 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by meta-type' (29:39)> -> __attr_title
                    __token = 1550
                    try:
                        __zt_tmp = __attrs_139922407037568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_139922496190256('string', 'Sort ${rkey_alt_up} by meta-type', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Meta-Type', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407042464
                    __default_139922407042464 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=meta_type&rkey=${rkey_alt}' (30:37)> -> __attr_href
                    __token = 1628
                    try:
                        __zt_tmp = __attrs_139922407037568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139922496190256('string', '${my_url}?skey=meta_type&rkey=${rkey_alt}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=meta_type&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407043616
                    __default_139922407043616 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='meta_type' and 'zmi-sort_key' or None" (31:37)> -> __attr_class
                    __token = 1716
                    try:
                        __zt_tmp = __attrs_139922407037568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139922496190256('python', "skey=='meta_type' and 'zmi-sort_key' or None", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x7f42395e2f50> name=None at 7f42395e0a30> -> __attrs_139922407045536
                    __attrs_139922407045536 = _static_139922407042896

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f42395e17b0> name=None at 7f42395e3730> -> __attrs_139922408287984
                    __attrs_139922408287984 = _static_139922407036848

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-id">\n              ')

                    # <Static value=<ast.Dict object at 0x7f4239712950> name=None at 7f4239710580> -> __attrs_139922408282464
                    __attrs_139922408282464 = _static_139922408286544

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408283184
                    __default_139922408283184 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by name' (39:39)> -> __attr_title
                    __token = 2066
                    try:
                        __zt_tmp = __attrs_139922408282464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_139922496190256('string', 'Sort ${rkey_alt_up} by name', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Name', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408282656
                    __default_139922408282656 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=id&rkey=${rkey_alt}' (40:37)> -> __attr_href
                    __token = 2139
                    try:
                        __zt_tmp = __attrs_139922408282464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139922496190256('string', '${my_url}?skey=id&rkey=${rkey_alt}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=id&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408292304
                    __default_139922408292304 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='id' and 'zmi-sort_key' or None" (41:37)> -> __attr_class
                    __token = 2220
                    try:
                        __zt_tmp = __attrs_139922408282464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139922496190256('python', "skey=='id' and 'zmi-sort_key' or None", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Name\n                ')

                    # <Static value=<ast.Dict object at 0x7f4239713e20> name=None at 7f4239712b90> -> __attrs_139922408287504
                    __attrs_139922408287504 = _static_139922408291872

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n              ')

                    # <Static value=<ast.Dict object at 0x7f4239710700> name=None at 7f4239710760> -> __attrs_139922408291344
                    __attrs_139922408291344 = _static_139922408277760

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-search tablefilter" onclick="$(\'#tablefilter\').focus()"></i>\n              ')

                    # <Static value=<ast.Dict object at 0x7f4239712f50> name=None at 7f4239713490> -> __attrs_139922408288848
                    __attrs_139922408288848 = _static_139922408288080

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input id="tablefilter" name="obj_ids:tokens" type="text" title="Filter object list by entering a name. Pressing the Enter key starts recursive search." />\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f42397126e0> name=None at 7f4239713340> -> __attrs_139922408276944
                    __attrs_139922408276944 = _static_139922408285920

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-size text-right hidden-xs">\n              ')

                    # <Static value=<ast.Dict object at 0x7f4239710940> name=None at 7f4239710250> -> __attrs_139922408291152
                    __attrs_139922408291152 = _static_139922408278336

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408283568
                    __default_139922408283568 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by size' (52:39)> -> __attr_title
                    __token = 2879
                    try:
                        __zt_tmp = __attrs_139922408291152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_139922496190256('string', 'Sort ${rkey_alt_up} by size', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by File-Size', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408288656
                    __default_139922408288656 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=get_size&rkey=${rkey_alt}' (53:37)> -> __attr_href
                    __token = 2952
                    try:
                        __zt_tmp = __attrs_139922408291152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139922496190256('string', '${my_url}?skey=get_size&rkey=${rkey_alt}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=get_size&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408291968
                    __default_139922408291968 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='get_size' and 'zmi-sort_key' or None" (54:37)> -> __attr_class
                    __token = 3039
                    try:
                        __zt_tmp = __attrs_139922408291152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139922496190256('python', "skey=='get_size' and 'zmi-sort_key' or None", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Size\n                ')

                    # <Static value=<ast.Dict object at 0x7f42397115d0> name=None at 7f42397113c0> -> __attrs_139922408288320
                    __attrs_139922408288320 = _static_139922408281552

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f4239712800> name=None at 7f42397117b0> -> __attrs_139922406734000
                    __attrs_139922406734000 = _static_139922408286208

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-date text-right hidden-xs">\n              ')

                    # <Static value=<ast.Dict object at 0x7f42396061a0> name=None at 7f4239606230> -> __attrs_139922406714064
                    __attrs_139922406714064 = _static_139922407186848

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406704848
                    __default_139922406704848 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by modification date' (63:39)> -> __attr_title
                    __token = 3451
                    try:
                        __zt_tmp = __attrs_139922406714064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_139922496190256('string', 'Sort ${rkey_alt_up} by modification date', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Modification Date', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406716944
                    __default_139922406716944 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=_p_mtime&rkey=${rkey_alt}' (64:37)> -> __attr_href
                    __token = 3537
                    try:
                        __zt_tmp = __attrs_139922406714064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139922496190256('string', '${my_url}?skey=_p_mtime&rkey=${rkey_alt}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=_p_mtime&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406709600
                    __default_139922406709600 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='_p_mtime' and 'zmi-sort_key' or None" (65:37)> -> __attr_class
                    __token = 3624
                    try:
                        __zt_tmp = __attrs_139922406714064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139922496190256('python', "skey=='_p_mtime' and 'zmi-sort_key' or None", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Last Modified\n                ')

                    # <Static value=<ast.Dict object at 0x7f4239591120> name=None at 7f4239590e50> -> __attrs_139922406718912
                    __attrs_139922406718912 = _static_139922406707488

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n          </tr>\n        </thead>\n        ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406712624
                    __attrs_139922406712624 = _static_139922496178928

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append('<tbody>\n          ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406719104
                    __attrs_139922406719104 = _static_139922496178928
                    __backup_ob_dict_139922407038672 = get('ob_dict', __marker)

                    # <Value 'obs' (74:34)> -> __iterator
                    __token = 3906
                    try:
                        __zt_tmp = __attrs_139922406719104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139922496190256('path', 'obs', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    (__iterator, ____index_139922406707056, ) = getname('repeat')('ob_dict', __iterator)
                    econtext['ob_dict'] = None
                    for __item in __iterator:
                        econtext['ob_dict'] = __item

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr>\n            ')

                        # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406707728
                        __attrs_139922406707728 = _static_139922496178928
                        __backup_ob_139922407039584 = get('ob', __marker)

                        # <Value 'nocall:ob_dict/obj' (75:32)> -> __value
                        __token = 3944
                        try:
                            __zt_tmp = __attrs_139922406707728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('nocall', 'ob_dict/obj', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['ob'] = __value
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f42395908e0> name=None at 7f4239590190> -> __attrs_139922406704176
                        __attrs_139922406704176 = _static_139922406705376

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-check text-right" onclick="$(this).children(\'input\').trigger(\'click\');">\n                ')

                        # <Static value=<ast.Dict object at 0x7f4239592260> name=None at 7f4239591de0> -> __attrs_139922406708304
                        __attrs_139922406708304 = _static_139922406711904

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="checkbox" class="checkbox-list-item" name="ids:list"                   onclick="event.stopPropagation();select_objectitem($(this));"')

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406711088
                        __default_139922406711088 = _DEFAULT_MARKER

                        # <Substitution 'ob_dict/id' (77:104)> -> __attr_value
                        __token = 4178
                        try:
                            __zt_tmp = __attrs_139922406708304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139922496190256('path', 'ob_dict/id', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f42395925c0> name=None at 7f4239590730> -> __attrs_139922406708688
                        __attrs_139922406708688 = _static_139922406712768

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-type" onclick="$(this).prev().children(\'input\').trigger(\'click\')">\n                ')

                        # <Static value=<ast.Dict object at 0x7f4239592800> name=None at 7f4239591720> -> __attrs_139922407102816
                        __attrs_139922407102816 = _static_139922406713344

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i')

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406978560
                        __default_139922406978560 = _DEFAULT_MARKER

                        # <Substitution 'ob/meta_type | default' (81:122)> -> __attr_title
                        __token = 4519
                        try:
                            __zt_tmp = __attrs_139922407102816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_139922496190256('path', 'ob/meta_type | default', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', 'Broken object', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407096960
                        __default_139922407096960 = _DEFAULT_MARKER

                        # <Substitution 'ob/zmi_icon | default' (81:94)> -> __attr_class
                        __token = 4491
                        try:
                            __zt_tmp = __attrs_139922407102816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_139922496190256('path', 'ob/zmi_icon | default', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', 'fas fa-ban text-danger', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f4239590d90> name=None at 7f4239590df0> -> __attrs_139922407058560
                        __attrs_139922407058560 = _static_139922406706576

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="sr-only">')

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406716800
                        __default_139922406716800 = _DEFAULT_MARKER

                        # <Value 'ob/meta_type | default' (82:53)> -> __cache_139922406715696
                        __token = 4598
                        try:
                            __zt_tmp = __attrs_139922407058560
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139922406715696 = _static_139922496190256('path', 'ob/meta_type | default', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                        # <BinOp left=<Value 'ob/meta_type | default' (82:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42395930d0> -> __condition
                        __expression = __cache_139922406715696

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Broken object')
                        else:
                            __content = __cache_139922406715696
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n                </i>\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f42395e6590> name=None at 7f42395e7160> -> __attrs_139922407059904
                        __attrs_139922407059904 = _static_139922407056784

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-id">\n                ')

                        # <Static value=<ast.Dict object at 0x7f42395e56c0> name=None at 7f42395e6d40> -> __attrs_139922407060720
                        __attrs_139922407060720 = _static_139922407052992

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407057888
                        __default_139922407057888 = _DEFAULT_MARKER

                        # <Substitution "python:'%s/manage_workspace'%(ob_dict['quoted_id'])" (86:40)> -> __attr_href
                        __token = 4765
                        try:
                            __zt_tmp = __attrs_139922407060720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139922496190256('python', "'%s/manage_workspace'%(ob_dict['quoted_id'])", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407059568
                        __attrs_139922407059568 = _static_139922496178928

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407048960
                        __default_139922407048960 = _DEFAULT_MARKER

                        # <Value 'ob_dict/id' (87:37)> -> __cache_139922407063072
                        __token = 4856
                        try:
                            __zt_tmp = __attrs_139922407059568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139922407063072 = _static_139922496190256('path', 'ob_dict/id', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                        # <BinOp left=<Value 'ob_dict/id' (87:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42395e4c10> -> __condition
                        __expression = __cache_139922407063072

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>Id</span>')
                        else:
                            __content = __cache_139922407063072
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f42395e5f60> name=None at 7f42395e5fc0> -> __attrs_139922407060384
                        __attrs_139922407060384 = _static_139922407055200

                        # <Value 'ob/wl_isLocked | nothing' (88:111)> -> __condition
                        __token = 4989
                        try:
                            __zt_tmp = __attrs_139922407060384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139922496190256('path', 'ob/wl_isLocked | nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge badge-warning" title="This item has been locked by WebDAV">\n                    ')

                            # <Static value=<ast.Dict object at 0x7f42395e6290> name=None at 7f42395e4dc0> -> __attrs_139922407056160
                            __attrs_139922407056160 = _static_139922407056016

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append('<i class="fa fa-lock"></i>\n                  </span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f42395e58a0> name=None at 7f42395e5420> -> __attrs_139922407055584
                        __attrs_139922407055584 = _static_139922407053472

                        # <Value 'ob/title|nothing' (91:74)> -> __condition
                        __token = 5163
                        try:
                            __zt_tmp = __attrs_139922407055584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139922496190256('path', 'ob/title|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="zmi-object-title hidden-xs">\n                    &nbsp;(')

                            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407049728
                            __attrs_139922407049728 = _static_139922496178928

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407055104
                            __default_139922407055104 = _DEFAULT_MARKER

                            # <Value 'ob/title' (92:46)> -> __cache_139922407060816
                            __token = 5228
                            try:
                                __zt_tmp = __attrs_139922407049728
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139922407060816 = _static_139922496190256('path', 'ob/title', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                            # <BinOp left=<Value 'ob/title' (92:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42395e5db0> -> __condition
                            __expression = __cache_139922407060816

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span></span>')
                            else:
                                __content = __cache_139922407060816
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(')\n                  </span>')
                        __append('\n                </a>\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f42395e4d00> name=None at 7f42395e5510> -> __attrs_139922407062976
                        __attrs_139922407062976 = _static_139922407050496

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-right zmi-object-size hidden-xs">')

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407056256
                        __default_139922407056256 = _DEFAULT_MARKER

                        # <Value 'python:here.compute_size(ob)' (96:76)> -> __cache_139922407052176
                        __token = 5390
                        try:
                            __zt_tmp = __attrs_139922407062976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139922407052176 = _static_139922496190256('python', 'here.compute_size(ob)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python:here.compute_size(ob)' (96:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42395e6230> -> __condition
                        __expression = __cache_139922407052176

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_139922407052176
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f42395e7d60> name=None at 7f42395e6dd0> -> __attrs_139922407062064
                        __attrs_139922407062064 = _static_139922407062880

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-right zmi-object-date hidden-xs pl-3">')

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407049008
                        __default_139922407049008 = _DEFAULT_MARKER

                        # <Value 'python:here.last_modified(ob)' (98:81)> -> __cache_139922407063456
                        __token = 5522
                        try:
                            __zt_tmp = __attrs_139922407062064
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139922407063456 = _static_139922496190256('python', 'here.last_modified(ob)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python:here.last_modified(ob)' (98:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42395e7880> -> __condition
                        __expression = __cache_139922407063456

                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_139922407063456
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>\n            ')
                        if (__backup_ob_139922407039584 is __marker):
                            del econtext['ob']
                        else:
                            econtext['ob'] = __backup_ob_139922407039584
                        __append('\n          </tr>')
                        ____index_139922406707056 -= 1
                        if (____index_139922406707056 > 0):
                            __append('\n          ')
                    if (__backup_ob_dict_139922407038672 is __marker):
                        del econtext['ob_dict']
                    else:
                        econtext['ob_dict'] = __backup_ob_dict_139922407038672
                    __append('\n        </tbody>\n      </table>')
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f4239590070> name=None at 7f4239591bd0> -> __attrs_139922406887184
                __attrs_139922406887184 = _static_139922406703216
                __backup_delete_allowed_139922406671360 = get('delete_allowed', __marker)

                # <Value "python:sm.checkPermission('Delete objects', context)" (106:23)> -> __value
                __token = 5737
                try:
                    __zt_tmp = __attrs_139922406887184
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139922496190256('python', "sm.checkPermission('Delete objects', context)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                econtext['delete_allowed'] = __value

                # <Value 'obs' (106:92)> -> __condition
                __token = 5806
                try:
                    __zt_tmp = __attrs_139922406887184
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('path', 'obs', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-group form-inline zmi-controls">\n        ')

                    # <Static value=<ast.Dict object at 0x7f42395bcc40> name=None at 7f42395bd330> -> __attrs_139922406888768
                    __attrs_139922406888768 = _static_139922406886464

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="input-group">\n          ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406894096
                    __attrs_139922406894096 = _static_139922496178928

                    # <Value 'not:context/dontAllowCopyAndPaste|nothing' (108:37)> -> __condition
                    __token = 5883
                    try:
                        __zt_tmp = __attrs_139922406894096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139922496190256('not', 'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f42395be8c0> name=None at 7f42395be860> -> __attrs_139922406889824
                        __attrs_139922406889824 = _static_139922406893760

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_renameForm:method" value="Rename" />\n            ')

                        # <Static value=<ast.Dict object at 0x7f42395bea40> name=None at 7f42395bda50> -> __attrs_139922406898032
                        __attrs_139922406898032 = _static_139922406894144

                        # <Value 'delete_allowed' (110:121)> -> __condition
                        __token = 6160
                        try:
                            __zt_tmp = __attrs_139922406898032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139922496190256('path', 'delete_allowed', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input class="btn btn-primary mr-2" type="submit" name="manage_cutObjects:method" value="Cut" />')
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f42395bfe80> name=None at 7f42395bef50> -> __attrs_139922406894288
                        __attrs_139922406894288 = _static_139922406899328

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_copyObjects:method" value="Copy" />\n            ')

                        # <Static value=<ast.Dict object at 0x7f42395bfa90> name=None at 7f42395bd750> -> __attrs_139922406892704
                        __attrs_139922406892704 = _static_139922406898320

                        # <Value 'here/cb_dataValid' (112:125)> -> __condition
                        __token = 6415
                        try:
                            __zt_tmp = __attrs_139922406892704
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139922496190256('path', 'here/cb_dataValid', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input class="btn btn-primary mr-2" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                        __append('\n          ')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f42395bfe20> name=None at 7f42395be050> -> __attrs_139922406885120
                    __attrs_139922406885120 = _static_139922406899232

                    # <Value 'delete_allowed' (114:122)> -> __condition
                    __token = 6587
                    try:
                        __zt_tmp = __attrs_139922406885120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139922496190256('path', 'delete_allowed', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_delObjects:method" value="Delete" />')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f42395bef80> name=None at 7f42395beec0> -> __attrs_139922406892464
                    __attrs_139922406892464 = _static_139922406895488

                    # <Value "python:sm.checkPermission('Import/Export objects', context)" (115:135)> -> __condition
                    __token = 6741
                    try:
                        __zt_tmp = __attrs_139922406892464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139922496190256('python', "sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f42395bfc10> name=None at 7f42395bde70> -> __attrs_139922407284240
                    __attrs_139922407284240 = _static_139922406898704

                    # <Value "python: has_order_support and sm.checkPermission('Manage properties', context)" (117:50)> -> __condition
                    __token = 6856
                    try:
                        __zt_tmp = __attrs_139922407284240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139922496190256('python', " has_order_support and sm.checkPermission('Manage properties', context)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="input-group">\n            ')

                        # <Static value=<ast.Dict object at 0x7f423961cac0> name=None at 7f423961cfd0> -> __attrs_139922407282656
                        __attrs_139922407282656 = _static_139922407279296

                        # <select ... (0:0)
                        # --------------------------------------------------------
                        __append('<select class="form-control btn btn-primary" name="delta:int">\n              ')

                        # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407279104
                        __attrs_139922407279104 = _static_139922496178928
                        __backup_val_139922406717664 = get('val', __marker)

                        # <Value 'python:range(1,min(5,len(obs)))' (119:38)> -> __iterator
                        __token = 7050
                        try:
                            __zt_tmp = __attrs_139922407279104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_139922496190256('python', 'range(1,min(5,len(obs)))', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        (__iterator, ____index_139922407278528, ) = getname('repeat')('val', __iterator)
                        econtext['val'] = None
                        for __item in __iterator:
                            econtext['val'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option>')

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407285536
                            __default_139922407285536 = _DEFAULT_MARKER

                            # <Value 'val' (119:84)> -> __cache_139922407286640
                            __token = 7096
                            try:
                                __zt_tmp = __attrs_139922407279104
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139922407286640 = _static_139922496190256('path', 'val', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                            # <BinOp left=<Value 'val' (119:84)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f423961e110> -> __condition
                            __expression = __cache_139922407286640

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_139922407286640
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>')
                            ____index_139922407278528 -= 1
                            if (____index_139922407278528 > 0):
                                __append('\n              ')
                        if (__backup_val_139922406717664 is __marker):
                            del econtext['val']
                        else:
                            econtext['val'] = __backup_val_139922406717664
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922407281264
                        __attrs_139922407281264 = _static_139922496178928
                        __backup_val_139922406710320 = get('val', __marker)

                        # <Value 'python:range(5,len(obs),5)' (120:38)> -> __iterator
                        __token = 7142
                        try:
                            __zt_tmp = __attrs_139922407281264
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_139922496190256('python', 'range(5,len(obs),5)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        (__iterator, ____index_139922407286736, ) = getname('repeat')('val', __iterator)
                        econtext['val'] = None
                        for __item in __iterator:
                            econtext['val'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option>')

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922407281120
                            __default_139922407281120 = _DEFAULT_MARKER

                            # <Value 'val' (120:79)> -> __cache_139922407277664
                            __token = 7183
                            try:
                                __zt_tmp = __attrs_139922407281264
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139922407277664 = _static_139922496190256('path', 'val', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                            # <BinOp left=<Value 'val' (120:79)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f423961f4f0> -> __condition
                            __expression = __cache_139922407277664

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_139922407277664
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>')
                            ____index_139922407286736 -= 1
                            if (____index_139922407286736 > 0):
                                __append('\n              ')
                        if (__backup_val_139922406710320 is __marker):
                            del econtext['val']
                        else:
                            econtext['val'] = __backup_val_139922406710320
                        __append('\n            </select>\n            ')

                        # <Static value=<ast.Dict object at 0x7f42395ab550> name=None at 7f42395ab4c0> -> __attrs_139922406803248
                        __attrs_139922406803248 = _static_139922406815056

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="input-group-append">\n              ')

                        # <Static value=<ast.Dict object at 0x7f42395a9420> name=None at 7f42395ab850> -> __attrs_139922406813328
                        __attrs_139922406813328 = _static_139922406806560

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_up:method" value="Move up"                 title="Move selected items up" class="btn btn-primary">\n                ')

                        # <Static value=<ast.Dict object at 0x7f42395a95a0> name=None at 7f42395a87f0> -> __attrs_139922406806032
                        __attrs_139922406806032 = _static_139922406806944

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-up"></i>\n              </button>\n              ')

                        # <Static value=<ast.Dict object at 0x7f42395a9a80> name=None at 7f42395aa8c0> -> __attrs_139922406804544
                        __attrs_139922406804544 = _static_139922406808192

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_down:method" value="Move down"                 title="Move selected items down" class="btn btn-primary rounded-right">\n                ')

                        # <Static value=<ast.Dict object at 0x7f42395aaf50> name=None at 7f42395ab3d0> -> __attrs_139922406802480
                        __attrs_139922406802480 = _static_139922406813520

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-down"></i>\n              </button>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x7f42395abf40> name=None at 7f42395ab4f0> -> __attrs_139922406807184
                        __attrs_139922406807184 = _static_139922406817600

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_to_top:method" value="Move to top"               title="Move selected items to top" class="btn btn-primary ml-2 mr-2">\n              ')

                        # <Static value=<ast.Dict object at 0x7f42395a8130> name=None at 7f42395a9c30> -> __attrs_139922406805168
                        __attrs_139922406805168 = _static_139922406801712

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-up" style="border-top: 0.2rem solid silver;"></i>\n            </button>\n            ')

                        # <Static value=<ast.Dict object at 0x7f42395a97e0> name=None at 7f42395a8970> -> __attrs_139922408315760
                        __attrs_139922408315760 = _static_139922406807520

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_to_bottom:method" value="Move to bottom"                title="Move selected items to bottom" class="btn btn-primary">\n              ')

                        # <Static value=<ast.Dict object at 0x7f423971a4a0> name=None at 7f423971bd60> -> __attrs_139922408318592
                        __attrs_139922408318592 = _static_139922408318112

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-down" style="border-bottom: 0.2rem solid silver;"></i>\n            </button>\n          </div>')
                    __append('\n        </div>\n\n      </div>')
                if (__backup_delete_allowed_139922406671360 is __marker):
                    del econtext['delete_allowed']
                else:
                    econtext['delete_allowed'] = __backup_delete_allowed_139922406671360
                __append('\n    ')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406885360
            __attrs_139922406885360 = _static_139922496178928

            # <Value 'not:obs' (146:26)> -> __condition
            __token = 8444
            try:
                __zt_tmp = __attrs_139922406885360
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139922496190256('not', 'obs', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f4239719060> name=None at 7f4239719e10> -> __attrs_139922408313552
                __attrs_139922408313552 = _static_139922408312928

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info mt-4 mb-4">\n        There are currently no items in ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408316288
                __attrs_139922408316288 = _static_139922496178928

                # <em ... (0:0)
                # --------------------------------------------------------
                __append('<em>')

                # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408310480
                __default_139922408310480 = _DEFAULT_MARKER

                # <Value 'here/title_or_id' (148:57)> -> __cache_139922408319360
                __token = 8558
                try:
                    __zt_tmp = __attrs_139922408316288
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139922408319360 = _static_139922496190256('path', 'here/title_or_id', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                # <BinOp left=<Value 'here/title_or_id' (148:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f423971baf0> -> __condition
                __expression = __cache_139922408319360

                # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139922408319360
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</em>.\n      </div>\n      ')

                # <Static value=<ast.Dict object at 0x7f4239719a50> name=None at 7f4239718400> -> __attrs_139922408314224
                __attrs_139922408314224 = _static_139922408315472

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group">\n        ')

                # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408316816
                __attrs_139922408316816 = _static_139922496178928

                # <Value 'not:context/dontAllowCopyAndPaste|nothing' (151:35)> -> __condition
                __token = 8662
                try:
                    __zt_tmp = __attrs_139922408316816
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('not', 'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f4239718730> name=None at 7f423971ae90> -> __attrs_139922408316048
                    __attrs_139922408316048 = _static_139922408310576

                    # <Value 'here/cb_dataValid' (152:118)> -> __condition
                    __token = 8824
                    try:
                        __zt_tmp = __attrs_139922408316048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139922496190256('path', 'here/cb_dataValid', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                    __append('\n        ')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f4239718cd0> name=None at 7f423971b5e0> -> __attrs_139922408310768
                __attrs_139922408310768 = _static_139922408312016

                # <Value "python:sm.checkPermission('Import/Export objects', context)" (154:128)> -> __condition
                __token = 9000
                try:
                    __zt_tmp = __attrs_139922408310768
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('python', "sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input class="btn btn-primary" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                __append('\n      </div>\n    ')
            __append('\n  </form>')
            if (__backup_my_url_139922406676544 is __marker):
                del econtext['my_url']
            else:
                econtext['my_url'] = __backup_my_url_139922406676544
            if (__backup_obs_139922406676304 is __marker):
                del econtext['obs']
            else:
                econtext['obs'] = __backup_obs_139922406676304
            if (__backup_rkey_alt_up_139922406670496 is __marker):
                del econtext['rkey_alt_up']
            else:
                econtext['rkey_alt_up'] = __backup_rkey_alt_up_139922406670496
            if (__backup_rkey_alt_139922406676208 is __marker):
                del econtext['rkey_alt']
            else:
                econtext['rkey_alt'] = __backup_rkey_alt_139922406676208
            if (__backup_rkey_139922406675728 is __marker):
                del econtext['rkey']
            else:
                econtext['rkey'] = __backup_rkey_139922406675728
            if (__backup_skey_139922406673712 is __marker):
                del econtext['skey']
            else:
                econtext['skey'] = __backup_skey_139922406673712
            if (__backup_default_sort_139922406682928 is __marker):
                del econtext['default_sort']
            else:
                econtext['default_sort'] = __backup_default_sort_139922406682928
            if (__backup_sm_139922406809008 is __marker):
                del econtext['sm']
            else:
                econtext['sm'] = __backup_sm_139922406809008
            if (__backup_has_order_support_139922406814816 is __marker):
                del econtext['has_order_support']
            else:
                econtext['has_order_support'] = __backup_has_order_support_139922406814816
            __append('\n\n</main>\n\n\n')

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408323392
            __attrs_139922408323392 = _static_139922496178928

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script>\n  // +++++++++++++++++++++++++++\n  // Item  Selection\n  // +++++++++++++++++++++++++++\n  function checkbox_all() {\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    // Toggle Highlighting CSS-Class\n    if (document.getElementById(\'checkAll\').checked) {\n      $(\'table.objectItems tbody tr\').addClass(\'checked\');\n    } else {\n      $(\'table.objectItems tbody tr\').removeClass(\'checked\');\n    };\n    // Set Checkbox like checkAll-Box\n    for (i = 0; i < checkboxes.length; i++) {\n      checkboxes[i].checked = document.getElementById(\'checkAll\').checked;\n    }\n  };\n\n  function zmicontrols_visible() {\n    var zmicontrols = $(\'form#objectItems .zmi-controls\');\n    var zmicontrols_top = zmicontrols.offset().top;\n    var zmicontrols_bottom = zmicontrols_top + zmicontrols.outerHeight();\n    var viewport_top = $(window).scrollTop();\n    var viewport_bottom = viewport_top + $(window).height();\n    return zmicontrols_bottom > viewport_top && zmicontrols_top < viewport_bottom;\n  };\n\n  function select_objectitem(ob) {\n    ob.parent().parent().toggleClass(\'checked\');\n    if ( !zmicontrols_visible() ) {\n      $(\'form#objectItems\').addClass(\'selected\');\n    }\n    // Anything selected?\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    var selected = false;\n    for (i = 0; i < checkboxes.length; i++) {\n      if ( checkboxes[i].checked ) {\n        selected = true;\n        break;\n      }\n    }\n    if ( !selected ) {\n      $(\'form#objectItems\').removeClass(\'selected\');\n      console.log(\'form#objectItems removed .selected\');\n    }\n  };\n\n\n  $(function () {\n\n    // +++++++++++++++++++++++++++\n    // Icon Tooltips\n    // +++++++++++++++++++++++++++\n    $(\'td.zmi-object-type i\').tooltip({\n      \'placement\': \'top\'\n    });\n\n    // +++++++++++++++++++++++++++\n    // Tablefilter/Search Element\n    // +++++++++++++++++++++++++++\n\n    function isModifierKeyPressed(event) {\n      return event.altKey ||\n        event.ctrlKey ||\n        event.metaKey;\n    }\n\n    $(document).keypress(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      // Set Focus to Tablefilter only when Modal Dialog is not Shown\n      if (!$(\'#zmi-modal\').hasClass(\'show\')) {\n        $(\'#tablefilter\').focus();\n        // Prevent Submitting a form by hitting Enter\n        // https://stackoverflow.com/questions/895171/prevent-users-from-submitting-a-form-by-hitting-enter\n        if (event.which == 13) {\n          event.preventDefault();\n          return false;\n        };\n      };\n    })\n\n    $(\'#tablefilter\').keyup(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      var tablefilter = $(this).val();\n      if (event.which == 13) {\n        if (1 === $(\'tbody tr:visible\').length) {\n          window.location.href = $(\'tbody tr:visible a\').attr(\'href\');\n        } else {\n          window.location.href = \'manage_findForm?btn_submit=Find&search_sub:int=1&obj_ids%3Atokens=\' + tablefilter;\n        }\n        event.preventDefault();\n      };\n      $(\'table.objectItems\').find("tbody tr").hide();\n      $(\'table.objectItems\').find("tbody tr td.zmi-object-id a:contains(" + tablefilter + ")").closest(\'tbody tr\').show();\n    });\n\n    // +++++++++++++++++++++++++++\n    // OBJECTIST SORTING: Show skey=meta_type\n    // +++++++++++++++++++++++++++\n    let searchParams = new URLSearchParams(window.location.search);\n    if (searchParams.get(\'skey\') == \'meta_type\') {\n      $(\'td.zmi-object-type i\').each(function () {\n        $(this).parent().parent().find(\'td.zmi-object-id\').prepend(\'')

            # <Static value=<ast.Dict object at 0x7f423971bdf0> name=None at 7f423971ad70> -> __attrs_139922408313408
            __attrs_139922408313408 = _static_139922408324592

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="zmi-typename_show">\' + $(this).text() + \'</span>\')\n      });\n      $(\'th.zmi-object-id\').addClass(\'zmi-typename_show\');\n    }\n\n  });\n\n</script>\n\n')

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922406948384
            __attrs_139922406948384 = _static_139922496178928

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922406947520
            __default_139922406947520 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (281:31)> -> __cache_139922408318880
            __token = 12921
            try:
                __zt_tmp = __attrs_139922406948384
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139922408318880 = _static_139922496190256('path', 'here/manage_page_footer', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (281:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42397182b0> -> __condition
            __expression = __cache_139922408318880

            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139922408318880
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }