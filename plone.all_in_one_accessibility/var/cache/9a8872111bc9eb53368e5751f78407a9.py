# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.content-4.0.2-py3.10.egg/plone/app/content/browser/contents/templates/rename.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_139673030596192 = {'class': 'thumb-thumb', 'src': '<%= item.getURL %>/@@images/image/thumb', }
_static_139673030541904 = {'class': 'form-control', 'name': 'newid_<%= index %>', 'value': '<%= item.id %>', }
_static_139673030542816 = {'class': 'form-label', }
_static_139673030549776 = {'class': 'mb-2', }
_static_139673030549440 = {'class': 'form-control', 'name': 'newtitle_<%= index %>', 'value': '<%= item.Title %>', }
_static_139673030551168 = {'class': 'form-label', }
_static_139673030545504 = {'class': 'mb-2', }
_static_139673030557408 = {'name': 'UID_<%= index %>', 'type': 'hidden', 'value': '<%- item.UID %>', }
_static_139673030554960 = {'class': 'mb-3 pb-3 <% if (items.length > 1){%>border-bottom<% } %>', }
_static_139673030552656 = {'class': 'itemstoremove row row-cols-1', }

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

            # <Static value=<ast.Dict object at 0x7f08295eec50> name=None at 7f08295eee00> -> __attrs_139673030549152
            __attrs_139673030549152 = _static_139673030552656
            __previous_i18n_domain_139673030548912 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="itemstoremove row row-cols-1">\n<% _.each(items, function(item, index) { %>\n  ')

            # <Static value=<ast.Dict object at 0x7f08295ef550> name=None at 7f08295ef580> -> __attrs_139673030555392
            __attrs_139673030555392 = _static_139673030554960

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-3 pb-3 <% if (items.length > 1){%>border-bottom<% } %>">\n    ')

            # <Static value=<ast.Dict object at 0x7f08295efee0> name=None at 7f08295efaf0> -> __attrs_139673030556784
            __attrs_139673030556784 = _static_139673030557408

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="UID_<%= index %>" type="hidden" value="<%- item.UID %>" />\n\n    ')

            # <Static value=<ast.Dict object at 0x7f08295ed060> name=None at 7f08295ec550> -> __attrs_139673030547952
            __attrs_139673030547952 = _static_139673030545504

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x7f08295ee680> name=None at 7f08295ee6e0> -> __attrs_139673030550976
            __attrs_139673030550976 = _static_139673030551168

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030545456 = []
            __append_139673030545456 = __stream_139673030545456.append
            __append_139673030545456('Title')
            __msgid_139673030545456 = __re_whitespace(''.join(__stream_139673030545456)).strip()
            if 'label_title':
                __append(translate('label_title', mapping=None, default=__msgid_139673030545456, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n      ')

            # <Static value=<ast.Dict object at 0x7f08295edfc0> name=None at 7f08295edf30> -> __attrs_139673030548288
            __attrs_139673030548288 = _static_139673030549440

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="newtitle_<%= index %>" value="<%= item.Title %>" />\n    </div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f08295ee110> name=None at 7f08295ee290> -> __attrs_139673030551648
            __attrs_139673030551648 = _static_139673030549776

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x7f08295ec5e0> name=None at 7f08295ec580> -> __attrs_139673030543584
            __attrs_139673030543584 = _static_139673030542816

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030544592 = []
            __append_139673030544592 = __stream_139673030544592.append
            __append_139673030544592('Short name')
            __msgid_139673030544592 = __re_whitespace(''.join(__stream_139673030544592)).strip()
            if 'label_short_name':
                __append(translate('label_short_name', mapping=None, default=__msgid_139673030544592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n      ')

            # <Static value=<ast.Dict object at 0x7f08295ec250> name=None at 7f08295ecd60> -> __attrs_139673030601472
            __attrs_139673030601472 = _static_139673030541904

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="newid_<%= index %>" value="<%= item.id %>" />\n    </div>\n\n    <% if(item.getIcon ){ %>')

            # <Static value=<ast.Dict object at 0x7f08295f9660> name=None at 7f08295f9690> -> __attrs_139673030596000
            __attrs_139673030596000 = _static_139673030596192

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img class="thumb-thumb" src="<%= item.getURL %>/@@images/image/thumb"><% } %>\n\n  </div>\n<% }) %>\n</div>')
            __i18n_domain = __previous_i18n_domain_139673030548912
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }