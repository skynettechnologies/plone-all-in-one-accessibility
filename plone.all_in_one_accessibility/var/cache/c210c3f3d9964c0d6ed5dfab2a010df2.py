# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/nextprevious/links.pt'

__tokens = {181: ('view/enabled|nothing', 5, 15), 224: (' view/isViewTemplate|nothin', 6, 21), 281: ('python:enabled and isViewTemplate', 8, 20), 455: ('view/previous', 16, 19), 503: ('previous', 18, 23), 553: ('previous/url', 20, 15), 738: ('view/next', 29, 15), 782: ('next', 31, 23), 828: ('next/url', 33, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882101070128 = {'href': '', 'rel': 'next', 'title': 'Go to next item', }
_static_139882205934016 = {'href': '', 'rel': 'previous', 'title': 'Go to previous item', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882205937184 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f38dd31fe20> name=None at 7f38dd31efb0> -> __attrs_139882205929888
            __attrs_139882205929888 = _static_139882205937184
            __backup_enabled_139882206111648 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (5:15)> -> __value
            __token = 181
            try:
                __zt_tmp = __attrs_139882205929888
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/enabled|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_139882206111456 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (6:21)> -> __value
            __token = 224
            try:
                __zt_tmp = __attrs_139882205929888
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (8:20)> -> __condition
            __token = 281
            try:
                __zt_tmp = __attrs_139882205929888
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('python', 'enabled and isViewTemplate', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38dd31f1c0> name=None at 7f38dd31e560> -> __attrs_139882101069216
                __attrs_139882101069216 = _static_139882205934016
                __backup_previous_139882206116832 = get('previous', __marker)

                # <Value 'view/previous' (16:19)> -> __value
                __token = 455
                try:
                    __zt_tmp = __attrs_139882101069216
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/previous', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'previous' (18:23)> -> __condition
                __token = 503
                try:
                    __zt_tmp = __attrs_139882101069216
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'previous', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append('<link')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101069648
                    __default_139882101069648 = _DEFAULT_MARKER

                    # <Substitution 'previous/url' (20:15)> -> __attr_href
                    __token = 553
                    try:
                        __zt_tmp = __attrs_139882101069216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('path', 'previous/url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="previous"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101069360
                    __default_139882101069360 = _DEFAULT_MARKER

                    # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x7f38d6f1cc10> at 7f38d6f1e410> -> __attr_title
                    __attr_title = 'Go to previous item'
                    __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                if (__backup_previous_139882206116832 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_139882206116832
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38d6f1d930> name=None at 7f38d6f1fd60> -> __attrs_139882101077952
                __attrs_139882101077952 = _static_139882101070128
                __backup_next_139882206117264 = get('next', __marker)

                # <Value 'view/next' (29:15)> -> __value
                __token = 738
                try:
                    __zt_tmp = __attrs_139882101077952
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/next', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['next'] = __value

                # <Value 'next' (31:23)> -> __condition
                __token = 782
                try:
                    __zt_tmp = __attrs_139882101077952
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'next', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append('<link')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101067392
                    __default_139882101067392 = _DEFAULT_MARKER

                    # <Substitution 'next/url' (33:15)> -> __attr_href
                    __token = 828
                    try:
                        __zt_tmp = __attrs_139882101077952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139882257081264('path', 'next/url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="next"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101078960
                    __default_139882101078960 = _DEFAULT_MARKER

                    # <Translate msgid='title_next_item' node=<ast.Constant object at 0x7f38d6f1f880> at 7f38d6f1d420> -> __attr_title
                    __attr_title = 'Go to next item'
                    __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                if (__backup_next_139882206117264 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_139882206117264
                __append('\n\n')
            if (__backup_isViewTemplate_139882206111456 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_139882206111456
            if (__backup_enabled_139882206111648 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_139882206111648
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }