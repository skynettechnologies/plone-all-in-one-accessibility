# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/links/search.pt'

__tokens = {55: ('view/navigation_root_url', 2, 34), 239: ('string:${navigation_root_url}/@@search', 10, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882205895104 = {'href': '', 'rel': 'search', 'title': 'Search this site', }
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

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205892704
            __attrs_139882205892704 = _static_139882337226896
            __backup_navigation_root_url_139882205928016 = get('navigation_root_url', __marker)

            # <Value 'view/navigation_root_url' (2:34)> -> __value
            __token = 55
            try:
                __zt_tmp = __attrs_139882205892704
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('path', 'view/navigation_root_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_139882205889872 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f38dd3159c0> name=None at 7f38dd3157b0> -> __attrs_139882205899760
            __attrs_139882205899760 = _static_139882205895104

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205895584
            __default_139882205895584 = _DEFAULT_MARKER

            # <Substitution 'string:${navigation_root_url}/@@search' (10:15)> -> __attr_href
            __token = 239
            try:
                __zt_tmp = __attrs_139882205899760
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139882257081264('string', '${navigation_root_url}/@@search', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' rel="search"')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205897408
            __default_139882205897408 = _DEFAULT_MARKER

            # <Translate msgid='title_search_this_site' node=<ast.Constant object at 0x7f38dd3158a0> at 7f38dd315420> -> __attr_title
            __attr_title = 'Search this site'
            __attr_title = translate('title_search_this_site', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' />\n')
            __i18n_domain = __previous_i18n_domain_139882205889872
            if (__backup_navigation_root_url_139882205928016 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_139882205928016
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }