# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.content-4.0.2-py3.10.egg/plone/app/content/browser/contents/templates/properties.pt'

__tokens = {795: ("multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", 22, 29), 857: ("python: options['vocabulary_url']", 23, 46), 1119: ("multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", 30, 29), 1181: ("python: options['vocabulary_url']", 31, 46)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140148358558192 = {'class': 'form-text', }
_static_140148358557664 = {'class': 'form-check-label', 'for': 'fcCheckRecurse', }
_static_140148358607920 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'recurse', 'value': 'yes', 'id': 'fcCheckRecurse', }
_static_140148358597840 = {'class': 'form-check', }
_static_140148358597072 = {'value': '<%= lang.value %>', }
_static_140148358600480 = {'class': 'form-select', 'name': 'language', }
_static_140148358609504 = {'class': 'form-label', }
_static_140148358610512 = {'class': 'mb-2', }
_static_140148358600240 = {'class': 'form-check-label', 'for': 'fcSwitchExcludeFromNavNo', }
_static_140148358608640 = {'class': 'form-check-input', 'type': 'radio', 'name': 'exclude-from-nav', 'id': 'fcSwitchExcludeFromNavNo', 'value': 'no', }
_static_140148358597696 = {'class': 'form-check', }
_static_140148358601296 = {'class': 'form-check-label', 'for': 'fcSwitchExcludeFromNavYes', }
_static_140148358810208 = {'class': 'form-check-input', 'type': 'radio', 'name': 'exclude-from-nav', 'id': 'fcSwitchExcludeFromNavYes', 'value': 'yes', }
_static_140148358815056 = {'class': 'form-check', }
_static_140148358814192 = {'class': 'form-label', 'for': 'fcSwitchExcludeFromNav', }
_static_140148358811312 = {'class': 'mb-2', }
_static_140148358814528 = {'name': 'contributors', 'class': 'pat-select2', 'data-pat-select2': "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_140148358809488 = {'class': 'form-label', }
_static_140148358816976 = {'class': 'mb-2', }
_static_140148447782144 = __C2ZContextWrapper
_static_140148447782432 = __compile_zt_expr
_static_140148358821584 = {'name': 'creators', 'class': 'pat-select2', 'data-pat-select2': "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_140148358690944 = {'class': 'form-label', }
_static_140148358679136 = {'class': 'mb-2', }
_static_140148358679856 = {'class': 'form-control', 'name': 'copyright', }
_static_140148358681776 = {'class': 'form-label', }
_static_140148358677648 = {'class': 'mb-2', }
_static_140148358678752 = {'class': 'form-control', 'name': 'expirationDate', 'type': 'datetime-local', }
_static_140148358692336 = {'class': 'form-label', }
_static_140148358685184 = {'class': 'mb-2', }
_static_140148358690848 = {'class': 'form-control', 'name': 'effectiveDate', 'type': 'datetime-local', }
_static_140148358677888 = {'class': 'form-label', }
_static_140148358683600 = {'class': 'mb-2', }
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

            # <Static value=<ast.Dict object at 0x7f76da6d79a0> name=None at 7f76da6d7cd0> -> __attrs_140148358691712
            __attrs_140148358691712 = _static_140148447476128
            __previous_i18n_domain_140148358678656 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f76d5229bd0> name=None at 7f76d522a770> -> __attrs_140148358690128
            __attrs_140148358690128 = _static_140148358683600

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5228580> name=None at 7f76d5229180> -> __attrs_140148358692288
            __attrs_140148358692288 = _static_140148358677888

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358682400 = []
            __append_140148358682400 = __stream_140148358682400.append
            __append_140148358682400('Publication Date')
            __msgid_140148358682400 = __re_whitespace(''.join(__stream_140148358682400)).strip()
            if 'publiciation_date':
                __append(translate('publiciation_date', mapping=None, default=__msgid_140148358682400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d522b820> name=None at 7f76d522a5f0> -> __attrs_140148358688832
            __attrs_140148358688832 = _static_140148358690848

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="effectiveDate" type="datetime-local" />\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f76d522a200> name=None at 7f76d52281f0> -> __attrs_140148358685280
            __attrs_140148358685280 = _static_140148358685184

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d522bdf0> name=None at 7f76d5229c60> -> __attrs_140148358681488
            __attrs_140148358681488 = _static_140148358692336

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358686288 = []
            __append_140148358686288 = __stream_140148358686288.append
            __append_140148358686288('Expiration Date')
            __msgid_140148358686288 = __re_whitespace(''.join(__stream_140148358686288)).strip()
            if 'expiration_date':
                __append(translate('expiration_date', mapping=None, default=__msgid_140148358686288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d52288e0> name=None at 7f76d522a920> -> __attrs_140148358687104
            __attrs_140148358687104 = _static_140148358678752

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="expirationDate" type="datetime-local" />\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f76d5228490> name=None at 7f76d522a170> -> __attrs_140148358676736
            __attrs_140148358676736 = _static_140148358677648

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d52294b0> name=None at 7f76d52292d0> -> __attrs_140148358681200
            __attrs_140148358681200 = _static_140148358681776

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358684416 = []
            __append_140148358684416 = __stream_140148358684416.append
            __append_140148358684416('Copyright')
            __msgid_140148358684416 = __re_whitespace(''.join(__stream_140148358684416)).strip()
            if 'copyright':
                __append(translate('copyright', mapping=None, default=__msgid_140148358684416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5228d30> name=None at 7f76d5228fa0> -> __attrs_140148358687056
            __attrs_140148358687056 = _static_140148358679856

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea class="form-control" name="copyright"></textarea>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f76d5228a60> name=None at 7f76d5229fc0> -> __attrs_140148358689648
            __attrs_140148358689648 = _static_140148358679136

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d522b880> name=None at 7f76d522a020> -> __attrs_140148358808960
            __attrs_140148358808960 = _static_140148358690944

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358689840 = []
            __append_140148358689840 = __stream_140148358689840.append
            __append_140148358689840('Creators')
            __msgid_140148358689840 = __re_whitespace(''.join(__stream_140148358689840)).strip()
            if 'creators':
                __append(translate('creators', mapping=None, default=__msgid_140148358689840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d524b6d0> name=None at 7f76d524a980> -> __attrs_140148358820912
            __attrs_140148358820912 = _static_140148358821584

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="creators" class="form-control" class="pat-select2"')

            # <Symbol value=<DEFAULT> at 7f76da6a9fc0> -> __default_140148358817600
            __default_140148358817600 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}" (22:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f76d524ae00> -> __attr_data_pat_select2
            __token = 795
            __token = 857
            try:
                __zt_tmp = __attrs_140148358820912
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_140148447782432('python', " options['vocabulary_url']", econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))
            __attr_data_pat_select2 = __quote(__attr_data_pat_select2, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_pat_select2 = ('%s%s' % ('multiple: true;\n                             vocabularyUrl: ', (__attr_data_pat_select2 if (__attr_data_pat_select2 is not None) else ''), ))
            if (__attr_data_pat_select2 is None):
                pass
            else:
                if (__attr_data_pat_select2 is _DEFAULT_MARKER):
                    __attr_data_pat_select2 = None
                else:
                    __tt = type(__attr_data_pat_select2)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_data_pat_select2 = str(__attr_data_pat_select2)
                    else:
                        if (__tt is bytes):
                            __attr_data_pat_select2 = decode(__attr_data_pat_select2)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_data_pat_select2 = __attr_data_pat_select2.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_pat_select2)
                                    __attr_data_pat_select2 = (str(__attr_data_pat_select2) if (__attr_data_pat_select2 is __converted) else __converted)
                                else:
                                    __attr_data_pat_select2 = __attr_data_pat_select2()
            if (__attr_data_pat_select2 is not None):
                __append((' data-pat-select2="%s"' % __attr_data_pat_select2))
            __append('/>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f76d524a4d0> name=None at 7f76d5249780> -> __attrs_140148358815680
            __attrs_140148358815680 = _static_140148358816976

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5248790> name=None at 7f76d524b250> -> __attrs_140148358816016
            __attrs_140148358816016 = _static_140148358809488

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358808288 = []
            __append_140148358808288 = __stream_140148358808288.append
            __append_140148358808288('Contributors')
            __msgid_140148358808288 = __re_whitespace(''.join(__stream_140148358808288)).strip()
            if 'contributors':
                __append(translate('contributors', mapping=None, default=__msgid_140148358808288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5249b40> name=None at 7f76d524b5e0> -> __attrs_140148358823552
            __attrs_140148358823552 = _static_140148358814528

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="contributors" class="form-control" class="pat-select2"')

            # <Symbol value=<DEFAULT> at 7f76da6a9fc0> -> __default_140148358810496
            __default_140148358810496 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}" (30:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f76d5249ff0> -> __attr_data_pat_select2
            __token = 1119
            __token = 1181
            try:
                __zt_tmp = __attrs_140148358823552
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_140148447782432('python', " options['vocabulary_url']", econtext=econtext)(_static_140148447782144(econtext, __zt_tmp))
            __attr_data_pat_select2 = __quote(__attr_data_pat_select2, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_pat_select2 = ('%s%s' % ('multiple: true;\n                             vocabularyUrl: ', (__attr_data_pat_select2 if (__attr_data_pat_select2 is not None) else ''), ))
            if (__attr_data_pat_select2 is None):
                pass
            else:
                if (__attr_data_pat_select2 is _DEFAULT_MARKER):
                    __attr_data_pat_select2 = None
                else:
                    __tt = type(__attr_data_pat_select2)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_data_pat_select2 = str(__attr_data_pat_select2)
                    else:
                        if (__tt is bytes):
                            __attr_data_pat_select2 = decode(__attr_data_pat_select2)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_data_pat_select2 = __attr_data_pat_select2.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_pat_select2)
                                    __attr_data_pat_select2 = (str(__attr_data_pat_select2) if (__attr_data_pat_select2 is __converted) else __converted)
                                else:
                                    __attr_data_pat_select2 = __attr_data_pat_select2()
            if (__attr_data_pat_select2 is not None):
                __append((' data-pat-select2="%s"' % __attr_data_pat_select2))
            __append('/>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f76d5248eb0> name=None at 7f76d524a5f0> -> __attrs_140148358821008
            __attrs_140148358821008 = _static_140148358811312

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d52499f0> name=None at 7f76d52483a0> -> __attrs_140148358811984
            __attrs_140148358811984 = _static_140148358814192

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label" for="fcSwitchExcludeFromNav">')
            __stream_140148358822016 = []
            __append_140148358822016 = __stream_140148358822016.append
            __append_140148358822016('Exclude from navigation')
            __msgid_140148358822016 = __re_whitespace(''.join(__stream_140148358822016)).strip()
            if 'exclude_from_nav':
                __append(translate('exclude_from_nav', mapping=None, default=__msgid_140148358822016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5249d50> name=None at 7f76d524a1d0> -> __attrs_140148358811024
            __attrs_140148358811024 = _static_140148358815056

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n      ')

            # <Static value=<ast.Dict object at 0x7f76d5248a60> name=None at 7f76d52480d0> -> __attrs_140148358606288
            __attrs_140148358606288 = _static_140148358810208

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="radio" name="exclude-from-nav" id="fcSwitchExcludeFromNavYes" value="yes">\n      ')

            # <Static value=<ast.Dict object at 0x7f76d5215a50> name=None at 7f76d5215090> -> __attrs_140148358609072
            __attrs_140148358609072 = _static_140148358601296

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcSwitchExcludeFromNavYes">')
            __stream_140148358608016 = []
            __append_140148358608016 = __stream_140148358608016.append
            __append_140148358608016('Yes')
            __msgid_140148358608016 = __re_whitespace(''.join(__stream_140148358608016)).strip()
            if 'yes':
                __append(translate('yes', mapping=None, default=__msgid_140148358608016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    </div>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5214c40> name=None at 7f76d52147c0> -> __attrs_140148358600864
            __attrs_140148358600864 = _static_140148358597696

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n      ')

            # <Static value=<ast.Dict object at 0x7f76d5217700> name=None at 7f76d5216800> -> __attrs_140148358601728
            __attrs_140148358601728 = _static_140148358608640

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="radio" name="exclude-from-nav" id="fcSwitchExcludeFromNavNo" value="no">\n      ')

            # <Static value=<ast.Dict object at 0x7f76d5215630> name=None at 7f76d5214d00> -> __attrs_140148358610224
            __attrs_140148358610224 = _static_140148358600240

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcSwitchExcludeFromNavNo">')
            __stream_140148358598320 = []
            __append_140148358598320 = __stream_140148358598320.append
            __append_140148358598320('No')
            __msgid_140148358598320 = __re_whitespace(''.join(__stream_140148358598320)).strip()
            if 'no':
                __append(translate('no', mapping=None, default=__msgid_140148358598320, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    </div>\n  </div>\n\n  <% if (data.languages) { %>\n  ')

            # <Static value=<ast.Dict object at 0x7f76d5217e50> name=None at 7f76d5215fc0> -> __attrs_140148358594672
            __attrs_140148358594672 = _static_140148358610512

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5217a60> name=None at 7f76d5215180> -> __attrs_140148358596016
            __attrs_140148358596016 = _static_140148358609504

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_140148358596880 = []
            __append_140148358596880 = __stream_140148358596880.append
            __append_140148358596880('Language')
            __msgid_140148358596880 = __re_whitespace(''.join(__stream_140148358596880)).strip()
            if 'label_language':
                __append(translate('label_language', mapping=None, default=__msgid_140148358596880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5215720> name=None at 7f76d5217e20> -> __attrs_140148358596928
            __attrs_140148358596928 = _static_140148358600480

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select class="form-select" name="language">\n      <% _.each(data.languages, function (lang) { %>\n        ')

            # <Static value=<ast.Dict object at 0x7f76d52149d0> name=None at 7f76d5214100> -> __attrs_140148358595824
            __attrs_140148358595824 = _static_140148358597072

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= lang.value %>"><%= lang.title %></option>\n      <% }); %>\n    </select>\n  </div>\n  <% } %>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f76d5214cd0> name=None at 7f76d5215450> -> __attrs_140148358603456
            __attrs_140148358603456 = _static_140148358597840

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n    ')

            # <Static value=<ast.Dict object at 0x7f76d5217430> name=None at 7f76d5216d40> -> __attrs_140148358560928
            __attrs_140148358560928 = _static_140148358607920

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="recurse" value="yes" id="fcCheckRecurse" />\n    ')

            # <Static value=<ast.Dict object at 0x7f76d520afe0> name=None at 7f76d520b040> -> __attrs_140148358561744
            __attrs_140148358561744 = _static_140148358557664

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcCheckRecurse">')
            __stream_140148358557088 = []
            __append_140148358557088 = __stream_140148358557088.append
            __append_140148358557088('Include contained items')
            __msgid_140148358557088 = __re_whitespace(''.join(__stream_140148358557088)).strip()
            if 'label_include_contained_objects':
                __append(translate('label_include_contained_objects', mapping=None, default=__msgid_140148358557088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f76d520b1f0> name=None at 7f76d520a800> -> __attrs_140148358549504
            __attrs_140148358549504 = _static_140148358558192

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_140148358546096 = []
            __append_140148358546096 = __stream_140148358546096.append
            __append_140148358546096('\n    If checked, this will attempt to modify the status of all content in any selected folders and their subfolders.\n    ')
            __msgid_140148358546096 = __re_whitespace(''.join(__stream_140148358546096)).strip()
            if 'help_include_contained_objects':
                __append(translate('help_include_contained_objects', mapping=None, default=__msgid_140148358546096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140148358678656
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }