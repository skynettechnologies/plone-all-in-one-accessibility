# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.formwidget.recurrence-3.0.3-py3.10.egg/plone/formwidget/recurrence/z3cform/recurrence_input.pt'

__tokens = {182: ("python:view.read_only != 'true'", 6, 27), 298: ('view/id', 9, 17), 325: (' view/nam', 10, 18), 355: ('e view/sty', 11, 18), 386: ('le view/ti', 12, 17), 431: ('nce python: view.get_pattern_optio', 13, 30), 240: ('view/value', 7, 25), 553: ("python:view.read_only == 'true'", 17, 23), 666: ('string:${view/id}-start', 20, 13), 705: (' string:${view/name}-star', 21, 14), 607: ('view/get_start_date', 18, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139856820731232 = {'style': 'display:none;', 'id': 'string:${view/id}-start', 'name': 'string:${view/name}-start', }
_static_139856914195856 = __C2ZContextWrapper
_static_139856914196144 = __compile_zt_expr
_static_139856823418064 = {'class': 'pat-recurrence', 'id': 'view/id', 'name': 'view/name', 'style': 'view/style', 'title': 'view/title', 'data-pat-recurrence': 'python: view.get_pattern_options()', }
_static_139856823409136 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f32f44759f0> name=None at 7f32f4477370> -> __attrs_139856823411920
            __attrs_139856823411920 = _static_139856823409136
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f32f4477cd0> name=None at 7f32f4477d30> -> __attrs_139856823408512
            __attrs_139856823408512 = _static_139856823418064

            # <Value "python:view.read_only != 'true'" (6:27)> -> __condition
            __token = 182
            try:
                __zt_tmp = __attrs_139856823408512
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139856914196144('python', "view.read_only != 'true'", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if __condition:

                # <textarea ... (0:0)
                # --------------------------------------------------------
                __append('<textarea class="pat-recurrence"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823403280
                __default_139856823403280 = _DEFAULT_MARKER

                # <Substitution 'view/id' (9:17)> -> __attr_id
                __token = 298
                try:
                    __zt_tmp = __attrs_139856823408512
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_139856914196144('path', 'view/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823402752
                __default_139856823402752 = _DEFAULT_MARKER

                # <Substitution 'view/name' (10:18)> -> __attr_name
                __token = 325
                try:
                    __zt_tmp = __attrs_139856823408512
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_139856914196144('path', 'view/name', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823407888
                __default_139856823407888 = _DEFAULT_MARKER

                # <Substitution 'view/style' (11:18)> -> __attr_style
                __token = 355
                try:
                    __zt_tmp = __attrs_139856823408512
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_style = _static_139856914196144('path', 'view/style', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_style is not None):
                    __append((' style="%s"' % __attr_style))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823408656
                __default_139856823408656 = _DEFAULT_MARKER

                # <Substitution 'view/title' (12:17)> -> __attr_title
                __token = 386
                try:
                    __zt_tmp = __attrs_139856823408512
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_139856914196144('path', 'view/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823417824
                __default_139856823417824 = _DEFAULT_MARKER

                # <Substitution 'python: view.get_pattern_options()' (13:30)> -> __attr_data_pat_recurrence
                __token = 431
                try:
                    __zt_tmp = __attrs_139856823408512
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_recurrence = _static_139856914196144('python', ' view.get_pattern_options()', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_data_pat_recurrence = __quote(__attr_data_pat_recurrence, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_pat_recurrence is not None):
                    __append((' data-pat-recurrence="%s"' % __attr_data_pat_recurrence))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823414320
                __default_139856823414320 = _DEFAULT_MARKER

                # <Value 'view/value' (7:25)> -> __cache_139856823413840
                __token = 240
                try:
                    __zt_tmp = __attrs_139856823408512
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139856823413840 = _static_139856914196144('path', 'view/value', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/value' (7:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f4477dc0> -> __condition
                __expression = __cache_139856823413840

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139856823413840
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</textarea>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f32f41e7d60> name=None at 7f32f41e6170> -> __attrs_139856820725424
            __attrs_139856820725424 = _static_139856820731232

            # <Value "python:view.read_only == 'true'" (17:23)> -> __condition
            __token = 553
            try:
                __zt_tmp = __attrs_139856820725424
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139856914196144('python', "view.read_only == 'true'", econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span style="display:none;"')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820726000
                __default_139856820726000 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-start' (20:13)> -> __attr_id
                __token = 666
                try:
                    __zt_tmp = __attrs_139856820725424
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_139856914196144('string', '${view/id}-start', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820719232
                __default_139856820719232 = _DEFAULT_MARKER

                # <Substitution 'string:${view/name}-start' (21:14)> -> __attr_name
                __token = 705
                try:
                    __zt_tmp = __attrs_139856820725424
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_139856914196144('string', '${view/name}-start', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856820729168
                __default_139856820729168 = _DEFAULT_MARKER

                # <Value 'view/get_start_date' (18:21)> -> __cache_139856822273792
                __token = 607
                try:
                    __zt_tmp = __attrs_139856820725424
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139856822273792 = _static_139856914196144('path', 'view/get_start_date', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/get_start_date' (18:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f43632e0> -> __condition
                __expression = __cache_139856822273792

                # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139856822273792
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>')
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }