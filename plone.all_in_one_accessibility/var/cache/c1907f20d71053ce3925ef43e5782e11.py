# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.content-4.0.2-py3.10.egg/plone/app/content/browser/contents/templates/workflow.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_140148358595056 = {'class': 'form-text', }
_static_140148358604752 = {'class': 'form-check-label', 'for': 'fcWorkflowRecurse', }
_static_140148358758064 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'recurse', 'value': 'yes', 'id': 'fcWorkflowRecurse', }
_static_140148358755616 = {'class': 'form-check', }
_static_140148358757392 = {'class': 'form-text', }
_static_140148358754272 = {'value': '<%= transition.id %>', }
_static_140148358753024 = {'class': 'form-select', 'name': 'transition', }
_static_140148358751200 = {'class': 'form-label', }
_static_140148358742080 = {'class': 'mb-2', }
_static_140148358743136 = {'class': 'form-control', 'rows': '2', 'name': 'comments', }
_static_140148358744912 = {'class': 'form-label', }
_static_140148358746400 = {'class': 'mb-2', }
_static_140148447476128 = {}

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

            # <Static value=<ast.Dict object at 0x7f76da6d79a0> name=None at 7f76da6d7cd0> -> __attrs_140148358747504
            __attrs_140148358747504 = _static_140148447476128
            __previous_i18n_domain_140148358747360 = __i18n_domain
            __i18n_domain = 'plone'

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset>\n  ')

            # <Static value=<ast.Dict object at 0x7f76d5239120> name=None at 7f76d52390f0> -> __attrs_140148358746016
            __attrs_140148358746016 = _static_140148358746400

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5238b50> name=None at 7f76d5238b20> -> __attrs_140148358744528
            __attrs_140148358744528 = _static_140148358744912

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358745392 = []
            __append_140148358745392 = __stream_140148358745392.append
            __append_140148358745392('Comments')
            __msgid_140148358745392 = __re_whitespace(''.join(__stream_140148358745392)).strip()
            if 'label_comments':
                __append(translate('label_comments', mapping=None, default=__msgid_140148358745392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5238460> name=None at 7f76d5238430> -> __attrs_140148358742752
            __attrs_140148358742752 = _static_140148358743136

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea class="form-control" rows="2" name="comments"></textarea>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f76d5238040> name=None at 7f76d5239e70> -> __attrs_140148358750144
            __attrs_140148358750144 = _static_140148358742080

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d523a3e0> name=None at 7f76d523a410> -> __attrs_140148358751584
            __attrs_140148358751584 = _static_140148358751200

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358750720 = []
            __append_140148358750720 = __stream_140148358750720.append
            __append_140148358750720('Change State')
            __msgid_140148358750720 = __re_whitespace(''.join(__stream_140148358750720)).strip()
            if 'label_change_status':
                __append(translate('label_change_status', mapping=None, default=__msgid_140148358750720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d523ab00> name=None at 7f76d523a740> -> __attrs_140148358753072
            __attrs_140148358753072 = _static_140148358753024

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select class="form-select" name="transition">\n      <% if(data.transitions){\n        _.each(data.transitions, function(transition){\n          %>')

            # <Static value=<ast.Dict object at 0x7f76d523afe0> name=None at 7f76d523ae60> -> __attrs_140148358754656
            __attrs_140148358754656 = _static_140148358754272

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= transition.id %>"><%= transition.title %></option>\n          <%\n        });\n      } %>\n    </select>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d523bc10> name=None at 7f76d523bbe0> -> __attrs_140148358757584
            __attrs_140148358757584 = _static_140148358757392

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_140148358758016 = []
            __append_140148358758016 = __stream_140148358758016.append
            __append_140148358758016('Select the transition to be used for modifying the items state.')
            __msgid_140148358758016 = __re_whitespace(''.join(__stream_140148358758016)).strip()
            if 'help_change_status_action':
                __append(translate('help_change_status_action', mapping=None, default=__msgid_140148358758016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n  ')

            # <Static value=<ast.Dict object at 0x7f76d523b520> name=None at 7f76d523b550> -> __attrs_140148358756000
            __attrs_140148358756000 = _static_140148358755616

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d523beb0> name=None at 7f76d523ba30> -> __attrs_140148358604704
            __attrs_140148358604704 = _static_140148358758064

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="recurse" value="yes" id="fcWorkflowRecurse" />\n    ')

            # <Static value=<ast.Dict object at 0x7f76d52167d0> name=None at 7f76d5215a20> -> __attrs_140148358610608
            __attrs_140148358610608 = _static_140148358604752

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcWorkflowRecurse">')
            __stream_140148358600288 = []
            __append_140148358600288 = __stream_140148358600288.append
            __append_140148358600288('Include contained items')
            __msgid_140148358600288 = __re_whitespace(''.join(__stream_140148358600288)).strip()
            if 'label_include_contained_objects':
                __append(translate('label_include_contained_objects', mapping=None, default=__msgid_140148358600288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d52141f0> name=None at 7f76d52171c0> -> __attrs_140148358597312
            __attrs_140148358597312 = _static_140148358595056

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_140148358597024 = []
            __append_140148358597024 = __stream_140148358597024.append
            __append_140148358597024('\n    If checked, this will attempt to modify the status of all content in any selected folders and their subfolders.\n    ')
            __msgid_140148358597024 = __re_whitespace(''.join(__stream_140148358597024)).strip()
            if 'help_include_contained_objects':
                __append(translate('help_include_contained_objects', mapping=None, default=__msgid_140148358597024, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n</fieldset>')
            __i18n_domain = __previous_i18n_domain_140148358747360
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }