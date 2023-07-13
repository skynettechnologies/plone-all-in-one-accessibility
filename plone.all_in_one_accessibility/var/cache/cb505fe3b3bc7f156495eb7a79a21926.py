# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/social_tags_body.pt'

__tokens = {141: ('view/body_tags', 6, 24), 243: ('tag/itemprop|nothing', 9, 19), 178: ('tag/content|nothing', 7, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882206156288 = {'itemprop': 'tag/itemprop|nothing', }
_static_139882239384912 = {'id': 'social-tags-body', 'itemscope': '', 'itemtype': 'http://schema.org/WebPage', 'style': 'display: none', }

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

            # <Static value=<ast.Dict object at 0x7f38df305d50> name=None at 7f38dd3a18a0> -> __attrs_139882206151056
            __attrs_139882206151056 = _static_139882239384912

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span id="social-tags-body" itemscope itemtype="http://schema.org/WebPage" style="display: none" >\n  ')

            # <Static value=<ast.Dict object at 0x7f38dd355600> name=None at 7f38dd357d90> -> __attrs_139882206157008
            __attrs_139882206157008 = _static_139882206156288
            __backup_tag_139882241549184 = get('tag', __marker)

            # <Value 'view/body_tags' (6:24)> -> __iterator
            __token = 141
            try:
                __zt_tmp = __attrs_139882206157008
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139882257081264('path', 'view/body_tags', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            (__iterator, ____index_139882206164736, ) = getname('repeat')('tag', __iterator)
            econtext['tag'] = None
            for __item in __iterator:
                econtext['tag'] = __item

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206152640
                __default_139882206152640 = _DEFAULT_MARKER

                # <Substitution 'tag/itemprop|nothing' (9:19)> -> __attr_itemprop
                __token = 243
                try:
                    __zt_tmp = __attrs_139882206157008
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_itemprop = _static_139882257081264('path', 'tag/itemprop|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                __attr_itemprop = __quote(__attr_itemprop, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_itemprop is not None):
                    __append((' itemprop="%s"' % __attr_itemprop))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206164256
                __default_139882206164256 = _DEFAULT_MARKER

                # <Value 'tag/content|nothing' (7:21)> -> __cache_139882206161520
                __token = 178
                try:
                    __zt_tmp = __attrs_139882206157008
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882206161520 = _static_139882257081264('path', 'tag/content|nothing', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                # <BinOp left=<Value 'tag/content|nothing' (7:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd354fd0> -> __condition
                __expression = __cache_139882206161520

                # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139882206161520
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>')
                ____index_139882206164736 -= 1
                if (____index_139882206164736 > 0):
                    __append('\n  ')
            if (__backup_tag_139882241549184 is __marker):
                del econtext['tag']
            else:
                econtext['tag'] = __backup_tag_139882241549184
            __append('\n</span>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }