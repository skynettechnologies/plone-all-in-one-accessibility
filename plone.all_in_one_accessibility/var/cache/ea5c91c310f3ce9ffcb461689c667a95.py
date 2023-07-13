# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.content-4.0.2-py3.10.egg/plone/app/content/browser/contents/templates/rename.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_140148358687920 = {'class': 'thumb-thumb', 'src': '<%= item.getURL %>/@@images/image/thumb', }
_static_140148358684848 = {'class': 'form-control', 'name': 'newid_<%= index %>', 'value': '<%= item.id %>', }
_static_140148358680192 = {'class': 'form-label', }
_static_140148358680048 = {'class': 'mb-2', }
_static_140148358681632 = {'class': 'form-control', 'name': 'newtitle_<%= index %>', 'value': '<%= item.Title %>', }
_static_140148358556560 = {'class': 'form-label', }
_static_140148358558384 = {'class': 'mb-2', }
_static_140148358559248 = {'name': 'UID_<%= index %>', 'type': 'hidden', 'value': '<%- item.UID %>', }
_static_140148358559776 = {'class': 'mb-3 pb-3 <% if (items.length > 1){%>border-bottom<% } %>', }
_static_140148358555504 = {'class': 'itemstoremove row row-cols-1', }

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

            # <Static value=<ast.Dict object at 0x7f76d520a770> name=None at 7f76d520a7a0> -> __attrs_140148358555072
            __attrs_140148358555072 = _static_140148358555504
            __previous_i18n_domain_140148358549792 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="itemstoremove row row-cols-1">\n<% _.each(items, function(item, index) { %>\n  ')

            # <Static value=<ast.Dict object at 0x7f76d520b820> name=None at 7f76d520bf70> -> __attrs_140148358556896
            __attrs_140148358556896 = _static_140148358559776

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-3 pb-3 <% if (items.length > 1){%>border-bottom<% } %>">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d520b610> name=None at 7f76d520b6a0> -> __attrs_140148358559824
            __attrs_140148358559824 = _static_140148358559248

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="UID_<%= index %>" type="hidden" value="<%- item.UID %>" />\n\n    ')

            # <Static value=<ast.Dict object at 0x7f76d520b2b0> name=None at 7f76d520b2e0> -> __attrs_140148358557904
            __attrs_140148358557904 = _static_140148358558384

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x7f76d520ab90> name=None at 7f76d520ac50> -> __attrs_140148358679712
            __attrs_140148358679712 = _static_140148358556560

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358556944 = []
            __append_140148358556944 = __stream_140148358556944.append
            __append_140148358556944('Title')
            __msgid_140148358556944 = __re_whitespace(''.join(__stream_140148358556944)).strip()
            if 'label_title':
                __append(translate('label_title', mapping=None, default=__msgid_140148358556944, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n      ')

            # <Static value=<ast.Dict object at 0x7f76d5229420> name=None at 7f76d5229f60> -> __attrs_140148358683792
            __attrs_140148358683792 = _static_140148358681632

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="newtitle_<%= index %>" value="<%= item.Title %>" />\n    </div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5228df0> name=None at 7f76d5228d60> -> __attrs_140148358679472
            __attrs_140148358679472 = _static_140148358680048

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x7f76d5228e80> name=None at 7f76d5228b50> -> __attrs_140148358678080
            __attrs_140148358678080 = _static_140148358680192

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358680672 = []
            __append_140148358680672 = __stream_140148358680672.append
            __append_140148358680672('Short name')
            __msgid_140148358680672 = __re_whitespace(''.join(__stream_140148358680672)).strip()
            if 'label_short_name':
                __append(translate('label_short_name', mapping=None, default=__msgid_140148358680672, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n      ')

            # <Static value=<ast.Dict object at 0x7f76d522a0b0> name=None at 7f76d522a0e0> -> __attrs_140148358685184
            __attrs_140148358685184 = _static_140148358684848

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="newid_<%= index %>" value="<%= item.id %>" />\n    </div>\n\n    <% if(item.getIcon ){ %>')

            # <Static value=<ast.Dict object at 0x7f76d522acb0> name=None at 7f76d522ace0> -> __attrs_140148358688016
            __attrs_140148358688016 = _static_140148358687920

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img class="thumb-thumb" src="<%= item.getURL %>/@@images/image/thumb"><% } %>\n\n  </div>\n<% }) %>\n</div>')
            __i18n_domain = __previous_i18n_domain_140148358549792
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }