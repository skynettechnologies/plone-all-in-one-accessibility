# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.z3cform-4.2.1-py3.10.egg/plone/app/z3cform/templates/image_input.pt'

__tokens = {38: ('view/download_url', 2, 20), 70: (' python: view.value is not Non', 3, 13), 115: ('n view/acti', 4, 12), 149: ('ge view/allow_nocha', 5, 19), 185: ('ype view/file_content_', 6, 12), 220: ('icon view/file', 7, 7), 251: ('ename view/fi', 8, 10), 311: ('view/id', 11, 10), 332: (' view/styl', 12, 12), 356: ('e view/tit', 13, 11), 379: ('ng view/l', 14, 9), 404: ('ick view/onc', 15, 11), 435: ('lick view/ondbl', 16, 13), 470: ('edown view/onmou', 17, 13), 504: ('ouseup view/on', 18, 10), 538: ('useover view/onm', 19, 11), 574: ('ousemove view/on', 20, 10), 609: ('nmouseout view/', 21, 8), 643: ('onkeypress view', 22, 7), 676: ('  onkeydown vi', 23, 5), 706: ('     onkeyup', 24, 2), 734: ('      onfocu', 25, 1), 761: ('\n       onb', 25, 28), 789: ('       onchan', 27, 0), 819: ('\n       reado', 27, 30), 850: ('\n       access', 28, 30), 881: ('y;\n       ons', 29, 30), 990: ('view/file_upload_id', 35, 18), 1048: ('up_id', 37, 25), 1076: ('${view/name}.file_upload_id', 39, 17), 1078: ('view/name', 39, 19), 1148: ('${up_id}', 41, 18), 1150: ('up_id', 41, 20), 1275: ('${view/value/filename}', 45, 8), 1277: ('view/value/filename', 45, 10), 1345: ("python:exists and download_url and action=='nochange'", 48, 23), 1439: ('download_url', 50, 14), 1497: ('view/thumb_tag', 52, 34), 1587: ('icon', 56, 24), 1654: (' doc_typ', 59, 14), 1634: ('icon', 58, 15), 1680: ('e filena', 60, 15), 1778: ('download_url', 65, 14), 1730: ('filename', 63, 20), 1885: ('doc_type', 69, 38), 1923: ('doc_type', 70, 27), 2055: ('view/file_size', 74, 21), 2110: ('sizekb', 76, 25), 2212: ('allow_nochange', 81, 24), 2402: ('string:${view/name}.action', 87, 20), 2447: (' string:${view/id}-nochang', 88, 17), 2497: ("k string:document.getElementById('${view/id}-input').disabled=tr", 89, 21), 2585: ("ed python:'checked' if action == 'nochange' else N", 90, 20), 2751: ('string:${view/id}-nochange', 95, 19), 2933: ('not:view/field/required', 101, 24), 3106: ('string:${view/name}.action', 107, 20), 3151: (' string:${view/id}-remov', 108, 17), 3199: ("k string:document.getElementById('${view/id}-input').disabled=tr", 109, 21), 3287: ("ed python:'checked' if action == 'remove' else N", 110, 20), 3451: ('string:${view/id}-remove', 115, 19), 3756: ('string:${view/name}.action', 126, 20), 3801: (' string:${view/id}-replac', 127, 17), 3850: ("k string:document.getElementById('${view/id}-input').disabled=fal", 128, 21), 3939: ("ed python:'checked' if action == 'replace' else N", 129, 20), 4104: ('string:${view/id}-replace', 134, 19), 4346: ('string:${view/id}-input', 144, 14), 4386: (' view/nam', 145, 15), 4416: ("d python:view.required and 'required' or No", 146, 18), 4476: ('ze view/s', 147, 13), 4506: ('led view/disa', 148, 16), 4541: ('ngth view/maxl', 149, 16), 4637: ("python:allow_nochange and action != 'replace'", 154, 25), 4707: ("string:document.getElementById('${view/id}-input').disabled=true;", 155, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139856821413216 = {'type': 'text/javascript', }
_static_139856822169136 = {'class': 'form-control', 'type': 'file', 'id': 'string:${view/id}-input', 'name': 'view/name', 'required': "python:view.required and 'required' or None", 'size': 'view/size', 'disabled': 'view/disabled', 'maxlength': 'view/maxlength', }
_static_139856821414128 = {'class': 'form-check-label', 'for': 'string:${view/id}-replace', }
_static_139856821405152 = {'class': 'form-check-input', 'type': 'radio', 'value': 'replace', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-replace', 'onclick': "string:document.getElementById('${view/id}-input').disabled=false", 'checked': "python:'checked' if action == 'replace' else None", }
_static_139856822171152 = {'class': 'form-check', }
_static_139856822161024 = {'class': 'form-check-label', 'for': 'string:${view/id}-remove', }
_static_139856822158192 = {'class': 'form-check-input', 'type': 'radio', 'value': 'remove', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-remove', 'onclick': "string:document.getElementById('${view/id}-input').disabled=true", 'checked': "python:'checked' if action == 'remove' else None", }
_static_139856822169712 = {'class': 'form-check', }
_static_139856822172208 = {'class': 'form-check-label', 'for': 'string:${view/id}-nochange', }
_static_139856822166256 = {'class': 'form-check-input', 'type': 'radio', 'value': 'nochange', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-nochange', 'onclick': "string:document.getElementById('${view/id}-input').disabled=true", 'checked': "python:'checked' if action == 'nochange' else None", }
_static_139856822158288 = {'class': 'form-check', }
_static_139856822224928 = {'class': 'discreet', }
_static_139856820438208 = {'href': 'download_url', }
_static_139856820440656 = {'alt': '', 'src': '', 'title': 'filename', }
_static_139856820445696 = {'href': 'download_url', }
_static_139856823378192 = {'name': '${view/name}.file_upload_id', 'type': 'hidden', 'value': '${up_id}', }
_static_139856913889840 = {}
_static_139856914195856 = __C2ZContextWrapper
_static_139856914196144 = __compile_zt_expr
_static_139856821974448 = {'id': 'view/id', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'accesskey': 'view/accesskey', 'onselect': 'view/onselect', }

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

            # <Static value=<ast.Dict object at 0x7f32f43175b0> name=None at 7f32f4314ca0> -> __attrs_139856823371184
            __attrs_139856823371184 = _static_139856821974448
            __backup_download_url_139856820495904 = get('download_url', __marker)

            # <Value 'view/download_url' (2:20)> -> __value
            __token = 38
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('path', 'view/download_url', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['download_url'] = __value
            __backup_exists_139856820723600 = get('exists', __marker)

            # <Value 'python: view.value is not None' (3:13)> -> __value
            __token = 70
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('python', ' view.value is not None', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['exists'] = __value
            __backup_action_139856822324912 = get('action', __marker)

            # <Value 'view/action' (4:12)> -> __value
            __token = 115
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('path', 'view/action', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['action'] = __value
            __backup_allow_nochange_139856823380688 = get('allow_nochange', __marker)

            # <Value 'view/allow_nochange' (5:19)> -> __value
            __token = 149
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('path', 'view/allow_nochange', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['allow_nochange'] = __value
            __backup_doc_type_139856822396352 = get('doc_type', __marker)

            # <Value 'view/file_content_type' (6:12)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('path', 'view/file_content_type', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['doc_type'] = __value
            __backup_icon_139856822389008 = get('icon', __marker)

            # <Value 'view/file_icon' (7:7)> -> __value
            __token = 220
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('path', 'view/file_icon', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['icon'] = __value
            __backup_filename_139856822173648 = get('filename', __marker)

            # <Value 'view/filename' (8:10)> -> __value
            __token = 251
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('path', 'view/filename', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['filename'] = __value
            __previous_i18n_domain_139856823373680 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823375840
            __default_139856823375840 = _DEFAULT_MARKER

            # <Substitution 'view/id' (11:10)> -> __attr_id
            __token = 311
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_139856914196144('path', 'view/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823380448
            __default_139856823380448 = _DEFAULT_MARKER

            # <Substitution 'view/style' (12:12)> -> __attr_style
            __token = 332
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_139856914196144('path', 'view/style', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823373008
            __default_139856823373008 = _DEFAULT_MARKER

            # <Substitution 'view/title' (13:11)> -> __attr_title
            __token = 356
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_139856914196144('path', 'view/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823372000
            __default_139856823372000 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (14:9)> -> __attr_lang
            __token = 379
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_139856914196144('path', 'view/lang', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823380928
            __default_139856823380928 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (15:11)> -> __attr_onclick
            __token = 404
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_139856914196144('path', 'view/onclick', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823370224
            __default_139856823370224 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (16:13)> -> __attr_ondblclick
            __token = 435
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_139856914196144('path', 'view/ondblclick', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823376608
            __default_139856823376608 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (17:13)> -> __attr_onmousedown
            __token = 470
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_139856914196144('path', 'view/onmousedown', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823370896
            __default_139856823370896 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (18:10)> -> __attr_onmouseup
            __token = 504
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_139856914196144('path', 'view/onmouseup', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823377424
            __default_139856823377424 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (19:11)> -> __attr_onmouseover
            __token = 538
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_139856914196144('path', 'view/onmouseover', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823376752
            __default_139856823376752 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (20:10)> -> __attr_onmousemove
            __token = 574
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_139856914196144('path', 'view/onmousemove', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823385152
            __default_139856823385152 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (21:8)> -> __attr_onmouseout
            __token = 609
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_139856914196144('path', 'view/onmouseout', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823377952
            __default_139856823377952 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (22:7)> -> __attr_onkeypress
            __token = 643
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_139856914196144('path', 'view/onkeypress', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823378672
            __default_139856823378672 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (23:5)> -> __attr_onkeydown
            __token = 676
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_139856914196144('path', 'view/onkeydown', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823372480
            __default_139856823372480 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (24:2)> -> __attr_onkeyup
            __token = 706
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_139856914196144('path', 'view/onkeyup', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823374112
            __default_139856823374112 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (25:1)> -> __attr_onfocus
            __token = 734
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_139856914196144('path', 'view/onfocus', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823385872
            __default_139856823385872 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (25:28)> -> __attr_onblur
            __token = 761
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_139856914196144('path', 'view/onblur', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823372720
            __default_139856823372720 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (27:0)> -> __attr_onchange
            __token = 789
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_139856914196144('path', 'view/onchange', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823373440
            __default_139856823373440 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (27:30)> -> __attr_readonly
            __token = 819
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_139856914196144('path', 'view/readonly', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = None
            else:
                if __attr_readonly:
                    __attr_readonly = 'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823379392
            __default_139856823379392 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (28:30)> -> __attr_accesskey
            __token = 850
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_139856914196144('path', 'view/accesskey', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823378912
            __default_139856823378912 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (29:30)> -> __attr_onselect
            __token = 881
            try:
                __zt_tmp = __attrs_139856823371184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_139856914196144('path', 'view/onselect', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823374352
            __attrs_139856823374352 = _static_139856913889840
            __backup_up_id_139856822229728 = get('up_id', __marker)

            # <Value 'view/file_upload_id' (35:18)> -> __value
            __token = 990
            try:
                __zt_tmp = __attrs_139856823374352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139856914196144('path', 'view/file_upload_id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            econtext['up_id'] = __value

            # <Value 'up_id' (37:25)> -> __condition
            __token = 1048
            try:
                __zt_tmp = __attrs_139856823374352
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139856914196144('path', 'up_id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f32f446e110> name=None at 7f32f446f430> -> __attrs_139856823291280
                __attrs_139856823291280 = _static_139856823378192

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823377568
                __default_139856823377568 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${view/name}.file_upload_id' (39:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f32f446d2a0> -> __attr_name
                __token = 1076
                __token = 1078
                try:
                    __zt_tmp = __attrs_139856823291280
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_139856914196144('path', 'view/name', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_name = ('%s%s' % ((__attr_name if (__attr_name is not None) else ''), '.file_upload_id', ))
                if (__attr_name is None):
                    pass
                else:
                    if (__attr_name is _DEFAULT_MARKER):
                        __attr_name = None
                    else:
                        __tt = type(__attr_name)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_name = str(__attr_name)
                        else:
                            if (__tt is bytes):
                                __attr_name = decode(__attr_name)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_name = __attr_name.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_name)
                                        __attr_name = (str(__attr_name) if (__attr_name is __converted) else __converted)
                                    else:
                                        __attr_name = __attr_name()
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))
                __append(' type="hidden"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823300160
                __default_139856823300160 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${up_id}' (41:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f32f4458c40> -> __attr_value
                __token = 1148
                __token = 1150
                try:
                    __zt_tmp = __attrs_139856823291280
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_139856914196144('path', 'up_id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_value = __attr_value
                if (__attr_value is None):
                    pass
                else:
                    if (__attr_value is _DEFAULT_MARKER):
                        __attr_value = None
                    else:
                        __tt = type(__attr_value)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_value = str(__attr_value)
                        else:
                            if (__tt is bytes):
                                __attr_value = decode(__attr_value)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_value = __attr_value.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_value)
                                        __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                    else:
                                        __attr_value = __attr_value()
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n    ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823301600
                __attrs_139856823301600 = _static_139856913889840

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>\n      ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820447568
                __attrs_139856820447568 = _static_139856913889840
                __stream_139856823295552 = []
                __append_139856823295552 = __stream_139856823295552.append
                __append_139856823295552('Image already uploaded:')
                __msgid_139856823295552 = __re_whitespace(''.join(__stream_139856823295552)).strip()
                if 'image_already_uploaded':
                    __append(translate('image_already_uploaded', mapping=None, default=__msgid_139856823295552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))

                # <Interpolation value=<Substitution '\n        ${view/value/filename}\n    ' (44:90)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f32f4458bb0> -> __content_139857001570544
                __token = 1275
                __token = 1277
                try:
                    __zt_tmp = __attrs_139856823301600
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_139857001570544 = _static_139856914196144('path', 'view/value/filename', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __content_139857001570544 = __quote(__content_139857001570544, '\x00', '&#0;', None, None)
                __content_139857001570544 = ('%s%s%s' % ('\n        ', (__content_139857001570544 if (__content_139857001570544 is not None) else ''), '\n    ', ))
                if (__content_139857001570544 is None):
                    pass
                else:
                    if (__content_139857001570544 is None):
                        __content_139857001570544 = None
                    else:
                        __tt = type(__content_139857001570544)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139857001570544 = str(__content_139857001570544)
                        else:
                            if (__tt is bytes):
                                __content_139857001570544 = decode(__content_139857001570544)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139857001570544 = __content_139857001570544.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139857001570544)
                                        __content_139857001570544 = (str(__content_139857001570544) if (__content_139857001570544 is __converted) else __converted)
                                    else:
                                        __content_139857001570544 = __content_139857001570544()
                if (__content_139857001570544 is not None):
                    __append(__content_139857001570544)
                __append('</span>\n  ')
            if (__backup_up_id_139856822229728 is __marker):
                del econtext['up_id']
            else:
                econtext['up_id'] = __backup_up_id_139856822229728
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823294736
            __attrs_139856823294736 = _static_139856913889840

            # <Value "python:exists and download_url and action=='nochange'" (48:23)> -> __condition
            __token = 1345
            try:
                __zt_tmp = __attrs_139856823294736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139856914196144('python', "exists and download_url and action=='nochange'", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>\n    ')

                # <Static value=<ast.Dict object at 0x7f32f41a2200> name=None at 7f32f41a09a0> -> __attrs_139856820438928
                __attrs_139856820438928 = _static_139856820445696

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820440464
                __default_139856820440464 = _DEFAULT_MARKER

                # <Substitution 'download_url' (50:14)> -> __attr_href
                __token = 1439
                try:
                    __zt_tmp = __attrs_139856820438928
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139856914196144('path', 'download_url', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>\n      ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820446800
                __attrs_139856820446800 = _static_139856913889840

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820446656
                __default_139856820446656 = _DEFAULT_MARKER

                # <Value 'view/thumb_tag' (52:34)> -> __cache_139856820444592
                __token = 1497
                try:
                    __zt_tmp = __attrs_139856820446800
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139856820444592 = _static_139856914196144('path', 'view/thumb_tag', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/thumb_tag' (52:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f41a1d80> -> __condition
                __expression = __cache_139856820444592

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img />')
                else:
                    __content = __cache_139856820444592
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    </a>')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820445456
                __attrs_139856820445456 = _static_139856913889840

                # <br ... (0:0)
                # --------------------------------------------------------
                __append('<br />\n    ')

                # <Static value=<ast.Dict object at 0x7f32f41a0e50> name=None at 7f32f41a0dc0> -> __attrs_139856820443152
                __attrs_139856820443152 = _static_139856820440656

                # <Value 'icon' (56:24)> -> __condition
                __token = 1587
                try:
                    __zt_tmp = __attrs_139856820443152
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('path', 'icon', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820442432
                    __default_139856820442432 = _DEFAULT_MARKER

                    # <Substitution 'doc_type' (59:14)> -> __attr_alt
                    __token = 1654
                    try:
                        __zt_tmp = __attrs_139856820443152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_alt = _static_139856914196144('path', 'doc_type', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_alt is not None):
                        __append((' alt="%s"' % __attr_alt))

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820441280
                    __default_139856820441280 = _DEFAULT_MARKER

                    # <Substitution 'icon' (58:15)> -> __attr_src
                    __token = 1634
                    try:
                        __zt_tmp = __attrs_139856820443152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_src = _static_139856914196144('path', 'icon', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_src is not None):
                        __append((' src="%s"' % __attr_src))

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820452272
                    __default_139856820452272 = _DEFAULT_MARKER

                    # <Substitution 'filename' (60:15)> -> __attr_title
                    __token = 1680
                    try:
                        __zt_tmp = __attrs_139856820443152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_139856914196144('path', 'filename', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f32f41a04c0> name=None at 7f32f41a0c70> -> __attrs_139856822238464
                __attrs_139856822238464 = _static_139856820438208

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820440704
                __default_139856820440704 = _DEFAULT_MARKER

                # <Substitution 'download_url' (65:14)> -> __attr_href
                __token = 1778
                try:
                    __zt_tmp = __attrs_139856822238464
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139856914196144('path', 'download_url', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820446464
                __default_139856820446464 = _DEFAULT_MARKER

                # <Value 'filename' (63:20)> -> __cache_139856820446992
                __token = 1730
                try:
                    __zt_tmp = __attrs_139856822238464
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139856820446992 = _static_139856914196144('path', 'filename', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                # <BinOp left=<Value 'filename' (63:20)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f41a1a20> -> __condition
                __expression = __cache_139856820446992

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Filename')
                else:
                    __content = __cache_139856820446992
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</a>\n    ')

                # <Static value=<ast.Dict object at 0x7f32f4354820> name=None at 7f32f43544c0> -> __attrs_139856822229344
                __attrs_139856822229344 = _static_139856822224928

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="discreet">\n      &mdash;')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822235968
                __attrs_139856822235968 = _static_139856913889840

                # <Value 'doc_type' (69:38)> -> __condition
                __token = 1885
                try:
                    __zt_tmp = __attrs_139856822235968
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('path', 'doc_type', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822238944
                    __attrs_139856822238944 = _static_139856913889840

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822223824
                    __default_139856822223824 = _DEFAULT_MARKER

                    # <Value 'doc_type' (70:27)> -> __cache_139856822235056
                    __token = 1923
                    try:
                        __zt_tmp = __attrs_139856822238944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856822235056 = _static_139856914196144('path', 'doc_type', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'doc_type' (70:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f4355a20> -> __condition
                    __expression = __cache_139856822235056

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >ContentType</span>')
                    else:
                        __content = __cache_139856822235056
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(',')
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822230208
                __attrs_139856822230208 = _static_139856913889840
                __backup_sizekb_139856822179136 = get('sizekb', __marker)

                # <Value 'view/file_size' (74:21)> -> __value
                __token = 2055
                try:
                    __zt_tmp = __attrs_139856822230208
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/file_size', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['sizekb'] = __value

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822230496
                __default_139856822230496 = _DEFAULT_MARKER

                # <Value 'sizekb' (76:25)> -> __cache_139856822237696
                __token = 2110
                try:
                    __zt_tmp = __attrs_139856822230208
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139856822237696 = _static_139856914196144('path', 'sizekb', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                # <BinOp left=<Value 'sizekb' (76:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f43579d0> -> __condition
                __expression = __cache_139856822237696

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >100</span>')
                else:
                    __content = __cache_139856822237696
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                if (__backup_sizekb_139856822179136 is __marker):
                    del econtext['sizekb']
                else:
                    econtext['sizekb'] = __backup_sizekb_139856822179136
                __append('\n    </span>\n  </span>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822238848
            __attrs_139856822238848 = _static_139856913889840

            # <Value 'allow_nochange' (81:24)> -> __condition
            __token = 2212
            try:
                __zt_tmp = __attrs_139856822238848
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139856914196144('path', 'allow_nochange', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f32f43443d0> name=None at 7f32f43446a0> -> __attrs_139856822173168
                __attrs_139856822173168 = _static_139856822158288

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n      ')

                # <Static value=<ast.Dict object at 0x7f32f43462f0> name=None at 7f32f4344e50> -> __attrs_139856822170096
                __attrs_139856822170096 = _static_139856822166256

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-check-input" type="radio" value="nochange"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822159440
                __default_139856822159440 = _DEFAULT_MARKER

                # <Substitution 'string:${view/name}.action' (87:20)> -> __attr_name
                __token = 2402
                try:
                    __zt_tmp = __attrs_139856822170096
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_139856914196144('string', '${view/name}.action', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822158384
                __default_139856822158384 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-nochange' (88:17)> -> __attr_id
                __token = 2447
                try:
                    __zt_tmp = __attrs_139856822170096
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_139856914196144('string', '${view/id}-nochange', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822165680
                __default_139856822165680 = _DEFAULT_MARKER

                # <Substitution "string:document.getElementById('${view/id}-input').disabled=true" (89:21)> -> __attr_onclick
                __token = 2497
                try:
                    __zt_tmp = __attrs_139856822170096
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_onclick = _static_139856914196144('string', "document.getElementById('${view/id}-input').disabled=true", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_onclick is not None):
                    __append((' onclick="%s"' % __attr_onclick))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822167696
                __default_139856822167696 = _DEFAULT_MARKER

                # <Boolean "python:'checked' if action == 'nochange' else None" (90:20)> -> __attr_checked
                __token = 2585
                try:
                    __zt_tmp = __attrs_139856822170096
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_139856914196144('python', "'checked' if action == 'nochange' else None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append(' />\n      ')

                # <Static value=<ast.Dict object at 0x7f32f4347a30> name=None at 7f32f4344ca0> -> __attrs_139856822170816
                __attrs_139856822170816 = _static_139856822172208

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822171056
                __default_139856822171056 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-nochange' (95:19)> -> __attr_for
                __token = 2751
                try:
                    __zt_tmp = __attrs_139856822170816
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_139856914196144('string', '${view/id}-nochange', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append(' >')
                __stream_139856822163088 = []
                __append_139856822163088 = __stream_139856822163088.append
                __append_139856822163088('Keep existing image')
                __msgid_139856822163088 = __re_whitespace(''.join(__stream_139856822163088)).strip()
                if 'image_keep':
                    __append(translate('image_keep', mapping=None, default=__msgid_139856822163088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n    </div>\n    ')

                # <Static value=<ast.Dict object at 0x7f32f4347070> name=None at 7f32f4344cd0> -> __attrs_139856822157424
                __attrs_139856822157424 = _static_139856822169712

                # <Value 'not:view/field/required' (101:24)> -> __condition
                __token = 2933
                try:
                    __zt_tmp = __attrs_139856822157424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('not', 'view/field/required', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f32f4344370> name=None at 7f32f4345f00> -> __attrs_139856822159680
                    __attrs_139856822159680 = _static_139856822158192

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input class="form-check-input" type="radio" value="remove"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822168128
                    __default_139856822168128 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/name}.action' (107:20)> -> __attr_name
                    __token = 3106
                    try:
                        __zt_tmp = __attrs_139856822159680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_139856914196144('string', '${view/name}.action', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822169568
                    __default_139856822169568 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/id}-remove' (108:17)> -> __attr_id
                    __token = 3151
                    try:
                        __zt_tmp = __attrs_139856822159680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139856914196144('string', '${view/id}-remove', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822162512
                    __default_139856822162512 = _DEFAULT_MARKER

                    # <Substitution "string:document.getElementById('${view/id}-input').disabled=true" (109:21)> -> __attr_onclick
                    __token = 3199
                    try:
                        __zt_tmp = __attrs_139856822159680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_onclick = _static_139856914196144('string', "document.getElementById('${view/id}-input').disabled=true", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_onclick is not None):
                        __append((' onclick="%s"' % __attr_onclick))

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822169904
                    __default_139856822169904 = _DEFAULT_MARKER

                    # <Boolean "python:'checked' if action == 'remove' else None" (110:20)> -> __attr_checked
                    __token = 3287
                    try:
                        __zt_tmp = __attrs_139856822159680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_139856914196144('python', "'checked' if action == 'remove' else None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n      ')

                    # <Static value=<ast.Dict object at 0x7f32f4344e80> name=None at 7f32f4344d60> -> __attrs_139856822162320
                    __attrs_139856822162320 = _static_139856822161024

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822162176
                    __default_139856822162176 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/id}-remove' (115:19)> -> __attr_for
                    __token = 3451
                    try:
                        __zt_tmp = __attrs_139856822162320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_139856914196144('string', '${view/id}-remove', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append(' >')
                    __stream_139856822159584 = []
                    __append_139856822159584 = __stream_139856822159584.append
                    __append_139856822159584('Remove existing image')
                    __msgid_139856822159584 = __re_whitespace(''.join(__stream_139856822159584)).strip()
                    if 'image_remove':
                        __append(translate('image_remove', mapping=None, default=__msgid_139856822159584, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n    </div>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f32f4347610> name=None at 7f32f4345570> -> __attrs_139856822165200
                __attrs_139856822165200 = _static_139856822171152

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n      ')

                # <Static value=<ast.Dict object at 0x7f32f428c5e0> name=None at 7f32f428ea10> -> __attrs_139856821412832
                __attrs_139856821412832 = _static_139856821405152

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-check-input" type="radio" value="replace"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821412496
                __default_139856821412496 = _DEFAULT_MARKER

                # <Substitution 'string:${view/name}.action' (126:20)> -> __attr_name
                __token = 3756
                try:
                    __zt_tmp = __attrs_139856821412832
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_139856914196144('string', '${view/name}.action', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821414080
                __default_139856821414080 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-replace' (127:17)> -> __attr_id
                __token = 3801
                try:
                    __zt_tmp = __attrs_139856821412832
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_139856914196144('string', '${view/id}-replace', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821415328
                __default_139856821415328 = _DEFAULT_MARKER

                # <Substitution "string:document.getElementById('${view/id}-input').disabled=false" (128:21)> -> __attr_onclick
                __token = 3850
                try:
                    __zt_tmp = __attrs_139856821412832
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_onclick = _static_139856914196144('string', "document.getElementById('${view/id}-input').disabled=false", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_onclick is not None):
                    __append((' onclick="%s"' % __attr_onclick))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821417680
                __default_139856821417680 = _DEFAULT_MARKER

                # <Boolean "python:'checked' if action == 'replace' else None" (129:20)> -> __attr_checked
                __token = 3939
                try:
                    __zt_tmp = __attrs_139856821412832
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_139856914196144('python', "'checked' if action == 'replace' else None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append(' />\n      ')

                # <Static value=<ast.Dict object at 0x7f32f428e8f0> name=None at 7f32f428c250> -> __attrs_139856821411152
                __attrs_139856821411152 = _static_139856821414128

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821411440
                __default_139856821411440 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-replace' (134:19)> -> __attr_for
                __token = 4104
                try:
                    __zt_tmp = __attrs_139856821411152
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_139856914196144('string', '${view/id}-replace', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append(' >')
                __stream_139856821406256 = []
                __append_139856821406256 = __stream_139856821406256.append
                __append_139856821406256('Replace with new image')
                __msgid_139856821406256 = __re_whitespace(''.join(__stream_139856821406256)).strip()
                if 'image_replace':
                    __append(translate('image_replace', mapping=None, default=__msgid_139856821406256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n    </div>\n  ')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f32f4346e30> name=None at 7f32f4355e70> -> __attrs_139856821407312
            __attrs_139856821407312 = _static_139856822169136

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" type="file"')

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821413888
            __default_139856821413888 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-input' (144:14)> -> __attr_id
            __token = 4346
            try:
                __zt_tmp = __attrs_139856821407312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_139856914196144('string', '${view/id}-input', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821410624
            __default_139856821410624 = _DEFAULT_MARKER

            # <Substitution 'view/name' (145:15)> -> __attr_name
            __token = 4386
            try:
                __zt_tmp = __attrs_139856821407312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_139856914196144('path', 'view/name', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821416000
            __default_139856821416000 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (146:18)> -> __attr_required
            __token = 4416
            try:
                __zt_tmp = __attrs_139856821407312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_139856914196144('python', "view.required and 'required' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821406928
            __default_139856821406928 = _DEFAULT_MARKER

            # <Substitution 'view/size' (147:13)> -> __attr_size
            __token = 4476
            try:
                __zt_tmp = __attrs_139856821407312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_139856914196144('path', 'view/size', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821404432
            __default_139856821404432 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (148:16)> -> __attr_disabled
            __token = 4506
            try:
                __zt_tmp = __attrs_139856821407312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_139856914196144('path', 'view/disabled', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821412736
            __default_139856821412736 = _DEFAULT_MARKER

            # <Substitution 'view/maxlength' (149:16)> -> __attr_maxlength
            __token = 4541
            try:
                __zt_tmp = __attrs_139856821407312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_maxlength = _static_139856914196144('path', 'view/maxlength', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_maxlength is not None):
                __append((' maxlength="%s"' % __attr_maxlength))
            __append(' />\n\n  ')

            # <Static value=<ast.Dict object at 0x7f32f428e560> name=None at 7f32f428d240> -> __attrs_139856821408704
            __attrs_139856821408704 = _static_139856821413216

            # <Value "python:allow_nochange and action != 'replace'" (154:25)> -> __condition
            __token = 4637
            try:
                __zt_tmp = __attrs_139856821408704
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139856914196144('python', "allow_nochange and action != 'replace'", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if __condition:

                # <script ... (0:0)
                # --------------------------------------------------------
                __append('<script type="text/javascript" >')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821412880
                __default_139856821412880 = _DEFAULT_MARKER

                # <Value "string:document.getElementById('${view/id}-input').disabled=true;" (155:23)> -> __cache_139856821409280
                __token = 4707
                try:
                    __zt_tmp = __attrs_139856821408704
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139856821409280 = _static_139856914196144('string', "document.getElementById('${view/id}-input').disabled=true;", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                # <BinOp left=<Value "string:document.getElementById('${view/id}-input').disabled=true;" (155:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f428dc60> -> __condition
                __expression = __cache_139856821409280

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n  ')
                else:
                    __content = __cache_139856821409280
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</script>')
            __append('\n\n</div>')
            __i18n_domain = __previous_i18n_domain_139856823373680
            if (__backup_filename_139856822173648 is __marker):
                del econtext['filename']
            else:
                econtext['filename'] = __backup_filename_139856822173648
            if (__backup_icon_139856822389008 is __marker):
                del econtext['icon']
            else:
                econtext['icon'] = __backup_icon_139856822389008
            if (__backup_doc_type_139856822396352 is __marker):
                del econtext['doc_type']
            else:
                econtext['doc_type'] = __backup_doc_type_139856822396352
            if (__backup_allow_nochange_139856823380688 is __marker):
                del econtext['allow_nochange']
            else:
                econtext['allow_nochange'] = __backup_allow_nochange_139856823380688
            if (__backup_action_139856822324912 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_139856822324912
            if (__backup_exists_139856820723600 is __marker):
                del econtext['exists']
            else:
                econtext['exists'] = __backup_exists_139856820723600
            if (__backup_download_url_139856820495904 is __marker):
                del econtext['download_url']
            else:
                econtext['download_url'] = __backup_download_url_139856820495904
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }