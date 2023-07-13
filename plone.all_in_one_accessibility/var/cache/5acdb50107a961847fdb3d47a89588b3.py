# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.content-4.0.2-py3.10.egg/plone/app/content/browser/contents/templates/workflow.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_139673030547712 = {'class': 'form-text', }
_static_139673030542672 = {'class': 'form-check-label', 'for': 'fcWorkflowRecurse', }
_static_139673030546464 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'recurse', 'value': 'yes', 'id': 'fcWorkflowRecurse', }
_static_139673030829168 = {'class': 'form-check', }
_static_139673030828016 = {'class': 'form-text', }
_static_139673030829888 = {'value': '<%= transition.id %>', }
_static_139673030824368 = {'class': 'form-select', 'name': 'transition', }
_static_139673030827104 = {'class': 'form-label', }
_static_139673030825520 = {'class': 'mb-2', }
_static_139673030823120 = {'class': 'form-control', 'rows': '2', 'name': 'comments', }
_static_139673030821344 = {'class': 'form-label', }
_static_139673030831904 = {'class': 'mb-2', }
_static_139673198743600 = {}

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

            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673030835840
            __attrs_139673030835840 = _static_139673198743600
            __previous_i18n_domain_139673030835984 = __i18n_domain
            __i18n_domain = 'plone'

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset>\n  ')

            # <Static value=<ast.Dict object at 0x7f0829632f20> name=None at 7f0829632ef0> -> __attrs_139673030831520
            __attrs_139673030831520 = _static_139673030831904

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f08296305e0> name=None at 7f0829630610> -> __attrs_139673030821728
            __attrs_139673030821728 = _static_139673030821344

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030820864 = []
            __append_139673030820864 = __stream_139673030820864.append
            __append_139673030820864('Comments')
            __msgid_139673030820864 = __re_whitespace(''.join(__stream_139673030820864)).strip()
            if 'label_comments':
                __append(translate('label_comments', mapping=None, default=__msgid_139673030820864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f0829630cd0> name=None at 7f0829630d00> -> __attrs_139673030823504
            __attrs_139673030823504 = _static_139673030823120

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea class="form-control" rows="2" name="comments"></textarea>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f0829631630> name=None at 7f0829631660> -> __attrs_139673030825904
            __attrs_139673030825904 = _static_139673030825520

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f0829631c60> name=None at 7f0829631f90> -> __attrs_139673030827584
            __attrs_139673030827584 = _static_139673030827104

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030826480 = []
            __append_139673030826480 = __stream_139673030826480.append
            __append_139673030826480('Change State')
            __msgid_139673030826480 = __re_whitespace(''.join(__stream_139673030826480)).strip()
            if 'label_change_status':
                __append(translate('label_change_status', mapping=None, default=__msgid_139673030826480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f08296311b0> name=None at 7f08296313f0> -> __attrs_139673030824464
            __attrs_139673030824464 = _static_139673030824368

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select class="form-select" name="transition">\n      <% if(data.transitions){\n        _.each(data.transitions, function(transition){\n          %>')

            # <Static value=<ast.Dict object at 0x7f0829632740> name=None at 7f0829631030> -> __attrs_139673030829648
            __attrs_139673030829648 = _static_139673030829888

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= transition.id %>"><%= transition.title %></option>\n          <%\n        });\n      } %>\n    </select>\n    ')

            # <Static value=<ast.Dict object at 0x7f0829631ff0> name=None at 7f0829631fc0> -> __attrs_139673030828208
            __attrs_139673030828208 = _static_139673030828016

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_139673030829024 = []
            __append_139673030829024 = __stream_139673030829024.append
            __append_139673030829024('Select the transition to be used for modifying the items state.')
            __msgid_139673030829024 = __re_whitespace(''.join(__stream_139673030829024)).strip()
            if 'help_change_status_action':
                __append(translate('help_change_status_action', mapping=None, default=__msgid_139673030829024, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n  ')

            # <Static value=<ast.Dict object at 0x7f0829632470> name=None at 7f0829632440> -> __attrs_139673030820288
            __attrs_139673030820288 = _static_139673030829168

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n    ')

            # <Static value=<ast.Dict object at 0x7f08295ed420> name=None at 7f08295ee980> -> __attrs_139673030543776
            __attrs_139673030543776 = _static_139673030546464

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="recurse" value="yes" id="fcWorkflowRecurse" />\n    ')

            # <Static value=<ast.Dict object at 0x7f08295ec550> name=None at 7f08295eef50> -> __attrs_139673030544496
            __attrs_139673030544496 = _static_139673030542672

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcWorkflowRecurse">')
            __stream_139673030549824 = []
            __append_139673030549824 = __stream_139673030549824.append
            __append_139673030549824('Include contained items')
            __msgid_139673030549824 = __re_whitespace(''.join(__stream_139673030549824)).strip()
            if 'label_include_contained_objects':
                __append(translate('label_include_contained_objects', mapping=None, default=__msgid_139673030549824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f08295ed900> name=None at 7f08295ed9c0> -> __attrs_139673030555440
            __attrs_139673030555440 = _static_139673030547712

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_139673030542576 = []
            __append_139673030542576 = __stream_139673030542576.append
            __append_139673030542576('\n    If checked, this will attempt to modify the status of all content in any selected folders and their subfolders.\n    ')
            __msgid_139673030542576 = __re_whitespace(''.join(__stream_139673030542576)).strip()
            if 'help_include_contained_objects':
                __append(translate('help_include_contained_objects', mapping=None, default=__msgid_139673030542576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n</fieldset>')
            __i18n_domain = __previous_i18n_domain_139673030835984
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }