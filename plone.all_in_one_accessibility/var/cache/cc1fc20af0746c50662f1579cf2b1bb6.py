# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/browser/templates/footer.pt'

__tokens = {860: ('nocall:modules/DateTime.DateTime', 20, 30), 921: (' python:DateTime(', 21, 27), 963: ('python:myTime.year()', 22, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882205618832 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }
_static_139882206078544 = {'href': 'http://creativecommons.org/licenses/GPL/2.0/', }
_static_139882206083680 = {'href': 'http://plone.org/foundation', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882205620128 = {'title': 'Copyright', }
_static_139882205613648 = {'href': 'http://plone.org', }
_static_139882337226896 = {}
_static_139882205620944 = {'class': 'card-body', }
_static_139882205614512 = {'class': 'card card-classic', 'id': 'portal-footer-signature', }

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

            # <Static value=<ast.Dict object at 0x7f38dd2d11b0> name=None at 7f38dd2d3310> -> __attrs_139882205617152
            __attrs_139882205617152 = _static_139882205614512

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card card-classic" id="portal-footer-signature">\n\n    ')

            # <Static value=<ast.Dict object at 0x7f38dd2d2ad0> name=None at 7f38dd2d26e0> -> __attrs_139882205612256
            __attrs_139882205612256 = _static_139882205620944

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205623776
            __attrs_139882205623776 = _static_139882337226896
            __stream_139882101927584_copyright = ''
            __stream_139882101927584_plonecms = ''
            __stream_139882101927584_current_year = ''
            __stream_139882101927584_plonefoundation = ''
            __stream_139882205618784 = []
            __append_139882205618784 = __stream_139882205618784.append
            __append_139882205618784('\n      The\n      ')
            __stream_139882101927584_plonecms = []
            __append_139882101927584_plonecms = __stream_139882101927584_plonecms.append

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205611584
            __attrs_139882205611584 = _static_139882337226896
            __append_139882101927584_plonecms('\n           ')

            # <Static value=<ast.Dict object at 0x7f38dd2d0e50> name=None at 7f38dd2d3d90> -> __attrs_139882205615040
            __attrs_139882205615040 = _static_139882205613648

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139882101927584_plonecms('<a href="http://plone.org">')
            __stream_139882205611200 = []
            __append_139882205611200 = __stream_139882205611200.append
            __append_139882205611200('Plone')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205618928
            __attrs_139882205618928 = _static_139882337226896

            # <sup ... (0:0)
            # --------------------------------------------------------
            __append_139882205611200('<sup>&reg;</sup> Open Source CMS/WCM')
            __msgid_139882205611200 = __re_whitespace(''.join(__stream_139882205611200)).strip()
            if 'label_plone_cms':
                __append_139882101927584_plonecms(translate('label_plone_cms', mapping=None, default=__msgid_139882205611200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_139882101927584_plonecms('</a>\n      ')
            __append_139882205618784('${plonecms}')
            __stream_139882101927584_plonecms = ''.join(__stream_139882101927584_plonecms)
            __append_139882205618784('\n      is\n      ')
            __stream_139882101927584_copyright = []
            __append_139882101927584_copyright = __stream_139882101927584_copyright.append

            # <Static value=<ast.Dict object at 0x7f38dd2d27a0> name=None at 7f38dd2d00d0> -> __attrs_139882206076144
            __attrs_139882206076144 = _static_139882205620128

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_139882101927584_copyright('<abbr')

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206079984
            __default_139882206079984 = _DEFAULT_MARKER

            # <Translate msgid='title_copyright' node=<ast.Constant object at 0x7f38dd2d0fa0> at 7f38dd2d19f0> -> __attr_title
            __attr_title = 'Copyright'
            __attr_title = translate('title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_139882101927584_copyright((' title="%s"' % __attr_title))
            __append_139882101927584_copyright('>&copy;</abbr>')
            __append_139882205618784('${copyright}')
            __stream_139882101927584_copyright = ''.join(__stream_139882101927584_copyright)
            __append_139882205618784('\n      2000-')
            __stream_139882101927584_current_year = []
            __append_139882101927584_current_year = __stream_139882101927584_current_year.append

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206080896
            __attrs_139882206080896 = _static_139882337226896
            __backup_DateTime_139882206236144 = get('DateTime', __marker)

            # <Value 'nocall:modules/DateTime.DateTime' (20:30)> -> __value
            __token = 860
            try:
                __zt_tmp = __attrs_139882206080896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('nocall', 'modules/DateTime.DateTime', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['DateTime'] = __value
            __backup_myTime_139882245430704 = get('myTime', __marker)

            # <Value 'python:DateTime()' (21:27)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_139882206080896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139882257081264('python', 'DateTime()', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            econtext['myTime'] = __value

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206070816
            __default_139882206070816 = _DEFAULT_MARKER

            # <Value 'python:myTime.year()' (22:22)> -> __cache_139882206072496
            __token = 963
            try:
                __zt_tmp = __attrs_139882206080896
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882206072496 = _static_139882257081264('python', 'myTime.year()', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:myTime.year()' (22:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd3400d0> -> __condition
            __expression = __cache_139882206072496

            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139882206072496
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_139882101927584_current_year(__content)
            if (__backup_myTime_139882245430704 is __marker):
                del econtext['myTime']
            else:
                econtext['myTime'] = __backup_myTime_139882245430704
            if (__backup_DateTime_139882206236144 is __marker):
                del econtext['DateTime']
            else:
                econtext['DateTime'] = __backup_DateTime_139882206236144
            __append_139882205618784('${current_year}')
            __stream_139882101927584_current_year = ''.join(__stream_139882101927584_current_year)
            __append_139882205618784('\n      by the\n      ')
            __stream_139882101927584_plonefoundation = []
            __append_139882101927584_plonefoundation = __stream_139882101927584_plonefoundation.append

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206077488
            __attrs_139882206077488 = _static_139882337226896
            __append_139882101927584_plonefoundation('\n           ')

            # <Static value=<ast.Dict object at 0x7f38dd343a60> name=None at 7f38dd341f60> -> __attrs_139882206081568
            __attrs_139882206081568 = _static_139882206083680

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139882101927584_plonefoundation('<a href="http://plone.org/foundation">')
            __stream_139882206077536 = []
            __append_139882206077536 = __stream_139882206077536.append
            __append_139882206077536('Plone Foundation')
            __msgid_139882206077536 = __re_whitespace(''.join(__stream_139882206077536)).strip()
            if 'label_plone_foundation':
                __append_139882101927584_plonefoundation(translate('label_plone_foundation', mapping=None, default=__msgid_139882206077536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_139882101927584_plonefoundation('</a>')
            __append_139882205618784('${plonefoundation}')
            __stream_139882101927584_plonefoundation = ''.join(__stream_139882101927584_plonefoundation)
            __append_139882205618784('\n      and friends.\n      ')
            __msgid_139882205618784 = __re_whitespace(''.join(__stream_139882205618784)).strip()
            if 'description_copyright':
                __append(translate('description_copyright', mapping={'plonefoundation': __stream_139882101927584_plonefoundation, 'current_year': __stream_139882101927584_current_year, 'plonecms': __stream_139882101927584_plonecms, 'copyright': __stream_139882101927584_copyright, }, default=__msgid_139882205618784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206073168
            __attrs_139882206073168 = _static_139882337226896
            __stream_139882101927584_license = ''
            __stream_139882205615280 = []
            __append_139882205615280 = __stream_139882205615280.append
            __append_139882205615280('\n      Distributed under the\n           ')
            __stream_139882101927584_license = []
            __append_139882101927584_license = __stream_139882101927584_license.append

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206083488
            __attrs_139882206083488 = _static_139882337226896
            __append_139882101927584_license('\n                ')

            # <Static value=<ast.Dict object at 0x7f38dd342650> name=None at 7f38dd342110> -> __attrs_139882206079600
            __attrs_139882206079600 = _static_139882206078544

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139882101927584_license('<a href="http://creativecommons.org/licenses/GPL/2.0/">')
            __stream_139882206080800 = []
            __append_139882206080800 = __stream_139882206080800.append
            __append_139882206080800('GNU GPL license')
            __msgid_139882206080800 = __re_whitespace(''.join(__stream_139882206080800)).strip()
            if 'label_gnu_gpl_licence':
                __append_139882101927584_license(translate('label_gnu_gpl_licence', mapping=None, default=__msgid_139882206080800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_139882101927584_license('</a>')
            __append_139882205615280('${license}')
            __stream_139882101927584_license = ''.join(__stream_139882101927584_license)
            __append_139882205615280('.\n      ')
            __msgid_139882205615280 = __re_whitespace(''.join(__stream_139882205615280)).strip()
            if 'description_license':
                __append(translate('description_license', mapping={'license': __stream_139882101927584_license, }, default=__msgid_139882205615280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
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

            # <Static value=<ast.Dict object at 0x7f38dd2d2290> name=None at 7f38dd2d3370> -> __attrs_139882205624496
            __attrs_139882205624496 = _static_139882205618832
            __previous_i18n_domain_139882205617632 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_139882205617632
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_portlet': render_portlet, 'render': render, }