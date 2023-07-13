# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/footer.pt'

__tokens = {860: ('nocall:modules/DateTime.DateTime', 20, 30), 921: (' python:DateTime(', 21, 27), 963: ('python:myTime.year()', 22, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140310272336720 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }
_static_140310272556384 = {'href': 'http://creativecommons.org/licenses/GPL/2.0/', }
_static_140310475831904 = {'href': 'http://plone.org/foundation', }
_static_140310567013488 = __C2ZContextWrapper
_static_140310567013776 = __compile_zt_expr
_static_140310475828880 = {'title': 'Copyright', }
_static_140310475828784 = {'href': 'http://plone.org', }
_static_140310566789392 = {}
_static_140310475826480 = {'class': 'card-body', }
_static_140310272331776 = {'class': 'card card-classic', 'id': 'portal-footer-signature', }

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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f9c87f0d000> name=None at 7f9c87f0ca90> -> __attrs_140310475818896
            __attrs_140310475818896 = _static_140310272331776

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card card-classic" id="portal-footer-signature">\n\n    ')

            # <Static value=<ast.Dict object at 0x7f9c9411e530> name=None at 7f9c9411ff70> -> __attrs_140310475832960
            __attrs_140310475832960 = _static_140310475826480

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475829744
            __attrs_140310475829744 = _static_140310566789392
            __stream_140310476918784_copyright = ''
            __stream_140310476918784_plonecms = ''
            __stream_140310476918784_current_year = ''
            __stream_140310476918784_plonefoundation = ''
            __stream_140310475817264 = []
            __append_140310475817264 = __stream_140310475817264.append
            __append_140310475817264('\n      The\n      ')
            __stream_140310476918784_plonecms = []
            __append_140310476918784_plonecms = __stream_140310476918784_plonecms.append

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475829840
            __attrs_140310475829840 = _static_140310566789392
            __append_140310476918784_plonecms('\n           ')

            # <Static value=<ast.Dict object at 0x7f9c9411ee30> name=None at 7f9c9411fa90> -> __attrs_140310475823840
            __attrs_140310475823840 = _static_140310475828784

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140310476918784_plonecms('<a href="http://plone.org">')
            __stream_140310475832576 = []
            __append_140310475832576 = __stream_140310475832576.append
            __append_140310475832576('Plone')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475825184
            __attrs_140310475825184 = _static_140310566789392

            # <sup ... (0:0)
            # --------------------------------------------------------
            __append_140310475832576('<sup>&reg;</sup> Open Source CMS/WCM')
            __msgid_140310475832576 = __re_whitespace(''.join(__stream_140310475832576)).strip()
            if 'label_plone_cms':
                __append_140310476918784_plonecms(translate('label_plone_cms', mapping=None, default=__msgid_140310475832576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_140310476918784_plonecms('</a>\n      ')
            __append_140310475817264('${plonecms}')
            __stream_140310476918784_plonecms = ''.join(__stream_140310476918784_plonecms)
            __append_140310475817264('\n      is\n      ')
            __stream_140310476918784_copyright = []
            __append_140310476918784_copyright = __stream_140310476918784_copyright.append

            # <Static value=<ast.Dict object at 0x7f9c9411ee90> name=None at 7f9c9411ddb0> -> __attrs_140310475832192
            __attrs_140310475832192 = _static_140310475828880

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_140310476918784_copyright('<abbr')

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475829648
            __default_140310475829648 = _DEFAULT_MARKER

            # <Translate msgid='title_copyright' node=<ast.Constant object at 0x7f9c9411da50> at 7f9c9411ed70> -> __attr_title
            __attr_title = 'Copyright'
            __attr_title = translate('title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_140310476918784_copyright((' title="%s"' % __attr_title))
            __append_140310476918784_copyright('>&copy;</abbr>')
            __append_140310475817264('${copyright}')
            __stream_140310476918784_copyright = ''.join(__stream_140310476918784_copyright)
            __append_140310475817264('\n      2000-')
            __stream_140310476918784_current_year = []
            __append_140310476918784_current_year = __stream_140310476918784_current_year.append

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475818032
            __attrs_140310475818032 = _static_140310566789392
            __backup_DateTime_140310272328704 = get('DateTime', __marker)

            # <Value 'nocall:modules/DateTime.DateTime' (20:30)> -> __value
            __token = 860
            try:
                __zt_tmp = __attrs_140310475818032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('nocall', 'modules/DateTime.DateTime', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['DateTime'] = __value
            __backup_myTime_140310272288816 = get('myTime', __marker)

            # <Value 'python:DateTime()' (21:27)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_140310475818032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140310567013776('python', 'DateTime()', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))
            econtext['myTime'] = __value

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __default_140310475822496
            __default_140310475822496 = _DEFAULT_MARKER

            # <Value 'python:myTime.year()' (22:22)> -> __cache_140310475827536
            __token = 963
            try:
                __zt_tmp = __attrs_140310475818032
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140310475827536 = _static_140310567013776('python', 'myTime.year()', econtext=econtext)(_static_140310567013488(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:myTime.year()' (22:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f9c9979c730> at 7f9c9411ce80> -> __condition
            __expression = __cache_140310475827536

            # <Symbol value=<DEFAULT> at 7f9c9979c730> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140310475827536
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_140310476918784_current_year(__content)
            if (__backup_myTime_140310272288816 is __marker):
                del econtext['myTime']
            else:
                econtext['myTime'] = __backup_myTime_140310272288816
            if (__backup_DateTime_140310272328704 is __marker):
                del econtext['DateTime']
            else:
                econtext['DateTime'] = __backup_DateTime_140310272328704
            __append_140310475817264('${current_year}')
            __stream_140310476918784_current_year = ''.join(__stream_140310476918784_current_year)
            __append_140310475817264('\n      by the\n      ')
            __stream_140310476918784_plonefoundation = []
            __append_140310476918784_plonefoundation = __stream_140310476918784_plonefoundation.append

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475818272
            __attrs_140310475818272 = _static_140310566789392
            __append_140310476918784_plonefoundation('\n           ')

            # <Static value=<ast.Dict object at 0x7f9c9411fa60> name=None at 7f9c9411c610> -> __attrs_140310475817408
            __attrs_140310475817408 = _static_140310475831904

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140310476918784_plonefoundation('<a href="http://plone.org/foundation">')
            __stream_140310475833248 = []
            __append_140310475833248 = __stream_140310475833248.append
            __append_140310475833248('Plone Foundation')
            __msgid_140310475833248 = __re_whitespace(''.join(__stream_140310475833248)).strip()
            if 'label_plone_foundation':
                __append_140310476918784_plonefoundation(translate('label_plone_foundation', mapping=None, default=__msgid_140310475833248, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_140310476918784_plonefoundation('</a>')
            __append_140310475817264('${plonefoundation}')
            __stream_140310476918784_plonefoundation = ''.join(__stream_140310476918784_plonefoundation)
            __append_140310475817264('\n      and friends.\n      ')
            __msgid_140310475817264 = __re_whitespace(''.join(__stream_140310475817264)).strip()
            if 'description_copyright':
                __append(translate('description_copyright', mapping={'plonefoundation': __stream_140310476918784_plonefoundation, 'current_year': __stream_140310476918784_current_year, 'plonecms': __stream_140310476918784_plonecms, 'copyright': __stream_140310476918784_copyright, }, default=__msgid_140310475817264, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310475828928
            __attrs_140310475828928 = _static_140310566789392
            __stream_140310476918784_license = ''
            __stream_140310475824464 = []
            __append_140310475824464 = __stream_140310475824464.append
            __append_140310475824464('\n      Distributed under the\n           ')
            __stream_140310476918784_license = []
            __append_140310476918784_license = __stream_140310476918784_license.append

            # <Static value=<ast.Dict object at 0x7f9c997de110> name=None at 7f9c997de440> -> __attrs_140310272553456
            __attrs_140310272553456 = _static_140310566789392
            __append_140310476918784_license('\n                ')

            # <Static value=<ast.Dict object at 0x7f9c87f43d60> name=None at 7f9c87f41a50> -> __attrs_140310272555904
            __attrs_140310272555904 = _static_140310272556384

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140310476918784_license('<a href="http://creativecommons.org/licenses/GPL/2.0/">')
            __stream_140310272548512 = []
            __append_140310272548512 = __stream_140310272548512.append
            __append_140310272548512('GNU GPL license')
            __msgid_140310272548512 = __re_whitespace(''.join(__stream_140310272548512)).strip()
            if 'label_gnu_gpl_licence':
                __append_140310476918784_license(translate('label_gnu_gpl_licence', mapping=None, default=__msgid_140310272548512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_140310476918784_license('</a>')
            __append_140310475824464('${license}')
            __stream_140310476918784_license = ''.join(__stream_140310476918784_license)
            __append_140310475824464('.\n      ')
            __msgid_140310475824464 = __re_whitespace(''.join(__stream_140310475824464)).strip()
            if 'description_license':
                __append(translate('description_license', mapping={'license': __stream_140310476918784_license, }, default=__msgid_140310475824464, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n    </div>\n\n  </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x7f9c87f0e350> name=None at 7f9c87f0f400> -> __attrs_140310272337392
            __attrs_140310272337392 = _static_140310272336720
            __previous_i18n_domain_140310272334560 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_140310272334560
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_portlet': render_portlet, 'render': render, }