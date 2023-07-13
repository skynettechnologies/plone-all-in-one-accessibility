# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.layout-4.0.6-py3.10.egg/plone/app/layout/viewlets/document_byline.pt'

__tokens = {53: ('view/show', 2, 24), 154: ('here/creators', 6, 30), 206: (' context/@@plone_portal_state/navigation_root_ur', 7, 37), 306: ('python:creator_ids and view.show_about()', 9, 31), 427: ('creator_ids', 12, 29), 493: ('python: view.get_url_path(user_id)', 14, 27), 555: (' python:view.get_fullname(user_id', 15, 26), 761: ('url_path', 19, 26), 699: ('${navigation_root_url}/${url_path}', 18, 17), 701: ('navigation_root_url', 18, 19), 724: ('url_path', 18, 42), 780: ('${fullname}', 20, 9), 782: ('fullname', 20, 11), 900: ('not:url_path', 22, 29), 923: ('${fullname}', 23, 9), 925: ('fullname', 23, 11), 1053: ('view/pub_date', 30, 25), 1091: (' context/ModificationDat', 31, 23), 1154: ('e python:view.show_modification_date', 32, 36), 1271: ('published', 35, 25), 1373: ('python:context.toLocalizedTime(published)', 38, 25), 1452: ('show_modification_date', 38, 104), 1561: ('show_modification_date', 42, 25), 1698: ('python:context.toLocalizedTime(modified)', 47, 25), 1828: ('view/isExpired', 53, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882241831840 = {'class': 'state-expired', }
_static_139882206157632 = {'class': 'documentModified', }
_static_139882206157536 = {'class': 'documentPublished', }
_static_139882205853728 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', }
_static_139882205841776 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', 'href': '${navigation_root_url}/${url_path}', }
_static_139882337226896 = {}
_static_139882257080976 = __C2ZContextWrapper
_static_139882257081264 = __compile_zt_expr
_static_139882205848448 = {'id': 'section-byline', }

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

            # <Static value=<ast.Dict object at 0x7f38dd30a380> name=None at 7f38dd30a320> -> __attrs_139882205853440
            __attrs_139882205853440 = _static_139882205848448

            # <Value 'view/show' (2:24)> -> __condition
            __token = 53
            try:
                __zt_tmp = __attrs_139882205853440
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882257081264('path', 'view/show', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139882205853536 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-byline" >\n  ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205848592
                __attrs_139882205848592 = _static_139882337226896
                __backup_creator_ids_139882205845808 = get('creator_ids', __marker)

                # <Value 'here/creators' (6:30)> -> __value
                __token = 154
                try:
                    __zt_tmp = __attrs_139882205848592
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'here/creators', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['creator_ids'] = __value
                __backup_navigation_root_url_139882205855168 = get('navigation_root_url', __marker)

                # <Value 'context/@@plone_portal_state/navigation_root_url' (7:37)> -> __value
                __token = 206
                try:
                    __zt_tmp = __attrs_139882205848592
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['navigation_root_url'] = __value

                # <Value 'python:creator_ids and view.show_about()' (9:31)> -> __condition
                __token = 306
                try:
                    __zt_tmp = __attrs_139882205848592
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('python', 'creator_ids and view.show_about()', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205852144
                    __attrs_139882205852144 = _static_139882337226896
                    __stream_139882205840432 = []
                    __append_139882205840432 = __stream_139882205840432.append
                    __append_139882205840432('by')
                    __msgid_139882205840432 = __re_whitespace(''.join(__stream_139882205840432)).strip()
                    if __msgid_139882205840432:
                        __append(translate(__msgid_139882205840432, mapping=None, default=__msgid_139882205840432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205847776
                    __attrs_139882205847776 = _static_139882337226896
                    __backup_user_id_139882205849936 = get('user_id', __marker)

                    # <Value 'creator_ids' (12:29)> -> __iterator
                    __token = 427
                    try:
                        __zt_tmp = __attrs_139882205847776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139882257081264('path', 'creator_ids', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    (__iterator, ____index_139882205853776, ) = getname('repeat')('user_id', __iterator)
                    econtext['user_id'] = None
                    for __item in __iterator:
                        econtext['user_id'] = __item
                        __append('\n      ')

                        # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205852096
                        __attrs_139882205852096 = _static_139882337226896
                        __backup_url_path_139882205852480 = get('url_path', __marker)

                        # <Value 'python: view.get_url_path(user_id)' (14:27)> -> __value
                        __token = 493
                        try:
                            __zt_tmp = __attrs_139882205852096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139882257081264('python', ' view.get_url_path(user_id)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        econtext['url_path'] = __value
                        __backup_fullname_139882205845328 = get('fullname', __marker)

                        # <Value 'python:view.get_fullname(user_id)' (15:26)> -> __value
                        __token = 555
                        try:
                            __zt_tmp = __attrs_139882205852096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139882257081264('python', 'view.get_fullname(user_id)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        econtext['fullname'] = __value
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f38dd308970> name=None at 7f38dd309ae0> -> __attrs_139882205855552
                        __attrs_139882205855552 = _static_139882205841776

                        # <Value 'url_path' (19:26)> -> __condition
                        __token = 761
                        try:
                            __zt_tmp = __attrs_139882205855552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('path', 'url_path', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a class="badge rounded-pill bg-light text-dark fw-normal fs-6"')

                            # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882205853632
                            __default_139882205853632 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${navigation_root_url}/${url_path}' (18:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd30bb20> -> __attr_href
                            __token = 699
                            __token = 701
                            try:
                                __zt_tmp = __attrs_139882205855552
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_139882257081264('path', 'navigation_root_url', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __token = 724
                            try:
                                __zt_tmp = __attrs_139882205855552
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href_722 = _static_139882257081264('path', 'url_path', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            __attr_href_722 = __quote(__attr_href_722, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/', (__attr_href_722 if (__attr_href_722 is not None) else ''), ))
                            if (__attr_href is None):
                                pass
                            else:
                                if (__attr_href is _DEFAULT_MARKER):
                                    __attr_href = None
                                else:
                                    __tt = type(__attr_href)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_href = str(__attr_href)
                                    else:
                                        if (__tt is bytes):
                                            __attr_href = decode(__attr_href)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_href = __attr_href.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_href)
                                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                                else:
                                                    __attr_href = __attr_href()
                            if (__attr_href is not None):
                                __append((' href="%s"' % __attr_href))
                            __append(' >')

                            # <Interpolation value=<Substitution '${fullname}' (20:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd308880> -> __content_139882343851824
                            __token = 780
                            __token = 782
                            try:
                                __zt_tmp = __attrs_139882205855552
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_139882343851824 = _static_139882257081264('path', 'fullname', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            __content_139882343851824 = __quote(__content_139882343851824, '\x00', '&#0;', None, None)
                            __content_139882343851824 = __content_139882343851824
                            if (__content_139882343851824 is None):
                                pass
                            else:
                                if (__content_139882343851824 is None):
                                    __content_139882343851824 = None
                                else:
                                    __tt = type(__content_139882343851824)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_139882343851824 = str(__content_139882343851824)
                                    else:
                                        if (__tt is bytes):
                                            __content_139882343851824 = decode(__content_139882343851824)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_139882343851824 = __content_139882343851824.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_139882343851824)
                                                    __content_139882343851824 = (str(__content_139882343851824) if (__content_139882343851824 is __converted) else __converted)
                                                else:
                                                    __content_139882343851824 = __content_139882343851824()
                            if (__content_139882343851824 is not None):
                                __append(__content_139882343851824)
                            __append('</a>')
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f38dd30b820> name=None at 7f38dd30a4d0> -> __attrs_139882206162336
                        __attrs_139882206162336 = _static_139882205853728

                        # <Value 'not:url_path' (22:29)> -> __condition
                        __token = 900
                        try:
                            __zt_tmp = __attrs_139882206162336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139882257081264('not', 'url_path', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge rounded-pill bg-light text-dark fw-normal fs-6" >')

                            # <Interpolation value=<Substitution '${fullname}' (23:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f38dd355630> -> __content_139882343851824
                            __token = 923
                            __token = 925
                            try:
                                __zt_tmp = __attrs_139882206162336
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_139882343851824 = _static_139882257081264('path', 'fullname', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                            __content_139882343851824 = __quote(__content_139882343851824, '\x00', '&#0;', None, None)
                            __content_139882343851824 = __content_139882343851824
                            if (__content_139882343851824 is None):
                                pass
                            else:
                                if (__content_139882343851824 is None):
                                    __content_139882343851824 = None
                                else:
                                    __tt = type(__content_139882343851824)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_139882343851824 = str(__content_139882343851824)
                                    else:
                                        if (__tt is bytes):
                                            __content_139882343851824 = decode(__content_139882343851824)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_139882343851824 = __content_139882343851824.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_139882343851824)
                                                    __content_139882343851824 = (str(__content_139882343851824) if (__content_139882343851824 is __converted) else __converted)
                                                else:
                                                    __content_139882343851824 = __content_139882343851824()
                            if (__content_139882343851824 is not None):
                                __append(__content_139882343851824)
                            __append('</span>')
                        __append('\n      ')
                        if (__backup_fullname_139882205845328 is __marker):
                            del econtext['fullname']
                        else:
                            econtext['fullname'] = __backup_fullname_139882205845328
                        if (__backup_url_path_139882205852480 is __marker):
                            del econtext['url_path']
                        else:
                            econtext['url_path'] = __backup_url_path_139882205852480
                        __append('\n    ')
                        ____index_139882205853776 -= 1
                        if (____index_139882205853776 > 0):
                            __append('')
                    if (__backup_user_id_139882205849936 is __marker):
                        del econtext['user_id']
                    else:
                        econtext['user_id'] = __backup_user_id_139882205849936
                    __append('\n    &mdash;\n  ')
                if (__backup_navigation_root_url_139882205855168 is __marker):
                    del econtext['navigation_root_url']
                else:
                    econtext['navigation_root_url'] = __backup_navigation_root_url_139882205855168
                if (__backup_creator_ids_139882205845808 is __marker):
                    del econtext['creator_ids']
                else:
                    econtext['creator_ids'] = __backup_creator_ids_139882205845808
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882205841344
                __attrs_139882205841344 = _static_139882337226896
                __backup_published_139882205839712 = get('published', __marker)

                # <Value 'view/pub_date' (30:25)> -> __value
                __token = 1053
                try:
                    __zt_tmp = __attrs_139882205841344
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'view/pub_date', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['published'] = __value
                __backup_modified_139882205844752 = get('modified', __marker)

                # <Value 'context/ModificationDate' (31:23)> -> __value
                __token = 1091
                try:
                    __zt_tmp = __attrs_139882205841344
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('path', 'context/ModificationDate', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['modified'] = __value
                __backup_show_modification_date_139882205840528 = get('show_modification_date', __marker)

                # <Value 'python:view.show_modification_date()' (32:36)> -> __value
                __token = 1154
                try:
                    __zt_tmp = __attrs_139882205841344
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139882257081264('python', 'view.show_modification_date()', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                econtext['show_modification_date'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd355ae0> name=None at 7f38dd357520> -> __attrs_139882206153984
                __attrs_139882206153984 = _static_139882206157536

                # <Value 'published' (35:25)> -> __condition
                __token = 1271
                try:
                    __zt_tmp = __attrs_139882206153984
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'published', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentPublished" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206160032
                    __attrs_139882206160032 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139882206153456 = []
                    __append_139882206153456 = __stream_139882206153456.append
                    __append_139882206153456('published')
                    __msgid_139882206153456 = __re_whitespace(''.join(__stream_139882206153456)).strip()
                    if 'box_published':
                        __append(translate('box_published', mapping=None, default=__msgid_139882206153456, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206151824
                    __attrs_139882206151824 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206159744
                    __default_139882206159744 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(published)' (38:25)> -> __cache_139882206156432
                    __token = 1373
                    try:
                        __zt_tmp = __attrs_139882206151824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882206156432 = _static_139882257081264('python', 'context.toLocalizedTime(published)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(published)' (38:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd3573a0> -> __condition
                    __expression = __cache_139882206156432

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Published')
                    else:
                        __content = __cache_139882206156432
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206155424
                    __attrs_139882206155424 = _static_139882337226896

                    # <Value 'show_modification_date' (38:104)> -> __condition
                    __token = 1452
                    try:
                        __zt_tmp = __attrs_139882206155424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139882257081264('path', 'show_modification_date', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                    if __condition:
                        __append(',')
                    __append('\n    </span>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f38dd355b40> name=None at 7f38dd355c00> -> __attrs_139882206155904
                __attrs_139882206155904 = _static_139882206157632

                # <Value 'show_modification_date' (42:25)> -> __condition
                __token = 1561
                try:
                    __zt_tmp = __attrs_139882206155904
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'show_modification_date', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentModified" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206163632
                    __attrs_139882206163632 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139882206163344 = []
                    __append_139882206163344 = __stream_139882206163344.append
                    __append_139882206163344('\n      last modified\n      ')
                    __msgid_139882206163344 = __re_whitespace(''.join(__stream_139882206163344)).strip()
                    if 'box_last_modified':
                        __append(translate('box_last_modified', mapping=None, default=__msgid_139882206163344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206164688
                    __attrs_139882206164688 = _static_139882337226896

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __default_139882206166944
                    __default_139882206166944 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(modified)' (47:25)> -> __cache_139882206165744
                    __token = 1698
                    try:
                        __zt_tmp = __attrs_139882206164688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139882206165744 = _static_139882257081264('python', 'context.toLocalizedTime(modified)', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(modified)' (47:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e03863b0> at 7f38dd357f70> -> __condition
                    __expression = __cache_139882206165744

                    # <Symbol value=<DEFAULT> at 7f38e03863b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n      Modified\n      ')
                    else:
                        __content = __cache_139882206165744
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n    </span>')
                __append('\n  ')
                if (__backup_show_modification_date_139882205840528 is __marker):
                    del econtext['show_modification_date']
                else:
                    econtext['show_modification_date'] = __backup_show_modification_date_139882205840528
                if (__backup_modified_139882205844752 is __marker):
                    del econtext['modified']
                else:
                    econtext['modified'] = __backup_modified_139882205844752
                if (__backup_published_139882205839712 is __marker):
                    del econtext['published']
                else:
                    econtext['published'] = __backup_published_139882205839712
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f38e5055090> name=None at 7f38e50555a0> -> __attrs_139882206166272
                __attrs_139882206166272 = _static_139882337226896

                # <Value 'view/isExpired' (53:30)> -> __condition
                __token = 1828
                try:
                    __zt_tmp = __attrs_139882206166272
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139882257081264('path', 'view/isExpired', econtext=econtext)(_static_139882257080976(econtext, __zt_tmp))
                if __condition:
                    __append('\n    &mdash;\n    ')

                    # <Static value=<ast.Dict object at 0x7f38df55b3a0> name=None at 7f38df5580a0> -> __attrs_139882241819024
                    __attrs_139882241819024 = _static_139882241831840

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="state-expired" >')
                    __stream_139882241834144 = []
                    __append_139882241834144 = __stream_139882241834144.append
                    __append_139882241834144('expired')
                    __msgid_139882241834144 = __re_whitespace(''.join(__stream_139882241834144)).strip()
                    if 'time_expired':
                        __append(translate('time_expired', mapping=None, default=__msgid_139882241834144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n  ')
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_139882205853536
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }