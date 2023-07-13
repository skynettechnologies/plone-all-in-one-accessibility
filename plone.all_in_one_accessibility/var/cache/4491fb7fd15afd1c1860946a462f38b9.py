# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/controlpanel/browser/types.pt'

__tokens = {708: ('context/@@authenticator/token', 21, 27), 802: ('view/type_id', 23, 34), 853: ('string:${context/absolute_url}/@@content-controlpanel', 24, 37), 1063: ('type_id', 27, 74), 1321: ('view/selectable_types', 33, 55), 1488: ('selectable/id', 35, 58), 1563: (" python:type_id == selectable['id'] and 'selected' or Non", 36, 60), 1394: ('selectable/title', 34, 49), 1935: ("python:type_id == '' and 'selected' or None", 43, 53), 2542: ("python:type_id!=''", 57, 42), 2714: ('view/selected_type_description', 61, 39), 2643: ('view/selected_type_description', 60, 37), 3148: ("python:view.is_addable() and 'checked' or None", 71, 55), 3696: ("python:view.is_discussion_allowed() and 'checked' or None", 82, 55), 4221: ("python: view.is_searchable() and 'checked' or None", 93, 55), 4745: ("python: view.is_default_page_type() and 'checked' or None", 103, 55), 5090: ("python:type_id=='Link'", 109, 50), 5388: ("python: view.is_redirect_links_enabled() and 'checked' or None", 115, 57), 6123: ('view/current_versioning_policy', 128, 59), 6211: ('view/versioning_policies', 129, 55), 6295: ('policy/id', 130, 58), 6366: (" python:policy['id']==current_policy and 'selected' or Non", 131, 60), 6476: ('policy/title', 132, 49), 6668: ('string:${context/absolute_url}/@@manage-content-type-portlets?key=${type_id}&_authenticator=${token}', 137, 48), 7061: ('view/current_workflow', 144, 50), 7303: ('current_wf/title', 148, 43), 7581: ('current_wf/description', 155, 35), 7522: ('current_wf/description', 154, 37), 7647: ('desc', 156, 41), 8209: ('view/new_workflow', 166, 52), 8278: ('view/available_workflows', 168, 48), 8491: ("python:wf['id'] == selected_wf and 'selected' or None", 171, 65), 8607: (' wf/i', 172, 61), 8416: ('wf/title', 170, 53), 8855: ("python:selected_wf == '[none]' and 'selected' or None", 178, 57), 9695: ('view/have_new_workflow', 194, 39), 9911: ('view/new_workflow_description', 199, 35), 9845: ('view/new_workflow_description', 198, 37), 9984: ('desc', 200, 41), 10132: ('view/new_workflow', 204, 50), 10191: ('python:view.have_new_workflow() and not view.new_workflow_is_none() and view.new_workflow_is_different()', 205, 40), 10707: ('view/new_workflow_available_states', 214, 57), 11194: ('view/suggested_state_map', 222, 62), 11280: ('repeat/state_map/odd', 223, 59), 11365: ("python:oddrow and 'odd' or 'even'", 224, 62), 11604: ('string:new_wfstates.old_state:records', 227, 72), 11715: (' state_map/old_i', 228, 72), 11800: ('state_map/old_title', 229, 63), 12023: ('string:new_wfstates.new_state:records', 232, 73), 12196: ('new_wf_states', 233, 76), 12342: ('new_state/id', 235, 74), 12432: (" python:new_state['id'] == state_map['suggested_id'] and 'selected' or Non", 236, 76), 12574: ('new_state/title', 237, 65), 13313: ('view/have_new_workflow', 253, 36), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139856822039984 = {'type': 'submit', 'value': 'Cancel', 'name': 'form.button.Cancel', 'class': 'btn btn-secondary', }
_static_139856822037296 = {'type': 'submit', 'value': 'Save', 'name': 'form.button.Save', 'class': 'btn btn-primary', }
_static_139856822040608 = {'class': 'formControls mb-3', }
_static_139856820337824 = {'class': 'alert alert-primary mb-3', 'role': 'status', }
_static_139856820323232 = {'class': 'form-text text-muted', }
_static_139856820491296 = {'value': 'new_state/id', 'selected': "python:new_state['id'] == state_map['suggested_id'] and 'selected' or None", }
_static_139856820489616 = {'class': 'form-select select-widget required choice-field', 'name': 'string:new_wfstates.new_state:records', }
_static_139856820496336 = {'class': 'align-middle', }
_static_139856820498688 = {'type': 'hidden', 'name': 'string:new_wfstates.old_state:records', 'value': 'state_map/old_id', }
_static_139856820502048 = {'class': 'align-middle', }
_static_139856820486544 = {'class': "python:oddrow and 'odd' or 'even'", }
_static_139856820331632 = {'id': 'states', 'class': 'table table-bordered table-striped', }
_static_139856820333072 = {'class': 'form-label', 'for': 'states', }
_static_139856820337536 = {'class': 'field mb-3', }
_static_139856820330624 = {'type': 'hidden', 'name': 'form.workflow.submitted:boolean', 'value': 'True', }
_static_139856820891664 = {'type': 'submit', 'name': 'form.button.SelectWorkflow', 'class': 'btn btn-primary', 'value': 'Change', }
_static_139856820881824 = {'value': '[none]', 'selected': "python:selected_wf == '[none]' and 'selected' or None", }
_static_139856820884512 = {'selected': "python:wf['id'] == selected_wf and 'selected' or None", 'value': 'wf/id', }
_static_139856820888448 = {'onchange': 'form.submit()', 'id': 'workflows', 'class': 'form-select select-widget required choice-field', 'name': 'new_workflow', }
_static_139856820893296 = {'class': 'form-label', 'for': 'new_workflow', }
_static_139856820891040 = {'class': 'field mb-3', }
_static_139856820765312 = {'class': 'form-label', }
_static_139856820770880 = {'class': 'field mb-3', }
_static_139856820769776 = {'href': 'string:${context/absolute_url}/@@manage-content-type-portlets?key=${type_id}&_authenticator=${token}', }
_static_139856820776352 = {'class': 'field mb-3', }
_static_139856820774624 = {'value': 'policy/id', 'selected': "python:policy['id']==current_policy and 'selected' or None", }
_static_139856820778896 = {'class': 'form-select select-widget required choice-field', 'name': 'versionpolicy', }
_static_139856820780144 = {'for': 'versionpolicy', }
_static_139856820536176 = {'class': 'field mb-3', }
_static_139856820539488 = {'for': 'redirect_links', }
_static_139856820537808 = {'id': 'redirect_links', 'type': 'checkbox', 'class': 'noborder', 'name': 'redirect_links:boolean', 'checked': "python: view.is_redirect_links_enabled() and 'checked' or None", }
_static_139856820542944 = {'for': 'default_page_type', }
_static_139856820547744 = {'id': 'default_page_type', 'type': 'checkbox', 'class': 'noborder', 'name': 'default_page_type', 'checked': "python: view.is_default_page_type() and 'checked' or None", }
_static_139856820548416 = {'for': 'searchable', }
_static_139856820545248 = {'id': 'searchable', 'type': 'checkbox', 'class': 'noborder', 'name': 'searchable', 'checked': "python: view.is_searchable() and 'checked' or None", }
_static_139856820541552 = {'for': 'allow_discussion', }
_static_139856820993952 = {'id': 'allow_discussion', 'type': 'checkbox', 'class': 'noborder', 'name': 'allow_discussion:boolean', 'checked': "python:view.is_discussion_allowed() and 'checked' or None", }
_static_139856820989872 = {'for': 'addable', }
_static_139856820990736 = {'id': 'addable', 'type': 'checkbox', 'class': 'noborder', 'name': 'addable:boolean', 'checked': "python:view.is_addable() and 'checked' or None", }
_static_139856820985360 = {'class': 'field mb-3', }
_static_139856820984304 = {'class': 'text-muted', }
_static_139856820980992 = {'type': 'submit', 'name': 'form.button.SelectContentType', 'class': 'btn btn-primary', 'value': 'Change', }
_static_139856822072512 = {'value': '', 'selected': "python:type_id == '' and 'selected' or None", }
_static_139856820986464 = {'value': 'selectable/id', 'selected': "python:type_id == selectable['id'] and 'selected' or None", }
_static_139856822075344 = {'name': 'type_id', 'class': 'form-select select-widget required choice-field', 'onchange': 'form.submit()', }
_static_139856822075104 = {'class': 'field mb-3', }
_static_139856822069008 = {'type': 'hidden', 'name': 'old_type_id', 'value': 'type_id', }
_static_139856822067040 = {'type': 'hidden', 'name': 'form.submitted:boolean', 'value': 'True', }
_static_139856822061520 = {'method': 'post', 'action': 'string:${context/absolute_url}/@@content-controlpanel', }
_static_139856914195856 = __C2ZContextWrapper
_static_139856914196144 = __compile_zt_expr
_static_139856822063248 = {'id': 'content-core', }
_static_139856822062576 = {'class': 'lead', }
_static_139856820449392 = 'master'
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

            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820452224
            __attrs_139856820452224 = _static_139856913889840
            __previous_i18n_domain_139856820450880 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139856871219200 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f32f41a3070> name=None at 7f32f41a3cd0> -> __value
            __value = _static_139856820449392
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820438304
                __attrs_139856820438304 = _static_139856913889840
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822060224
                __attrs_139856822060224 = _static_139856913889840

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n        ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822060656
                __attrs_139856822060656 = _static_139856913889840

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>')
                __stream_139856822059840 = []
                __append_139856822059840 = __stream_139856822059840.append
                __append_139856822059840('Content Settings')
                __msgid_139856822059840 = __re_whitespace(''.join(__stream_139856822059840)).strip()
                if 'heading_type_settings':
                    __append(translate('heading_type_settings', mapping=None, default=__msgid_139856822059840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n        ')

                # <Static value=<ast.Dict object at 0x7f32f432cdf0> name=None at 7f32f432cbe0> -> __attrs_139856822062288
                __attrs_139856822062288 = _static_139856822062576

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_139856822061184 = []
                __append_139856822061184 = __stream_139856822061184.append
                __append_139856822061184('\n            Workflow, visibility and versioning settings for your content types.\n        ')
                __msgid_139856822061184 = __re_whitespace(''.join(__stream_139856822061184)).strip()
                if 'description_types_setup':
                    __append(translate('description_types_setup', mapping=None, default=__msgid_139856822061184, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n    </header>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f32f432d090> name=None at 7f32f432d060> -> __attrs_139856822063872
                __attrs_139856822063872 = _static_139856822063248
                __backup_token_139856823415040 = get('token', __marker)

                # <Value 'context/@@authenticator/token' (21:27)> -> __value
                __token = 708
                try:
                    __zt_tmp = __attrs_139856822063872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'context/@@authenticator/token', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['token'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n        ')

                # <Static value=<ast.Dict object at 0x7f32f432c9d0> name=None at 7f32f432e320> -> __attrs_139856822064784
                __attrs_139856822064784 = _static_139856822061520
                __backup_type_id_139856823415328 = get('type_id', __marker)

                # <Value 'view/type_id' (23:34)> -> __value
                __token = 802
                try:
                    __zt_tmp = __attrs_139856822064784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/type_id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['type_id'] = __value

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form method="post"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822068096
                __default_139856822068096 = _DEFAULT_MARKER

                # <Substitution 'string:${context/absolute_url}/@@content-controlpanel' (24:37)> -> __attr_action
                __token = 853
                try:
                    __zt_tmp = __attrs_139856822064784
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_139856914196144('string', '${context/absolute_url}/@@content-controlpanel', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append('>\n\n            ')

                # <Static value=<ast.Dict object at 0x7f32f432df60> name=None at 7f32f432e890> -> __attrs_139856822065984
                __attrs_139856822065984 = _static_139856822067040

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="form.submitted:boolean" value="True" />\n            ')

                # <Static value=<ast.Dict object at 0x7f32f432e710> name=None at 7f32f432e620> -> __attrs_139856822065936
                __attrs_139856822065936 = _static_139856822069008

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="old_type_id"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822070352
                __default_139856822070352 = _DEFAULT_MARKER

                # <Substitution 'type_id' (27:74)> -> __attr_value
                __token = 1063
                try:
                    __zt_tmp = __attrs_139856822065936
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_139856914196144('path', 'type_id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n\n            ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822065168
                __attrs_139856822065168 = _static_139856913889840

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset>\n                ')

                # <Static value=<ast.Dict object at 0x7f32f432fee0> name=None at 7f32f432fe80> -> __attrs_139856822072848
                __attrs_139856822072848 = _static_139856822075104

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="field mb-3">\n                    ')

                # <Static value=<ast.Dict object at 0x7f32f432ffd0> name=None at 7f32f432f310> -> __attrs_139856822069824
                __attrs_139856822069824 = _static_139856822075344

                # <select ... (0:0)
                # --------------------------------------------------------
                __append('<select name="type_id" class="form-select select-widget required choice-field" onchange="form.submit()">\n\n                        ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822066896
                __attrs_139856822066896 = _static_139856913889840
                __backup_selectable_139856822397840 = get('selectable', __marker)

                # <Value 'view/selectable_types' (33:55)> -> __iterator
                __token = 1321
                try:
                    __zt_tmp = __attrs_139856822066896
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139856914196144('path', 'view/selectable_types', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                (__iterator, ____index_139856822062000, ) = getname('repeat')('selectable', __iterator)
                econtext['selectable'] = None
                for __item in __iterator:
                    econtext['selectable'] = __item
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x7f32f4226260> name=None at 7f32f4226230> -> __attrs_139856820986992
                    __attrs_139856820986992 = _static_139856820986464

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820982000
                    __default_139856820982000 = _DEFAULT_MARKER

                    # <Substitution 'selectable/id' (35:58)> -> __attr_value
                    __token = 1488
                    try:
                        __zt_tmp = __attrs_139856820986992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139856914196144('path', 'selectable/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820990016
                    __default_139856820990016 = _DEFAULT_MARKER

                    # <Boolean "python:type_id == selectable['id'] and 'selected' or None" (36:60)> -> __attr_selected
                    __token = 1563
                    try:
                        __zt_tmp = __attrs_139856820986992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_139856914196144('python', "type_id == selectable['id'] and 'selected' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = 'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((' selected="%s"' % __attr_selected))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822068672
                    __default_139856822068672 = _DEFAULT_MARKER

                    # <Value 'selectable/title' (34:49)> -> __cache_139856822072752
                    __token = 1394
                    try:
                        __zt_tmp = __attrs_139856820986992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856822072752 = _static_139856914196144('path', 'selectable/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'selectable/title' (34:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f432f4f0> -> __condition
                    __expression = __cache_139856822072752

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                                    Content type\n                            ')
                    else:
                        __content = __cache_139856822072752
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>\n                        ')
                    ____index_139856822062000 -= 1
                    if (____index_139856822062000 > 0):
                        __append('')
                if (__backup_selectable_139856822397840 is __marker):
                    del econtext['selectable']
                else:
                    econtext['selectable'] = __backup_selectable_139856822397840
                __append('\n                        ')

                # <Static value=<ast.Dict object at 0x7f32f432f4c0> name=None at 7f32f432ead0> -> __attrs_139856820981856
                __attrs_139856820981856 = _static_139856822072512

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option value=""')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820986272
                __default_139856820986272 = _DEFAULT_MARKER

                # <Boolean "python:type_id == '' and 'selected' or None" (43:53)> -> __attr_selected
                __token = 1935
                try:
                    __zt_tmp = __attrs_139856820981856
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_selected = _static_139856914196144('python', "type_id == '' and 'selected' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if (__attr_selected is _DEFAULT_MARKER):
                    __attr_selected = None
                else:
                    if __attr_selected:
                        __attr_selected = 'selected'
                    else:
                        __attr_selected = None
                if (__attr_selected is not None):
                    __append((' selected="%s"' % __attr_selected))
                __append('>')
                __stream_139856822073568 = []
                __append_139856822073568 = __stream_139856822073568.append
                __append_139856822073568('\n                        (Default)\n                        ')
                __msgid_139856822073568 = __re_whitespace(''.join(__stream_139856822073568)).strip()
                if 'label_default_type':
                    __append(translate('label_default_type', mapping=None, default=__msgid_139856822073568, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</option>\n                    </select>\n                    ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820981616
                __attrs_139856820981616 = _static_139856913889840

                # <noscript ... (0:0)
                # --------------------------------------------------------
                __append('<noscript>\n                        ')

                # <Static value=<ast.Dict object at 0x7f32f4224d00> name=None at 7f32f4224d30> -> __attrs_139856820978016
                __attrs_139856820978016 = _static_139856820980992

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button type="submit" name="form.button.SelectContentType" class="btn btn-primary"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820980080
                __default_139856820980080 = _DEFAULT_MARKER

                # <Translate msgid='label_change' node=<ast.Constant object at 0x7f32f4224490> at 7f32f4224640> -> __attr_value
                __attr_value = 'Change'
                __attr_value = translate('label_change', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('>')
                __stream_139856820978304 = []
                __append_139856820978304 = __stream_139856820978304.append
                __append_139856820978304('Change')
                __msgid_139856820978304 = __re_whitespace(''.join(__stream_139856820978304)).strip()
                if __msgid_139856820978304:
                    __append(translate(__msgid_139856820978304, mapping=None, default=__msgid_139856820978304, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n                    </noscript>\n                </div>\n\n                ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820978448
                __attrs_139856820978448 = _static_139856913889840

                # <Value "python:type_id!=''" (57:42)> -> __condition
                __token = 2542
                try:
                    __zt_tmp = __attrs_139856820978448
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('python', "type_id!=''", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n                    ')

                    # <Static value=<ast.Dict object at 0x7f32f42259f0> name=None at 7f32f4225660> -> __attrs_139856820982432
                    __attrs_139856820982432 = _static_139856820984304

                    # <Value 'view/selected_type_description' (61:39)> -> __condition
                    __token = 2714
                    try:
                        __zt_tmp = __attrs_139856820982432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('path', 'view/selected_type_description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p class="text-muted">')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820983920
                        __default_139856820983920 = _DEFAULT_MARKER

                        # <Value 'view/selected_type_description' (60:37)> -> __cache_139856820980608
                        __token = 2643
                        try:
                            __zt_tmp = __attrs_139856820982432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856820980608 = _static_139856914196144('path', 'view/selected_type_description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'view/selected_type_description' (60:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f4225b40> -> __condition
                        __expression = __cache_139856820980608

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                        Type description\n                    ')
                        else:
                            __content = __cache_139856820980608
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</p>')
                    __append('\n\n                   ')

                    # <Static value=<ast.Dict object at 0x7f32f4225e10> name=None at 7f32f4225180> -> __attrs_139856820985888
                    __attrs_139856820985888 = _static_139856820985360

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="field mb-3">\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f4227310> name=None at 7f32f42269b0> -> __attrs_139856820991408
                    __attrs_139856820991408 = _static_139856820990736

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input id="addable" type="checkbox" class="noborder" name="addable:boolean"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820989008
                    __default_139856820989008 = _DEFAULT_MARKER

                    # <Boolean "python:view.is_addable() and 'checked' or None" (71:55)> -> __attr_checked
                    __token = 3148
                    try:
                        __zt_tmp = __attrs_139856820991408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_139856914196144('python', "view.is_addable() and 'checked' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f4226fb0> name=None at 7f32f4227280> -> __attrs_139856820992272
                    __attrs_139856820992272 = _static_139856820989872

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label for="addable">')
                    __stream_139856820988720 = []
                    __append_139856820988720 = __stream_139856820988720.append
                    __append_139856820988720('\n                            Globally addable\n                        ')
                    __msgid_139856820988720 = __re_whitespace(''.join(__stream_139856820988720)).strip()
                    if 'types_controlpanel_addable':
                        __append(translate('types_controlpanel_addable', mapping=None, default=__msgid_139856820988720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820993040
                    __attrs_139856820993040 = _static_139856913889840

                    # <br ... (0:0)
                    # --------------------------------------------------------
                    __append('<br />\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f4227fa0> name=None at 7f32f4227fd0> -> __attrs_139856820537568
                    __attrs_139856820537568 = _static_139856820993952

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input id="allow_discussion" type="checkbox" class="noborder" name="allow_discussion:boolean"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820543040
                    __default_139856820543040 = _DEFAULT_MARKER

                    # <Boolean "python:view.is_discussion_allowed() and 'checked' or None" (82:55)> -> __attr_checked
                    __token = 3696
                    try:
                        __zt_tmp = __attrs_139856820537568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_139856914196144('python', "view.is_discussion_allowed() and 'checked' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41b9870> name=None at 7f32f41bac50> -> __attrs_139856820550720
                    __attrs_139856820550720 = _static_139856820541552

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label for="allow_discussion">')
                    __stream_139856820542464 = []
                    __append_139856820542464 = __stream_139856820542464.append
                    __append_139856820542464('\n                            Allow comments\n                        ')
                    __msgid_139856820542464 = __re_whitespace(''.join(__stream_139856820542464)).strip()
                    if 'types_controlpanel_allow_discussion':
                        __append(translate('types_controlpanel_allow_discussion', mapping=None, default=__msgid_139856820542464, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820546352
                    __attrs_139856820546352 = _static_139856913889840

                    # <br ... (0:0)
                    # --------------------------------------------------------
                    __append('<br />\n\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41ba6e0> name=None at 7f32f41ba740> -> __attrs_139856820550000
                    __attrs_139856820550000 = _static_139856820545248

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input id="searchable" type="checkbox" class="noborder" name="searchable"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820540064
                    __default_139856820540064 = _DEFAULT_MARKER

                    # <Boolean "python: view.is_searchable() and 'checked' or None" (93:55)> -> __attr_checked
                    __token = 4221
                    try:
                        __zt_tmp = __attrs_139856820550000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_139856914196144('python', " view.is_searchable() and 'checked' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41bb340> name=None at 7f32f41bb3d0> -> __attrs_139856820551008
                    __attrs_139856820551008 = _static_139856820548416

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label for="searchable">')
                    __stream_139856820538624 = []
                    __append_139856820538624 = __stream_139856820538624.append
                    __append_139856820538624('\n                            Visible in searches\n                        ')
                    __msgid_139856820538624 = __re_whitespace(''.join(__stream_139856820538624)).strip()
                    if 'types_controlpanel_searchable':
                        __append(translate('types_controlpanel_searchable', mapping=None, default=__msgid_139856820538624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820548944
                    __attrs_139856820548944 = _static_139856913889840

                    # <br ... (0:0)
                    # --------------------------------------------------------
                    __append('<br />\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41bb0a0> name=None at 7f32f41ba860> -> __attrs_139856820536560
                    __attrs_139856820536560 = _static_139856820547744

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input id="default_page_type" type="checkbox" class="noborder" name="default_page_type"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820548224
                    __default_139856820548224 = _DEFAULT_MARKER

                    # <Boolean "python: view.is_default_page_type() and 'checked' or None" (103:55)> -> __attr_checked
                    __token = 4745
                    try:
                        __zt_tmp = __attrs_139856820536560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_139856914196144('python', " view.is_default_page_type() and 'checked' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41b9de0> name=None at 7f32f41b9ea0> -> __attrs_139856820543376
                    __attrs_139856820543376 = _static_139856820542944

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label for="default_page_type">')
                    __stream_139856820542080 = []
                    __append_139856820542080 = __stream_139856820542080.append
                    __append_139856820542080('\n                            Can be used as a default page\n                        ')
                    __msgid_139856820542080 = __re_whitespace(''.join(__stream_139856820542080)).strip()
                    if 'types_controlpanel_default_page_type':
                        __append(translate('types_controlpanel_default_page_type', mapping=None, default=__msgid_139856820542080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820541600
                    __attrs_139856820541600 = _static_139856913889840

                    # <br ... (0:0)
                    # --------------------------------------------------------
                    __append('<br />\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820536608
                    __attrs_139856820536608 = _static_139856913889840

                    # <Value "python:type_id=='Link'" (109:50)> -> __condition
                    __token = 5090
                    try:
                        __zt_tmp = __attrs_139856820536608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('python', "type_id=='Link'", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:
                        __append('\n\n                          ')

                        # <Static value=<ast.Dict object at 0x7f32f41b89d0> name=None at 7f32f41b89a0> -> __attrs_139856820539056
                        __attrs_139856820539056 = _static_139856820537808

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input id="redirect_links" type="checkbox" class="noborder" name="redirect_links:boolean"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820540688
                        __default_139856820540688 = _DEFAULT_MARKER

                        # <Boolean "python: view.is_redirect_links_enabled() and 'checked' or None" (115:57)> -> __attr_checked
                        __token = 5388
                        try:
                            __zt_tmp = __attrs_139856820539056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_139856914196144('python', " view.is_redirect_links_enabled() and 'checked' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))
                        __append(' />\n                          ')

                        # <Static value=<ast.Dict object at 0x7f32f41b9060> name=None at 7f32f41b9150> -> __attrs_139856820778080
                        __attrs_139856820778080 = _static_139856820539488

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append('<label for="redirect_links">')
                        __stream_139856820535456 = []
                        __append_139856820535456 = __stream_139856820535456.append
                        __append_139856820535456('\n                              Redirect immediately to link target\n                          ')
                        __msgid_139856820535456 = __re_whitespace(''.join(__stream_139856820535456)).strip()
                        if 'types_controlpanel_redirect_links':
                            __append(translate('types_controlpanel_redirect_links', mapping=None, default=__msgid_139856820535456, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</label>\n\n                        ')
                    __append('\n                    </div>\n\n                    ')

                    # <Static value=<ast.Dict object at 0x7f32f41b8370> name=None at 7f32f41b83d0> -> __attrs_139856820780528
                    __attrs_139856820780528 = _static_139856820536176

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="field mb-3">\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41f3c70> name=None at 7f32f41f2440> -> __attrs_139856820774048
                    __attrs_139856820774048 = _static_139856820780144

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label for="versionpolicy">')
                    __stream_139856820778608 = []
                    __append_139856820778608 = __stream_139856820778608.append
                    __append_139856820778608('\n                            Versioning policy:\n                        ')
                    __msgid_139856820778608 = __re_whitespace(''.join(__stream_139856820778608)).strip()
                    if 'types_controlpanel_versionpolicy':
                        __append(translate('types_controlpanel_versionpolicy', mapping=None, default=__msgid_139856820778608, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41f3790> name=None at 7f32f41f3760> -> __attrs_139856820774528
                    __attrs_139856820774528 = _static_139856820778896
                    __backup_current_policy_139856823416336 = get('current_policy', __marker)

                    # <Value 'view/current_versioning_policy' (128:59)> -> __value
                    __token = 6123
                    try:
                        __zt_tmp = __attrs_139856820774528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139856914196144('path', 'view/current_versioning_policy', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    econtext['current_policy'] = __value

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append('<select class="form-select select-widget required choice-field" name="versionpolicy">\n                            ')

                    # <Static value=<ast.Dict object at 0x7f32f41f26e0> name=None at 7f32f41f2740> -> __attrs_139856820772896
                    __attrs_139856820772896 = _static_139856820774624
                    __backup_policy_139856823415568 = get('policy', __marker)

                    # <Value 'view/versioning_policies' (129:55)> -> __iterator
                    __token = 6211
                    try:
                        __zt_tmp = __attrs_139856820772896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139856914196144('path', 'view/versioning_policies', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    (__iterator, ____index_139856820776400, ) = getname('repeat')('policy', __iterator)
                    econtext['policy'] = None
                    for __item in __iterator:
                        econtext['policy'] = __item

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append('<option')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820779616
                        __default_139856820779616 = _DEFAULT_MARKER

                        # <Substitution 'policy/id' (130:58)> -> __attr_value
                        __token = 6295
                        try:
                            __zt_tmp = __attrs_139856820772896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139856914196144('path', 'policy/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820775152
                        __default_139856820775152 = _DEFAULT_MARKER

                        # <Boolean "python:policy['id']==current_policy and 'selected' or None" (131:60)> -> __attr_selected
                        __token = 6366
                        try:
                            __zt_tmp = __attrs_139856820772896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_selected = _static_139856914196144('python', "policy['id']==current_policy and 'selected' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if (__attr_selected is _DEFAULT_MARKER):
                            __attr_selected = None
                        else:
                            if __attr_selected:
                                __attr_selected = 'selected'
                            else:
                                __attr_selected = None
                        if (__attr_selected is not None):
                            __append((' selected="%s"' % __attr_selected))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820775680
                        __default_139856820775680 = _DEFAULT_MARKER

                        # <Value 'policy/title' (132:49)> -> __cache_139856820779424
                        __token = 6476
                        try:
                            __zt_tmp = __attrs_139856820772896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856820779424 = _static_139856914196144('path', 'policy/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'policy/title' (132:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f41f3880> -> __condition
                        __expression = __cache_139856820779424

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('No versioning')
                        else:
                            __content = __cache_139856820779424
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</option>')
                        ____index_139856820776400 -= 1
                        if (____index_139856820776400 > 0):
                            __append('\n                            ')
                    if (__backup_policy_139856823415568 is __marker):
                        del econtext['policy']
                    else:
                        econtext['policy'] = __backup_policy_139856823415568
                    __append('\n                        </select>')
                    if (__backup_current_policy_139856823416336 is __marker):
                        del econtext['current_policy']
                    else:
                        econtext['current_policy'] = __backup_current_policy_139856823416336
                    __append('\n                    </div>\n\n                    ')

                    # <Static value=<ast.Dict object at 0x7f32f41f2da0> name=None at 7f32f41f2e00> -> __attrs_139856820776832
                    __attrs_139856820776832 = _static_139856820776352

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="field mb-3">\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41f13f0> name=None at 7f32f41f14e0> -> __attrs_139856820772272
                    __attrs_139856820772272 = _static_139856820769776

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820772560
                    __default_139856820772560 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/@@manage-content-type-portlets?key=${type_id}&_authenticator=${token}' (137:48)> -> __attr_href
                    __token = 6668
                    try:
                        __zt_tmp = __attrs_139856820772272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139856914196144('string', '${context/absolute_url}/@@manage-content-type-portlets?key=${type_id}&_authenticator=${token}', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')
                    __stream_139856820776688 = []
                    __append_139856820776688 = __stream_139856820776688.append
                    __append_139856820776688('\n                            Manage portlets assigned to this content type\n                        ')
                    __msgid_139856820776688 = __re_whitespace(''.join(__stream_139856820776688)).strip()
                    if 'types_controlpanel_manage_portlets':
                        __append(translate('types_controlpanel_manage_portlets', mapping=None, default=__msgid_139856820776688, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                    </div>\n                ')
                __append('\n\n                ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820771552
                __attrs_139856820771552 = _static_139856913889840
                __backup_current_wf_139856822464000 = get('current_wf', __marker)

                # <Value 'view/current_workflow' (144:50)> -> __value
                __token = 7061
                try:
                    __zt_tmp = __attrs_139856820771552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/current_workflow', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['current_wf'] = __value
                __append('\n\n                    ')

                # <Static value=<ast.Dict object at 0x7f32f41f1840> name=None at 7f32f41f1810> -> __attrs_139856820770448
                __attrs_139856820770448 = _static_139856820770880

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="field mb-3">\n                        ')

                # <Static value=<ast.Dict object at 0x7f32f41f0280> name=None at 7f32f41f0e50> -> __attrs_139856820767760
                __attrs_139856820767760 = _static_139856820765312

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label">')
                __stream_139856820765696 = []
                __append_139856820765696 = __stream_139856820765696.append
                __append_139856820765696('Current workflow:')
                __msgid_139856820765696 = __re_whitespace(''.join(__stream_139856820765696)).strip()
                if 'types_controlpanel_current_workflow':
                    __append(translate('types_controlpanel_current_workflow', mapping=None, default=__msgid_139856820765696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n                        ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820766416
                __attrs_139856820766416 = _static_139856913889840

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820767472
                __default_139856820767472 = _DEFAULT_MARKER

                # <Value 'current_wf/title' (148:43)> -> __cache_139856820766992
                __token = 7303
                try:
                    __zt_tmp = __attrs_139856820766416
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139856820766992 = _static_139856914196144('path', 'current_wf/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                # <BinOp left=<Value 'current_wf/title' (148:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f41f0310> -> __condition
                __expression = __cache_139856820766992

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Community Workflow')
                else:
                    __content = __cache_139856820766992
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n                    </div>\n\n                    ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820767136
                __attrs_139856820767136 = _static_139856913889840

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n                      ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820879520
                __attrs_139856820879520 = _static_139856913889840

                # <Value 'current_wf/description' (155:35)> -> __condition
                __token = 7581
                try:
                    __zt_tmp = __attrs_139856820879520
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('path', 'current_wf/description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:
                    __backup_desc_139856823416912 = get('desc', __marker)

                    # <Value 'current_wf/description' (154:37)> -> __iterator
                    __token = 7522
                    try:
                        __zt_tmp = __attrs_139856820879520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139856914196144('path', 'current_wf/description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    (__iterator, ____index_139856820894544, ) = getname('repeat')('desc', __iterator)
                    econtext['desc'] = None
                    for __item in __iterator:
                        econtext['desc'] = __item
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820895120
                        __attrs_139856820895120 = _static_139856913889840

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820890656
                        __default_139856820890656 = _DEFAULT_MARKER

                        # <Value 'desc' (156:41)> -> __cache_139856820890512
                        __token = 7647
                        try:
                            __zt_tmp = __attrs_139856820895120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856820890512 = _static_139856914196144('path', 'desc', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'desc' (156:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f420efe0> -> __condition
                        __expression = __cache_139856820890512

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Workflow description')
                        else:
                            __content = __cache_139856820890512
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</li>\n                      ')
                        ____index_139856820894544 -= 1
                        if (____index_139856820894544 > 0):
                            __append('')
                    if (__backup_desc_139856823416912 is __marker):
                        del econtext['desc']
                    else:
                        econtext['desc'] = __backup_desc_139856823416912
                __append('\n                    </ul>\n\n                    ')

                # <Static value=<ast.Dict object at 0x7f32f420eda0> name=None at 7f32f420fb80> -> __attrs_139856820894496
                __attrs_139856820894496 = _static_139856820891040

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="field mb-3">\n                        ')

                # <Static value=<ast.Dict object at 0x7f32f420f670> name=None at 7f32f420f130> -> __attrs_139856820893344
                __attrs_139856820893344 = _static_139856820893296

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label" for="new_workflow">')
                __stream_139856820892000 = []
                __append_139856820892000 = __stream_139856820892000.append
                __append_139856820892000('New workflow:')
                __msgid_139856820892000 = __re_whitespace(''.join(__stream_139856820892000)).strip()
                if 'types_controlpanel_new_workflow':
                    __append(translate('types_controlpanel_new_workflow', mapping=None, default=__msgid_139856820892000, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n\n                        ')

                # <Static value=<ast.Dict object at 0x7f32f420e380> name=None at 7f32f420e320> -> __attrs_139856820889696
                __attrs_139856820889696 = _static_139856820888448
                __backup_selected_wf_139856823418016 = get('selected_wf', __marker)

                # <Value 'view/new_workflow' (166:52)> -> __value
                __token = 8209
                try:
                    __zt_tmp = __attrs_139856820889696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/new_workflow', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['selected_wf'] = __value

                # <select ... (0:0)
                # --------------------------------------------------------
                __append('<select onchange="form.submit()" id="workflows" class ="form-select select-widget required choice-field" name="new_workflow">\n\n                            ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820883072
                __attrs_139856820883072 = _static_139856913889840
                __backup_wf_139856823049408 = get('wf', __marker)

                # <Value 'view/available_workflows' (168:48)> -> __iterator
                __token = 8278
                try:
                    __zt_tmp = __attrs_139856820883072
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139856914196144('path', 'view/available_workflows', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                (__iterator, ____index_139856820887632, ) = getname('repeat')('wf', __iterator)
                econtext['wf'] = None
                for __item in __iterator:
                    econtext['wf'] = __item
                    __append('\n                                ')

                    # <Static value=<ast.Dict object at 0x7f32f420d420> name=None at 7f32f420d1e0> -> __attrs_139856820880000
                    __attrs_139856820880000 = _static_139856820884512

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820885712
                    __default_139856820885712 = _DEFAULT_MARKER

                    # <Boolean "python:wf['id'] == selected_wf and 'selected' or None" (171:65)> -> __attr_selected
                    __token = 8491
                    try:
                        __zt_tmp = __attrs_139856820880000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_139856914196144('python', "wf['id'] == selected_wf and 'selected' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = 'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((' selected="%s"' % __attr_selected))

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820884608
                    __default_139856820884608 = _DEFAULT_MARKER

                    # <Substitution 'wf/id' (172:61)> -> __attr_value
                    __token = 8607
                    try:
                        __zt_tmp = __attrs_139856820880000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139856914196144('path', 'wf/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820885568
                    __default_139856820885568 = _DEFAULT_MARKER

                    # <Value 'wf/title' (170:53)> -> __cache_139856820887056
                    __token = 8416
                    try:
                        __zt_tmp = __attrs_139856820880000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856820887056 = _static_139856914196144('path', 'wf/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'wf/title' (170:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f420d7b0> -> __condition
                    __expression = __cache_139856820887056

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Intranet Workflow\n                                ')
                    else:
                        __content = __cache_139856820887056
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>\n                            ')
                    ____index_139856820887632 -= 1
                    if (____index_139856820887632 > 0):
                        __append('')
                if (__backup_wf_139856823049408 is __marker):
                    del econtext['wf']
                else:
                    econtext['wf'] = __backup_wf_139856823049408
                __append('\n\n                            ')

                # <Static value=<ast.Dict object at 0x7f32f420c9a0> name=None at 7f32f420ca00> -> __attrs_139856820882448
                __attrs_139856820882448 = _static_139856820881824

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option value="[none]"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820886192
                __default_139856820886192 = _DEFAULT_MARKER

                # <Boolean "python:selected_wf == '[none]' and 'selected' or None" (178:57)> -> __attr_selected
                __token = 8855
                try:
                    __zt_tmp = __attrs_139856820882448
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_selected = _static_139856914196144('python', "selected_wf == '[none]' and 'selected' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if (__attr_selected is _DEFAULT_MARKER):
                    __attr_selected = None
                else:
                    if __attr_selected:
                        __attr_selected = 'selected'
                    else:
                        __attr_selected = None
                if (__attr_selected is not None):
                    __append((' selected="%s"' % __attr_selected))
                __append('>')
                __stream_139856820885280 = []
                __append_139856820885280 = __stream_139856820885280.append
                __append_139856820885280('No Workflow')
                __msgid_139856820885280 = __re_whitespace(''.join(__stream_139856820885280)).strip()
                if 'types_controlpanel_no_workflow':
                    __append(translate('types_controlpanel_no_workflow', mapping=None, default=__msgid_139856820885280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</option>\n                        </select>')
                if (__backup_selected_wf_139856823418016 is __marker):
                    del econtext['selected_wf']
                else:
                    econtext['selected_wf'] = __backup_selected_wf_139856823418016
                __append('\n                        ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820882112
                __attrs_139856820882112 = _static_139856913889840

                # <noscript ... (0:0)
                # --------------------------------------------------------
                __append('<noscript>\n                            ')

                # <Static value=<ast.Dict object at 0x7f32f420f010> name=None at 7f32f420e470> -> __attrs_139856820880960
                __attrs_139856820880960 = _static_139856820891664

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button type="submit" name="form.button.SelectWorkflow" class="btn btn-primary"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820880336
                __default_139856820880336 = _DEFAULT_MARKER

                # <Translate msgid='label_change' node=<ast.Constant object at 0x7f32f420c1c0> at 7f32f420c190> -> __attr_value
                __attr_value = 'Change'
                __attr_value = translate('label_change', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('>')
                __stream_139856820881344 = []
                __append_139856820881344 = __stream_139856820881344.append
                __append_139856820881344('Change')
                __msgid_139856820881344 = __re_whitespace(''.join(__stream_139856820881344)).strip()
                if 'label_change':
                    __append(translate('label_change', mapping=None, default=__msgid_139856820881344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n                        </noscript>\n                    </div>\n\n                    ')

                # <Static value=<ast.Dict object at 0x7f32f4186080> name=None at 7f32f420c850> -> __attrs_139856820327696
                __attrs_139856820327696 = _static_139856820330624

                # <Value 'view/have_new_workflow' (194:39)> -> __condition
                __token = 9695
                try:
                    __zt_tmp = __attrs_139856820327696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('path', 'view/have_new_workflow', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="form.workflow.submitted:boolean" value="True" />')
                __append('\n                    ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820335664
                __attrs_139856820335664 = _static_139856913889840

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n                      ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820338256
                __attrs_139856820338256 = _static_139856913889840

                # <Value 'view/new_workflow_description' (199:35)> -> __condition
                __token = 9911
                try:
                    __zt_tmp = __attrs_139856820338256
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('path', 'view/new_workflow_description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:
                    __backup_desc_139856823295792 = get('desc', __marker)

                    # <Value 'view/new_workflow_description' (198:37)> -> __iterator
                    __token = 9845
                    try:
                        __zt_tmp = __attrs_139856820338256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139856914196144('path', 'view/new_workflow_description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    (__iterator, ____index_139856820334416, ) = getname('repeat')('desc', __iterator)
                    econtext['desc'] = None
                    for __item in __iterator:
                        econtext['desc'] = __item
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820337392
                        __attrs_139856820337392 = _static_139856913889840

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820328608
                        __default_139856820328608 = _DEFAULT_MARKER

                        # <Value 'desc' (200:41)> -> __cache_139856820336624
                        __token = 9984
                        try:
                            __zt_tmp = __attrs_139856820337392
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856820336624 = _static_139856914196144('path', 'desc', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'desc' (200:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f4187790> -> __condition
                        __expression = __cache_139856820336624

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Workflow description')
                        else:
                            __content = __cache_139856820336624
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</li>\n                      ')
                        ____index_139856820334416 -= 1
                        if (____index_139856820334416 > 0):
                            __append('')
                    if (__backup_desc_139856823295792 is __marker):
                        del econtext['desc']
                    else:
                        econtext['desc'] = __backup_desc_139856823295792
                __append('\n                    </ul>\n\n                    ')

                # <Static value=<ast.Dict object at 0x7f32f4187b80> name=None at 7f32f4187be0> -> __attrs_139856820338016
                __attrs_139856820338016 = _static_139856820337536
                __backup_new_workflow_139856822402400 = get('new_workflow', __marker)

                # <Value 'view/new_workflow' (204:50)> -> __value
                __token = 10132
                try:
                    __zt_tmp = __attrs_139856820338016
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/new_workflow', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['new_workflow'] = __value

                # <Value 'python:view.have_new_workflow() and not view.new_workflow_is_none() and view.new_workflow_is_different()' (205:40)> -> __condition
                __token = 10191
                try:
                    __zt_tmp = __attrs_139856820338016
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('python', 'view.have_new_workflow() and not view.new_workflow_is_none() and view.new_workflow_is_different()', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="field mb-3">\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f4186a10> name=None at 7f32f4185e40> -> __attrs_139856820332688
                    __attrs_139856820332688 = _static_139856820333072

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-label" for="states">')
                    __stream_139856820324096 = []
                    __append_139856820324096 = __stream_139856820324096.append
                    __append_139856820324096('\n                            State Mapping\n                        ')
                    __msgid_139856820324096 = __re_whitespace(''.join(__stream_139856820324096)).strip()
                    if 'types_controlpanel_state_mapping':
                        __append(translate('types_controlpanel_state_mapping', mapping=None, default=__msgid_139856820324096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f4186470> name=None at 7f32f41860e0> -> __attrs_139856820332160
                    __attrs_139856820332160 = _static_139856820331632
                    __backup_new_wf_states_139856823304096 = get('new_wf_states', __marker)

                    # <Value 'view/new_workflow_available_states' (214:57)> -> __value
                    __token = 10707
                    try:
                        __zt_tmp = __attrs_139856820332160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139856914196144('path', 'view/new_workflow_available_states', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    econtext['new_wf_states'] = __value

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table id="states" class="table table-bordered table-striped">\n                            ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820328704
                    __attrs_139856820328704 = _static_139856913889840

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead>\n                                ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820327744
                    __attrs_139856820327744 = _static_139856913889840

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                                    ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820328320
                    __attrs_139856820328320 = _static_139856913889840

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th>')
                    __stream_139856820327120 = []
                    __append_139856820327120 = __stream_139856820327120.append
                    __append_139856820327120('Old State:')
                    __msgid_139856820327120 = __re_whitespace(''.join(__stream_139856820327120)).strip()
                    if 'types_controlpanel_old_state':
                        __append(translate('types_controlpanel_old_state', mapping=None, default=__msgid_139856820327120, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                                    ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820325536
                    __attrs_139856820325536 = _static_139856913889840

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th>')
                    __stream_139856820325776 = []
                    __append_139856820325776 = __stream_139856820325776.append
                    __append_139856820325776('New State:')
                    __msgid_139856820325776 = __re_whitespace(''.join(__stream_139856820325776)).strip()
                    if 'types_controlpanel_new_state':
                        __append(translate('types_controlpanel_new_state', mapping=None, default=__msgid_139856820325776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                                </tr>\n                            </thead>\n                            ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820324576
                    __attrs_139856820324576 = _static_139856913889840

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append('<tbody>\n                                ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820323472
                    __attrs_139856820323472 = _static_139856913889840
                    __backup_state_map_139856821587632 = get('state_map', __marker)

                    # <Value 'view/suggested_state_map' (222:62)> -> __iterator
                    __token = 11194
                    try:
                        __zt_tmp = __attrs_139856820323472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139856914196144('path', 'view/suggested_state_map', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    (__iterator, ____index_139856820323280, ) = getname('repeat')('state_map', __iterator)
                    econtext['state_map'] = None
                    for __item in __iterator:
                        econtext['state_map'] = __item
                        __append('\n                                    ')

                        # <Static value=<ast.Dict object at 0x7f32f41ac190> name=None at 7f32f41afe80> -> __attrs_139856820488512
                        __attrs_139856820488512 = _static_139856820486544
                        __backup_oddrow_139856821585712 = get('oddrow', __marker)

                        # <Value 'repeat/state_map/odd' (223:59)> -> __value
                        __token = 11280
                        try:
                            __zt_tmp = __attrs_139856820488512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139856914196144('path', 'repeat/state_map/odd', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        econtext['oddrow'] = __value

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820499312
                        __default_139856820499312 = _DEFAULT_MARKER

                        # <Substitution "python:oddrow and 'odd' or 'even'" (224:62)> -> __attr_class
                        __token = 11365
                        try:
                            __zt_tmp = __attrs_139856820488512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_139856914196144('python', "oddrow and 'odd' or 'even'", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>\n                                        ')

                        # <Static value=<ast.Dict object at 0x7f32f41afe20> name=None at 7f32f41afd30> -> __attrs_139856820501616
                        __attrs_139856820501616 = _static_139856820502048

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="align-middle">\n                                            ')

                        # <Static value=<ast.Dict object at 0x7f32f41af100> name=None at 7f32f41af6d0> -> __attrs_139856820495568
                        __attrs_139856820495568 = _static_139856820498688

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820499600
                        __default_139856820499600 = _DEFAULT_MARKER

                        # <Substitution 'string:new_wfstates.old_state:records' (227:72)> -> __attr_name
                        __token = 11604
                        try:
                            __zt_tmp = __attrs_139856820495568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_139856914196144('string', 'new_wfstates.old_state:records', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820500752
                        __default_139856820500752 = _DEFAULT_MARKER

                        # <Substitution 'state_map/old_id' (228:72)> -> __attr_value
                        __token = 11715
                        try:
                            __zt_tmp = __attrs_139856820495568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139856914196144('path', 'state_map/old_id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n                                            ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820497056
                        __attrs_139856820497056 = _static_139856913889840

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820497440
                        __default_139856820497440 = _DEFAULT_MARKER

                        # <Value 'state_map/old_title' (229:63)> -> __cache_139856820498112
                        __token = 11800
                        try:
                            __zt_tmp = __attrs_139856820497056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856820498112 = _static_139856914196144('path', 'state_map/old_title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'state_map/old_title' (229:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f41aca00> -> __condition
                        __expression = __cache_139856820498112

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Published')
                        else:
                            __content = __cache_139856820498112
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n                                        </td>\n                                        ')

                        # <Static value=<ast.Dict object at 0x7f32f41ae7d0> name=None at 7f32f41ae740> -> __attrs_139856820496432
                        __attrs_139856820496432 = _static_139856820496336

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="align-middle">\n                                            ')

                        # <Static value=<ast.Dict object at 0x7f32f41acd90> name=None at 7f32f41ada50> -> __attrs_139856820488416
                        __attrs_139856820488416 = _static_139856820489616

                        # <select ... (0:0)
                        # --------------------------------------------------------
                        __append('<select class ="form-select select-widget required choice-field"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820494176
                        __default_139856820494176 = _DEFAULT_MARKER

                        # <Substitution 'string:new_wfstates.new_state:records' (232:73)> -> __attr_name
                        __token = 12023
                        try:
                            __zt_tmp = __attrs_139856820488416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_139856914196144('string', 'new_wfstates.new_state:records', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))
                        __append('>\n                                              ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856820490096
                        __attrs_139856820490096 = _static_139856913889840
                        __backup_new_state_139856820501136 = get('new_state', __marker)

                        # <Value 'new_wf_states' (233:76)> -> __iterator
                        __token = 12196
                        try:
                            __zt_tmp = __attrs_139856820490096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_139856914196144('path', 'new_wf_states', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        (__iterator, ____index_139856820492208, ) = getname('repeat')('new_state', __iterator)
                        econtext['new_state'] = None
                        for __item in __iterator:
                            econtext['new_state'] = __item
                            __append('\n                                                ')

                            # <Static value=<ast.Dict object at 0x7f32f41ad420> name=None at 7f32f41ac6a0> -> __attrs_139856820486400
                            __attrs_139856820486400 = _static_139856820491296

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option')

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820488128
                            __default_139856820488128 = _DEFAULT_MARKER

                            # <Substitution 'new_state/id' (235:74)> -> __attr_value
                            __token = 12342
                            try:
                                __zt_tmp = __attrs_139856820486400
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_139856914196144('path', 'new_state/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820490912
                            __default_139856820490912 = _DEFAULT_MARKER

                            # <Boolean "python:new_state['id'] == state_map['suggested_id'] and 'selected' or None" (236:76)> -> __attr_selected
                            __token = 12432
                            try:
                                __zt_tmp = __attrs_139856820486400
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_selected = _static_139856914196144('python', "new_state['id'] == state_map['suggested_id'] and 'selected' or None", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                            if (__attr_selected is _DEFAULT_MARKER):
                                __attr_selected = None
                            else:
                                if __attr_selected:
                                    __attr_selected = 'selected'
                                else:
                                    __attr_selected = None
                            if (__attr_selected is not None):
                                __append((' selected="%s"' % __attr_selected))
                            __append('>')

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820490576
                            __default_139856820490576 = _DEFAULT_MARKER

                            # <Value 'new_state/title' (237:65)> -> __cache_139856820489376
                            __token = 12574
                            try:
                                __zt_tmp = __attrs_139856820486400
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139856820489376 = _static_139856914196144('path', 'new_state/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                            # <BinOp left=<Value 'new_state/title' (237:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f41acee0> -> __condition
                            __expression = __cache_139856820489376

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('Pending')
                            else:
                                __content = __cache_139856820489376
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>\n                                              ')
                            ____index_139856820492208 -= 1
                            if (____index_139856820492208 > 0):
                                __append('')
                        if (__backup_new_state_139856820501136 is __marker):
                            del econtext['new_state']
                        else:
                            econtext['new_state'] = __backup_new_state_139856820501136
                        __append('\n                                            </select>\n                                        </td>\n                                    </tr>')
                        if (__backup_oddrow_139856821585712 is __marker):
                            del econtext['oddrow']
                        else:
                            econtext['oddrow'] = __backup_oddrow_139856821585712
                        __append('\n                                ')
                        ____index_139856820323280 -= 1
                        if (____index_139856820323280 > 0):
                            __append('')
                    if (__backup_state_map_139856821587632 is __marker):
                        del econtext['state_map']
                    else:
                        econtext['state_map'] = __backup_state_map_139856821587632
                    __append('\n                            </tbody>\n                        </table>')
                    if (__backup_new_wf_states_139856823304096 is __marker):
                        del econtext['new_wf_states']
                    else:
                        econtext['new_wf_states'] = __backup_new_wf_states_139856823304096
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x7f32f41843a0> name=None at 7f32f4184c40> -> __attrs_139856820492352
                    __attrs_139856820492352 = _static_139856820323232

                    # <small ... (0:0)
                    # --------------------------------------------------------
                    __append('<small class="form-text text-muted">')
                    __stream_139856820322512 = []
                    __append_139856820322512 = __stream_139856820322512.append
                    __append_139856820322512('\n                            When changing workflows, you have to select a state equivalent in the\n                            new workflow.\n                        ')
                    __msgid_139856820322512 = __re_whitespace(''.join(__stream_139856820322512)).strip()
                    if 'types_controlpanel_state_mapping_help':
                        __append(translate('types_controlpanel_state_mapping_help', mapping=None, default=__msgid_139856820322512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</small>\n                    </div>')
                if (__backup_new_workflow_139856822402400 is __marker):
                    del econtext['new_workflow']
                else:
                    econtext['new_workflow'] = __backup_new_workflow_139856822402400
                __append('\n\n                ')
                if (__backup_current_wf_139856822464000 is __marker):
                    del econtext['current_wf']
                else:
                    econtext['current_wf'] = __backup_current_wf_139856822464000
                __append('\n\n                ')

                # <Static value=<ast.Dict object at 0x7f32f4187ca0> name=None at 7f32f4186e60> -> __attrs_139856820486208
                __attrs_139856820486208 = _static_139856820337824

                # <Value 'view/have_new_workflow' (253:36)> -> __condition
                __token = 13313
                try:
                    __zt_tmp = __attrs_139856820486208
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('path', 'view/have_new_workflow', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-primary mb-3" role="status">\n                    ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822030624
                    __attrs_139856822030624 = _static_139856913889840

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139856820489280 = []
                    __append_139856820489280 = __stream_139856820489280.append
                    __append_139856820489280('Info:')
                    __msgid_139856820489280 = __re_whitespace(''.join(__stream_139856820489280)).strip()
                    if __msgid_139856820489280:
                        __append(translate(__msgid_139856820489280, mapping=None, default=__msgid_139856820489280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822039024
                    __attrs_139856822039024 = _static_139856913889840

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139856822038640 = []
                    __append_139856822038640 = __stream_139856822038640.append
                    __append_139856822038640('\n                        Changing the workflow of a type will take a while, and may slow down\n                        the site significantly while the content is updated to the new setting.\n                    ')
                    __msgid_139856822038640 = __re_whitespace(''.join(__stream_139856822038640)).strip()
                    if 'types_controlpanel_warn_remap':
                        __append(translate('types_controlpanel_warn_remap', mapping=None, default=__msgid_139856822038640, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n                </div>')
                __append('\n\n                ')

                # <Static value=<ast.Dict object at 0x7f32f4327820> name=None at 7f32f4326710> -> __attrs_139856822041952
                __attrs_139856822041952 = _static_139856822040608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls mb-3">\n                  ')

                # <Static value=<ast.Dict object at 0x7f32f4326b30> name=None at 7f32f4326e00> -> __attrs_139856822041088
                __attrs_139856822041088 = _static_139856822037296

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button type="submit"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822038112
                __default_139856822038112 = _DEFAULT_MARKER

                # <Translate msgid='Save' node=<ast.Constant object at 0x7f32f4326d40> at 7f32f4326ad0> -> __attr_value
                __attr_value = 'Save'
                __attr_value = translate('Save', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' name="form.button.Save" class="btn btn-primary">')
                __stream_139856822041904 = []
                __append_139856822041904 = __stream_139856822041904.append
                __append_139856822041904('Save')
                __msgid_139856822041904 = __re_whitespace(''.join(__stream_139856822041904)).strip()
                if __msgid_139856822041904:
                    __append(translate(__msgid_139856822041904, mapping=None, default=__msgid_139856822041904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n\n                  ')

                # <Static value=<ast.Dict object at 0x7f32f43275b0> name=None at 7f32f4327610> -> __attrs_139856822032064
                __attrs_139856822032064 = _static_139856822039984

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button type="submit"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856822031680
                __default_139856822031680 = _DEFAULT_MARKER

                # <Translate msgid='label_cancel' node=<ast.Constant object at 0x7f32f4326740> at 7f32f4327700> -> __attr_value
                __attr_value = 'Cancel'
                __attr_value = translate('label_cancel', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' name="form.button.Cancel" class="btn btn-secondary">')
                __stream_139856822038976 = []
                __append_139856822038976 = __stream_139856822038976.append
                __append_139856822038976('Cancel')
                __msgid_139856822038976 = __re_whitespace(''.join(__stream_139856822038976)).strip()
                if __msgid_139856822038976:
                    __append(translate(__msgid_139856822038976, mapping=None, default=__msgid_139856822038976, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n                </div>\n\n            </fieldset>\n\n        </form>')
                if (__backup_type_id_139856823415328 is __marker):
                    del econtext['type_id']
                else:
                    econtext['type_id'] = __backup_type_id_139856823415328
                __append('\n    </div>')
                if (__backup_token_139856823415040 is __marker):
                    del econtext['token']
                else:
                    econtext['token'] = __backup_token_139856823415040
                __append('\n')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_139856820452224
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139856914196144('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139856871219200 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139856871219200
            __i18n_domain = __previous_i18n_domain_139856820450880
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }