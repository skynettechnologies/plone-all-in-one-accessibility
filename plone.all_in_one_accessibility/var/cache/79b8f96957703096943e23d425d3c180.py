# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.content-4.0.2-py3.10.egg/plone/app/content/browser/contents/templates/properties.pt'

__tokens = {795: ("multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", 22, 29), 857: ("python: options['vocabulary_url']", 23, 46), 1119: ("multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", 30, 29), 1181: ("python: options['vocabulary_url']", 31, 46)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139673030596240 = {'class': 'form-text', }
_static_139673030597968 = {'class': 'form-check-label', 'for': 'fcCheckRecurse', }
_static_139673030596672 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'recurse', 'value': 'yes', 'id': 'fcCheckRecurse', }
_static_139673030591200 = {'class': 'form-check', }
_static_139673030554624 = {'value': '<%= lang.value %>', }
_static_139673030549104 = {'class': 'form-select', 'name': 'language', }
_static_139673030544640 = {'class': 'form-label', }
_static_139673030552848 = {'class': 'mb-2', }
_static_139673030548096 = {'class': 'form-check-label', 'for': 'fcSwitchExcludeFromNavNo', }
_static_139673030544256 = {'class': 'form-check-input', 'type': 'radio', 'name': 'exclude-from-nav', 'id': 'fcSwitchExcludeFromNavNo', 'value': 'no', }
_static_139673030553952 = {'class': 'form-check', }
_static_139673030557408 = {'class': 'form-check-label', 'for': 'fcSwitchExcludeFromNavYes', }
_static_139673030555728 = {'class': 'form-check-input', 'type': 'radio', 'name': 'exclude-from-nav', 'id': 'fcSwitchExcludeFromNavYes', 'value': 'yes', }
_static_139673067453648 = {'class': 'form-check', }
_static_139673030734080 = {'class': 'form-label', 'for': 'fcSwitchExcludeFromNav', }
_static_139673030728800 = {'class': 'mb-2', }
_static_139673030736000 = {'name': 'contributors', 'class': 'pat-select2', 'data-pat-select2': "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_139673030729424 = {'class': 'form-label', }
_static_139673030723856 = {'class': 'mb-2', }
_static_139673118568320 = __C2ZContextWrapper
_static_139673118568608 = __compile_zt_expr
_static_139673030722176 = {'name': 'creators', 'class': 'pat-select2', 'data-pat-select2': "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_139673030734560 = {'class': 'form-label', }
_static_139673030724528 = {'class': 'mb-2', }
_static_139673030730864 = {'class': 'form-control', 'name': 'copyright', }
_static_139673030724144 = {'class': 'form-label', }
_static_139673030863424 = {'class': 'mb-2', }
_static_139673030862416 = {'class': 'form-control', 'name': 'expirationDate', 'type': 'datetime-local', }
_static_139673030860736 = {'class': 'form-label', }
_static_139673030859296 = {'class': 'mb-2', }
_static_139673030858336 = {'class': 'form-control', 'name': 'effectiveDate', 'type': 'datetime-local', }
_static_139673030856608 = {'class': 'form-label', }
_static_139673030855168 = {'class': 'mb-2', }
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

            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673030854112
            __attrs_139673030854112 = _static_139673198743600
            __previous_i18n_domain_139673030854256 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f0829638a00> name=None at 7f0829638a30> -> __attrs_139673030855552
            __attrs_139673030855552 = _static_139673030855168

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f0829638fa0> name=None at 7f0829638fd0> -> __attrs_139673030856992
            __attrs_139673030856992 = _static_139673030856608

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030856128 = []
            __append_139673030856128 = __stream_139673030856128.append
            __append_139673030856128('Publication Date')
            __msgid_139673030856128 = __re_whitespace(''.join(__stream_139673030856128)).strip()
            if 'publiciation_date':
                __append(translate('publiciation_date', mapping=None, default=__msgid_139673030856128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f0829639660> name=None at 7f0829639690> -> __attrs_139673030858624
            __attrs_139673030858624 = _static_139673030858336

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="effectiveDate" type="datetime-local" />\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f0829639a20> name=None at 7f0829639a50> -> __attrs_139673030859680
            __attrs_139673030859680 = _static_139673030859296

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f0829639fc0> name=None at 7f0829639ff0> -> __attrs_139673030861120
            __attrs_139673030861120 = _static_139673030860736

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030860256 = []
            __append_139673030860256 = __stream_139673030860256.append
            __append_139673030860256('Expiration Date')
            __msgid_139673030860256 = __re_whitespace(''.join(__stream_139673030860256)).strip()
            if 'expiration_date':
                __append(translate('expiration_date', mapping=None, default=__msgid_139673030860256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f082963a650> name=None at 7f082963a680> -> __attrs_139673030862752
            __attrs_139673030862752 = _static_139673030862416

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="expirationDate" type="datetime-local" />\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f082963aa40> name=None at 7f082963aa70> -> __attrs_139673030863808
            __attrs_139673030863808 = _static_139673030863424

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f0829618a30> name=None at 7f0829619cf0> -> __attrs_139673030733552
            __attrs_139673030733552 = _static_139673030724144

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030729040 = []
            __append_139673030729040 = __stream_139673030729040.append
            __append_139673030729040('Copyright')
            __msgid_139673030729040 = __re_whitespace(''.join(__stream_139673030729040)).strip()
            if 'copyright':
                __append(translate('copyright', mapping=None, default=__msgid_139673030729040, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f082961a470> name=None at 7f082961a260> -> __attrs_139673030733744
            __attrs_139673030733744 = _static_139673030730864

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea class="form-control" name="copyright"></textarea>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f0829618bb0> name=None at 7f082961a860> -> __attrs_139673030734368
            __attrs_139673030734368 = _static_139673030724528

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f082961b2e0> name=None at 7f082961b640> -> __attrs_139673030727648
            __attrs_139673030727648 = _static_139673030734560

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030725488 = []
            __append_139673030725488 = __stream_139673030725488.append
            __append_139673030725488('Creators')
            __msgid_139673030725488 = __re_whitespace(''.join(__stream_139673030725488)).strip()
            if 'creators':
                __append(translate('creators', mapping=None, default=__msgid_139673030725488, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f0829618280> name=None at 7f082961a800> -> __attrs_139673030732160
            __attrs_139673030732160 = _static_139673030722176

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="creators" class="form-control" class="pat-select2"')

            # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030725104
            __default_139673030725104 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}" (22:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f082961b790> -> __attr_data_pat_select2
            __token = 795
            __token = 857
            try:
                __zt_tmp = __attrs_139673030732160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_139673118568608('python', " options['vocabulary_url']", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
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

            # <Static value=<ast.Dict object at 0x7f0829618910> name=None at 7f082961a9b0> -> __attrs_139673030734128
            __attrs_139673030734128 = _static_139673030723856

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f0829619ed0> name=None at 7f0829619ba0> -> __attrs_139673030722416
            __attrs_139673030722416 = _static_139673030729424

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030732544 = []
            __append_139673030732544 = __stream_139673030732544.append
            __append_139673030732544('Contributors')
            __msgid_139673030732544 = __re_whitespace(''.join(__stream_139673030732544)).strip()
            if 'contributors':
                __append(translate('contributors', mapping=None, default=__msgid_139673030732544, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f082961b880> name=None at 7f082961b8b0> -> __attrs_139673030737728
            __attrs_139673030737728 = _static_139673030736000

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="contributors" class="form-control" class="pat-select2"')

            # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030737824
            __default_139673030737824 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}" (30:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f082961bb80> -> __attr_data_pat_select2
            __token = 1119
            __token = 1181
            try:
                __zt_tmp = __attrs_139673030737728
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_139673118568608('python', " options['vocabulary_url']", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
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

            # <Static value=<ast.Dict object at 0x7f0829619c60> name=None at 7f082961a080> -> __attrs_139673030729712
            __attrs_139673030729712 = _static_139673030728800

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f082961b100> name=None at 7f0829619f00> -> __attrs_139673030721984
            __attrs_139673030721984 = _static_139673030734080

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label" for="fcSwitchExcludeFromNav">')
            __stream_139673030728320 = []
            __append_139673030728320 = __stream_139673030728320.append
            __append_139673030728320('Exclude from navigation')
            __msgid_139673030728320 = __re_whitespace(''.join(__stream_139673030728320)).strip()
            if 'exclude_from_nav':
                __append(translate('exclude_from_nav', mapping=None, default=__msgid_139673030728320, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f082b91fcd0> name=None at 7f082b91c040> -> __attrs_139673030155312
            __attrs_139673030155312 = _static_139673067453648

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n      ')

            # <Static value=<ast.Dict object at 0x7f08295ef850> name=None at 7f08295ecfa0> -> __attrs_139673030554768
            __attrs_139673030554768 = _static_139673030555728

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="radio" name="exclude-from-nav" id="fcSwitchExcludeFromNavYes" value="yes">\n      ')

            # <Static value=<ast.Dict object at 0x7f08295efee0> name=None at 7f08295eff40> -> __attrs_139673030556544
            __attrs_139673030556544 = _static_139673030557408

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcSwitchExcludeFromNavYes">')
            __stream_139673030556016 = []
            __append_139673030556016 = __stream_139673030556016.append
            __append_139673030556016('Yes')
            __msgid_139673030556016 = __re_whitespace(''.join(__stream_139673030556016)).strip()
            if 'yes':
                __append(translate('yes', mapping=None, default=__msgid_139673030556016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    </div>\n    ')

            # <Static value=<ast.Dict object at 0x7f08295ef160> name=None at 7f08295ec3d0> -> __attrs_139673030555584
            __attrs_139673030555584 = _static_139673030553952

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n      ')

            # <Static value=<ast.Dict object at 0x7f08295ecb80> name=None at 7f08295ed120> -> __attrs_139673030547616
            __attrs_139673030547616 = _static_139673030544256

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="radio" name="exclude-from-nav" id="fcSwitchExcludeFromNavNo" value="no">\n      ')

            # <Static value=<ast.Dict object at 0x7f08295eda80> name=None at 7f08295ee5c0> -> __attrs_139673030553568
            __attrs_139673030553568 = _static_139673030548096

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcSwitchExcludeFromNavNo">')
            __stream_139673030551744 = []
            __append_139673030551744 = __stream_139673030551744.append
            __append_139673030551744('No')
            __msgid_139673030551744 = __re_whitespace(''.join(__stream_139673030551744)).strip()
            if 'no':
                __append(translate('no', mapping=None, default=__msgid_139673030551744, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    </div>\n  </div>\n\n  <% if (data.languages) { %>\n  ')

            # <Static value=<ast.Dict object at 0x7f08295eed10> name=None at 7f08295ef4f0> -> __attrs_139673030554480
            __attrs_139673030554480 = _static_139673030552848

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x7f08295ecd00> name=None at 7f08295ed060> -> __attrs_139673030549824
            __attrs_139673030549824 = _static_139673030544640

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_139673030544496 = []
            __append_139673030544496 = __stream_139673030544496.append
            __append_139673030544496('Language')
            __msgid_139673030544496 = __re_whitespace(''.join(__stream_139673030544496)).strip()
            if 'label_language':
                __append(translate('label_language', mapping=None, default=__msgid_139673030544496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f08295ede70> name=None at 7f08295effa0> -> __attrs_139673030553088
            __attrs_139673030553088 = _static_139673030549104

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select class="form-select" name="language">\n      <% _.each(data.languages, function (lang) { %>\n        ')

            # <Static value=<ast.Dict object at 0x7f08295ef400> name=None at 7f08295eed40> -> __attrs_139673030594704
            __attrs_139673030594704 = _static_139673030554624

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= lang.value %>"><%= lang.title %></option>\n      <% }); %>\n    </select>\n  </div>\n  <% } %>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f08295f82e0> name=None at 7f08295fae00> -> __attrs_139673030596432
            __attrs_139673030596432 = _static_139673030591200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n    ')

            # <Static value=<ast.Dict object at 0x7f08295f9840> name=None at 7f08295fb3d0> -> __attrs_139673030592784
            __attrs_139673030592784 = _static_139673030596672

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="recurse" value="yes" id="fcCheckRecurse" />\n    ')

            # <Static value=<ast.Dict object at 0x7f08295f9d50> name=None at 7f08295f8b50> -> __attrs_139673030596864
            __attrs_139673030596864 = _static_139673030597968

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcCheckRecurse">')
            __stream_139673030597872 = []
            __append_139673030597872 = __stream_139673030597872.append
            __append_139673030597872('Include contained items')
            __msgid_139673030597872 = __re_whitespace(''.join(__stream_139673030597872)).strip()
            if 'label_include_contained_objects':
                __append(translate('label_include_contained_objects', mapping=None, default=__msgid_139673030597872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f08295f9690> name=None at 7f08295f8b20> -> __attrs_139673030591968
            __attrs_139673030591968 = _static_139673030596240

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_139673030604448 = []
            __append_139673030604448 = __stream_139673030604448.append
            __append_139673030604448('\n    If checked, this will attempt to modify the status of all content in any selected folders and their subfolders.\n    ')
            __msgid_139673030604448 = __re_whitespace(''.join(__stream_139673030604448)).strip()
            if 'help_include_contained_objects':
                __append(translate('help_include_contained_objects', mapping=None, default=__msgid_139673030604448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_139673030854256
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }