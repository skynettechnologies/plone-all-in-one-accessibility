# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/Products.CMFPlone-6.0.6-py3.10.egg/Products/CMFPlone/controlpanel/browser/quickinstaller.pt'

__tokens = {1150: ('view/get_upgrades', 35, 36), 1208: (' python:len(products', 36, 39), 1386: ('not:products', 39, 30), 1667: ('products', 43, 27), 1781: ('products', 45, 44), 1822: ('product/id', 46, 30), 2084: ('pid', 50, 44), 2355: ('string:Upgrade ${pid}', 56, 44), 2451: ('product/title', 59, 33), 2648: ('product/description', 64, 39), 2682: ('product/description', 64, 73), 2809: ('pid', 65, 58), 2856: ('product/version', 65, 105), 3022: ('product/upgrade_info', 68, 43), 3237: ('not:upgrade_info/hasProfile', 72, 39), 3419: ('upgrade_info/installedVersion', 74, 77), 3533: ('upgrade_info/hasProfile', 76, 39), 3736: ('upgrade_info/installedVersion', 78, 87), 3993: ('upgrade_info/newVersion', 81, 86), 4133: ('not:upgrade_info/available', 85, 38), 4617: ('python:num_products > 1', 96, 29), 4787: ('products', 98, 51), 4953: ('product/id', 101, 44), 5522: ('view/get_available', 116, 36), 5578: (' python:len(products', 117, 36), 5829: ('products', 121, 34), 5909: ('product/id', 122, 35), 6129: ('pid', 126, 46), 6485: ('product/title', 137, 33), 6682: ('product/description', 142, 39), 6766: ('product/description', 144, 29), 6875: ('pid', 145, 58), 6922: ('product/version', 145, 105), 7091: ('not:product/uninstall_profile', 149, 31), 7389: ('view/get_installed', 158, 36), 7448: (' python:len(products', 159, 39), 7701: ('products', 163, 34), 7781: ('product/id', 164, 35), 7995: ('pid', 168, 42), 8213: ('product/uninstall_profile', 173, 37), 8405: ('product/title', 179, 35), 8612: ('product/description', 184, 41), 8700: ('product/description', 186, 31), 8811: ('pid', 187, 60), 8858: ('product/version', 187, 107), 9032: ('not:product/uninstall_profile', 191, 33), 9331: ('view/get_broken', 200, 36), 9388: (' python:len(products', 201, 40), 9443: ('num_products', 202, 31), 9685: ('products', 206, 34), 9780: ('product/product_id', 208, 33), 9976: ('product/type', 213, 33), 10087: ('product/value', 214, 61), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882100640496 = {'class': 'discreet', }
_static_139882100648368 = {'class': 'configletDescription discreet', }
_static_139882100643760 = {'class': 'list-group-item mt-2 pb-3', }
_static_139882100640208 = {'class': 'configlets list-group list-group-flush', }
_static_139882100604736 = {'class': 'card-header', }
_static_139882206292208 = {'id': 'broken-products', 'class': 'card mb-4', }
_static_139882100598544 = {'class': 'alert alert-info mt-2 mb-0', 'role': 'status', }
_static_139882100588848 = {'class': 'discreet', }
_static_139882100593168 = {'class': 'configletDescription discreet', }
_static_139882101369696 = {'class': 'btn btn-sm btn-danger', 'type': 'submit', 'value': 'Uninstall', 'name': 'form.submitted', }
_static_139882101372000 = {'type': 'hidden', 'name': 'uninstall_product', 'value': 'pid', }
_static_139882206294608 = {'action': 'uninstall_products', 'method': 'post', 'class': 'float-end', }
_static_139882206296960 = {'class': 'list-group-item mt-2 pb-3', }
_static_139882206297344 = {'class': 'configlets list-group list-group-flush', }
_static_139882206296576 = {'class': 'card-header', }
_static_139882101465696 = {'id': 'activated-products', 'class': 'card mb-4', }
_static_139882100926608 = {'class': 'alert alert-warning mt-2 mb-0', 'role': 'status', }
_static_139882100920032 = {'class': 'discreet', }
_static_139882100920896 = {'class': 'configletDescription discreet', }
_static_139882100918352 = {'class': 'btn btn-sm btn-primary', 'type': 'submit', 'value': 'Install', 'name': 'form.submitted', }
_static_139882100923056 = {'type': 'hidden', 'name': 'install_product', 'value': 'pid', }
_static_139882101462192 = {'action': 'install_products', 'method': 'post', 'class': 'float-end', }
_static_139882101460032 = {'class': 'list-group-item mt-2 pb-3', }
_static_139882101463152 = {'class': 'configlets list-group list-group-flush', }
_static_139882101470016 = {'class': 'card-header', }
_static_139882205614464 = {'id': 'install-products', 'class': 'card mb-4', }
_static_139882101470976 = {'class': 'btn btn-primary', 'type': 'submit', 'value': 'Upgrade them ALL!', 'name': 'form.submitted', }
_static_139882205611584 = {'type': 'hidden', 'value': 'product', 'name': 'prefs_reinstallProducts:list', }
_static_139882205616240 = {'action': 'upgrade_products', 'method': 'post', }
_static_139882205651648 = {'class': 'list-group-item mt-2 pb-3', }
_static_139882205655008 = {'class': 'list-group-item mt-2 pb-3', }
_static_139882205644832 = {'class': 'configletDetails list-group list-group-flush', }
_static_139882206232880 = {'class': 'discreet', }
_static_139882206242528 = {'class': 'configletDescription discreet', }
_static_139882205851040 = {'class': 'btn btn-secondary', 'type': 'submit', 'value': 'Upgrade ${pid}', 'name': 'form.submitted', }
_static_139882205848976 = {'type': 'hidden', 'name': 'prefs_reinstallProducts:list', 'value': 'pid', }
_static_139882205855408 = {'action': 'upgrade_products', 'method': 'post', 'class': 'float-end', }
_static_139882205843648 = {'class': 'list-group-item mt-2 pb-3', }
_static_139882205889392 = {'class': 'configlets list-group list-group-flush', }
_static_139882205893088 = {'id': 'up-to-date-message', 'class': 'alert alert-info m-3 mb-0', 'role': 'status', }
_static_139882205902544 = {'class': 'card-header', }
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882205992976 = {'id': 'upgrade-products', 'class': 'card mb-4', }
_static_139882205994608 = {'id': 'content-core', }
_static_139882205997824 = {'href': 'http://docs.plone.org/manage/installing/installing_addons.html', }
_static_139882205996240 = {'class': 'discreet', }
_static_139882205990576 = {'class': 'lead', }
_static_139882206140480 = {'class': 'documentFirstHeading', }
_static_139882206144560 = 'master'
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

            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206144464
            __attrs_139882206144464 = _static_139882337226896
            __backup_macroname_139882237147264 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f38dd352830> name=None at 7f38dd353940> -> __value
            __value = _static_139882206144560
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206146192
                __attrs_139882206146192 = _static_139882337226896
                __previous_i18n_domain_139882206138608 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206149168
                __attrs_139882206149168 = _static_139882337226896

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd351840> name=None at 7f38dd350610> -> __attrs_139882206148688
                __attrs_139882206148688 = _static_139882206140480

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_139882206145184 = []
                __append_139882206145184 = __stream_139882206145184.append
                __append_139882206145184('Add-ons')
                __msgid_139882206145184 = __re_whitespace(''.join(__stream_139882206145184)).strip()
                if __msgid_139882206145184:
                    __append(translate(__msgid_139882206145184, mapping=None, default=__msgid_139882206145184, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd32ceb0> name=None at 7f38dd32e8c0> -> __attrs_139882205987072
                __attrs_139882205987072 = _static_139882205990576

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_139882206000416 = []
                __append_139882206000416 = __stream_139882206000416.append
                __append_139882206000416('\n      This is the Add-on configuration section, you can activate and deactivate\n      add-ons in the lists below.\n    ')
                __msgid_139882206000416 = __re_whitespace(''.join(__stream_139882206000416)).strip()
                if __msgid_139882206000416:
                    __append(translate(__msgid_139882206000416, mapping=None, default=__msgid_139882206000416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd32e4d0> name=None at 7f38dd32e740> -> __attrs_139882205988896
                __attrs_139882205988896 = _static_139882205996240

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="discreet">')
                __stream_139882100477504_third_party_product = ''
                __stream_139882205996000 = []
                __append_139882205996000 = __stream_139882205996000.append
                __append_139882205996000('\n      To make new add-ons show up here, add them to your buildout\n      configuration, run buildout, and restart the server process.\n      For detailed instructions see\n      ')
                __stream_139882100477504_third_party_product = []
                __append_139882100477504_third_party_product = __stream_139882100477504_third_party_product.append

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205995664
                __attrs_139882205995664 = _static_139882337226896

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_139882100477504_third_party_product('<span>\n      ')

                # <Static value=<ast.Dict object at 0x7f38dd32eb00> name=None at 7f38dd32c400> -> __attrs_139882205989136
                __attrs_139882205989136 = _static_139882205997824

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_139882100477504_third_party_product('<a href="http://docs.plone.org/manage/installing/installing_addons.html">')
                __stream_139882205989328 = []
                __append_139882205989328 = __stream_139882205989328.append
                __append_139882205989328('\n        Installing a third party add-on\n      ')
                __msgid_139882205989328 = __re_whitespace(''.join(__stream_139882205989328)).strip()
                if __msgid_139882205989328:
                    __append_139882100477504_third_party_product(translate(__msgid_139882205989328, mapping=None, default=__msgid_139882205989328, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_139882100477504_third_party_product('</a>\n      </span>')
                __append_139882205996000('${third_party_product}')
                __stream_139882100477504_third_party_product = ''.join(__stream_139882100477504_third_party_product)
                __append_139882205996000('.\n    ')
                __msgid_139882205996000 = __re_whitespace(''.join(__stream_139882205996000)).strip()
                if __msgid_139882205996000:
                    __append(translate(__msgid_139882205996000, mapping={'third_party_product': __stream_139882100477504_third_party_product, }, default=__msgid_139882205996000, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x7f38dd32de70> name=None at 7f38dd32db70> -> __attrs_139882206001520
                __attrs_139882206001520 = _static_139882205994608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n\n\n      ')

                # <Static value=<ast.Dict object at 0x7f38dd32d810> name=None at 7f38dd32d1e0> -> __attrs_139882205902832
                __attrs_139882205902832 = _static_139882205992976
                __backup_products_139882206136160 = get('products', __marker)

                # <Value 'view/get_upgrades' (35:36)> -> __value
                __token = 1150
                try:
                    __zt_tmp = __attrs_139882205902832
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/get_upgrades', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_139882206146288 = get('num_products', __marker)

                # <Value 'python:len(products)' (36:39)> -> __value
                __token = 1208
                try:
                    __zt_tmp = __attrs_139882205902832
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('python', 'len(products)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="upgrade-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f38dd3176d0> name=None at 7f38dd317490> -> __attrs_139882205898176
                __attrs_139882205898176 = _static_139882205902544

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_139882205891264 = []
                __append_139882205891264 = __stream_139882205891264.append
                __append_139882205891264('Upgrades')
                __msgid_139882205891264 = __re_whitespace(''.join(__stream_139882205891264)).strip()
                if __msgid_139882205891264:
                    __append(translate(__msgid_139882205891264, mapping=None, default=__msgid_139882205891264, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n          ')

                # <Static value=<ast.Dict object at 0x7f38dd3151e0> name=None at 7f38dd317b20> -> __attrs_139882205892800
                __attrs_139882205892800 = _static_139882205893088

                # <Value 'not:products' (39:30)> -> __condition
                __token = 1386
                try:
                    __zt_tmp = __attrs_139882205892800
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('not', 'products', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="up-to-date-message" class="alert alert-info m-3 mb-0" role="status">\n            ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205890880
                    __attrs_139882205890880 = _static_139882337226896

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139882205892848 = []
                    __append_139882205892848 = __stream_139882205892848.append
                    __append_139882205892848('No upgrades in this corner.')
                    __msgid_139882205892848 = __re_whitespace(''.join(__stream_139882205892848)).strip()
                    if __msgid_139882205892848:
                        __append(translate(__msgid_139882205892848, mapping=None, default=__msgid_139882205892848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n            ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205891648
                    __attrs_139882205891648 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139882205904272 = []
                    __append_139882205904272 = __stream_139882205904272.append
                    __append_139882205904272('You are up to date. High fives.')
                    __msgid_139882205904272 = __re_whitespace(''.join(__stream_139882205904272)).strip()
                    if __msgid_139882205904272:
                        __append(translate(__msgid_139882205904272, mapping=None, default=__msgid_139882205904272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n          </div>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f38dd314370> name=None at 7f38dd317df0> -> __attrs_139882205849504
                __attrs_139882205849504 = _static_139882205889392

                # <Value 'products' (43:27)> -> __condition
                __token = 1667
                try:
                    __zt_tmp = __attrs_139882205849504
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'products', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205849216
                    __attrs_139882205849216 = _static_139882337226896
                    __backup_product_139882205987792 = get('product', __marker)

                    # <Value 'products' (45:44)> -> __iterator
                    __token = 1781
                    try:
                        __zt_tmp = __attrs_139882205849216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139882257081264('path', 'products', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    (__iterator, ____index_139882205845136, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7f38dd3090c0> name=None at 7f38dd30b010> -> __attrs_139882205849360
                        __attrs_139882205849360 = _static_139882205843648
                        __backup_pid_139882205893952 = get('pid', __marker)

                        # <Value 'product/id' (46:30)> -> __value
                        __token = 1822
                        try:
                            __zt_tmp = __attrs_139882205849360
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139882257081264('path', 'product/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        econtext['pid'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f38dd30beb0> name=None at 7f38dd3089d0> -> __attrs_139882205841056
                        __attrs_139882205841056 = _static_139882205855408

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post" class="float-end">\n              ')

                        # <Static value=<ast.Dict object at 0x7f38dd30a590> name=None at 7f38dd30abf0> -> __attrs_139882205848016
                        __attrs_139882205848016 = _static_139882205848976

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="prefs_reinstallProducts:list"')

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205847392
                        __default_139882205847392 = _DEFAULT_MARKER

                        # <Substitution 'pid' (50:44)> -> __attr_value
                        __token = 2084
                        try:
                            __zt_tmp = __attrs_139882205848016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139882257081264('path', 'pid', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x7f38dd30ada0> name=None at 7f38ddba39d0> -> __attrs_139882206235712
                        __attrs_139882206235712 = _static_139882205851040

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-secondary" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205843840
                        __default_139882205843840 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<Substitution 'string:Upgrade ${pid}' (56:44)> at 7f38dd30ba30> -> __attr_value

                        # <Substitution 'string:Upgrade ${pid}' (56:44)> -> __attr_value
                        __token = 2355
                        try:
                            __zt_tmp = __attrs_139882206235712
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139882257081264('string', 'Upgrade ${pid}', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', 'Upgrade ${pid}', _DEFAULT_MARKER)
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted"/>\n            </form>\n            ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206244256
                        __attrs_139882206244256 = _static_139882337226896

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206232928
                        __attrs_139882206232928 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206246560
                        __default_139882206246560 = _DEFAULT_MARKER

                        # <Value 'product/title' (59:33)> -> __cache_139882206238832
                        __token = 2451
                        try:
                            __zt_tmp = __attrs_139882206232928
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882206238832 = _static_139882257081264('path', 'product/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/title' (59:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd368e50> -> __condition
                        __expression = __cache_139882206238832

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_139882206238832
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x7f38dd36a6e0> name=None at 7f38dd3683d0> -> __attrs_139882206237536
                        __attrs_139882206237536 = _static_139882206242528

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206242720
                        __attrs_139882206242720 = _static_139882337226896

                        # <Value 'product/description' (64:39)> -> __condition
                        __token = 2648
                        try:
                            __zt_tmp = __attrs_139882206242720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('path', 'product/description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206239648
                            __default_139882206239648 = _DEFAULT_MARKER

                            # <Value 'product/description' (64:73)> -> __cache_139882206248528
                            __token = 2682
                            try:
                                __zt_tmp = __attrs_139882206242720
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139882206248528 = _static_139882257081264('path', 'product/description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                            # <BinOp left=<Value 'product/description' (64:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd369a50> -> __condition
                            __expression = __cache_139882206248528

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('add-on description')
                            else:
                                __content = __cache_139882206248528
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f38dd368130> name=None at 7f38dd3685b0> -> __attrs_139882206238400
                        __attrs_139882206238400 = _static_139882206232880

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> – (')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206239936
                        __attrs_139882206239936 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206238736
                        __default_139882206238736 = _DEFAULT_MARKER

                        # <Value 'pid' (65:58)> -> __cache_139882206239360
                        __token = 2809
                        try:
                            __zt_tmp = __attrs_139882206239936
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882206239360 = _static_139882257081264('path', 'pid', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pid' (65:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd36b790> -> __condition
                        __expression = __cache_139882206239360

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>plugin.app.name</span>')
                        else:
                            __content = __cache_139882206239360
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(' ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206238160
                        __attrs_139882206238160 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206244688
                        __default_139882206244688 = _DEFAULT_MARKER

                        # <Value 'product/version' (65:105)> -> __cache_139882206248864
                        __token = 2856
                        try:
                            __zt_tmp = __attrs_139882206238160
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882206248864 = _static_139882257081264('path', 'product/version', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/version' (65:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd368f40> -> __condition
                        __expression = __cache_139882206248864

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>1.0</span>')
                        else:
                            __content = __cache_139882206248864
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(')</em>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x7f38dd2d8820> name=None at 7f38dd369db0> -> __attrs_139882205652128
                        __attrs_139882205652128 = _static_139882205644832

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="configletDetails list-group list-group-flush">\n              ')

                        # <Static value=<ast.Dict object at 0x7f38dd2dafe0> name=None at 7f38dd2d9d80> -> __attrs_139882205656928
                        __attrs_139882205656928 = _static_139882205655008
                        __backup_upgrade_info_139882205840336 = get('upgrade_info', __marker)

                        # <Value 'product/upgrade_info' (68:43)> -> __value
                        __token = 3022
                        try:
                            __zt_tmp = __attrs_139882205656928
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139882257081264('path', 'product/upgrade_info', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        econtext['upgrade_info'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n                  ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205648816
                        __attrs_139882205648816 = _static_139882337226896

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_139882205643728 = []
                        __append_139882205643728 = __stream_139882205643728.append
                        __append_139882205643728('\n                    This addon has been upgraded.\n                  ')
                        __msgid_139882205643728 = __re_whitespace(''.join(__stream_139882205643728)).strip()
                        if __msgid_139882205643728:
                            __append(translate(__msgid_139882205643728, mapping=None, default=__msgid_139882205643728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205651600
                        __attrs_139882205651600 = _static_139882337226896

                        # <Value 'not:upgrade_info/hasProfile' (72:39)> -> __condition
                        __token = 3237
                        try:
                            __zt_tmp = __attrs_139882205651600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('not', 'upgrade_info/hasProfile', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_139882100479296_version = ''
                            __stream_139882205658800 = []
                            __append_139882205658800 = __stream_139882205658800.append
                            __append_139882205658800('\n                    Old version was ')
                            __stream_139882100479296_version = []
                            __append_139882100479296_version = __stream_139882100479296_version.append

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205655488
                            __attrs_139882205655488 = _static_139882337226896

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_139882100479296_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205649680
                            __default_139882205649680 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (74:77)> -> __cache_139882205646704
                            __token = 3419
                            try:
                                __zt_tmp = __attrs_139882205655488
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139882205646704 = _static_139882257081264('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (74:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2db340> -> __condition
                            __expression = __cache_139882205646704

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_139882100479296_version('version')
                            else:
                                __content = __cache_139882205646704
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_139882100479296_version(__content)
                            __append_139882100479296_version('</strong>')
                            __append_139882205658800('${version}')
                            __stream_139882100479296_version = ''.join(__stream_139882100479296_version)
                            __append_139882205658800('.\n                  ')
                            __msgid_139882205658800 = __re_whitespace(''.join(__stream_139882205658800)).strip()
                            if 'label_product_upgrade_old_version':
                                __append(translate('label_product_upgrade_old_version', mapping={'version': __stream_139882100479296_version, }, default=__msgid_139882205658800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205646992
                        __attrs_139882205646992 = _static_139882337226896

                        # <Value 'upgrade_info/hasProfile' (76:39)> -> __condition
                        __token = 3533
                        try:
                            __zt_tmp = __attrs_139882205646992
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('path', 'upgrade_info/hasProfile', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205981008
                            __attrs_139882205981008 = _static_139882337226896
                            __stream_139882100479744_version = ''
                            __stream_139882205646896 = []
                            __append_139882205646896 = __stream_139882205646896.append
                            __append_139882205646896('\n                      Old profile version was ')
                            __stream_139882100479744_version = []
                            __append_139882100479744_version = __stream_139882100479744_version.append

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205617104
                            __attrs_139882205617104 = _static_139882337226896

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_139882100479744_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205611296
                            __default_139882205611296 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (78:87)> -> __cache_139882205921824
                            __token = 3736
                            try:
                                __zt_tmp = __attrs_139882205617104
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139882205921824 = _static_139882257081264('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (78:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd31caf0> -> __condition
                            __expression = __cache_139882205921824

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_139882100479744_version('version')
                            else:
                                __content = __cache_139882205921824
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_139882100479744_version(__content)
                            __append_139882100479744_version('</strong>')
                            __append_139882205646896('${version}')
                            __stream_139882100479744_version = ''.join(__stream_139882100479744_version)
                            __append_139882205646896('.\n                    ')
                            __msgid_139882205646896 = __re_whitespace(''.join(__stream_139882205646896)).strip()
                            if 'label_product_upgrade_old_profile_version':
                                __append(translate('label_product_upgrade_old_profile_version', mapping={'version': __stream_139882100479744_version, }, default=__msgid_139882205646896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205624976
                            __attrs_139882205624976 = _static_139882337226896
                            __stream_139882100479744_version = ''
                            __stream_139882205972224 = []
                            __append_139882205972224 = __stream_139882205972224.append
                            __append_139882205972224('\n                      New profile version is ')
                            __stream_139882100479744_version = []
                            __append_139882100479744_version = __stream_139882100479744_version.append

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205626272
                            __attrs_139882205626272 = _static_139882337226896

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_139882100479744_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205622192
                            __default_139882205622192 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/newVersion' (81:86)> -> __cache_139882205616048
                            __token = 3993
                            try:
                                __zt_tmp = __attrs_139882205626272
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139882205616048 = _static_139882257081264('path', 'upgrade_info/newVersion', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/newVersion' (81:86)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd2d3010> -> __condition
                            __expression = __cache_139882205616048

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_139882100479744_version('version')
                            else:
                                __content = __cache_139882205616048
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_139882100479744_version(__content)
                            __append_139882100479744_version('</strong>')
                            __append_139882205972224('${version}')
                            __stream_139882100479744_version = ''.join(__stream_139882100479744_version)
                            __append_139882205972224('.\n                    ')
                            __msgid_139882205972224 = __re_whitespace(''.join(__stream_139882205972224)).strip()
                            if 'label_product_upgrade_new_profile_version':
                                __append(translate('label_product_upgrade_new_profile_version', mapping={'version': __stream_139882100479744_version, }, default=__msgid_139882205972224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                  </span>')
                        __append('\n\n                  ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205615232
                        __attrs_139882205615232 = _static_139882337226896

                        # <Value 'not:upgrade_info/available' (85:38)> -> __condition
                        __token = 4133
                        try:
                            __zt_tmp = __attrs_139882205615232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('not', 'upgrade_info/available', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205624448
                            __attrs_139882205624448 = _static_139882337226896

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')
                            __stream_139882205621136 = []
                            __append_139882205621136 = __stream_139882205621136.append
                            __append_139882205621136('Warning')
                            __msgid_139882205621136 = __re_whitespace(''.join(__stream_139882205621136)).strip()
                            if __msgid_139882205621136:
                                __append(translate(__msgid_139882205621136, mapping=None, default=__msgid_139882205621136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</strong>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205622048
                            __attrs_139882205622048 = _static_139882337226896

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_139882205617488 = []
                            __append_139882205617488 = __stream_139882205617488.append
                            __append_139882205617488('There is no upgrade procedure defined for this\n                    addon. Please consult the addon documentation\n                    for upgrade information, or contact the addon\n                    author.')
                            __msgid_139882205617488 = __re_whitespace(''.join(__stream_139882205617488)).strip()
                            if __msgid_139882205617488:
                                __append(translate(__msgid_139882205617488, mapping=None, default=__msgid_139882205617488, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>\n                  </div>')
                        __append('\n              </li>')
                        if (__backup_upgrade_info_139882205840336 is __marker):
                            del econtext['upgrade_info']
                        else:
                            econtext['upgrade_info'] = __backup_upgrade_info_139882205840336
                        __append('\n            </ul>\n          </li>')
                        if (__backup_pid_139882205893952 is __marker):
                            del econtext['pid']
                        else:
                            econtext['pid'] = __backup_pid_139882205893952
                        __append('\n          ')
                        ____index_139882205845136 -= 1
                        if (____index_139882205845136 > 0):
                            __append('')
                    if (__backup_product_139882205987792 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_139882205987792
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f38dd2da2c0> name=None at 7f38dd2d83a0> -> __attrs_139882205617200
                    __attrs_139882205617200 = _static_139882205651648

                    # <Value 'python:num_products > 1' (96:29)> -> __condition
                    __token = 4617
                    try:
                        __zt_tmp = __attrs_139882205617200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('python', 'num_products > 1', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f38dd2d1870> name=None at 7f38dd2d20e0> -> __attrs_139882205619072
                        __attrs_139882205619072 = _static_139882205616240

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post">\n                ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205613264
                        __attrs_139882205613264 = _static_139882337226896
                        __backup_product_139882206245744 = get('product', __marker)

                        # <Value 'products' (98:51)> -> __iterator
                        __token = 4787
                        try:
                            __zt_tmp = __attrs_139882205613264
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_139882257081264('path', 'products', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        (__iterator, ____index_139882205614800, ) = getname('repeat')('product', __iterator)
                        econtext['product'] = None
                        for __item in __iterator:
                            econtext['product'] = __item
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x7f38dd2d0640> name=None at 7f38dd2d0eb0> -> __attrs_139882101090640
                            __attrs_139882101090640 = _static_139882205611584

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden"')

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206039776
                            __default_139882206039776 = _DEFAULT_MARKER

                            # <Substitution 'product/id' (101:44)> -> __attr_value
                            __token = 4953
                            try:
                                __zt_tmp = __attrs_139882101090640
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_139882257081264('path', 'product/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'product', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' name="prefs_reinstallProducts:list" />\n                ')
                            ____index_139882205614800 -= 1
                            if (____index_139882205614800 > 0):
                                __append('')
                        if (__backup_product_139882206245744 is __marker):
                            del econtext['product']
                        else:
                            econtext['product'] = __backup_product_139882206245744
                        __append('\n                ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101091072
                        __attrs_139882101091072 = _static_139882337226896

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101459264
                        __attrs_139882101459264 = _static_139882337226896

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>')
                        __stream_139882101083008 = []
                        __append_139882101083008 = __stream_139882101083008.append
                        __append_139882101083008('This can be risky, are you sure you want to do this?')
                        __msgid_139882101083008 = __re_whitespace(''.join(__stream_139882101083008)).strip()
                        if 'label_product_upgrade_all_action':
                            __append(translate('label_product_upgrade_all_action', mapping=None, default=__msgid_139882101083008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f38d6f7f700> name=None at 7f38d6f7ddb0> -> __attrs_139882101472128
                        __attrs_139882101472128 = _static_139882101470976

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101462864
                        __default_139882101462864 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<ast.Constant object at 0x7f38d6f7cb50> at 7f38d6f7df00> -> __attr_value
                        __attr_value = 'Upgrade them ALL!'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted" />\n                </span>\n            </form>\n            </li>')
                    __append('\n          </ul>')
                __append('\n      </section>')
                if (__backup_num_products_139882206146288 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_139882206146288
                if (__backup_products_139882206136160 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_139882206136160
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f38dd2d1180> name=None at 7f38d6f21600> -> __attrs_139882101468672
                __attrs_139882101468672 = _static_139882205614464
                __backup_products_139882206137648 = get('products', __marker)

                # <Value 'view/get_available' (116:36)> -> __value
                __token = 5522
                try:
                    __zt_tmp = __attrs_139882101468672
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/get_available', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_139882205988416 = get('num_products', __marker)

                # <Value 'python:len(products)' (117:36)> -> __value
                __token = 5578
                try:
                    __zt_tmp = __attrs_139882101468672
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('python', 'len(products)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="install-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f38d6f7f340> name=None at 7f38d6f7ca30> -> __attrs_139882101473136
                __attrs_139882101473136 = _static_139882101470016

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_139882101471072 = []
                __append_139882101471072 = __stream_139882101471072.append
                __append_139882101471072('Available add-ons')
                __msgid_139882101471072 = __re_whitespace(''.join(__stream_139882101471072)).strip()
                if __msgid_139882101471072:
                    __append(translate(__msgid_139882101471072, mapping=None, default=__msgid_139882101471072, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x7f38d6f7d870> name=None at 7f38d6f7f370> -> __attrs_139882101464688
                __attrs_139882101464688 = _static_139882101463152

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x7f38d6f7cc40> name=None at 7f38d6f7f040> -> __attrs_139882101471024
                __attrs_139882101471024 = _static_139882101460032
                __backup_product_139882205847776 = get('product', __marker)

                # <Value 'products' (121:34)> -> __iterator
                __token = 5829
                try:
                    __zt_tmp = __attrs_139882101471024
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139882257081264('path', 'products', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                (__iterator, ____index_139882101462048, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101469344
                    __attrs_139882101469344 = _static_139882337226896
                    __backup_pid_139882205846576 = get('pid', __marker)

                    # <Value 'product/id' (122:35)> -> __value
                    __token = 5909
                    try:
                        __zt_tmp = __attrs_139882101469344
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139882257081264('path', 'product/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f38d6f7d4b0> name=None at 7f38d6f7de10> -> __attrs_139882100917920
                    __attrs_139882100917920 = _static_139882101462192

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="install_products" method="post" class="float-end">\n                ')

                    # <Static value=<ast.Dict object at 0x7f38d6ef9ab0> name=None at 7f38d6ef9ba0> -> __attrs_139882100925936
                    __attrs_139882100925936 = _static_139882100923056

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="install_product"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100923488
                    __default_139882100923488 = _DEFAULT_MARKER

                    # <Substitution 'pid' (126:46)> -> __attr_value
                    __token = 6129
                    try:
                        __zt_tmp = __attrs_139882100925936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139882257081264('path', 'pid', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x7f38d6ef8850> name=None at 7f38d6efb790> -> __attrs_139882100928576
                    __attrs_139882100928576 = _static_139882100918352

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-sm btn-primary" type="submit" value="Install" name="form.submitted">')
                    __stream_139882100929776 = []
                    __append_139882100929776 = __stream_139882100929776.append
                    __append_139882100929776('\n                    Install\n                ')
                    __msgid_139882100929776 = __re_whitespace(''.join(__stream_139882100929776)).strip()
                    if __msgid_139882100929776:
                        __append(translate(__msgid_139882100929776, mapping=None, default=__msgid_139882100929776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100931840
                    __attrs_139882100931840 = _static_139882337226896

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n              ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100924688
                    __attrs_139882100924688 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100921040
                    __default_139882100921040 = _DEFAULT_MARKER

                    # <Value 'product/title' (137:33)> -> __cache_139882100931120
                    __token = 6485
                    try:
                        __zt_tmp = __attrs_139882100924688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100931120 = _static_139882257081264('path', 'product/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (137:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6ef93f0> -> __condition
                    __expression = __cache_139882100931120

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                Add-on Name\n              </span>')
                    else:
                        __content = __cache_139882100931120
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            </h3>\n            ')

                    # <Static value=<ast.Dict object at 0x7f38d6ef9240> name=None at 7f38d6efa1d0> -> __attrs_139882100918448
                    __attrs_139882100918448 = _static_139882100920896

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n              ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100932032
                    __attrs_139882100932032 = _static_139882337226896

                    # <Value 'product/description' (142:39)> -> __condition
                    __token = 6682
                    try:
                        __zt_tmp = __attrs_139882100932032
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('path', 'product/description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100925552
                        __default_139882100925552 = _DEFAULT_MARKER

                        # <Value 'product/description' (144:29)> -> __cache_139882100931408
                        __token = 6766
                        try:
                            __zt_tmp = __attrs_139882100932032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882100931408 = _static_139882257081264('path', 'product/description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (144:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6ef9e70> -> __condition
                        __expression = __cache_139882100931408

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_139882100931408
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7f38d6ef8ee0> name=None at 7f38d6efaef0> -> __attrs_139882100927568
                    __attrs_139882100927568 = _static_139882100920032

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100919408
                    __attrs_139882100919408 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100917200
                    __default_139882100917200 = _DEFAULT_MARKER

                    # <Value 'pid' (145:58)> -> __cache_139882100917248
                    __token = 6875
                    try:
                        __zt_tmp = __attrs_139882100919408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100917248 = _static_139882257081264('path', 'pid', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (145:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6ef8190> -> __condition
                    __expression = __cache_139882100917248

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_139882100917248
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100923968
                    __attrs_139882100923968 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100916816
                    __default_139882100916816 = _DEFAULT_MARKER

                    # <Value 'product/version' (145:105)> -> __cache_139882100916720
                    __token = 6922
                    try:
                        __zt_tmp = __attrs_139882100923968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100916720 = _static_139882257081264('path', 'product/version', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (145:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6efb190> -> __condition
                    __expression = __cache_139882100916720

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_139882100916720
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n            </div>\n            ')

                    # <Static value=<ast.Dict object at 0x7f38d6efa890> name=None at 7f38d6efa560> -> __attrs_139882206290528
                    __attrs_139882206290528 = _static_139882100926608

                    # <Value 'not:product/uninstall_profile' (149:31)> -> __condition
                    __token = 7091
                    try:
                        __zt_tmp = __attrs_139882206290528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('not', 'product/uninstall_profile', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-warning mt-2 mb-0" role="status">\n              ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206288032
                        __attrs_139882206288032 = _static_139882337226896

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_139882206287168 = []
                        __append_139882206287168 = __stream_139882206287168.append
                        __append_139882206287168('Warning')
                        __msgid_139882206287168 = __re_whitespace(''.join(__stream_139882206287168)).strip()
                        if __msgid_139882206287168:
                            __append(translate(__msgid_139882206287168, mapping=None, default=__msgid_139882206287168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n              ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206287360
                        __attrs_139882206287360 = _static_139882337226896

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_139882206284528 = []
                        __append_139882206284528 = __stream_139882206284528.append
                        __append_139882206284528('This product cannot be uninstalled!')
                        __msgid_139882206284528 = __re_whitespace(''.join(__stream_139882206284528)).strip()
                        if __msgid_139882206284528:
                            __append(translate(__msgid_139882206284528, mapping=None, default=__msgid_139882206284528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_139882205846576 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_139882205846576
                    __append('\n          </li>')
                    ____index_139882101462048 -= 1
                    if (____index_139882101462048 > 0):
                        __append('\n          ')
                if (__backup_product_139882205847776 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_139882205847776
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_139882205988416 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_139882205988416
                if (__backup_products_139882206137648 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_139882206137648
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f38d6f7e260> name=None at 7f38d6efbc70> -> __attrs_139882206286784
                __attrs_139882206286784 = _static_139882101465696
                __backup_products_139882205987120 = get('products', __marker)

                # <Value 'view/get_installed' (158:36)> -> __value
                __token = 7389
                try:
                    __zt_tmp = __attrs_139882206286784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/get_installed', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_139882205891024 = get('num_products', __marker)

                # <Value 'python:len(products)' (159:39)> -> __value
                __token = 7448
                try:
                    __zt_tmp = __attrs_139882206286784
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('python', 'len(products)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="activated-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f38dd377a00> name=None at 7f38dd374d90> -> __attrs_139882206296768
                __attrs_139882206296768 = _static_139882206296576

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_139882206282896 = []
                __append_139882206282896 = __stream_139882206282896.append
                __append_139882206282896('Activated add-ons')
                __msgid_139882206282896 = __re_whitespace(''.join(__stream_139882206282896)).strip()
                if __msgid_139882206282896:
                    __append(translate(__msgid_139882206282896, mapping=None, default=__msgid_139882206282896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x7f38dd377d00> name=None at 7f38dd375360> -> __attrs_139882206285152
                __attrs_139882206285152 = _static_139882206297344

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x7f38dd377b80> name=None at 7f38dd374a00> -> __attrs_139882206283904
                __attrs_139882206283904 = _static_139882206296960
                __backup_product_139882205649584 = get('product', __marker)

                # <Value 'products' (163:34)> -> __iterator
                __token = 7701
                try:
                    __zt_tmp = __attrs_139882206283904
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139882257081264('path', 'products', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                (__iterator, ____index_139882206285968, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206297680
                    __attrs_139882206297680 = _static_139882337226896
                    __backup_pid_139882206246128 = get('pid', __marker)

                    # <Value 'product/id' (164:35)> -> __value
                    __token = 7781
                    try:
                        __zt_tmp = __attrs_139882206297680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139882257081264('path', 'product/id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f38dd377250> name=None at 7f38dd374250> -> __attrs_139882101362208
                    __attrs_139882101362208 = _static_139882206294608

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="uninstall_products" method="post" class="float-end">\n              ')

                    # <Static value=<ast.Dict object at 0x7f38d6f67460> name=None at 7f38d6f64520> -> __attrs_139882101360816
                    __attrs_139882101360816 = _static_139882101372000

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="uninstall_product"')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882101370320
                    __default_139882101370320 = _DEFAULT_MARKER

                    # <Substitution 'pid' (168:42)> -> __attr_value
                    __token = 7995
                    try:
                        __zt_tmp = __attrs_139882101360816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139882257081264('path', 'pid', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n              ')

                    # <Static value=<ast.Dict object at 0x7f38d6f66b60> name=None at 7f38d6f65d20> -> __attrs_139882101362496
                    __attrs_139882101362496 = _static_139882101369696

                    # <Value 'product/uninstall_profile' (173:37)> -> __condition
                    __token = 8213
                    try:
                        __zt_tmp = __attrs_139882101362496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('path', 'product/uninstall_profile', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button class="btn btn-sm btn-danger" type="submit" value="Uninstall" name="form.submitted">')
                        __stream_139882101365568 = []
                        __append_139882101365568 = __stream_139882101365568.append
                        __append_139882101365568('\n                Uninstall\n              ')
                        __msgid_139882101365568 = __re_whitespace(''.join(__stream_139882101365568)).strip()
                        if __msgid_139882101365568:
                            __append(translate(__msgid_139882101365568, mapping=None, default=__msgid_139882101365568, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>')
                    __append('\n            </form>\n              ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882101369024
                    __attrs_139882101369024 = _static_139882337226896

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n                ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100591200
                    __attrs_139882100591200 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100591536
                    __default_139882100591536 = _DEFAULT_MARKER

                    # <Value 'product/title' (179:35)> -> __cache_139882100600896
                    __token = 8405
                    try:
                        __zt_tmp = __attrs_139882100591200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100600896 = _static_139882257081264('path', 'product/title', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (179:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6eaa500> -> __condition
                    __expression = __cache_139882100600896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  Add-on Name\n                </span>')
                    else:
                        __content = __cache_139882100600896
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n              </h3>\n              ')

                    # <Static value=<ast.Dict object at 0x7f38d6ea9210> name=None at 7f38d6ea8310> -> __attrs_139882100597632
                    __attrs_139882100597632 = _static_139882100593168

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n                ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100596384
                    __attrs_139882100596384 = _static_139882337226896

                    # <Value 'product/description' (184:41)> -> __condition
                    __token = 8612
                    try:
                        __zt_tmp = __attrs_139882100596384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('path', 'product/description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100597056
                        __default_139882100597056 = _DEFAULT_MARKER

                        # <Value 'product/description' (186:31)> -> __cache_139882100593024
                        __token = 8700
                        try:
                            __zt_tmp = __attrs_139882100596384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882100593024 = _static_139882257081264('path', 'product/description', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (186:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6ea8220> -> __condition
                        __expression = __cache_139882100593024

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_139882100593024
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f38d6ea8130> name=None at 7f38d6ea87c0> -> __attrs_139882100594512
                    __attrs_139882100594512 = _static_139882100588848

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100594944
                    __attrs_139882100594944 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100589952
                    __default_139882100589952 = _DEFAULT_MARKER

                    # <Value 'pid' (187:60)> -> __cache_139882100589712
                    __token = 8811
                    try:
                        __zt_tmp = __attrs_139882100594944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100589712 = _static_139882257081264('path', 'pid', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (187:60)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6eab8b0> -> __condition
                    __expression = __cache_139882100589712

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_139882100589712
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100600224
                    __attrs_139882100600224 = _static_139882337226896

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100592448
                    __default_139882100592448 = _DEFAULT_MARKER

                    # <Value 'product/version' (187:107)> -> __cache_139882100592880
                    __token = 8858
                    try:
                        __zt_tmp = __attrs_139882100600224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882100592880 = _static_139882257081264('path', 'product/version', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (187:107)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6ea8df0> -> __condition
                    __expression = __cache_139882100592880

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_139882100592880
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n              </div>\n              ')

                    # <Static value=<ast.Dict object at 0x7f38d6eaa710> name=None at 7f38d6eab0a0> -> __attrs_139882100598592
                    __attrs_139882100598592 = _static_139882100598544

                    # <Value 'not:product/uninstall_profile' (191:33)> -> __condition
                    __token = 9032
                    try:
                        __zt_tmp = __attrs_139882100598592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('not', 'product/uninstall_profile', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-info mt-2 mb-0" role="status">\n                ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100595040
                        __attrs_139882100595040 = _static_139882337226896

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_139882100602432 = []
                        __append_139882100602432 = __stream_139882100602432.append
                        __append_139882100602432('Info')
                        __msgid_139882100602432 = __re_whitespace(''.join(__stream_139882100602432)).strip()
                        if __msgid_139882100602432:
                            __append(translate(__msgid_139882100602432, mapping=None, default=__msgid_139882100602432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n                ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100599168
                        __attrs_139882100599168 = _static_139882337226896

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_139882100593312 = []
                        __append_139882100593312 = __stream_139882100593312.append
                        __append_139882100593312('This product cannot be uninstalled!')
                        __msgid_139882100593312 = __re_whitespace(''.join(__stream_139882100593312)).strip()
                        if __msgid_139882100593312:
                            __append(translate(__msgid_139882100593312, mapping=None, default=__msgid_139882100593312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_139882206246128 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_139882206246128
                    __append('\n          </li>')
                    ____index_139882206285968 -= 1
                    if (____index_139882206285968 > 0):
                        __append('\n          ')
                if (__backup_product_139882205649584 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_139882205649584
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_139882205891024 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_139882205891024
                if (__backup_products_139882205987120 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_139882205987120
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f38dd3768f0> name=None at 7f38dd375ae0> -> __attrs_139882100595280
                __attrs_139882100595280 = _static_139882206292208
                __backup_products_139882206001184 = get('products', __marker)

                # <Value 'view/get_broken' (200:36)> -> __value
                __token = 9331
                try:
                    __zt_tmp = __attrs_139882100595280
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/get_broken', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_139882205851376 = get('num_products', __marker)

                # <Value 'python:len(products)' (201:40)> -> __value
                __token = 9388
                try:
                    __zt_tmp = __attrs_139882100595280
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('python', 'len(products)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value 'num_products' (202:31)> -> __condition
                __token = 9443
                try:
                    __zt_tmp = __attrs_139882100595280
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'num_products', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append('<section id="broken-products" class="card mb-4">\n        ')

                    # <Static value=<ast.Dict object at 0x7f38d6eabf40> name=None at 7f38d6eab100> -> __attrs_139882100641408
                    __attrs_139882100641408 = _static_139882100604736

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header class="card-header">')
                    __stream_139882100598064 = []
                    __append_139882100598064 = __stream_139882100598064.append
                    __append_139882100598064('Broken add-ons')
                    __msgid_139882100598064 = __re_whitespace(''.join(__stream_139882100598064)).strip()
                    if __msgid_139882100598064:
                        __append(translate(__msgid_139882100598064, mapping=None, default=__msgid_139882100598064, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</header>\n        ')

                    # <Static value=<ast.Dict object at 0x7f38d6eb49d0> name=None at 7f38d6eb4880> -> __attrs_139882100643376
                    __attrs_139882100643376 = _static_139882100640208

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x7f38d6eb57b0> name=None at 7f38d6eb4d60> -> __attrs_139882100637760
                    __attrs_139882100637760 = _static_139882100643760
                    __backup_product_139882206287072 = get('product', __marker)

                    # <Value 'products' (206:34)> -> __iterator
                    __token = 9685
                    try:
                        __zt_tmp = __attrs_139882100637760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139882257081264('path', 'products', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    (__iterator, ____index_139882100638576, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100645968
                        __attrs_139882100645968 = _static_139882337226896

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100652256
                        __attrs_139882100652256 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100651728
                        __default_139882100651728 = _DEFAULT_MARKER

                        # <Value 'product/product_id' (208:33)> -> __cache_139882100643712
                        __token = 9780
                        try:
                            __zt_tmp = __attrs_139882100652256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882100643712 = _static_139882257081264('path', 'product/product_id', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/product_id' (208:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6eb6380> -> __condition
                        __expression = __cache_139882100643712

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_139882100643712
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x7f38d6eb69b0> name=None at 7f38d6eb7640> -> __attrs_139882100643856
                        __attrs_139882100643856 = _static_139882100648368

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100649376
                        __attrs_139882100649376 = _static_139882337226896

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100643232
                        __default_139882100643232 = _DEFAULT_MARKER

                        # <Value 'product/type' (213:33)> -> __cache_139882100650768
                        __token = 9976
                        try:
                            __zt_tmp = __attrs_139882100649376
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882100650768 = _static_139882257081264('path', 'product/type', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/type' (213:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6eb7dc0> -> __condition
                        __expression = __cache_139882100650768

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Type')
                        else:
                            __content = __cache_139882100650768
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n              ')

                        # <Static value=<ast.Dict object at 0x7f38d6eb4af0> name=None at 7f38d6eb4b80> -> __attrs_139882100643664
                        __attrs_139882100643664 = _static_139882100640496

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> - ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882100652064
                        __attrs_139882100652064 = _static_139882337226896

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882100644960
                        __default_139882100644960 = _DEFAULT_MARKER

                        # <Value 'product/value' (214:61)> -> __cache_139882100644240
                        __token = 10087
                        try:
                            __zt_tmp = __attrs_139882100652064
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139882100644240 = _static_139882257081264('path', 'product/value', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/value' (214:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38d6eb5360> -> __condition
                        __expression = __cache_139882100644240

                        # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Reason')
                        else:
                            __content = __cache_139882100644240
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</em>\n            </div>\n          </li>')
                        ____index_139882100638576 -= 1
                        if (____index_139882100638576 > 0):
                            __append('\n          ')
                    if (__backup_product_139882206287072 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_139882206287072
                    __append('\n        </ul>\n      </section>')
                if (__backup_num_products_139882205851376 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_139882205851376
                if (__backup_products_139882206001184 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_139882206001184
                __append('\n\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_139882206138608
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_139882206144464
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139882257081264('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139882237147264 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139882237147264
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }