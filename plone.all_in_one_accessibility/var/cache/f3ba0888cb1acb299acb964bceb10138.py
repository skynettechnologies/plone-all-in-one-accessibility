# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.z3cform-4.2.1-py3.10.egg/plone/app/z3cform/templates/widget.pt'

__tokens = {331: ('nocall:context', 6, 14), 359: (' python:widget.erro', 7, 12), 398: ("s python:error and ' error' or ", 8, 17), 450: ("es python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', '", 9, 17), 536: ("ass python: (widget.value in empty_values) and ' empty' o", 10, 15), 12: ("mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}", 1, 12), 35: ('python:widget.name', 1, 35), 69: ('python:widget.mode', 1, 69), 90: ('error_class', 1, 90), 104: ('empty_class', 1, 104), 119: ("python:getattr(widget, 'wrapper_css_class', False) or False", 1, 119), 190: ('formfield-${python:widget.id}', 2, 9), 202: ('python:widget.id', 2, 21), 283: ('${widget/name}', 4, 21), 285: ('widget/name', 4, 23), 720: ("python: widget.mode == 'input' and widget.label", 16, 24), 675: ('${python:widget.id}', 15, 14), 677: ('python:widget.id', 15, 16), 796: ('python:widget.label', 18, 23), 943: ('python:widget.required', 24, 25), 1106: ("python: widget.mode == 'display' and widget.label", 29, 20), 1184: ('python:widget.label', 31, 23), 1348: ('python:widget.render()', 38, 32), 1444: ("python: getattr(widget, 'description', widget.field.description)", 43, 21), 1541: ("python:description and widget.mode == 'input'", 45, 22), 1618: ('description', 46, 30), 1708: ('error', 52, 22), 1745: ('python:error.render() or False', 53, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882205991536 = {'class': 'form-text', }
_static_139882241830496 = {'type': 'text', }
_static_139882098523968 = {'class': 'widget-label form-label d-block', }
_static_139882098520944 = {'class': 'required', 'title': 'Required', }
_static_139882337226896 = {}
_static_139882098512544 = {'class': 'form-label', 'for': '${python:widget.id}', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882098511536 = {'class': "mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}", 'id': 'formfield-${python:widget.id}', 'data-fieldname': '${widget/name}', }

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

    def render_widget_wrapper(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_widget = econtext['__slot_widget'].pop()
        except:
            __slot_widget = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f38d6caceb0> name=None at 7f38d6cac580> -> __attrs_139882098511728
            __attrs_139882098511728 = _static_139882098511536
            __backup_widget_139882100930160 = get('widget', __marker)

            # <Value 'nocall:context' (6:14)> -> __value
            __token = 331
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('nocall', 'context', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['widget'] = __value
            __backup_error_139882206283088 = get('error', __marker)

            # <Value 'python:widget.error' (7:12)> -> __value
            __token = 359
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', 'widget.error', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_error_class_139882205855072 = get('error_class', __marker)

            # <Value "python:error and ' error' or ''" (8:17)> -> __value
            __token = 398
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', "error and ' error' or ''", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['error_class'] = __value
            __backup_empty_values_139882101461136 = get('empty_values', __marker)

            # <Value "python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))" (9:17)> -> __value
            __token = 450
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', " (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['empty_values'] = __value
            __backup_empty_class_139882099586624 = get('empty_class', __marker)

            # <Value "python: (widget.value in empty_values) and ' empty' or ''" (10:15)> -> __value
            __token = 536
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', " (widget.value in empty_values) and ' empty' or ''", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['empty_class'] = __value
            __previous_i18n_domain_139882098519168 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098515568
            __default_139882098515568 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}" (1:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38d6cadb70> -> __attr_class
            __token = 12
            __token = 35
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139882257081264('python', 'widget.name', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 69
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_67 = _static_139882257081264('python', 'widget.mode', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class_67 = __quote(__attr_class_67, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 90
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_88 = _static_139882257081264('path', 'error_class', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class_88 = __quote(__attr_class_88, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 104
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_102 = _static_139882257081264('path', 'empty_class', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class_102 = __quote(__attr_class_102, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 119
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_117 = _static_139882257081264('python', "getattr(widget, 'wrapper_css_class', False) or False", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_class_117 = __quote(__attr_class_117, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s%s%s%s%s%s%s' % ('mb-3 field fieldname-', (__attr_class if (__attr_class is not None) else ''), ' widget-mode-', (__attr_class_67 if (__attr_class_67 is not None) else ''), (__attr_class_88 if (__attr_class_88 is not None) else ''), (__attr_class_102 if (__attr_class_102 is not None) else ''), ' ', (__attr_class_117 if (__attr_class_117 is not None) else ''), ))
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098512400
            __default_139882098512400 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'formfield-${python:widget.id}' (2:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38d6cac130> -> __attr_id
            __token = 190
            __token = 202
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_139882257081264('python', 'widget.id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_id = ('%s%s' % ('formfield-', (__attr_id if (__attr_id is not None) else ''), ))
            if (__attr_id is None):
                pass
            else:
                if (__attr_id is _DEFAULT_MARKER):
                    __attr_id = None
                else:
                    __tt = type(__attr_id)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_id = str(__attr_id)
                    else:
                        if (__tt is bytes):
                            __attr_id = decode(__attr_id)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_id = __attr_id.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_id)
                                    __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                else:
                                    __attr_id = __attr_id()
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098514272
            __default_139882098514272 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${widget/name}' (4:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38d6cad9f0> -> __attr_data_fieldname
            __token = 283
            __token = 285
            try:
                __zt_tmp = __attrs_139882098511728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_139882257081264('path', 'widget/name', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_fieldname = __attr_data_fieldname
            if (__attr_data_fieldname is None):
                pass
            else:
                if (__attr_data_fieldname is _DEFAULT_MARKER):
                    __attr_data_fieldname = None
                else:
                    __tt = type(__attr_data_fieldname)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_data_fieldname = str(__attr_data_fieldname)
                    else:
                        if (__tt is bytes):
                            __attr_data_fieldname = decode(__attr_data_fieldname)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_data_fieldname = __attr_data_fieldname.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_fieldname)
                                    __attr_data_fieldname = (str(__attr_data_fieldname) if (__attr_data_fieldname is __converted) else __converted)
                                else:
                                    __attr_data_fieldname = __attr_data_fieldname()
            if (__attr_data_fieldname is not None):
                __append((' data-fieldname="%s"' % __attr_data_fieldname))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7f38d6cad2a0> name=None at 7f38d6cae5f0> -> __attrs_139882098516144
            __attrs_139882098516144 = _static_139882098512544

            # <Value "python: widget.mode == 'input' and widget.label" (16:24)> -> __condition
            __token = 720
            try:
                __zt_tmp = __attrs_139882098516144
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('python', " widget.mode == 'input' and widget.label", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label"')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098512832
                __default_139882098512832 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${python:widget.id}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38d6caead0> -> __attr_for
                __token = 675
                __token = 677
                try:
                    __zt_tmp = __attrs_139882098516144
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_139882257081264('python', 'widget.id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_for = __attr_for
                if (__attr_for is None):
                    pass
                else:
                    if (__attr_for is _DEFAULT_MARKER):
                        __attr_for = None
                    else:
                        __tt = type(__attr_for)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_for = str(__attr_for)
                        else:
                            if (__tt is bytes):
                                __attr_for = decode(__attr_for)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_for = __attr_for.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_for)
                                        __attr_for = (str(__attr_for) if (__attr_for is __converted) else __converted)
                                    else:
                                        __attr_for = __attr_for()
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append(' >\n    ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882098522816
                __attrs_139882098522816 = _static_139882337226896

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098522720
                __default_139882098522720 = _DEFAULT_MARKER

                # <Value 'python:widget.label' (18:23)> -> __cache_139882098521232
                __token = 796
                try:
                    __zt_tmp = __attrs_139882098522816
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882098521232 = _static_139882257081264('python', 'widget.label', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.label' (18:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6cafee0> -> __condition
                __expression = __cache_139882098521232

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >label</span>')
                else:
                    __content = __cache_139882098521232
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38d6caf370> name=None at 7f38d6cafd30> -> __attrs_139882098520368
                __attrs_139882098520368 = _static_139882098520944

                # <Value 'python:widget.required' (24:25)> -> __condition
                __token = 943
                try:
                    __zt_tmp = __attrs_139882098520368
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('python', 'widget.required', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="required"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098523104
                    __default_139882098523104 = _DEFAULT_MARKER

                    # <Translate msgid='title_required' node=<ast.Constant object at 0x7f38d6cafc70> at 7f38d6caee90> -> __attr_title
                    __attr_title = 'Required'
                    __attr_title = translate('title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' ></span>')
                __append('\n  </label>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f38d6caff40> name=None at 7f38d6caf400> -> __attrs_139882098511920
            __attrs_139882098511920 = _static_139882098523968

            # <Value "python: widget.mode == 'display' and widget.label" (29:20)> -> __condition
            __token = 1106
            try:
                __zt_tmp = __attrs_139882098511920
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('python', " widget.mode == 'display' and widget.label", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:

                # <b ... (0:0)
                # --------------------------------------------------------
                __append('<b class="widget-label form-label d-block" >\n    ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882217705808
                __attrs_139882217705808 = _static_139882337226896

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882098513312
                __default_139882098513312 = _DEFAULT_MARKER

                # <Value 'python:widget.label' (31:23)> -> __cache_139882098511872
                __token = 1184
                try:
                    __zt_tmp = __attrs_139882217705808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882098511872 = _static_139882257081264('python', 'widget.label', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.label' (31:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6caf460> -> __condition
                __expression = __cache_139882098511872

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >label</span>')
                else:
                    __content = __cache_139882098511872
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </b>')
            __append('\n\n  ')
            if (__slot_widget is None):

                # <Static value=<ast.Dict object at 0x7f38df55ae60> name=None at 7f38df55a920> -> __attrs_139882205990912
                __attrs_139882205990912 = _static_139882241830496

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205999552
                __default_139882205999552 = _DEFAULT_MARKER

                # <Value 'python:widget.render()' (38:32)> -> __cache_139882206000608
                __token = 1348
                try:
                    __zt_tmp = __attrs_139882205990912
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882206000608 = _static_139882257081264('python', 'widget.render()', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.render()' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd32e380> -> __condition
                __expression = __cache_139882206000608

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="text" />')
                else:
                    __content = __cache_139882206000608
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            else:
                __slot_widget(__stream, econtext.copy(), rcontext)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f38dd32d270> name=None at 7f38dd32db40> -> __attrs_139882206003152
            __attrs_139882206003152 = _static_139882205991536
            __backup_description_139882101372144 = get('description', __marker)

            # <Value "python: getattr(widget, 'description', widget.field.description)" (43:21)> -> __value
            __token = 1444
            try:
                __zt_tmp = __attrs_139882206003152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', " getattr(widget, 'description', widget.field.description)", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['description'] = __value

            # <Value "python:description and widget.mode == 'input'" (45:22)> -> __condition
            __token = 1541
            try:
                __zt_tmp = __attrs_139882206003152
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('python', "description and widget.mode == 'input'", econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text" >')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205993648
                __default_139882205993648 = _DEFAULT_MARKER

                # <Value 'description' (46:30)> -> __cache_139882205987552
                __token = 1618
                try:
                    __zt_tmp = __attrs_139882206003152
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882205987552 = _static_139882257081264('path', 'description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value 'description' (46:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd32db70> -> __condition
                __expression = __cache_139882205987552

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      help text\n  ')
                else:
                    __content = __cache_139882205987552
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            if (__backup_description_139882101372144 is __marker):
                del econtext['description']
            else:
                econtext['description'] = __backup_description_139882101372144
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206002480
            __attrs_139882206002480 = _static_139882337226896

            # <Value 'error' (52:22)> -> __condition
            __token = 1708
            try:
                __zt_tmp = __attrs_139882206002480
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('path', 'error', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206001616
                __default_139882206001616 = _DEFAULT_MARKER

                # <Value 'python:error.render() or False' (53:30)> -> __cache_139882206001136
                __token = 1745
                try:
                    __zt_tmp = __attrs_139882206002480
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882206001136 = _static_139882257081264('python', 'error.render() or False', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:error.render() or False' (53:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd32d090> -> __condition
                __expression = __cache_139882206001136

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div >\n        Error\n  </div>')
                else:
                    __content = __cache_139882206001136
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n\n</div>')
            __i18n_domain = __previous_i18n_domain_139882098519168
            if (__backup_empty_class_139882099586624 is __marker):
                del econtext['empty_class']
            else:
                econtext['empty_class'] = __backup_empty_class_139882099586624
            if (__backup_empty_values_139882101461136 is __marker):
                del econtext['empty_values']
            else:
                econtext['empty_values'] = __backup_empty_values_139882101461136
            if (__backup_error_class_139882205855072 is __marker):
                del econtext['error_class']
            else:
                econtext['error_class'] = __backup_error_class_139882205855072
            if (__backup_error_139882206283088 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_139882206283088
            if (__backup_widget_139882100930160 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_139882100930160
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
            render_widget_wrapper(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_widget_wrapper': render_widget_wrapper, 'render': render, }