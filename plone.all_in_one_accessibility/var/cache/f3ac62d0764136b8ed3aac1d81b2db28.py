# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.z3cform-4.2.1-py3.10.egg/plone/app/z3cform/templates/macros.pt'

__tokens = {383: ('view/label | nothing', 15, 27), 430: ('view/label', 16, 25), 644: ('view/status', 25, 29), 688: (" python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None", 26, 31), 798: ('s view/widgets/erro', 27, 27), 846: ('ns nocall: context/@@iconresol', 28, 25), 938: ('python: status', 30, 35), 1109: ('python:not (has_error or errors)', 34, 30), 1200: ("python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')", 36, 45), 1438: ('status | nothing', 40, 41), 1746: ('python:has_error or errors', 48, 30), 1831: ("python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')", 50, 45), 2071: ('status | nothing', 54, 41), 2289: ("python:[e for e in errors if not getattr(e, 'widget', None)]", 60, 32), 2428: ('errors', 63, 44), 2474: ('not:nocall:error/widget', 64, 37), 2544: ('error/render', 65, 45), 3000: ('view/groups | nothing', 81, 23), 3048: (' view/form_name | nothin', 82, 25), 3100: ('s view/css_class | strin', 83, 25), 3164: ('el view/default_fieldset_label | form_n', 84, 36), 3240: ('ing view/enable_form_tabbing | python:', 85, 32), 3320: ('tion view/enable_unload_protection|python', 86, 36), 3396: ("ction python:enable_unload_protection and 'pat-formunload", 87, 28), 3487: ('ofocus view/enable_autofocus|pyth', 88, 26), 3547: ("tofocus python:enable_autofocus and 'pat-formau", 89, 18), 3622: ("lidation python:'pat-validation' if Tru", 90, 18), 3689: ('as_groups python:bo', 91, 17), 3738: ("rm_tabbing python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-aut", 92, 18), 3859: ('fault_label python:has_groups and default_fieldset_label and len(v', 93, 23), 3961: ('iew_name_raw python:view.__name__ or request.getURL().s', 94, 22), 4048: ("orm_view_name python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.spli", 95, 17), 4304: ('s string:rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_na', 100, 20), 4218: ('view/action|request/getURL', 98, 23), 4504: ('thod view/method|string', 103, 18), 4269: (' view/enctyp', 99, 23), 4442: ('id view', 101, 16), 4471: ('ame form_', 102, 17), 4799: ('request/fieldset | python:None', 113, 38), 4886: ('python:has_groups and enable_form_tabbing and current_fieldset is not None', 115, 34), 5025: ('current_fieldset', 117, 27), 9301: ('view/enableCSRFProtection|nothing', 224, 36), 9380: ('context/@@authenticator/authenticator', 225, 44), 5252: ('show_default_label|nothing', 124, 47), 5318: (' has_groups|nothin', 125, 38), 5466: ('not:show_default_label', 130, 38), 5546: ('show_default_label', 133, 39), 5697: ('string:fieldsetlegend-default', 136, 29), 5603: ('default_fieldset_label', 134, 37), 6391: ('has_groups', 152, 36), 6446: ('groups', 153, 43), 6553: ('nocall:context/@@plone/normalizeString', 156, 44), 6635: (' group/labe', 157, 42), 6689: ("e python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_lab", 158, 40), 6832: ('me python:normalizeString(fieldset_na', 159, 39), 6976: ('string:fieldset-${fieldset_name}', 162, 31), 7043: (' string:kssattr-fieldset-${fieldset_name', 163, 33), 7126: ('t fieldset_na', 164, 40), 7231: ('fieldset_label', 168, 41), 7376: ('string:fieldsetlegend-${fieldset_name}', 171, 31), 7286: ('fieldset_label', 169, 39), 7602: ('group/description|nothing', 177, 41), 7688: ('group_description', 179, 36), 7751: ('group_description', 180, 44), 7987: ('group/widgets/errors', 187, 38), 8084: ('errors', 189, 44), 8139: ('errors', 190, 47), 8252: ('not:nocall:error/widget', 193, 40), 8325: ('error/render', 194, 48), 8473: ('nocall:group', 199, 36), 8563: ('context/@@ploneform-macros/widget_rendering', 201, 44), 8563: ('context/@@ploneform-macros/widget_rendering', 201, 44), 5900: ('python:view.widgets.values()', 141, 46), 6106: ('widget/@@ploneform-render-widget', 144, 59), 8984: ('view/actions/values|nothing', 215, 34), 9071: ('view/actions/values', 217, 42), 9141: ('action/render', 218, 48)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272719408 = {'xmlns': 'http://www.w3.org/1999/xhtml', }
_static_140310272589008 = {'class': 'formControls', }
_static_140310272580560 = 'widget_rendering'
_static_140310272584448 = {'class': 'field error', }
_static_140310475822160 = {'id': 'string:fieldsetlegend-${fieldset_name}', }
_static_140310475823696 = {'id': 'string:fieldset-${fieldset_name}', 'class': 'string:kssattr-fieldset-${fieldset_name}', 'data-fieldset': 'fieldset_name', }
_static_140310475168000 = {'id': 'string:fieldsetlegend-default', }
_static_140310475165168 = {'id': 'fieldset-default', }
_static_140310475278416 = {'name': 'fieldset', 'type': 'hidden', 'value': 'current_fieldset', }
_static_140310476132304 = {'class': 'rowlike enableUnloadProtection', 'action': '.', 'method': 'post', 'data-pat-autotoc': 'levels: legend; section: fieldset; className: autotabs', 'enctype': 'view/enctype', 'id': 'view/id', 'name': 'form_name', }
_static_140310476137824 = {'class': 'mt-2 field error', }
_static_140310476134224 = {'class': 'content', }
_static_140310476132880 = {'alt': 'alt', }
_static_140310476144304 = {'class': 'portalMessage statusmessage statusmessage-error alert alert-danger', 'role': 'alert', }
_static_140310476131920 = {'class': 'content', }
_static_140310476140512 = {'alt': 'alt', }
_static_140310476130528 = {'class': 'portalMessage statusmessage statusmessage-info alert alert-info', 'role': 'alert', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310566789392 = {}
_static_140310272336912 = {'class': 'form', }

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
            __slot_title = econtext['__slot_title'].pop()
        except:
            __slot_title = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f9c87f0e410> name=None at 7f9c87f0c850> -> __attrs_140310272337152
            __attrs_140310272337152 = _static_140310272336912

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form" >\n\n      ')
            if (__slot_title is None):

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272329424
                __attrs_140310272329424 = _static_140310566789392
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476137920
                __attrs_140310476137920 = _static_140310566789392

                # <Value 'view/label | nothing' (15:27)> -> __condition
                __token = 383
                try:
                    __zt_tmp = __attrs_140310476137920
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('path', 'view/label | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3 >')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272341280
                    __default_140310272341280 = _DEFAULT_MARKER

                    # <Value 'view/label' (16:25)> -> __cache_140310272332928
                    __token = 430
                    try:
                        __zt_tmp = __attrs_140310476137920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272332928 = _static_140310567013776('path', 'view/label', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/label' (16:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f0e350> -> __condition
                    __expression = __cache_140310272332928

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310272332928
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h3>')
                __append('\n      ')
            else:
                __slot_title(__stream, econtext.copy(), rcontext)
            __append('\n\n      ')
            __token = None
            render_titlelessform(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n    </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_titlelessform(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_formtop = econtext['__slot_formtop'].pop()
        except:
            __slot_formtop = None

        try:
            __slot_formbottom = econtext['__slot_formbottom'].pop()
        except:
            __slot_formbottom = None

        try:
            __slot_belowfields = econtext['__slot_belowfields'].pop()
        except:
            __slot_belowfields = None

        try:
            __slot_actions = econtext['__slot_actions'].pop()
        except:
            __slot_actions = None

        try:
            __slot_fields = econtext['__slot_fields'].pop()
        except:
            __slot_fields = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476135808
            __attrs_140310476135808 = _static_140310566789392
            __previous_i18n_domain_140310476140416 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476141280
            __attrs_140310476141280 = _static_140310566789392
            __backup_status_140310272704960 = get('status', __marker)

            # <Value 'view/status' (25:29)> -> __value
            __token = 644
            try:
                __zt_tmp = __attrs_140310476141280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/status', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['status'] = __value
            __backup_has_error_140310475281152 = get('has_error', __marker)

            # <Value "python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)" (26:31)> -> __value
            __token = 688
            try:
                __zt_tmp = __attrs_140310476141280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['has_error'] = __value
            __backup_errors_140310272712400 = get('errors', __marker)

            # <Value 'view/widgets/errors' (27:27)> -> __value
            __token = 798
            try:
                __zt_tmp = __attrs_140310476141280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/widgets/errors', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_icons_140310272335040 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (28:25)> -> __value
            __token = 846
            try:
                __zt_tmp = __attrs_140310476141280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('nocall', ' context/@@iconresolver', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['icons'] = __value

            # <Value 'python: status' (30:35)> -> __condition
            __token = 938
            try:
                __zt_tmp = __attrs_140310476141280
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('python', ' status', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f9c941688e0> name=None at 7f9c941694b0> -> __attrs_140310476141184
                __attrs_140310476141184 = _static_140310476130528

                # <Value 'python:not (has_error or errors)' (34:30)> -> __condition
                __token = 1109
                try:
                    __zt_tmp = __attrs_140310476141184
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('python', 'not (has_error or errors)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="portalMessage statusmessage statusmessage-info alert alert-info" role="alert" >\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c9416afe0> name=None at 7f9c94168550> -> __attrs_140310476131200
                    __attrs_140310476131200 = _static_140310476140512

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476130336
                    __default_140310476130336 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')" (36:45)> -> __cache_140310476136192
                    __token = 1200
                    try:
                        __zt_tmp = __attrs_140310476131200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310476136192 = _static_140310567013776('python', "icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')" (36:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94168c10> -> __condition
                    __expression = __cache_140310476136192

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310476136192
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c94168e50> name=None at 7f9c94168bb0> -> __attrs_140310476141760
                    __attrs_140310476141760 = _static_140310476131920

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476132112
                    __default_140310476132112 = _DEFAULT_MARKER

                    # <Value 'status | nothing' (40:41)> -> __cache_140310476130672
                    __token = 1438
                    try:
                        __zt_tmp = __attrs_140310476141760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310476130672 = _static_140310567013776('path', 'status | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'status | nothing' (40:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9416b5e0> -> __condition
                    __expression = __cache_140310476130672

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content" >\n                              The info status message.\n            </span>')
                    else:
                        __content = __cache_140310476130672
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          </div>')
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f9c9416beb0> name=None at 7f9c9416a140> -> __attrs_140310476134704
                __attrs_140310476134704 = _static_140310476144304

                # <Value 'python:has_error or errors' (48:30)> -> __condition
                __token = 1746
                try:
                    __zt_tmp = __attrs_140310476134704
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('python', 'has_error or errors', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="portalMessage statusmessage statusmessage-error alert alert-danger" role="alert" >\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c94169210> name=None at 7f9c94169120> -> __attrs_140310476135712
                    __attrs_140310476135712 = _static_140310476132880

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476135328
                    __default_140310476135328 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')" (50:45)> -> __cache_140310476132928
                    __token = 1831
                    try:
                        __zt_tmp = __attrs_140310476135712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310476132928 = _static_140310567013776('python', "icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')" (50:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94168a00> -> __condition
                    __expression = __cache_140310476132928

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140310476132928
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c94169750> name=None at 7f9c94169c00> -> __attrs_140310476138160
                    __attrs_140310476138160 = _static_140310476134224

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476141136
                    __default_140310476141136 = _DEFAULT_MARKER

                    # <Value 'status | nothing' (54:41)> -> __cache_140310476134752
                    __token = 2071
                    try:
                        __zt_tmp = __attrs_140310476138160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310476134752 = _static_140310567013776('path', 'status | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'status | nothing' (54:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9416a3e0> -> __condition
                    __expression = __cache_140310476134752

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content" >\n                              The error status message.\n            </span>')
                    else:
                        __content = __cache_140310476134752
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f9c9416a560> name=None at 7f9c9416a620> -> __attrs_140310476958512
                    __attrs_140310476958512 = _static_140310476137824

                    # <Value "python:[e for e in errors if not getattr(e, 'widget', None)]" (60:32)> -> __condition
                    __token = 2289
                    try:
                        __zt_tmp = __attrs_140310476958512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140310567013776('python', "[e for e in errors if not getattr(e, 'widget', None)]", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="mt-2 field error" >\n              ')

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476953280
                        __attrs_140310476953280 = _static_140310566789392

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul>\n                ')

                        # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476956112
                        __attrs_140310476956112 = _static_140310566789392
                        __backup_error_140310475671392 = get('error', __marker)

                        # <Value 'errors' (63:44)> -> __iterator
                        __token = 2428
                        try:
                            __zt_tmp = __attrs_140310476956112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140310567013776('path', 'errors', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        (__iterator, ____index_140310476960768, ) = getname('repeat')('error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append('\n                  ')

                            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310476963648
                            __attrs_140310476963648 = _static_140310566789392

                            # <Value 'not:nocall:error/widget' (64:37)> -> __condition
                            __token = 2474
                            try:
                                __zt_tmp = __attrs_140310476963648
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140310567013776('not', 'nocall:error/widget', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append('<li >')

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476951984
                                __default_140310476951984 = _DEFAULT_MARKER

                                # <Value 'error/render' (65:45)> -> __cache_140310476957792
                                __token = 2544
                                try:
                                    __zt_tmp = __attrs_140310476963648
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140310476957792 = _static_140310567013776('path', 'error/render', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                # <BinOp left=<Value 'error/render' (65:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c94232fb0> -> __condition
                                __expression = __cache_140310476957792

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                                        Error\n                  ')
                                else:
                                    __content = __cache_140310476957792
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</li>')
                            __append('\n                ')
                            ____index_140310476960768 -= 1
                            if (____index_140310476960768 > 0):
                                __append('')
                        if (__backup_error_140310475671392 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_140310475671392
                        __append('\n              </ul>\n            </div>')
                    __append('\n          </div>')
                __append('\n        ')
            if (__backup_icons_140310272335040 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140310272335040
            if (__backup_errors_140310272712400 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140310272712400
            if (__backup_has_error_140310475281152 is __marker):
                del econtext['has_error']
            else:
                econtext['has_error'] = __backup_has_error_140310475281152
            if (__backup_status_140310272704960 is __marker):
                del econtext['status']
            else:
                econtext['status'] = __backup_status_140310272704960
            __append('\n\n\n        ')

            # <Static value=<ast.Dict object at 0x7f9c94168fd0> name=None at 7f9c9416a470> -> __attrs_140310476959904
            __attrs_140310476959904 = _static_140310476132304
            __backup_groups_140310272669104 = get('groups', __marker)

            # <Value 'view/groups | nothing' (81:23)> -> __value
            __token = 3000
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/groups | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['groups'] = __value
            __backup_form_name_140310272495952 = get('form_name', __marker)

            # <Value 'view/form_name | nothing' (82:25)> -> __value
            __token = 3048
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/form_name | nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['form_name'] = __value
            __backup_form_class_140310272332112 = get('form_class', __marker)

            # <Value 'view/css_class | string:' (83:25)> -> __value
            __token = 3100
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/css_class | string:', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['form_class'] = __value
            __backup_default_fieldset_label_140310272340272 = get('default_fieldset_label', __marker)

            # <Value 'view/default_fieldset_label | form_name' (84:36)> -> __value
            __token = 3164
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/default_fieldset_label | form_name', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['default_fieldset_label'] = __value
            __backup_enable_form_tabbing_140310476139312 = get('enable_form_tabbing', __marker)

            # <Value 'view/enable_form_tabbing | python:True' (85:32)> -> __value
            __token = 3240
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/enable_form_tabbing | python:True', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['enable_form_tabbing'] = __value
            __backup_enable_unload_protection_140310272633024 = get('enable_unload_protection', __marker)

            # <Value 'view/enable_unload_protection|python:True' (86:36)> -> __value
            __token = 3320
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/enable_unload_protection|python:True', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['enable_unload_protection'] = __value
            __backup_unload_protection_140310476141952 = get('unload_protection', __marker)

            # <Value "python:enable_unload_protection and 'pat-formunloadalert'" (87:28)> -> __value
            __token = 3396
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "enable_unload_protection and 'pat-formunloadalert'", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['unload_protection'] = __value
            __backup_enable_autofocus_140310476141616 = get('enable_autofocus', __marker)

            # <Value 'view/enable_autofocus|python:True' (88:26)> -> __value
            __token = 3487
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'view/enable_autofocus|python:True', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['enable_autofocus'] = __value
            __backup_autofocus_140310475915328 = get('autofocus', __marker)

            # <Value "python:enable_autofocus and 'pat-formautofocus'" (89:18)> -> __value
            __token = 3547
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "enable_autofocus and 'pat-formautofocus'", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['autofocus'] = __value
            __backup_validation_140310475676240 = get('validation', __marker)

            # <Value "python:'pat-validation' if True else ''" (90:18)> -> __value
            __token = 3622
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "'pat-validation' if True else ''", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['validation'] = __value
            __backup_has_groups_140310272707456 = get('has_groups', __marker)

            # <Value 'python:bool(groups)' (91:17)> -> __value
            __token = 3689
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', 'bool(groups)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __backup_form_tabbing_140310272717728 = get('form_tabbing', __marker)

            # <Value "python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''" (92:18)> -> __value
            __token = 3738
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['form_tabbing'] = __value
            __backup_show_default_label_140310272718448 = get('show_default_label', __marker)

            # <Value 'python:has_groups and default_fieldset_label and len(view.widgets)' (93:23)> -> __value
            __token = 3859
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', 'has_groups and default_fieldset_label and len(view.widgets)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_form_view_name_raw_140310476958752 = get('form_view_name_raw', __marker)

            # <Value "python:view.__name__ or request.getURL().split('/')[-1]" (94:22)> -> __value
            __token = 3961
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "view.__name__ or request.getURL().split('/')[-1]", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['form_view_name_raw'] = __value
            __backup_form_view_name_140310476955824 = get('form_view_name', __marker)

            # <Value "python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])" (95:17)> -> __value
            __token = 4048
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', "'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['form_view_name'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476960240
            __default_140310476960240 = _DEFAULT_MARKER

            # <Substitution 'string:rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_name' (100:20)> -> __attr_class
            __token = 4304
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140310567013776('string', 'rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_name', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', 'rowlike enableUnloadProtection', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476952416
            __default_140310476952416 = _DEFAULT_MARKER

            # <Substitution 'view/action|request/getURL' (98:23)> -> __attr_action
            __token = 4218
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140310567013776('path', 'view/action|request/getURL', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476948624
            __default_140310476948624 = _DEFAULT_MARKER

            # <Substitution 'view/method|string:post' (103:18)> -> __attr_method
            __token = 4504
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_method = _static_140310567013776('path', 'view/method|string:post', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_method = __quote(__attr_method, '"', '&quot;', 'post', _DEFAULT_MARKER)
            if (__attr_method is not None):
                __append((' method="%s"' % __attr_method))
            __append(' data-pat-autotoc="levels: legend; section: fieldset; className: autotabs"')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476956976
            __default_140310476956976 = _DEFAULT_MARKER

            # <Substitution 'view/enctype' (99:23)> -> __attr_enctype
            __token = 4269
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_enctype = _static_140310567013776('path', 'view/enctype', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_enctype = __quote(__attr_enctype, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_enctype is not None):
                __append((' enctype="%s"' % __attr_enctype))

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476952512
            __default_140310476952512 = _DEFAULT_MARKER

            # <Substitution 'view/id' (101:16)> -> __attr_id
            __token = 4442
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140310567013776('path', 'view/id', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310476952608
            __default_140310476952608 = _DEFAULT_MARKER

            # <Substitution 'form_name' (102:17)> -> __attr_name
            __token = 4471
            try:
                __zt_tmp = __attrs_140310476959904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140310567013776('path', 'form_name', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' >\n\n          ')
            if (__slot_formtop is None):

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475289984
                __attrs_140310475289984 = _static_140310566789392
            else:
                __slot_formtop(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')
            if (__slot_fields is None):

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475282064
                __attrs_140310475282064 = _static_140310566789392
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f9c94098850> name=None at 7f9c94098460> -> __attrs_140310475283408
                __attrs_140310475283408 = _static_140310475278416
                __backup_current_fieldset_140310475292240 = get('current_fieldset', __marker)

                # <Value 'request/fieldset | python:None' (113:38)> -> __value
                __token = 4799
                try:
                    __zt_tmp = __attrs_140310475283408
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140310567013776('path', 'request/fieldset | python:None', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                econtext['current_fieldset'] = __value

                # <Value 'python:has_groups and enable_form_tabbing and current_fieldset is not None' (115:34)> -> __condition
                __token = 4886
                try:
                    __zt_tmp = __attrs_140310475283408
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140310567013776('python', 'has_groups and enable_form_tabbing and current_fieldset is not None', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="fieldset" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475281536
                    __default_140310475281536 = _DEFAULT_MARKER

                    # <Substitution 'current_fieldset' (117:27)> -> __attr_value
                    __token = 5025
                    try:
                        __zt_tmp = __attrs_140310475283408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140310567013776('path', 'current_fieldset', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />')
                if (__backup_current_fieldset_140310475292240 is __marker):
                    del econtext['current_fieldset']
                else:
                    econtext['current_fieldset'] = __backup_current_fieldset_140310475292240
                __append('\n\n            <!-- Default fieldset -->\n            ')
                __token = None
                render_fields(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n          ')
            else:
                __slot_fields(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')
            if (__slot_belowfields is None):

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475282640
                __attrs_140310475282640 = _static_140310566789392
            else:
                __slot_belowfields(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')
            if (__slot_actions is None):

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475166944
                __attrs_140310475166944 = _static_140310566789392
                __append('\n            ')
                __token = None
                render_actions(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n          ')
            else:
                __slot_actions(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272578496
            __attrs_140310272578496 = _static_140310566789392

            # <Value 'view/enableCSRFProtection|nothing' (224:36)> -> __condition
            __token = 9301
            try:
                __zt_tmp = __attrs_140310272578496
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'view/enableCSRFProtection|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272573648
                __default_140310272573648 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (225:44)> -> __cache_140310272583920
                __token = 9380
                try:
                    __zt_tmp = __attrs_140310272578496
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310272583920 = _static_140310567013776('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (225:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f4ab90> -> __condition
                __expression = __cache_140310272583920

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140310272583920
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n          ')
            if (__slot_formbottom is None):

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272586368
                __attrs_140310272586368 = _static_140310566789392
            else:
                __slot_formbottom(__stream, econtext.copy(), rcontext)
            __append('\n\n        </form>')
            if (__backup_form_view_name_140310476955824 is __marker):
                del econtext['form_view_name']
            else:
                econtext['form_view_name'] = __backup_form_view_name_140310476955824
            if (__backup_form_view_name_raw_140310476958752 is __marker):
                del econtext['form_view_name_raw']
            else:
                econtext['form_view_name_raw'] = __backup_form_view_name_raw_140310476958752
            if (__backup_show_default_label_140310272718448 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_140310272718448
            if (__backup_form_tabbing_140310272717728 is __marker):
                del econtext['form_tabbing']
            else:
                econtext['form_tabbing'] = __backup_form_tabbing_140310272717728
            if (__backup_has_groups_140310272707456 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_140310272707456
            if (__backup_validation_140310475676240 is __marker):
                del econtext['validation']
            else:
                econtext['validation'] = __backup_validation_140310475676240
            if (__backup_autofocus_140310475915328 is __marker):
                del econtext['autofocus']
            else:
                econtext['autofocus'] = __backup_autofocus_140310475915328
            if (__backup_enable_autofocus_140310476141616 is __marker):
                del econtext['enable_autofocus']
            else:
                econtext['enable_autofocus'] = __backup_enable_autofocus_140310476141616
            if (__backup_unload_protection_140310476141952 is __marker):
                del econtext['unload_protection']
            else:
                econtext['unload_protection'] = __backup_unload_protection_140310476141952
            if (__backup_enable_unload_protection_140310272633024 is __marker):
                del econtext['enable_unload_protection']
            else:
                econtext['enable_unload_protection'] = __backup_enable_unload_protection_140310272633024
            if (__backup_enable_form_tabbing_140310476139312 is __marker):
                del econtext['enable_form_tabbing']
            else:
                econtext['enable_form_tabbing'] = __backup_enable_form_tabbing_140310476139312
            if (__backup_default_fieldset_label_140310272340272 is __marker):
                del econtext['default_fieldset_label']
            else:
                econtext['default_fieldset_label'] = __backup_default_fieldset_label_140310272340272
            if (__backup_form_class_140310272332112 is __marker):
                del econtext['form_class']
            else:
                econtext['form_class'] = __backup_form_class_140310272332112
            if (__backup_form_name_140310272495952 is __marker):
                del econtext['form_name']
            else:
                econtext['form_name'] = __backup_form_name_140310272495952
            if (__backup_groups_140310272669104 is __marker):
                del econtext['groups']
            else:
                econtext['groups'] = __backup_groups_140310272669104
            __append('\n      ')
            __i18n_domain = __previous_i18n_domain_140310476140416
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_fields(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475285232
            __attrs_140310475285232 = _static_140310566789392
            __backup_show_default_label_140310475284368 = get('show_default_label', __marker)

            # <Value 'show_default_label|nothing' (124:47)> -> __value
            __token = 5252
            try:
                __zt_tmp = __attrs_140310475285232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'show_default_label|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_has_groups_140310475280528 = get('has_groups', __marker)

            # <Value 'has_groups|nothing' (125:38)> -> __value
            __token = 5318
            try:
                __zt_tmp = __attrs_140310475285232
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('path', 'has_groups|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __append('\n\n              ')

            # <Static value=<ast.Dict object at 0x7f9c9407cdf0> name=None at 7f9c9407d0f0> -> __attrs_140310475168864
            __attrs_140310475168864 = _static_140310475165168

            # <Negate value=<Value 'not:show_default_label' (130:38)> at 7f9c9407df00> -> __cache_140310475169536

            # <Value 'not:show_default_label' (130:38)> -> __cache_140310475169536
            __token = 5466
            try:
                __zt_tmp = __attrs_140310475168864
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140310475169536 = _static_140310567013776('not', 'show_default_label', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            __cache_140310475169536 = not __cache_140310475169536
            __condition = __cache_140310475169536
            if __condition:

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset id="fieldset-default" >')
            __append('\n\n                ')

            # <Static value=<ast.Dict object at 0x7f9c9407d900> name=None at 7f9c9407f4f0> -> __attrs_140310475163200
            __attrs_140310475163200 = _static_140310475168000

            # <Value 'show_default_label' (133:39)> -> __condition
            __token = 5546
            try:
                __zt_tmp = __attrs_140310475163200
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'show_default_label', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475162000
                __default_140310475162000 = _DEFAULT_MARKER

                # <Substitution 'string:fieldsetlegend-default' (136:29)> -> __attr_id
                __token = 5697
                try:
                    __zt_tmp = __attrs_140310475163200
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140310567013776('string', 'fieldsetlegend-default', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475163728
                __default_140310475163728 = _DEFAULT_MARKER

                # <Value 'default_fieldset_label' (134:37)> -> __cache_140310475171792
                __token = 5603
                try:
                    __zt_tmp = __attrs_140310475163200
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140310475171792 = _static_140310567013776('path', 'default_fieldset_label', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                # <BinOp left=<Value 'default_fieldset_label' (134:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9407dd50> -> __condition
                __expression = __cache_140310475171792

                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Form name')
                else:
                    __content = __cache_140310475171792
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</legend>')
            __append('\n\n                ')
            __token = None
            render_widget_rendering(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n              ')
            __condition = __cache_140310475169536
            if __condition:
                __append('</fieldset>')
            __append('\n\n              <!-- Secondary fieldsets -->\n              ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475172080
            __attrs_140310475172080 = _static_140310566789392

            # <Value 'has_groups' (152:36)> -> __condition
            __token = 6391
            try:
                __zt_tmp = __attrs_140310475172080
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'has_groups', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:
                __backup_group_140310475172368 = get('group', __marker)

                # <Value 'groups' (153:43)> -> __iterator
                __token = 6446
                try:
                    __zt_tmp = __attrs_140310475172080
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140310567013776('path', 'groups', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                (__iterator, ____index_140310475822832, ) = getname('repeat')('group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f9c9411da50> name=None at 7f9c9411c280> -> __attrs_140310475829552
                    __attrs_140310475829552 = _static_140310475823696
                    __backup_normalizeString_140310475169920 = get('normalizeString', __marker)

                    # <Value 'nocall:context/@@plone/normalizeString' (156:44)> -> __value
                    __token = 6553
                    try:
                        __zt_tmp = __attrs_140310475829552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('nocall', 'context/@@plone/normalizeString', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value
                    __backup_fieldset_label_140310475167712 = get('fieldset_label', __marker)

                    # <Value 'group/label' (157:42)> -> __value
                    __token = 6635
                    try:
                        __zt_tmp = __attrs_140310475829552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('path', 'group/label', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['fieldset_label'] = __value
                    __backup_fieldset_name_140310475173328 = get('fieldset_name', __marker)

                    # <Value "python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label" (158:40)> -> __value
                    __token = 6689
                    try:
                        __zt_tmp = __attrs_140310475829552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('python', "getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label", econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_fieldset_name_140310475823648 = get('fieldset_name', __marker)

                    # <Value 'python:normalizeString(fieldset_name)' (159:39)> -> __value
                    __token = 6832
                    try:
                        __zt_tmp = __attrs_140310475829552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('python', 'normalizeString(fieldset_name)', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset')

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475832576
                    __default_140310475832576 = _DEFAULT_MARKER

                    # <Substitution 'string:fieldset-${fieldset_name}' (162:31)> -> __attr_id
                    __token = 6976
                    try:
                        __zt_tmp = __attrs_140310475829552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140310567013776('string', 'fieldset-${fieldset_name}', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475820288
                    __default_140310475820288 = _DEFAULT_MARKER

                    # <Substitution 'string:kssattr-fieldset-${fieldset_name}' (163:33)> -> __attr_class
                    __token = 7043
                    try:
                        __zt_tmp = __attrs_140310475829552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140310567013776('string', 'kssattr-fieldset-${fieldset_name}', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475830224
                    __default_140310475830224 = _DEFAULT_MARKER

                    # <Substitution 'fieldset_name' (164:40)> -> __attr_data_fieldset
                    __token = 7126
                    try:
                        __zt_tmp = __attrs_140310475829552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_fieldset = _static_140310567013776('path', 'fieldset_name', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __attr_data_fieldset = __quote(__attr_data_fieldset, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_fieldset is not None):
                        __append((' data-fieldset="%s"' % __attr_data_fieldset))
                    __append(' >\n\n                  ')

                    # <Static value=<ast.Dict object at 0x7f9c9411d450> name=None at 7f9c9411f2b0> -> __attrs_140310475827536
                    __attrs_140310475827536 = _static_140310475822160

                    # <Value 'fieldset_label' (168:41)> -> __condition
                    __token = 7231
                    try:
                        __zt_tmp = __attrs_140310475827536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140310567013776('path', 'fieldset_label', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    if __condition:

                        # <legend ... (0:0)
                        # --------------------------------------------------------
                        __append('<legend')

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475826192
                        __default_140310475826192 = _DEFAULT_MARKER

                        # <Substitution 'string:fieldsetlegend-${fieldset_name}' (171:31)> -> __attr_id
                        __token = 7376
                        try:
                            __zt_tmp = __attrs_140310475827536
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140310567013776('string', 'fieldsetlegend-${fieldset_name}', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475818368
                        __default_140310475818368 = _DEFAULT_MARKER

                        # <Value 'fieldset_label' (169:39)> -> __cache_140310475818032
                        __token = 7286
                        try:
                            __zt_tmp = __attrs_140310475827536
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140310475818032 = _static_140310567013776('path', 'fieldset_label', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                        # <BinOp left=<Value 'fieldset_label' (169:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9411c220> -> __condition
                        __expression = __cache_140310475818032

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Form name')
                        else:
                            __content = __cache_140310475818032
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</legend>')
                    __append('\n\n                  ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475825376
                    __attrs_140310475825376 = _static_140310566789392
                    __backup_group_description_140310475832432 = get('group_description', __marker)

                    # <Value 'group/description|nothing' (177:41)> -> __value
                    __token = 7602
                    try:
                        __zt_tmp = __attrs_140310475825376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('path', 'group/description|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['group_description'] = __value

                    # <Value 'group_description' (179:36)> -> __condition
                    __token = 7688
                    try:
                        __zt_tmp = __attrs_140310475825376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140310567013776('path', 'group_description', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p >')

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475826768
                        __default_140310475826768 = _DEFAULT_MARKER

                        # <Value 'group_description' (180:44)> -> __cache_140310475832960
                        __token = 7751
                        try:
                            __zt_tmp = __attrs_140310475825376
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140310475832960 = _static_140310567013776('path', 'group_description', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                        # <BinOp left=<Value 'group_description' (180:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9411fc40> -> __condition
                        __expression = __cache_140310475832960

                        # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                                          Description\n                  ')
                        else:
                            __content = __cache_140310475832960
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('</p>')
                    if (__backup_group_description_140310475832432 is __marker):
                        del econtext['group_description']
                    else:
                        econtext['group_description'] = __backup_group_description_140310475832432
                    __append('\n\n                  ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475823984
                    __attrs_140310475823984 = _static_140310566789392
                    __backup_errors_140310475822928 = get('errors', __marker)

                    # <Value 'group/widgets/errors' (187:38)> -> __value
                    __token = 7987
                    try:
                        __zt_tmp = __attrs_140310475823984
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('path', 'group/widgets/errors', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['errors'] = __value

                    # <Value 'errors' (189:44)> -> __condition
                    __token = 8084
                    try:
                        __zt_tmp = __attrs_140310475823984
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140310567013776('path', 'errors', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    if __condition:
                        __backup_error_140310475822112 = get('error', __marker)

                        # <Value 'errors' (190:47)> -> __iterator
                        __token = 8139
                        try:
                            __zt_tmp = __attrs_140310475823984
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140310567013776('path', 'errors', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                        (__iterator, ____index_140310272583872, ) = getname('repeat')('error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f9c87f4ab00> name=None at 7f9c87f49f60> -> __attrs_140310272581520
                            __attrs_140310272581520 = _static_140310272584448

                            # <Value 'not:nocall:error/widget' (193:40)> -> __condition
                            __token = 8252
                            try:
                                __zt_tmp = __attrs_140310272581520
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140310567013776('not', 'nocall:error/widget', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="field error" >')

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272583056
                                __default_140310272583056 = _DEFAULT_MARKER

                                # <Value 'error/render' (194:48)> -> __cache_140310272582432
                                __token = 8325
                                try:
                                    __zt_tmp = __attrs_140310272581520
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140310272582432 = _static_140310567013776('path', 'error/render', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                                # <BinOp left=<Value 'error/render' (194:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f4ab30> -> __condition
                                __expression = __cache_140310272582432

                                # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140310272582432
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</div>')
                            __append('\n                  ')
                            ____index_140310272583872 -= 1
                            if (____index_140310272583872 > 0):
                                __append('')
                        if (__backup_error_140310475822112 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_140310475822112
                    if (__backup_errors_140310475822928 is __marker):
                        del econtext['errors']
                    else:
                        econtext['errors'] = __backup_errors_140310475822928
                    __append('\n\n                  ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272585264
                    __attrs_140310272585264 = _static_140310566789392
                    __backup_view_140310475822640 = get('view', __marker)

                    # <Value 'nocall:group' (199:36)> -> __value
                    __token = 8473
                    try:
                        __zt_tmp = __attrs_140310272585264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140310567013776('nocall', 'group', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    econtext['view'] = __value
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272580752
                    __attrs_140310272580752 = _static_140310566789392
                    __backup_macroname_140310523519424 = get('macroname', __marker)

                    # <Static value=<ast.Constant object at 0x7f9c87f49bd0> name=None at 7f9c87f485b0> -> __value
                    __value = _static_140310272580560
                    econtext['macroname'] = __value

                    # <Value 'context/@@ploneform-macros/widget_rendering' (201:44)> -> __macro
                    __token = 8563
                    try:
                        __zt_tmp = __attrs_140310272580752
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140310567013776('path', 'context/@@ploneform-macros/widget_rendering', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                    __token = 8563
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140310523519424 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140310523519424
                    __append('\n                  ')
                    if (__backup_view_140310475822640 is __marker):
                        del econtext['view']
                    else:
                        econtext['view'] = __backup_view_140310475822640
                    __append('\n\n                </fieldset>')
                    if (__backup_fieldset_name_140310475823648 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140310475823648
                    if (__backup_fieldset_name_140310475173328 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140310475173328
                    if (__backup_fieldset_label_140310475167712 is __marker):
                        del econtext['fieldset_label']
                    else:
                        econtext['fieldset_label'] = __backup_fieldset_label_140310475167712
                    if (__backup_normalizeString_140310475169920 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_140310475169920
                    __append('\n              ')
                    ____index_140310475822832 -= 1
                    if (____index_140310475822832 > 0):
                        __append('')
                if (__backup_group_140310475172368 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140310475172368
            __append('\n\n            ')
            if (__backup_has_groups_140310475280528 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_140310475280528
            if (__backup_show_default_label_140310475284368 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_140310475284368
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475174336
            __attrs_140310475174336 = _static_140310566789392
            __append('\n                  ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475167376
            __attrs_140310475167376 = _static_140310566789392
            __backup_widget_140310475163584 = get('widget', __marker)

            # <Value 'python:view.widgets.values()' (141:46)> -> __iterator
            __token = 5900
            try:
                __zt_tmp = __attrs_140310475167376
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140310567013776('python', 'view.widgets.values()', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            (__iterator, ____index_140310475163440, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n                    ')
                if (__slot_field is None):

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475832000
                    __attrs_140310475832000 = _static_140310566789392
                    __append('\n                      ')
                    __token = None
                    render_field(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n                    ')
                else:
                    __slot_field(__stream, econtext.copy(), rcontext)
                __append('\n                  ')
                ____index_140310475163440 -= 1
                if (____index_140310475163440 > 0):
                    __append('')
            if (__backup_widget_140310475163584 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140310475163584
            __append('\n                ')
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475823120
            __attrs_140310475823120 = _static_140310566789392
            __append('\n                        ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475817072
            __attrs_140310475817072 = _static_140310566789392

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475825952
            __default_140310475825952 = _DEFAULT_MARKER

            # <Value 'widget/@@ploneform-render-widget' (144:59)> -> __cache_140310475822736
            __token = 6106
            try:
                __zt_tmp = __attrs_140310475817072
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140310475822736 = _static_140310567013776('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

            # <BinOp left=<Value 'widget/@@ploneform-render-widget' (144:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9411fca0> -> __condition
            __expression = __cache_140310475822736

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140310475822736
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n                      ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_actions(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272576912
            __attrs_140310272576912 = _static_140310566789392
            __append('\n              ')

            # <Static value=<ast.Dict object at 0x7f9c87f4bcd0> name=None at 7f9c87f4a650> -> __attrs_140310272573840
            __attrs_140310272573840 = _static_140310272589008

            # <Value 'view/actions/values|nothing' (215:34)> -> __condition
            __token = 8984
            try:
                __zt_tmp = __attrs_140310272573840
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140310567013776('path', 'view/actions/values|nothing', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls" >\n                ')

                # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272584256
                __attrs_140310272584256 = _static_140310566789392
                __backup_action_140310475818272 = get('action', __marker)

                # <Value 'view/actions/values' (217:42)> -> __iterator
                __token = 9071
                try:
                    __zt_tmp = __attrs_140310272584256
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140310567013776('path', 'view/actions/values', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
                (__iterator, ____index_140310272574704, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append('\n                  ')

                    # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272576384
                    __attrs_140310272576384 = _static_140310566789392

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310272574176
                    __default_140310272574176 = _DEFAULT_MARKER

                    # <Value 'action/render' (218:48)> -> __cache_140310272588912
                    __token = 9141
                    try:
                        __zt_tmp = __attrs_140310272576384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140310272588912 = _static_140310567013776('path', 'action/render', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/render' (218:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c87f4a470> -> __condition
                    __expression = __cache_140310272588912

                    # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input />')
                    else:
                        __content = __cache_140310272588912
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                ')
                    ____index_140310272574704 -= 1
                    if (____index_140310272574704 > 0):
                        __append('')
                if (__backup_action_140310475818272 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140310475818272
                __append('\n              </div>')
            __append('\n            ')
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

            # <Static value=<ast.Dict object at 0x7f9c87f6ba30> name=None at 7f9c87f6a5c0> -> __attrs_140310272718112
            __attrs_140310272718112 = _static_140310272719408
            __previous_i18n_domain_140310272705008 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" >\n\n  ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272333696
            __attrs_140310272333696 = _static_140310566789392

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n    ')
            __token = None
            render_form(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140310272705008
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_form': render_form, 'render_titlelessform': render_titlelessform, 'render_fields': render_fields, 'render_widget_rendering': render_widget_rendering, 'render_field': render_field, 'render_actions': render_actions, 'render': render, }