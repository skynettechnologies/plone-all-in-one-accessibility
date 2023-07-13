# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/controlpanel/browser/quickinstaller.pt'

__tokens = {1150: ('view/get_upgrades', 35, 36), 1208: (' python:len(products', 36, 39), 1386: ('not:products', 39, 30), 1667: ('products', 43, 27), 1781: ('products', 45, 44), 1822: ('product/id', 46, 30), 2084: ('pid', 50, 44), 2355: ('string:Upgrade ${pid}', 56, 44), 2451: ('product/title', 59, 33), 2648: ('product/description', 64, 39), 2682: ('product/description', 64, 73), 2809: ('pid', 65, 58), 2856: ('product/version', 65, 105), 3022: ('product/upgrade_info', 68, 43), 3237: ('not:upgrade_info/hasProfile', 72, 39), 3419: ('upgrade_info/installedVersion', 74, 77), 3533: ('upgrade_info/hasProfile', 76, 39), 3736: ('upgrade_info/installedVersion', 78, 87), 3993: ('upgrade_info/newVersion', 81, 86), 4133: ('not:upgrade_info/available', 85, 38), 4617: ('python:num_products > 1', 96, 29), 4787: ('products', 98, 51), 4953: ('product/id', 101, 44), 5522: ('view/get_available', 116, 36), 5578: (' python:len(products', 117, 36), 5829: ('products', 121, 34), 5909: ('product/id', 122, 35), 6129: ('pid', 126, 46), 6485: ('product/title', 137, 33), 6682: ('product/description', 142, 39), 6766: ('product/description', 144, 29), 6875: ('pid', 145, 58), 6922: ('product/version', 145, 105), 7091: ('not:product/uninstall_profile', 149, 31), 7389: ('view/get_installed', 158, 36), 7448: (' python:len(products', 159, 39), 7701: ('products', 163, 34), 7781: ('product/id', 164, 35), 7995: ('pid', 168, 42), 8213: ('product/uninstall_profile', 173, 37), 8405: ('product/title', 179, 35), 8612: ('product/description', 184, 41), 8700: ('product/description', 186, 31), 8811: ('pid', 187, 60), 8858: ('product/version', 187, 107), 9032: ('not:product/uninstall_profile', 191, 33), 9331: ('view/get_broken', 200, 36), 9388: (' python:len(products', 201, 40), 9443: ('num_products', 202, 31), 9685: ('products', 206, 34), 9780: ('product/product_id', 208, 33), 9976: ('product/type', 213, 33), 10087: ('product/value', 214, 61), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139856821593728 = {'class': 'discreet', }
_static_139856821585280 = {'class': 'configletDescription discreet', }
_static_139856821589456 = {'class': 'list-group-item mt-2 pb-3', }
_static_139856821590896 = {'class': 'configlets list-group list-group-flush', }
_static_139856823252880 = {'class': 'card-header', }
_static_139856821457904 = {'id': 'broken-products', 'class': 'card mb-4', }
_static_139856821410144 = {'class': 'alert alert-info mt-2 mb-0', 'role': 'status', }
_static_139856821414992 = {'class': 'discreet', }
_static_139856821417968 = {'class': 'configletDescription discreet', }
_static_139856821452864 = {'class': 'btn btn-sm btn-danger', 'type': 'submit', 'value': 'Uninstall', 'name': 'form.submitted', }
_static_139856821453872 = {'type': 'hidden', 'name': 'uninstall_product', 'value': 'pid', }
_static_139856821456320 = {'action': 'uninstall_products', 'method': 'post', 'class': 'float-end', }
_static_139856821459872 = {'class': 'list-group-item mt-2 pb-3', }
_static_139856821461456 = {'class': 'configlets list-group list-group-flush', }
_static_139856821462752 = {'class': 'card-header', }
_static_139856821485232 = {'id': 'activated-products', 'class': 'card mb-4', }
_static_139856821467840 = {'class': 'alert alert-warning mt-2 mb-0', 'role': 'status', }
_static_139856821472320 = {'class': 'discreet', }
_static_139856821475248 = {'class': 'configletDescription discreet', }
_static_139856821478896 = {'class': 'btn btn-sm btn-primary', 'type': 'submit', 'value': 'Install', 'name': 'form.submitted', }
_static_139856821481920 = {'type': 'hidden', 'name': 'install_product', 'value': 'pid', }
_static_139856821483648 = {'action': 'install_products', 'method': 'post', 'class': 'float-end', }
_static_139856821536032 = {'class': 'list-group-item mt-2 pb-3', }
_static_139856821537760 = {'class': 'configlets list-group list-group-flush', }
_static_139856821539152 = {'class': 'card-header', }
_static_139856821540256 = {'id': 'install-products', 'class': 'card mb-4', }
_static_139856821541072 = {'class': 'btn btn-primary', 'type': 'submit', 'value': 'Upgrade them ALL!', 'name': 'form.submitted', }
_static_139856821546016 = {'type': 'hidden', 'value': 'product', 'name': 'prefs_reinstallProducts:list', }
_static_139856821548752 = {'action': 'upgrade_products', 'method': 'post', }
_static_139856823304928 = {'class': 'list-group-item mt-2 pb-3', }
_static_139856823304448 = {'class': 'list-group-item mt-2 pb-3', }
_static_139856823306272 = {'class': 'configletDetails list-group list-group-flush', }
_static_139856823310880 = {'class': 'discreet', }
_static_139856823313808 = {'class': 'configletDescription discreet', }
_static_139856823317072 = {'class': 'btn btn-secondary', 'type': 'submit', 'value': 'Upgrade ${pid}', 'name': 'form.submitted', }
_static_139856823137088 = {'type': 'hidden', 'name': 'prefs_reinstallProducts:list', 'value': 'pid', }
_static_139856823137232 = {'action': 'upgrade_products', 'method': 'post', 'class': 'float-end', }
_static_139856824720192 = {'class': 'list-group-item mt-2 pb-3', }
_static_139856822401728 = {'class': 'configlets list-group list-group-flush', }
_static_139856823371904 = {'id': 'up-to-date-message', 'class': 'alert alert-info m-3 mb-0', 'role': 'status', }
_static_139856823373728 = {'class': 'card-header', }
_static_139856914195856 = __C2ZContextWrapper
_static_139856914196144 = __compile_zt_expr
_static_139856823374928 = {'id': 'upgrade-products', 'class': 'card mb-4', }
_static_139856823377232 = {'id': 'content-core', }
_static_139856823377904 = {'href': 'http://docs.plone.org/manage/installing/installing_addons.html', }
_static_139856823381024 = {'class': 'discreet', }
_static_139856823382560 = {'class': 'lead', }
_static_139856823384048 = {'class': 'documentFirstHeading', }
_static_139856823414128 = 'master'
_static_139856913889840 = {}

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

            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823413504
            __attrs_139856823413504 = _static_139856913889840
            __backup_macroname_139856872880128 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f32f4476d70> name=None at 7f32f4476bf0> -> __value
            __value = _static_139856823414128
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823403088
                __attrs_139856823403088 = _static_139856913889840
                __previous_i18n_domain_139856823403040 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823385392
                __attrs_139856823385392 = _static_139856913889840

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f32f446f7f0> name=None at 7f32f446f9a0> -> __attrs_139856823383664
                __attrs_139856823383664 = _static_139856823384048

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_139856823384192 = []
                __append_139856823384192 = __stream_139856823384192.append
                __append_139856823384192('Add-ons')
                __msgid_139856823384192 = __re_whitespace(''.join(__stream_139856823384192)).strip()
                if __msgid_139856823384192:
                    __append(translate(__msgid_139856823384192, mapping=None, default=__msgid_139856823384192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f32f446f220> name=None at 7f32f446ef80> -> __attrs_139856823382128
                __attrs_139856823382128 = _static_139856823382560

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_139856823383136 = []
                __append_139856823383136 = __stream_139856823383136.append
                __append_139856823383136('\n      This is the Add-on configuration section, you can activate and deactivate\n      add-ons in the lists below.\n    ')
                __msgid_139856823383136 = __re_whitespace(''.join(__stream_139856823383136)).strip()
                if __msgid_139856823383136:
                    __append(translate(__msgid_139856823383136, mapping=None, default=__msgid_139856823383136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n    ')

                # <Static value=<ast.Dict object at 0x7f32f446ec20> name=None at 7f32f446eb90> -> __attrs_139856823380112
                __attrs_139856823380112 = _static_139856823381024

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="discreet">')
                __stream_139856822444416_third_party_product = ''
                __stream_139856823381552 = []
                __append_139856823381552 = __stream_139856823381552.append
                __append_139856823381552('\n      To make new add-ons show up here, add them to your buildout\n      configuration, run buildout, and restart the server process.\n      For detailed instructions see\n      ')
                __stream_139856822444416_third_party_product = []
                __append_139856822444416_third_party_product = __stream_139856822444416_third_party_product.append

                # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823379104
                __attrs_139856823379104 = _static_139856913889840

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_139856822444416_third_party_product('<span>\n      ')

                # <Static value=<ast.Dict object at 0x7f32f446dff0> name=None at 7f32f446e170> -> __attrs_139856823378000
                __attrs_139856823378000 = _static_139856823377904

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_139856822444416_third_party_product('<a href="http://docs.plone.org/manage/installing/installing_addons.html">')
                __stream_139856823378768 = []
                __append_139856823378768 = __stream_139856823378768.append
                __append_139856823378768('\n        Installing a third party add-on\n      ')
                __msgid_139856823378768 = __re_whitespace(''.join(__stream_139856823378768)).strip()
                if __msgid_139856823378768:
                    __append_139856822444416_third_party_product(translate(__msgid_139856823378768, mapping=None, default=__msgid_139856823378768, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_139856822444416_third_party_product('</a>\n      </span>')
                __append_139856823381552('${third_party_product}')
                __stream_139856822444416_third_party_product = ''.join(__stream_139856822444416_third_party_product)
                __append_139856823381552('.\n    ')
                __msgid_139856823381552 = __re_whitespace(''.join(__stream_139856823381552)).strip()
                if __msgid_139856823381552:
                    __append(translate(__msgid_139856823381552, mapping={'third_party_product': __stream_139856822444416_third_party_product, }, default=__msgid_139856823381552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x7f32f446dd50> name=None at 7f32f446dd80> -> __attrs_139856823376848
                __attrs_139856823376848 = _static_139856823377232

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n\n\n      ')

                # <Static value=<ast.Dict object at 0x7f32f446d450> name=None at 7f32f446d600> -> __attrs_139856823374640
                __attrs_139856823374640 = _static_139856823374928
                __backup_products_139856823402800 = get('products', __marker)

                # <Value 'view/get_upgrades' (35:36)> -> __value
                __token = 1150
                try:
                    __zt_tmp = __attrs_139856823374640
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/get_upgrades', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_139856823385056 = get('num_products', __marker)

                # <Value 'python:len(products)' (36:39)> -> __value
                __token = 1208
                try:
                    __zt_tmp = __attrs_139856823374640
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('python', 'len(products)', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="upgrade-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f32f446cfa0> name=None at 7f32f446cd30> -> __attrs_139856823373344
                __attrs_139856823373344 = _static_139856823373728

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_139856823374256 = []
                __append_139856823374256 = __stream_139856823374256.append
                __append_139856823374256('Upgrades')
                __msgid_139856823374256 = __re_whitespace(''.join(__stream_139856823374256)).strip()
                if __msgid_139856823374256:
                    __append(translate(__msgid_139856823374256, mapping=None, default=__msgid_139856823374256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n          ')

                # <Static value=<ast.Dict object at 0x7f32f446c880> name=None at 7f32f446c8b0> -> __attrs_139856823371376
                __attrs_139856823371376 = _static_139856823371904

                # <Value 'not:products' (39:30)> -> __condition
                __token = 1386
                try:
                    __zt_tmp = __attrs_139856823371376
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('not', 'products', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="up-to-date-message" class="alert alert-info m-3 mb-0" role="status">\n            ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823369888
                    __attrs_139856823369888 = _static_139856913889840

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139856823370128 = []
                    __append_139856823370128 = __stream_139856823370128.append
                    __append_139856823370128('No upgrades in this corner.')
                    __msgid_139856823370128 = __re_whitespace(''.join(__stream_139856823370128)).strip()
                    if __msgid_139856823370128:
                        __append(translate(__msgid_139856823370128, mapping=None, default=__msgid_139856823370128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n            ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856824464240
                    __attrs_139856824464240 = _static_139856913889840

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139856825471216 = []
                    __append_139856825471216 = __stream_139856825471216.append
                    __append_139856825471216('You are up to date. High fives.')
                    __msgid_139856825471216 = __re_whitespace(''.join(__stream_139856825471216)).strip()
                    if __msgid_139856825471216:
                        __append(translate(__msgid_139856825471216, mapping=None, default=__msgid_139856825471216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n          </div>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f32f437fac0> name=None at 7f32f437fb50> -> __attrs_139856822391984
                __attrs_139856822391984 = _static_139856822401728

                # <Value 'products' (43:27)> -> __condition
                __token = 1667
                try:
                    __zt_tmp = __attrs_139856822391984
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('path', 'products', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856822465392
                    __attrs_139856822465392 = _static_139856913889840
                    __backup_product_139856823377616 = get('product', __marker)

                    # <Value 'products' (45:44)> -> __iterator
                    __token = 1781
                    try:
                        __zt_tmp = __attrs_139856822465392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139856914196144('path', 'products', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    (__iterator, ____index_139856822463328, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7f32f45b5b40> name=None at 7f32f45b5e10> -> __attrs_139856825325632
                        __attrs_139856825325632 = _static_139856824720192
                        __backup_pid_139856823370944 = get('pid', __marker)

                        # <Value 'product/id' (46:30)> -> __value
                        __token = 1822
                        try:
                            __zt_tmp = __attrs_139856825325632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139856914196144('path', 'product/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        econtext['pid'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f32f44333d0> name=None at 7f32f4432e30> -> __attrs_139856823137184
                        __attrs_139856823137184 = _static_139856823137232

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post" class="float-end">\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f4433340> name=None at 7f32f4430f40> -> __attrs_139856823318704
                        __attrs_139856823318704 = _static_139856823137088

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="prefs_reinstallProducts:list"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823320048
                        __default_139856823320048 = _DEFAULT_MARKER

                        # <Substitution 'pid' (50:44)> -> __attr_value
                        __token = 2084
                        try:
                            __zt_tmp = __attrs_139856823318704
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139856914196144('path', 'pid', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f445f250> name=None at 7f32f445f280> -> __attrs_139856823318752
                        __attrs_139856823318752 = _static_139856823317072

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-secondary" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823318032
                        __default_139856823318032 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<Substitution 'string:Upgrade ${pid}' (56:44)> at 7f32f445f580> -> __attr_value

                        # <Substitution 'string:Upgrade ${pid}' (56:44)> -> __attr_value
                        __token = 2355
                        try:
                            __zt_tmp = __attrs_139856823318752
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139856914196144('string', 'Upgrade ${pid}', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', 'Upgrade ${pid}', _DEFAULT_MARKER)
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted"/>\n            </form>\n            ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823316352
                        __attrs_139856823316352 = _static_139856913889840

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823314816
                        __attrs_139856823314816 = _static_139856913889840

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823314912
                        __default_139856823314912 = _DEFAULT_MARKER

                        # <Value 'product/title' (59:33)> -> __cache_139856823315392
                        __token = 2451
                        try:
                            __zt_tmp = __attrs_139856823314816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856823315392 = _static_139856914196144('path', 'product/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/title' (59:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f445eb60> -> __condition
                        __expression = __cache_139856823315392

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_139856823315392
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x7f32f445e590> name=None at 7f32f445e7a0> -> __attrs_139856823313472
                        __attrs_139856823313472 = _static_139856823313808

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823311216
                        __attrs_139856823311216 = _static_139856913889840

                        # <Value 'product/description' (64:39)> -> __condition
                        __token = 2648
                        try:
                            __zt_tmp = __attrs_139856823311216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139856914196144('path', 'product/description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823311744
                            __default_139856823311744 = _DEFAULT_MARKER

                            # <Value 'product/description' (64:73)> -> __cache_139856823312320
                            __token = 2682
                            try:
                                __zt_tmp = __attrs_139856823311216
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139856823312320 = _static_139856914196144('path', 'product/description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                            # <BinOp left=<Value 'product/description' (64:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f445e140> -> __condition
                            __expression = __cache_139856823312320

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('add-on description')
                            else:
                                __content = __cache_139856823312320
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f445da20> name=None at 7f32f445d960> -> __attrs_139856823309872
                        __attrs_139856823309872 = _static_139856823310880

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> – (')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823308672
                        __attrs_139856823308672 = _static_139856913889840

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823308336
                        __default_139856823308336 = _DEFAULT_MARKER

                        # <Value 'pid' (65:58)> -> __cache_139856823308816
                        __token = 2809
                        try:
                            __zt_tmp = __attrs_139856823308672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856823308816 = _static_139856914196144('path', 'pid', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pid' (65:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f445d360> -> __condition
                        __expression = __cache_139856823308816

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>plugin.app.name</span>')
                        else:
                            __content = __cache_139856823308816
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(' ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823306848
                        __attrs_139856823306848 = _static_139856913889840

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823307136
                        __default_139856823307136 = _DEFAULT_MARKER

                        # <Value 'product/version' (65:105)> -> __cache_139856823307712
                        __token = 2856
                        try:
                            __zt_tmp = __attrs_139856823306848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856823307712 = _static_139856914196144('path', 'product/version', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/version' (65:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f445cc40> -> __condition
                        __expression = __cache_139856823307712

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>1.0</span>')
                        else:
                            __content = __cache_139856823307712
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(')</em>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x7f32f445c820> name=None at 7f32f445c5e0> -> __attrs_139856823305744
                        __attrs_139856823305744 = _static_139856823306272

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="configletDetails list-group list-group-flush">\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f445c100> name=None at 7f32f445c370> -> __attrs_139856823044752
                        __attrs_139856823044752 = _static_139856823304448
                        __backup_upgrade_info_139856822583248 = get('upgrade_info', __marker)

                        # <Value 'product/upgrade_info' (68:43)> -> __value
                        __token = 3022
                        try:
                            __zt_tmp = __attrs_139856823044752
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139856914196144('path', 'product/upgrade_info', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        econtext['upgrade_info'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n                  ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823054976
                        __attrs_139856823054976 = _static_139856913889840

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_139856823055504 = []
                        __append_139856823055504 = __stream_139856823055504.append
                        __append_139856823055504('\n                    This addon has been upgraded.\n                  ')
                        __msgid_139856823055504 = __re_whitespace(''.join(__stream_139856823055504)).strip()
                        if __msgid_139856823055504:
                            __append(translate(__msgid_139856823055504, mapping=None, default=__msgid_139856823055504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823051328
                        __attrs_139856823051328 = _static_139856913889840

                        # <Value 'not:upgrade_info/hasProfile' (72:39)> -> __condition
                        __token = 3237
                        try:
                            __zt_tmp = __attrs_139856823051328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139856914196144('not', 'upgrade_info/hasProfile', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_139856822442624_version = ''
                            __stream_139856823042640 = []
                            __append_139856823042640 = __stream_139856823042640.append
                            __append_139856823042640('\n                    Old version was ')
                            __stream_139856822442624_version = []
                            __append_139856822442624_version = __stream_139856822442624_version.append

                            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823296224
                            __attrs_139856823296224 = _static_139856913889840

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_139856822442624_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823046480
                            __default_139856823046480 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (74:77)> -> __cache_139856823048688
                            __token = 3419
                            try:
                                __zt_tmp = __attrs_139856823296224
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139856823048688 = _static_139856914196144('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (74:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f441dae0> -> __condition
                            __expression = __cache_139856823048688

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_139856822442624_version('version')
                            else:
                                __content = __cache_139856823048688
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_139856822442624_version(__content)
                            __append_139856822442624_version('</strong>')
                            __append_139856823042640('${version}')
                            __stream_139856822442624_version = ''.join(__stream_139856822442624_version)
                            __append_139856823042640('.\n                  ')
                            __msgid_139856823042640 = __re_whitespace(''.join(__stream_139856823042640)).strip()
                            if 'label_product_upgrade_old_version':
                                __append(translate('label_product_upgrade_old_version', mapping={'version': __stream_139856822442624_version, }, default=__msgid_139856823042640, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823303040
                        __attrs_139856823303040 = _static_139856913889840

                        # <Value 'upgrade_info/hasProfile' (76:39)> -> __condition
                        __token = 3533
                        try:
                            __zt_tmp = __attrs_139856823303040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139856914196144('path', 'upgrade_info/hasProfile', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823302272
                            __attrs_139856823302272 = _static_139856913889840
                            __stream_139856822436128_version = ''
                            __stream_139856823302608 = []
                            __append_139856823302608 = __stream_139856823302608.append
                            __append_139856823302608('\n                      Old profile version was ')
                            __stream_139856822436128_version = []
                            __append_139856822436128_version = __stream_139856822436128_version.append

                            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823300496
                            __attrs_139856823300496 = _static_139856913889840

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_139856822436128_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823301072
                            __default_139856823301072 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (78:87)> -> __cache_139856823301552
                            __token = 3736
                            try:
                                __zt_tmp = __attrs_139856823300496
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139856823301552 = _static_139856914196144('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (78:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f445b490> -> __condition
                            __expression = __cache_139856823301552

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_139856822436128_version('version')
                            else:
                                __content = __cache_139856823301552
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_139856822436128_version(__content)
                            __append_139856822436128_version('</strong>')
                            __append_139856823302608('${version}')
                            __stream_139856822436128_version = ''.join(__stream_139856822436128_version)
                            __append_139856823302608('.\n                    ')
                            __msgid_139856823302608 = __re_whitespace(''.join(__stream_139856823302608)).strip()
                            if 'label_product_upgrade_old_profile_version':
                                __append(translate('label_product_upgrade_old_profile_version', mapping={'version': __stream_139856822436128_version, }, default=__msgid_139856823302608, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823299872
                            __attrs_139856823299872 = _static_139856913889840
                            __stream_139856822436128_version = ''
                            __stream_139856823302512 = []
                            __append_139856823302512 = __stream_139856823302512.append
                            __append_139856823302512('\n                      New profile version is ')
                            __stream_139856822436128_version = []
                            __append_139856822436128_version = __stream_139856822436128_version.append

                            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823289168
                            __attrs_139856823289168 = _static_139856913889840

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_139856822436128_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856823288976
                            __default_139856823288976 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/newVersion' (81:86)> -> __cache_139856823298672
                            __token = 3993
                            try:
                                __zt_tmp = __attrs_139856823289168
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139856823298672 = _static_139856914196144('path', 'upgrade_info/newVersion', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/newVersion' (81:86)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f445abc0> -> __condition
                            __expression = __cache_139856823298672

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_139856822436128_version('version')
                            else:
                                __content = __cache_139856823298672
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_139856822436128_version(__content)
                            __append_139856822436128_version('</strong>')
                            __append_139856823302512('${version}')
                            __stream_139856822436128_version = ''.join(__stream_139856822436128_version)
                            __append_139856823302512('.\n                    ')
                            __msgid_139856823302512 = __re_whitespace(''.join(__stream_139856823302512)).strip()
                            if 'label_product_upgrade_new_profile_version':
                                __append(translate('label_product_upgrade_new_profile_version', mapping={'version': __stream_139856822436128_version, }, default=__msgid_139856823302512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                  </span>')
                        __append('\n\n                  ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823298192
                        __attrs_139856823298192 = _static_139856913889840

                        # <Value 'not:upgrade_info/available' (85:38)> -> __condition
                        __token = 4133
                        try:
                            __zt_tmp = __attrs_139856823298192
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139856914196144('not', 'upgrade_info/available', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856823297088
                            __attrs_139856823297088 = _static_139856913889840

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')
                            __stream_139856823297520 = []
                            __append_139856823297520 = __stream_139856823297520.append
                            __append_139856823297520('Warning')
                            __msgid_139856823297520 = __re_whitespace(''.join(__stream_139856823297520)).strip()
                            if __msgid_139856823297520:
                                __append(translate(__msgid_139856823297520, mapping=None, default=__msgid_139856823297520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</strong>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821550528
                            __attrs_139856821550528 = _static_139856913889840

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_139856823296608 = []
                            __append_139856823296608 = __stream_139856823296608.append
                            __append_139856823296608('There is no upgrade procedure defined for this\n                    addon. Please consult the addon documentation\n                    for upgrade information, or contact the addon\n                    author.')
                            __msgid_139856823296608 = __re_whitespace(''.join(__stream_139856823296608)).strip()
                            if __msgid_139856823296608:
                                __append(translate(__msgid_139856823296608, mapping=None, default=__msgid_139856823296608, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>\n                  </div>')
                        __append('\n              </li>')
                        if (__backup_upgrade_info_139856822583248 is __marker):
                            del econtext['upgrade_info']
                        else:
                            econtext['upgrade_info'] = __backup_upgrade_info_139856822583248
                        __append('\n            </ul>\n          </li>')
                        if (__backup_pid_139856823370944 is __marker):
                            del econtext['pid']
                        else:
                            econtext['pid'] = __backup_pid_139856823370944
                        __append('\n          ')
                        ____index_139856822463328 -= 1
                        if (____index_139856822463328 > 0):
                            __append('')
                    if (__backup_product_139856823377616 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_139856823377616
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f32f445c2e0> name=None at 7f32f441eb00> -> __attrs_139856821549952
                    __attrs_139856821549952 = _static_139856823304928

                    # <Value 'python:num_products > 1' (96:29)> -> __condition
                    __token = 4617
                    try:
                        __zt_tmp = __attrs_139856821549952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('python', 'num_products > 1', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f32f42af6d0> name=None at 7f32f42af700> -> __attrs_139856821548656
                        __attrs_139856821548656 = _static_139856821548752

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post">\n                ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821547168
                        __attrs_139856821547168 = _static_139856913889840
                        __backup_product_139856823313904 = get('product', __marker)

                        # <Value 'products' (98:51)> -> __iterator
                        __token = 4787
                        try:
                            __zt_tmp = __attrs_139856821547168
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_139856914196144('path', 'products', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                        (__iterator, ____index_139856821546928, ) = getname('repeat')('product', __iterator)
                        econtext['product'] = None
                        for __item in __iterator:
                            econtext['product'] = __item
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x7f32f42aec20> name=None at 7f32f42ae9b0> -> __attrs_139856821544864
                            __attrs_139856821544864 = _static_139856821546016

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden"')

                            # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821546160
                            __default_139856821546160 = _DEFAULT_MARKER

                            # <Substitution 'product/id' (101:44)> -> __attr_value
                            __token = 4953
                            try:
                                __zt_tmp = __attrs_139856821544864
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_139856914196144('path', 'product/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'product', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' name="prefs_reinstallProducts:list" />\n                ')
                            ____index_139856821546928 -= 1
                            if (____index_139856821546928 > 0):
                                __append('')
                        if (__backup_product_139856823313904 is __marker):
                            del econtext['product']
                        else:
                            econtext['product'] = __backup_product_139856823313904
                        __append('\n                ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821544912
                        __attrs_139856821544912 = _static_139856913889840

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821543328
                        __attrs_139856821543328 = _static_139856913889840

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>')
                        __stream_139856821543808 = []
                        __append_139856821543808 = __stream_139856821543808.append
                        __append_139856821543808('This can be risky, are you sure you want to do this?')
                        __msgid_139856821543808 = __re_whitespace(''.join(__stream_139856821543808)).strip()
                        if 'label_product_upgrade_all_action':
                            __append(translate('label_product_upgrade_all_action', mapping=None, default=__msgid_139856821543808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f32f42ad8d0> name=None at 7f32f42ada80> -> __attrs_139856821543232
                        __attrs_139856821543232 = _static_139856821541072

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821542512
                        __default_139856821542512 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<ast.Constant object at 0x7f32f42addb0> at 7f32f42add80> -> __attr_value
                        __attr_value = 'Upgrade them ALL!'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted" />\n                </span>\n            </form>\n            </li>')
                    __append('\n          </ul>')
                __append('\n      </section>')
                if (__backup_num_products_139856823385056 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_139856823385056
                if (__backup_products_139856823402800 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_139856823402800
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f32f42ad5a0> name=None at 7f32f42ad750> -> __attrs_139856821540016
                __attrs_139856821540016 = _static_139856821540256
                __backup_products_139856823385968 = get('products', __marker)

                # <Value 'view/get_available' (116:36)> -> __value
                __token = 5522
                try:
                    __zt_tmp = __attrs_139856821540016
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/get_available', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_139856823382752 = get('num_products', __marker)

                # <Value 'python:len(products)' (117:36)> -> __value
                __token = 5578
                try:
                    __zt_tmp = __attrs_139856821540016
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('python', 'len(products)', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="install-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f32f42ad150> name=None at 7f32f42acee0> -> __attrs_139856821538720
                __attrs_139856821538720 = _static_139856821539152

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_139856821539632 = []
                __append_139856821539632 = __stream_139856821539632.append
                __append_139856821539632('Available add-ons')
                __msgid_139856821539632 = __re_whitespace(''.join(__stream_139856821539632)).strip()
                if __msgid_139856821539632:
                    __append(translate(__msgid_139856821539632, mapping=None, default=__msgid_139856821539632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x7f32f42acbe0> name=None at 7f32f42ac940> -> __attrs_139856821537136
                __attrs_139856821537136 = _static_139856821537760

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x7f32f42ac520> name=None at 7f32f42ac4c0> -> __attrs_139856821535552
                __attrs_139856821535552 = _static_139856821536032
                __backup_product_139856822465584 = get('product', __marker)

                # <Value 'products' (121:34)> -> __iterator
                __token = 5829
                try:
                    __zt_tmp = __attrs_139856821535552
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139856914196144('path', 'products', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                (__iterator, ____index_139856821535312, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821485280
                    __attrs_139856821485280 = _static_139856913889840
                    __backup_pid_139856824185040 = get('pid', __marker)

                    # <Value 'product/id' (122:35)> -> __value
                    __token = 5909
                    try:
                        __zt_tmp = __attrs_139856821485280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139856914196144('path', 'product/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f32f429f880> name=None at 7f32f429f8b0> -> __attrs_139856821482784
                    __attrs_139856821482784 = _static_139856821483648

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="install_products" method="post" class="float-end">\n                ')

                    # <Static value=<ast.Dict object at 0x7f32f429f1c0> name=None at 7f32f429ef80> -> __attrs_139856821480816
                    __attrs_139856821480816 = _static_139856821481920

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="install_product"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821482592
                    __default_139856821482592 = _DEFAULT_MARKER

                    # <Substitution 'pid' (126:46)> -> __attr_value
                    __token = 6129
                    try:
                        __zt_tmp = __attrs_139856821480816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139856914196144('path', 'pid', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x7f32f429e5f0> name=None at 7f32f429e620> -> __attrs_139856821480528
                    __attrs_139856821480528 = _static_139856821478896

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-sm btn-primary" type="submit" value="Install" name="form.submitted">')
                    __stream_139856821480864 = []
                    __append_139856821480864 = __stream_139856821480864.append
                    __append_139856821480864('\n                    Install\n                ')
                    __msgid_139856821480864 = __re_whitespace(''.join(__stream_139856821480864)).strip()
                    if __msgid_139856821480864:
                        __append(translate(__msgid_139856821480864, mapping=None, default=__msgid_139856821480864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821478272
                    __attrs_139856821478272 = _static_139856913889840

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n              ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821476688
                    __attrs_139856821476688 = _static_139856913889840

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821476784
                    __default_139856821476784 = _DEFAULT_MARKER

                    # <Value 'product/title' (137:33)> -> __cache_139856821477264
                    __token = 6485
                    try:
                        __zt_tmp = __attrs_139856821476688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856821477264 = _static_139856914196144('path', 'product/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (137:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f429df30> -> __condition
                    __expression = __cache_139856821477264

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                Add-on Name\n              </span>')
                    else:
                        __content = __cache_139856821477264
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            </h3>\n            ')

                    # <Static value=<ast.Dict object at 0x7f32f429d7b0> name=None at 7f32f429db10> -> __attrs_139856821475440
                    __attrs_139856821475440 = _static_139856821475248

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n              ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821473616
                    __attrs_139856821473616 = _static_139856913889840

                    # <Value 'product/description' (142:39)> -> __condition
                    __token = 6682
                    try:
                        __zt_tmp = __attrs_139856821473616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('path', 'product/description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821474192
                        __default_139856821474192 = _DEFAULT_MARKER

                        # <Value 'product/description' (144:29)> -> __cache_139856821474768
                        __token = 6766
                        try:
                            __zt_tmp = __attrs_139856821473616
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856821474768 = _static_139856914196144('path', 'product/description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (144:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f429d480> -> __condition
                        __expression = __cache_139856821474768

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_139856821474768
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7f32f429cc40> name=None at 7f32f429cdc0> -> __attrs_139856821472368
                    __attrs_139856821472368 = _static_139856821472320

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821470784
                    __attrs_139856821470784 = _static_139856913889840

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821470880
                    __default_139856821470880 = _DEFAULT_MARKER

                    # <Value 'pid' (145:58)> -> __cache_139856821471408
                    __token = 6875
                    try:
                        __zt_tmp = __attrs_139856821470784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856821471408 = _static_139856914196144('path', 'pid', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (145:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f429c850> -> __condition
                    __expression = __cache_139856821471408

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_139856821471408
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821469040
                    __attrs_139856821469040 = _static_139856913889840

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821468944
                    __default_139856821468944 = _DEFAULT_MARKER

                    # <Value 'product/version' (145:105)> -> __cache_139856821469296
                    __token = 6922
                    try:
                        __zt_tmp = __attrs_139856821469040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856821469296 = _static_139856914196144('path', 'product/version', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (145:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f429c1c0> -> __condition
                    __expression = __cache_139856821469296

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_139856821469296
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n            </div>\n            ')

                    # <Static value=<ast.Dict object at 0x7f32f429bac0> name=None at 7f32f429ba30> -> __attrs_139856821467504
                    __attrs_139856821467504 = _static_139856821467840

                    # <Value 'not:product/uninstall_profile' (149:31)> -> __condition
                    __token = 7091
                    try:
                        __zt_tmp = __attrs_139856821467504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('not', 'product/uninstall_profile', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-warning mt-2 mb-0" role="status">\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821466208
                        __attrs_139856821466208 = _static_139856913889840

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_139856821466784 = []
                        __append_139856821466784 = __stream_139856821466784.append
                        __append_139856821466784('Warning')
                        __msgid_139856821466784 = __re_whitespace(''.join(__stream_139856821466784)).strip()
                        if __msgid_139856821466784:
                            __append(translate(__msgid_139856821466784, mapping=None, default=__msgid_139856821466784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821465200
                        __attrs_139856821465200 = _static_139856913889840

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_139856821465728 = []
                        __append_139856821465728 = __stream_139856821465728.append
                        __append_139856821465728('This product cannot be uninstalled!')
                        __msgid_139856821465728 = __re_whitespace(''.join(__stream_139856821465728)).strip()
                        if __msgid_139856821465728:
                            __append(translate(__msgid_139856821465728, mapping=None, default=__msgid_139856821465728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_139856824185040 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_139856824185040
                    __append('\n          </li>')
                    ____index_139856821535312 -= 1
                    if (____index_139856821535312 > 0):
                        __append('\n          ')
                if (__backup_product_139856822465584 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_139856822465584
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_139856823382752 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_139856823382752
                if (__backup_products_139856823385968 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_139856823385968
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f32f429feb0> name=None at 7f32f429fe20> -> __attrs_139856821464336
                __attrs_139856821464336 = _static_139856821485232
                __backup_products_139856823378864 = get('products', __marker)

                # <Value 'view/get_installed' (158:36)> -> __value
                __token = 7389
                try:
                    __zt_tmp = __attrs_139856821464336
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/get_installed', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_139856825473280 = get('num_products', __marker)

                # <Value 'python:len(products)' (159:39)> -> __value
                __token = 7448
                try:
                    __zt_tmp = __attrs_139856821464336
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('python', 'len(products)', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="activated-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f32f429a6e0> name=None at 7f32f429a710> -> __attrs_139856821462320
                __attrs_139856821462320 = _static_139856821462752

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_139856821463232 = []
                __append_139856821463232 = __stream_139856821463232.append
                __append_139856821463232('Activated add-ons')
                __msgid_139856821463232 = __re_whitespace(''.join(__stream_139856821463232)).strip()
                if __msgid_139856821463232:
                    __append(translate(__msgid_139856821463232, mapping=None, default=__msgid_139856821463232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x7f32f429a1d0> name=None at 7f32f429a200> -> __attrs_139856821461120
                __attrs_139856821461120 = _static_139856821461456

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x7f32f4299ba0> name=None at 7f32f4299de0> -> __attrs_139856821459008
                __attrs_139856821459008 = _static_139856821459872
                __backup_product_139856823050224 = get('product', __marker)

                # <Value 'products' (163:34)> -> __iterator
                __token = 7701
                try:
                    __zt_tmp = __attrs_139856821459008
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139856914196144('path', 'products', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                (__iterator, ____index_139856821458720, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821458384
                    __attrs_139856821458384 = _static_139856913889840
                    __backup_pid_139856823311072 = get('pid', __marker)

                    # <Value 'product/id' (164:35)> -> __value
                    __token = 7781
                    try:
                        __zt_tmp = __attrs_139856821458384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139856914196144('path', 'product/id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f32f4298dc0> name=None at 7f32f4298e20> -> __attrs_139856821455408
                    __attrs_139856821455408 = _static_139856821456320

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="uninstall_products" method="post" class="float-end">\n              ')

                    # <Static value=<ast.Dict object at 0x7f32f4298430> name=None at 7f32f42985b0> -> __attrs_139856821453728
                    __attrs_139856821453728 = _static_139856821453872

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="uninstall_product"')

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821455264
                    __default_139856821455264 = _DEFAULT_MARKER

                    # <Substitution 'pid' (168:42)> -> __attr_value
                    __token = 7995
                    try:
                        __zt_tmp = __attrs_139856821453728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139856914196144('path', 'pid', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n              ')

                    # <Static value=<ast.Dict object at 0x7f32f4298040> name=None at 7f32f42980a0> -> __attrs_139856821405680
                    __attrs_139856821405680 = _static_139856821452864

                    # <Value 'product/uninstall_profile' (173:37)> -> __condition
                    __token = 8213
                    try:
                        __zt_tmp = __attrs_139856821405680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('path', 'product/uninstall_profile', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button class="btn btn-sm btn-danger" type="submit" value="Uninstall" name="form.submitted">')
                        __stream_139856821453392 = []
                        __append_139856821453392 = __stream_139856821453392.append
                        __append_139856821453392('\n                Uninstall\n              ')
                        __msgid_139856821453392 = __re_whitespace(''.join(__stream_139856821453392)).strip()
                        if __msgid_139856821453392:
                            __append(translate(__msgid_139856821453392, mapping=None, default=__msgid_139856821453392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>')
                    __append('\n            </form>\n              ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821406592
                    __attrs_139856821406592 = _static_139856913889840

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n                ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821418400
                    __attrs_139856821418400 = _static_139856913889840

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821419024
                    __default_139856821419024 = _DEFAULT_MARKER

                    # <Value 'product/title' (179:35)> -> __cache_139856821419552
                    __token = 8405
                    try:
                        __zt_tmp = __attrs_139856821418400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856821419552 = _static_139856914196144('path', 'product/title', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (179:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f428fb80> -> __condition
                    __expression = __cache_139856821419552

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  Add-on Name\n                </span>')
                    else:
                        __content = __cache_139856821419552
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n              </h3>\n              ')

                    # <Static value=<ast.Dict object at 0x7f32f428f7f0> name=None at 7f32f428fa00> -> __attrs_139856821417104
                    __attrs_139856821417104 = _static_139856821417968

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n                ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821416000
                    __attrs_139856821416000 = _static_139856913889840

                    # <Value 'product/description' (184:41)> -> __condition
                    __token = 8612
                    try:
                        __zt_tmp = __attrs_139856821416000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('path', 'product/description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821416528
                        __default_139856821416528 = _DEFAULT_MARKER

                        # <Value 'product/description' (186:31)> -> __cache_139856821417056
                        __token = 8700
                        try:
                            __zt_tmp = __attrs_139856821416000
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856821417056 = _static_139856914196144('path', 'product/description', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (186:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f428f310> -> __condition
                        __expression = __cache_139856821417056

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_139856821417056
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f32f428ec50> name=None at 7f32f428ec80> -> __attrs_139856821414512
                    __attrs_139856821414512 = _static_139856821414992

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821412400
                    __attrs_139856821412400 = _static_139856913889840

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821413072
                    __default_139856821413072 = _DEFAULT_MARKER

                    # <Value 'pid' (187:60)> -> __cache_139856821413552
                    __token = 8811
                    try:
                        __zt_tmp = __attrs_139856821412400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856821413552 = _static_139856914196144('path', 'pid', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (187:60)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f428e440> -> __condition
                    __expression = __cache_139856821413552

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_139856821413552
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821411248
                    __attrs_139856821411248 = _static_139856913889840

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821411488
                    __default_139856821411488 = _DEFAULT_MARKER

                    # <Value 'product/version' (187:107)> -> __cache_139856821411968
                    __token = 8858
                    try:
                        __zt_tmp = __attrs_139856821411248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139856821411968 = _static_139856914196144('path', 'product/version', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (187:107)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f428e020> -> __condition
                    __expression = __cache_139856821411968

                    # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_139856821411968
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n              </div>\n              ')

                    # <Static value=<ast.Dict object at 0x7f32f428d960> name=None at 7f32f428d990> -> __attrs_139856821409520
                    __attrs_139856821409520 = _static_139856821410144

                    # <Value 'not:product/uninstall_profile' (191:33)> -> __condition
                    __token = 9032
                    try:
                        __zt_tmp = __attrs_139856821409520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139856914196144('not', 'product/uninstall_profile', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-info mt-2 mb-0" role="status">\n                ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821408704
                        __attrs_139856821408704 = _static_139856913889840

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_139856821409184 = []
                        __append_139856821409184 = __stream_139856821409184.append
                        __append_139856821409184('Info')
                        __msgid_139856821409184 = __re_whitespace(''.join(__stream_139856821409184)).strip()
                        if __msgid_139856821409184:
                            __append(translate(__msgid_139856821409184, mapping=None, default=__msgid_139856821409184, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n                ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821407456
                        __attrs_139856821407456 = _static_139856913889840

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_139856821408224 = []
                        __append_139856821408224 = __stream_139856821408224.append
                        __append_139856821408224('This product cannot be uninstalled!')
                        __msgid_139856821408224 = __re_whitespace(''.join(__stream_139856821408224)).strip()
                        if __msgid_139856821408224:
                            __append(translate(__msgid_139856821408224, mapping=None, default=__msgid_139856821408224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_139856823311072 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_139856823311072
                    __append('\n          </li>')
                    ____index_139856821458720 -= 1
                    if (____index_139856821458720 > 0):
                        __append('\n          ')
                if (__backup_product_139856823050224 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_139856823050224
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_139856825473280 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_139856825473280
                if (__backup_products_139856823378864 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_139856823378864
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f32f42993f0> name=None at 7f32f4299990> -> __attrs_139856821407168
                __attrs_139856821407168 = _static_139856821457904
                __backup_products_139856823379152 = get('products', __marker)

                # <Value 'view/get_broken' (200:36)> -> __value
                __token = 9331
                try:
                    __zt_tmp = __attrs_139856821407168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('path', 'view/get_broken', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_139856823138720 = get('num_products', __marker)

                # <Value 'python:len(products)' (201:40)> -> __value
                __token = 9388
                try:
                    __zt_tmp = __attrs_139856821407168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139856914196144('python', 'len(products)', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value 'num_products' (202:31)> -> __condition
                __token = 9443
                try:
                    __zt_tmp = __attrs_139856821407168
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139856914196144('path', 'num_products', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append('<section id="broken-products" class="card mb-4">\n        ')

                    # <Static value=<ast.Dict object at 0x7f32f444f790> name=None at 7f32f444fc70> -> __attrs_139856821591760
                    __attrs_139856821591760 = _static_139856823252880

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header class="card-header">')
                    __stream_139856823251200 = []
                    __append_139856823251200 = __stream_139856823251200.append
                    __append_139856823251200('Broken add-ons')
                    __msgid_139856823251200 = __re_whitespace(''.join(__stream_139856823251200)).strip()
                    if __msgid_139856823251200:
                        __append(translate(__msgid_139856823251200, mapping=None, default=__msgid_139856823251200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</header>\n        ')

                    # <Static value=<ast.Dict object at 0x7f32f42b9b70> name=None at 7f32f42b9840> -> __attrs_139856821590416
                    __attrs_139856821590416 = _static_139856821590896

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x7f32f42b95d0> name=None at 7f32f42b9570> -> __attrs_139856821589024
                    __attrs_139856821589024 = _static_139856821589456
                    __backup_product_139856821457616 = get('product', __marker)

                    # <Value 'products' (206:34)> -> __iterator
                    __token = 9685
                    try:
                        __zt_tmp = __attrs_139856821589024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139856914196144('path', 'products', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
                    (__iterator, ____index_139856821588784, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821587440
                        __attrs_139856821587440 = _static_139856913889840

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821585664
                        __attrs_139856821585664 = _static_139856913889840

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821586336
                        __default_139856821586336 = _DEFAULT_MARKER

                        # <Value 'product/product_id' (208:33)> -> __cache_139856821586864
                        __token = 9780
                        try:
                            __zt_tmp = __attrs_139856821585664
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856821586864 = _static_139856914196144('path', 'product/product_id', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/product_id' (208:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f42b8910> -> __condition
                        __expression = __cache_139856821586864

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_139856821586864
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x7f32f42b8580> name=None at 7f32f42b8520> -> __attrs_139856821584800
                        __attrs_139856821584800 = _static_139856821585280

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821592864
                        __attrs_139856821592864 = _static_139856913889840

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821592336
                        __default_139856821592336 = _DEFAULT_MARKER

                        # <Value 'product/type' (213:33)> -> __cache_139856821584224
                        __token = 9976
                        try:
                            __zt_tmp = __attrs_139856821592864
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856821584224 = _static_139856914196144('path', 'product/type', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/type' (213:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f42b80d0> -> __condition
                        __expression = __cache_139856821584224

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Type')
                        else:
                            __content = __cache_139856821584224
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n              ')

                        # <Static value=<ast.Dict object at 0x7f32f42ba680> name=None at 7f32f42ba6b0> -> __attrs_139856821594112
                        __attrs_139856821594112 = _static_139856821593728

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> - ')

                        # <Static value=<ast.Dict object at 0x7f32f9abfa30> name=None at 7f32f9abfd60> -> __attrs_139856821595648
                        __attrs_139856821595648 = _static_139856913889840

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __default_139856821595168
                        __default_139856821595168 = _DEFAULT_MARKER

                        # <Value 'product/value' (214:61)> -> __cache_139856821594688
                        __token = 10087
                        try:
                            __zt_tmp = __attrs_139856821595648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139856821594688 = _static_139856914196144('path', 'product/value', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/value' (214:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f32f9a8e050> at 7f32f42bab00> -> __condition
                        __expression = __cache_139856821594688

                        # <Symbol value=<DEFAULT> at 7f32f9a8e050> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Reason')
                        else:
                            __content = __cache_139856821594688
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</em>\n            </div>\n          </li>')
                        ____index_139856821588784 -= 1
                        if (____index_139856821588784 > 0):
                            __append('\n          ')
                    if (__backup_product_139856821457616 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_139856821457616
                    __append('\n        </ul>\n      </section>')
                if (__backup_num_products_139856823138720 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_139856823138720
                if (__backup_products_139856823379152 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_139856823379152
                __append('\n\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_139856823403040
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_139856823413504
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139856914196144('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_139856914195856(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139856872880128 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139856872880128
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }