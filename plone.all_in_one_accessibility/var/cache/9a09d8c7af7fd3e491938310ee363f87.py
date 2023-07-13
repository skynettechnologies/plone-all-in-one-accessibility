# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.discussion-4.0.1-py3.10.egg/plone/app/discussion/browser/comments.pt'

__tokens = {46: ('view/can_reply', 1, 46), 104: (' view/is_discussion_allowe', 2, 42), 183: ('d view/anonymous_discussion_allow', 3, 50), 261: ('ed view/edit_comment_allo', 4, 41), 336: ('wed view/delete_own_comment_all', 5, 45), 398: ('Anon view/is_anon', 6, 25), 449: ('eview view/can_', 7, 27), 496: ('eplies python:view.get_replies(can', 8, 24), 566: ('replies python:view.has_replies(ca', 9, 27), 643: ('terImage view/show_commen', 10, 33), 699: ('   errors options/state/getErro', 11, 20), 760: ('     wtool context/@@plone_too', 12, 18), 825: (' auth_token context/@@authenticator/t', 13, 22), 895: ('python:isDiscussionAllowed or has_replies', 14, 19), 1050: ('python:isAnon and not isAnonymousDiscussionAllowed', 18, 27), 1144: ('view/login_action', 19, 41), 1567: ('has_replies', 29, 27), 1628: ('replies', 30, 47), 1714: ('reply_dict/comment', 33, 38), 1773: (' reply/getI', 34, 39), 1820: ('h reply_dict/depth|python', 35, 33), 1881: ("th python: depth > 10 and '10' or de", 36, 32), 1963: ('url python:view.get_commenter_home_url(username=reply.author_usern', 37, 41), 2075: ('link python:author_home_url and not i', 38, 40), 2155: ('t_url python:view.get_commenter_portrait(reply.author_use', 39, 36), 2255: ("_state python:wtool.getInfoFor(reply, 'review_state', ", 40, 35), 2347: ('canEdit python:view.can_edi', 41, 29), 2414: ('anDelete python:view.can_dele', 42, 30), 2484: ("olorclass python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else '", 43, 30), 2817: ("python:canReview or review_state == 'published'", 46, 35), 2641: ("python:'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))", 44, 42), 2769: (' comment_i', 45, 35), 3091: ('showCommenterImage', 52, 43), 3198: ('has_author_link', 54, 47), 3268: ('author_home_url', 55, 53), 3444: ('portrait_url', 58, 56), 3461: (' reply/author_nam', 58, 73), 3658: ('not: has_author_link', 62, 47), 3732: ('portrait_url', 63, 52), 3749: (' reply/author_nam', 63, 69), 4001: ('has_author_link', 70, 47), 4071: ('author_home_url', 71, 53), 4088: ('${reply/author_name}', 71, 70), 4090: ('reply/author_name', 71, 72), 4163: ('not: has_author_link', 73, 49), 4185: ('${reply/author_name}', 73, 71), 4187: ('reply/author_name', 73, 73), 4263: ('not: reply/author_name', 75, 49), 4505: ('python:view.format_time(reply.modification_date)', 81, 45), 4842: ('reply/getText', 93, 53), 5107: ('python:isEditCommentAllowed and canEdit', 99, 47), 5364: ('auth_token', 103, 51), 5433: ('string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', 104, 57), 5842: ('not: auth_token', 111, 51), 5918: ('string:${reply/absolute_url}/@@edit-comment', 112, 59), 6013: (' string:edit-${comment_id', 113, 50), 6659: ('python:canDelete', 127, 47), 7011: ('python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', 134, 51), 7155: ('string:${reply/absolute_url}/@@delete-own-comment', 135, 59), 7259: (" python:view.can_delete_own(reply) and 'display: inline' or 'display: none", 136, 53), 7385: ('d string:delete-${comment_i', 137, 49), 8210: ('python:canDelete', 151, 51), 8287: ('string:${reply/absolute_url}/@@moderate-delete-comment', 152, 59), 8393: (' string:delete-${comment_id', 153, 50), 9070: ('reply_dict/actions|nothing', 165, 47), 9371: ('canReview', 171, 51), 9437: ('reply_dict/actions|nothing', 172, 55), 9625: (' action/i', 174, 52), 9524: ('string:${reply/absolute_url}/@@transmit-comment', 173, 59), 9284: ('comment-action action-${action/id}', 170, 43), 9308: ('action/id', 170, 67), 9686: ('d string:${action/id}-${comment_i', 175, 49), 9956: ('action/id', 179, 62), 10240: ('${action/title}', 183, 58), 10242: ('action/title', 183, 60), 10607: ('python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 194, 39), 10905: ('python: has_replies and not isDiscussionAllowed', 203, 32), 11179: ('python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)', 212, 27), 11291: ('view/login_action', 213, 41), 11795: ('python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 225, 27), 12034: ('view/comment_transform_message', 231, 32), 12241: ('view/form/render', 236, 44)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139673028411200 = {'id': 'commenting', 'class': 'reply border p-3', }
_static_139673028411008 = {'class': 'standalone loginbutton btn btn-primary', 'type': 'submit', 'value': 'Log in to add comments', }
_static_139673028343936 = {'class': 'mb-3', 'action': 'view/login_action', }
_static_139673028344224 = {'class': 'reply', }
_static_139673028267648 = {'class': 'discreet', }
_static_139673028332656 = {'class': 'context reply-to-comment-button hide allowMultiSubmit btn btn-primary btn-sm', }
_static_139673028335440 = {'name': 'form.button.TransmitComment', 'class': 'context btn btn-primary btn-sm', 'type': 'submit', }
_static_139673028337360 = {'type': 'hidden', 'name': 'workflow_action', 'value': 'action/id', }
_static_139673028333280 = {'name': '', 'action': '', 'method': 'get', 'class': 'comment-action action-${action/id}', 'id': 'string:${action/id}-${comment_id}', }
_static_139673028335104 = {'class': 'comment-actions actions-workflow d-flex flex-row', }
_static_139673030724528 = {'name': 'form.button.DeleteComment', 'class': 'destructive btn btn-danger btn-sm', 'type': 'submit', 'value': 'Delete', }
_static_139673030024768 = {'name': 'delete', 'action': '', 'method': 'post', 'class': 'comment-action action-delete', 'id': 'string:delete-${comment_id}', }
_static_139673030026640 = {'name': 'form.button.DeleteComment', 'class': 'destructive btn btn-danger btn-sm', 'type': 'submit', 'value': 'Delete', }
_static_139673030019248 = {'name': 'delete', 'action': '', 'method': 'post', 'class': 'comment-action action-delete', 'style': "python:view.can_delete_own(reply) and 'display: inline' or 'display: none'", 'id': 'string:delete-${comment_id}', }
_static_139673030019488 = {'class': 'comment-actions actions-delete', }
_static_139673028363984 = {'name': 'form.button.EditComment', 'class': 'context btn btn-primary btn-sm', 'type': 'submit', 'value': 'Edit', }
_static_139673028364320 = {'name': 'edit', 'action': '', 'method': 'get', 'class': 'comment-action action-edit', 'id': 'string:edit-${comment_id}', }
_static_139673028369648 = {'class': 'pat-plone-modal context comment-action action-edit btn btn-primary btn-sm', 'href': 'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', }
_static_139673028369456 = {'class': 'comment-actions actions-edit', }
_static_139673028372768 = {'class': 'd-flex flex-row justify-content-end mb-3', }
_static_139673028376656 = {'class': 'comment-body', }
_static_139673028365376 = {'class': 'text-muted', }
_static_139673028062144 = {'href': '', }
_static_139673028051824 = {'class': 'comment-author', }
_static_139673028057776 = {'src': 'defaultUser.png', 'alt': '', }
_static_139673028063392 = {'src': 'defaultUser.png', 'alt': '', }
_static_139673028053024 = {'href': '', }
_static_139673028054416 = {'class': 'comment-image me-3', }
_static_139673028057248 = {'class': 'd-flex flex-row align-items-center mb-3', }
_static_139673028268560 = {'class': 'comment', 'id': 'comment_id', }
_static_139673029899984 = {'class': 'discussion', }
_static_139673029901328 = {'class': 'btn btn-primary mb-3', 'type': 'submit', 'value': 'Log in to add comments', }
_static_139673029895520 = {'action': 'view/login_action', }
_static_139673029902240 = {'class': 'reply', }
_static_139673029896336 = {'class': 'pat-discussion', }
_static_139673118568320 = __C2ZContextWrapper
_static_139673118568608 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673027985664
            __attrs_139673027985664 = _static_139673198743600
            __backup_userHasReplyPermission_139673027996032 = get('userHasReplyPermission', __marker)

            # <Value 'view/can_reply' (1:46)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'view/can_reply', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['userHasReplyPermission'] = __value
            __backup_isDiscussionAllowed_139673027994208 = get('isDiscussionAllowed', __marker)

            # <Value 'view/is_discussion_allowed' (2:42)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'view/is_discussion_allowed', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['isDiscussionAllowed'] = __value
            __backup_isAnonymousDiscussionAllowed_139673027990800 = get('isAnonymousDiscussionAllowed', __marker)

            # <Value 'view/anonymous_discussion_allowed' (3:50)> -> __value
            __token = 183
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'view/anonymous_discussion_allowed', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['isAnonymousDiscussionAllowed'] = __value
            __backup_isEditCommentAllowed_139673027990704 = get('isEditCommentAllowed', __marker)

            # <Value 'view/edit_comment_allowed' (4:41)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'view/edit_comment_allowed', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['isEditCommentAllowed'] = __value
            __backup_isDeleteOwnCommentAllowed_139673027988976 = get('isDeleteOwnCommentAllowed', __marker)

            # <Value 'view/delete_own_comment_allowed' (5:45)> -> __value
            __token = 336
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'view/delete_own_comment_allowed', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['isDeleteOwnCommentAllowed'] = __value
            __backup_isAnon_139673027991808 = get('isAnon', __marker)

            # <Value 'view/is_anonymous' (6:25)> -> __value
            __token = 398
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'view/is_anonymous', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_canReview_139673027988352 = get('canReview', __marker)

            # <Value 'view/can_review' (7:27)> -> __value
            __token = 449
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'view/can_review', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['canReview'] = __value
            __backup_replies_139673027987680 = get('replies', __marker)

            # <Value 'python:view.get_replies(canReview)' (8:24)> -> __value
            __token = 496
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('python', 'view.get_replies(canReview)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['replies'] = __value
            __backup_has_replies_139673027986672 = get('has_replies', __marker)

            # <Value 'python:view.has_replies(canReview)' (9:27)> -> __value
            __token = 566
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('python', 'view.has_replies(canReview)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['has_replies'] = __value
            __backup_showCommenterImage_139673027986768 = get('showCommenterImage', __marker)

            # <Value 'view/show_commenter_image' (10:33)> -> __value
            __token = 643
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'view/show_commenter_image', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['showCommenterImage'] = __value
            __backup_errors_139673027988784 = get('errors', __marker)

            # <Value 'options/state/getErrors|nothing' (11:20)> -> __value
            __token = 699
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'options/state/getErrors|nothing', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_wtool_139673027997856 = get('wtool', __marker)

            # <Value 'context/@@plone_tools/workflow' (12:18)> -> __value
            __token = 760
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'context/@@plone_tools/workflow', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['wtool'] = __value
            __backup_auth_token_139673027991328 = get('auth_token', __marker)

            # <Value 'context/@@authenticator/token|nothing' (13:22)> -> __value
            __token = 825
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139673118568608('path', 'context/@@authenticator/token|nothing', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            econtext['auth_token'] = __value

            # <Value 'python:isDiscussionAllowed or has_replies' (14:19)> -> __condition
            __token = 895
            try:
                __zt_tmp = __attrs_139673027985664
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139673118568608('python', 'isDiscussionAllowed or has_replies', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139673029901664 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f082954e890> name=None at 7f082954e230> -> __attrs_139673029898976
                __attrs_139673029898976 = _static_139673029896336

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-discussion">\n        ')

                # <Static value=<ast.Dict object at 0x7f082954ffa0> name=None at 7f082954eef0> -> __attrs_139673029900704
                __attrs_139673029900704 = _static_139673029902240

                # <Value 'python:isAnon and not isAnonymousDiscussionAllowed' (18:27)> -> __condition
                __token = 1050
                try:
                    __zt_tmp = __attrs_139673029900704
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139673118568608('python', 'isAnon and not isAnonymousDiscussionAllowed', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply">\n            ')

                    # <Static value=<ast.Dict object at 0x7f082954e560> name=None at 7f082954e950> -> __attrs_139673029895760
                    __attrs_139673029895760 = _static_139673029895520

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form')

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673029896240
                    __default_139673029896240 = _DEFAULT_MARKER

                    # <Substitution 'view/login_action' (19:41)> -> __attr_action
                    __token = 1144
                    try:
                        __zt_tmp = __attrs_139673029895760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_139673118568608('path', 'view/login_action', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x7f082954fc10> name=None at 7f082954dcc0> -> __attrs_139673029899072
                    __attrs_139673029899072 = _static_139673029901328

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-primary mb-3" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673029889952
                    __default_139673029889952 = _DEFAULT_MARKER

                    # <Translate msgid='label_login_to_add_comments' node=<ast.Constant object at 0x7f082954eaa0> at 7f082954d930> -> __attr_value
                    __attr_value = 'Log in to add comments'
                    __attr_value = translate('label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_139673029894656 = []
                    __append_139673029894656 = __stream_139673029894656.append
                    __append_139673029894656('Log in to add comments')
                    __msgid_139673029894656 = __re_whitespace(''.join(__stream_139673029894656)).strip()
                    if 'label_login_to_add_comments':
                        __append(translate('label_login_to_add_comments', mapping=None, default=__msgid_139673029894656, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f082954f6d0> name=None at 7f082954fa30> -> __attrs_139673029893456
                __attrs_139673029893456 = _static_139673029899984

                # <Value 'has_replies' (29:27)> -> __condition
                __token = 1567
                try:
                    __zt_tmp = __attrs_139673029893456
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139673118568608('path', 'has_replies', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="discussion">\n            ')

                    # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029892544
                    __attrs_139673029892544 = _static_139673198743600
                    __backup_reply_dict_139673029888560 = get('reply_dict', __marker)

                    # <Value 'replies' (30:47)> -> __iterator
                    __token = 1628
                    try:
                        __zt_tmp = __attrs_139673029892544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139673118568608('path', 'replies', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                    (__iterator, ____index_139673031113504, ) = getname('repeat')('reply_dict', __iterator)
                    econtext['reply_dict'] = None
                    for __item in __iterator:
                        econtext['reply_dict'] = __item
                        __append('\n\n                ')

                        # <Static value=<ast.Dict object at 0x7f08293c1210> name=None at 7f08293c0400> -> __attrs_139673028033024
                        __attrs_139673028033024 = _static_139673028268560
                        __backup_reply_139673029892496 = get('reply', __marker)

                        # <Value 'reply_dict/comment' (33:38)> -> __value
                        __token = 1714
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('path', 'reply_dict/comment', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['reply'] = __value
                        __backup_comment_id_139673029896816 = get('comment_id', __marker)

                        # <Value 'reply/getId' (34:39)> -> __value
                        __token = 1773
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('path', 'reply/getId', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['comment_id'] = __value
                        __backup_depth_139673029894560 = get('depth', __marker)

                        # <Value 'reply_dict/depth|python:0' (35:33)> -> __value
                        __token = 1820
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('path', 'reply_dict/depth|python:0', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_depth_139673028032592 = get('depth', __marker)

                        # <Value "python: depth > 10 and '10' or depth" (36:32)> -> __value
                        __token = 1881
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('python', " depth > 10 and '10' or depth", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_author_home_url_139673028034272 = get('author_home_url', __marker)

                        # <Value 'python:view.get_commenter_home_url(username=reply.author_username)' (37:41)> -> __value
                        __token = 1963
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('python', 'view.get_commenter_home_url(username=reply.author_username)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['author_home_url'] = __value
                        __backup_has_author_link_139673028028368 = get('has_author_link', __marker)

                        # <Value 'python:author_home_url and not isAnon' (38:40)> -> __value
                        __token = 2075
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('python', 'author_home_url and not isAnon', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['has_author_link'] = __value
                        __backup_portrait_url_139673028018624 = get('portrait_url', __marker)

                        # <Value 'python:view.get_commenter_portrait(reply.author_username)' (39:36)> -> __value
                        __token = 2155
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('python', 'view.get_commenter_portrait(reply.author_username)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['portrait_url'] = __value
                        __backup_review_state_139673028034320 = get('review_state', __marker)

                        # <Value "python:wtool.getInfoFor(reply, 'review_state', 'none')" (40:35)> -> __value
                        __token = 2255
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('python', "wtool.getInfoFor(reply, 'review_state', 'none')", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['review_state'] = __value
                        __backup_canEdit_139673028027936 = get('canEdit', __marker)

                        # <Value 'python:view.can_edit(reply)' (41:29)> -> __value
                        __token = 2347
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('python', 'view.can_edit(reply)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['canEdit'] = __value
                        __backup_canDelete_139673028028224 = get('canDelete', __marker)

                        # <Value 'python:view.can_delete(reply)' (42:30)> -> __value
                        __token = 2414
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('python', 'view.can_delete(reply)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['canDelete'] = __value
                        __backup_colorclass_139673028018336 = get('colorclass', __marker)

                        # <Value "python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)" (43:30)> -> __value
                        __token = 2484
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139673118568608('python', "lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        econtext['colorclass'] = __value

                        # <Value "python:canReview or review_state == 'published'" (46:35)> -> __condition
                        __token = 2817
                        try:
                            __zt_tmp = __attrs_139673028033024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139673118568608('python', "canReview or review_state == 'published'", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div')

                            # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028268512
                            __default_139673028268512 = _DEFAULT_MARKER

                            # <Substitution "python:'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))" (44:42)> -> __attr_class
                            __token = 2641
                            try:
                                __zt_tmp = __attrs_139673028033024
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_139673118568608('python', "'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', 'comment', _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))

                            # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028269376
                            __default_139673028269376 = _DEFAULT_MARKER

                            # <Substitution 'comment_id' (45:35)> -> __attr_id
                            __token = 2769
                            try:
                                __zt_tmp = __attrs_139673028033024
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_139673118568608('path', 'comment_id', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((' id="%s"' % __attr_id))
                            __append('>\n\n                    ')

                            # <Static value=<ast.Dict object at 0x7f082938d8a0> name=None at 7f082938e770> -> __attrs_139673028056528
                            __attrs_139673028056528 = _static_139673028057248

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="d-flex flex-row align-items-center mb-3">\n\n                        <!-- commenter image -->\n                        ')

                            # <Static value=<ast.Dict object at 0x7f082938cd90> name=None at 7f082938cfa0> -> __attrs_139673028060368
                            __attrs_139673028060368 = _static_139673028054416

                            # <Value 'showCommenterImage' (52:43)> -> __condition
                            __token = 3091
                            try:
                                __zt_tmp = __attrs_139673028060368
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139673118568608('path', 'showCommenterImage', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-image me-3">\n                            ')

                                # <Static value=<ast.Dict object at 0x7f082938c820> name=None at 7f082938dc90> -> __attrs_139673028052784
                                __attrs_139673028052784 = _static_139673028053024

                                # <Value 'has_author_link' (54:47)> -> __condition
                                __token = 3198
                                try:
                                    __zt_tmp = __attrs_139673028052784
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139673118568608('path', 'has_author_link', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028057104
                                    __default_139673028057104 = _DEFAULT_MARKER

                                    # <Substitution 'author_home_url' (55:53)> -> __attr_href
                                    __token = 3268
                                    try:
                                        __zt_tmp = __attrs_139673028052784
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_139673118568608('path', 'author_home_url', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((' href="%s"' % __attr_href))
                                    __append('>\n                                ')

                                    # <Static value=<ast.Dict object at 0x7f082938f0a0> name=None at 7f082938d930> -> __attrs_139673028057872
                                    __attrs_139673028057872 = _static_139673028063392

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<img')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028066272
                                    __default_139673028066272 = _DEFAULT_MARKER

                                    # <Substitution 'portrait_url' (58:56)> -> __attr_src
                                    __token = 3444
                                    try:
                                        __zt_tmp = __attrs_139673028057872
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_139673118568608('path', 'portrait_url', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', 'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028056000
                                    __default_139673028056000 = _DEFAULT_MARKER

                                    # <Substitution 'reply/author_name' (58:73)> -> __attr_alt
                                    __token = 3461
                                    try:
                                        __zt_tmp = __attrs_139673028057872
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_139673118568608('path', 'reply/author_name', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((' alt="%s"' % __attr_alt))
                                    __append(' />\n                            </a>')
                                __append('\n                            ')

                                # <Static value=<ast.Dict object at 0x7f082938dab0> name=None at 7f082938f550> -> __attrs_139673028060464
                                __attrs_139673028060464 = _static_139673028057776

                                # <Value 'not: has_author_link' (62:47)> -> __condition
                                __token = 3658
                                try:
                                    __zt_tmp = __attrs_139673028060464
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139673118568608('not', ' has_author_link', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                if __condition:

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<img')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028051200
                                    __default_139673028051200 = _DEFAULT_MARKER

                                    # <Substitution 'portrait_url' (63:52)> -> __attr_src
                                    __token = 3732
                                    try:
                                        __zt_tmp = __attrs_139673028060464
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_139673118568608('path', 'portrait_url', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', 'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028055184
                                    __default_139673028055184 = _DEFAULT_MARKER

                                    # <Substitution 'reply/author_name' (63:69)> -> __attr_alt
                                    __token = 3749
                                    try:
                                        __zt_tmp = __attrs_139673028060464
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_139673118568608('path', 'reply/author_name', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((' alt="%s"' % __attr_alt))
                                    __append(' />')
                                __append('\n                        </div>')
                            __append('\n\n                        <!-- commenter name and date -->\n                        ')

                            # <Static value=<ast.Dict object at 0x7f082938c370> name=None at 7f082938d210> -> __attrs_139673028057584
                            __attrs_139673028057584 = _static_139673028051824

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="comment-author">\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f082938ebc0> name=None at 7f082938ca00> -> __attrs_139673028058688
                            __attrs_139673028058688 = _static_139673028062144

                            # <Value 'has_author_link' (70:47)> -> __condition
                            __token = 4001
                            try:
                                __zt_tmp = __attrs_139673028058688
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139673118568608('path', 'has_author_link', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028055472
                                __default_139673028055472 = _DEFAULT_MARKER

                                # <Substitution 'author_home_url' (71:53)> -> __attr_href
                                __token = 4071
                                try:
                                    __zt_tmp = __attrs_139673028058688
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_139673118568608('path', 'author_home_url', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))
                                __append('>')

                                # <Interpolation value=<Substitution '${reply/author_name}' (71:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f082938e170> -> __content_139673205368624
                                __token = 4088
                                __token = 4090
                                try:
                                    __zt_tmp = __attrs_139673028058688
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_139673205368624 = _static_139673118568608('path', 'reply/author_name', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                __content_139673205368624 = __quote(__content_139673205368624, '\x00', '&#0;', None, None)
                                __content_139673205368624 = __content_139673205368624
                                if (__content_139673205368624 is None):
                                    pass
                                else:
                                    if (__content_139673205368624 is None):
                                        __content_139673205368624 = None
                                    else:
                                        __tt = type(__content_139673205368624)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139673205368624 = str(__content_139673205368624)
                                        else:
                                            if (__tt is bytes):
                                                __content_139673205368624 = decode(__content_139673205368624)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139673205368624 = __content_139673205368624.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139673205368624)
                                                        __content_139673205368624 = (str(__content_139673205368624) if (__content_139673205368624 is __converted) else __converted)
                                                    else:
                                                        __content_139673205368624 = __content_139673205368624()
                                if (__content_139673205368624 is not None):
                                    __append(__content_139673205368624)
                                __append('</a>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673028052688
                            __attrs_139673028052688 = _static_139673198743600

                            # <Value 'not: has_author_link' (73:49)> -> __condition
                            __token = 4163
                            try:
                                __zt_tmp = __attrs_139673028052688
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139673118568608('not', ' has_author_link', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span>')

                                # <Interpolation value=<Substitution '${reply/author_name}' (73:71)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f082b8f0040> -> __content_139673205368624
                                __token = 4185
                                __token = 4187
                                try:
                                    __zt_tmp = __attrs_139673028052688
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_139673205368624 = _static_139673118568608('path', 'reply/author_name', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                __content_139673205368624 = __quote(__content_139673205368624, '\x00', '&#0;', None, None)
                                __content_139673205368624 = __content_139673205368624
                                if (__content_139673205368624 is None):
                                    pass
                                else:
                                    if (__content_139673205368624 is None):
                                        __content_139673205368624 = None
                                    else:
                                        __tt = type(__content_139673205368624)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139673205368624 = str(__content_139673205368624)
                                        else:
                                            if (__tt is bytes):
                                                __content_139673205368624 = decode(__content_139673205368624)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139673205368624 = __content_139673205368624.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139673205368624)
                                                        __content_139673205368624 = (str(__content_139673205368624) if (__content_139673205368624 is __converted) else __converted)
                                                    else:
                                                        __content_139673205368624 = __content_139673205368624()
                                if (__content_139673205368624 is not None):
                                    __append(__content_139673205368624)
                                __append('</span>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673029065744
                            __attrs_139673029065744 = _static_139673198743600

                            # <Value 'not: reply/author_name' (75:49)> -> __condition
                            __token = 4263
                            try:
                                __zt_tmp = __attrs_139673029065744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139673118568608('not', ' reply/author_name', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span>')
                                __stream_139673075271664 = []
                                __append_139673075271664 = __stream_139673075271664.append
                                __append_139673075271664('Anonymous')
                                __msgid_139673075271664 = __re_whitespace(''.join(__stream_139673075271664)).strip()
                                if 'label_anonymous':
                                    __append(translate('label_anonymous', mapping=None, default=__msgid_139673075271664, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</span>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673028371184
                            __attrs_139673028371184 = _static_139673198743600

                            # <br ... (0:0)
                            # --------------------------------------------------------
                            __append('<br />\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f08293d8c40> name=None at 7f08293d9b40> -> __attrs_139673028366864
                            __attrs_139673028366864 = _static_139673028365376

                            # <small ... (0:0)
                            # --------------------------------------------------------
                            __append('<small class="text-muted">')

                            # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028375744
                            __default_139673028375744 = _DEFAULT_MARKER

                            # <Value 'python:view.format_time(reply.modification_date)' (81:45)> -> __cache_139673028374880
                            __token = 4505
                            try:
                                __zt_tmp = __attrs_139673028366864
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139673028374880 = _static_139673118568608('python', 'view.format_time(reply.modification_date)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.format_time(reply.modification_date)' (81:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f082eb5a980> at 7f08293db610> -> __condition
                            __expression = __cache_139673028374880

                            # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('\n                      8/23/2001 12:40:44 PM\n                            ')
                            else:
                                __content = __cache_139673028374880
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</small>\n\n                        </div>\n                    </div>\n\n\n\n                    <!-- comment body -->\n                    ')

                            # <Static value=<ast.Dict object at 0x7f08293db850> name=None at 7f08293dbd00> -> __attrs_139673028371568
                            __attrs_139673028371568 = _static_139673028376656

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="comment-body">\n\n                        ')

                            # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673028368400
                            __attrs_139673028368400 = _static_139673198743600

                            # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028368736
                            __default_139673028368736 = _DEFAULT_MARKER

                            # <Value 'reply/getText' (93:53)> -> __cache_139673028372096
                            __token = 4842
                            try:
                                __zt_tmp = __attrs_139673028368400
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139673028372096 = _static_139673118568608('path', 'reply/getText', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))

                            # <BinOp left=<Value 'reply/getText' (93:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f082eb5a980> at 7f08293da650> -> __condition
                            __expression = __cache_139673028372096

                            # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span />')
                            else:
                                __content = __cache_139673028372096
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n\n                        <!-- comment actions -->\n                        ')

                            # <Static value=<ast.Dict object at 0x7f08293da920> name=None at 7f08293d8d60> -> __attrs_139673028366624
                            __attrs_139673028366624 = _static_139673028372768

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="d-flex flex-row justify-content-end mb-3">\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f08293d9c30> name=None at 7f08293d8340> -> __attrs_139673028366048
                            __attrs_139673028366048 = _static_139673028369456

                            # <Value 'python:isEditCommentAllowed and canEdit' (99:47)> -> __condition
                            __token = 5107
                            try:
                                __zt_tmp = __attrs_139673028366048
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139673118568608('python', 'isEditCommentAllowed and canEdit', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-edit">\n\n                                <!-- edit -->\n                                ')

                                # <Static value=<ast.Dict object at 0x7f08293d9cf0> name=None at 7f08293dac80> -> __attrs_139673028374016
                                __attrs_139673028374016 = _static_139673028369648

                                # <Value 'auth_token' (103:51)> -> __condition
                                __token = 5364
                                try:
                                    __zt_tmp = __attrs_139673028374016
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139673118568608('path', 'auth_token', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a class="pat-plone-modal context comment-action action-edit btn btn-primary btn-sm"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028377184
                                    __default_139673028377184 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}' (104:57)> -> __attr_href
                                    __token = 5433
                                    try:
                                        __zt_tmp = __attrs_139673028374016
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_139673118568608('string', '${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((' href="%s"' % __attr_href))
                                    __append('>')
                                    __stream_139673028377904 = []
                                    __append_139673028377904 = __stream_139673028377904.append
                                    __append_139673028377904('Edit')
                                    __msgid_139673028377904 = __re_whitespace(''.join(__stream_139673028377904)).strip()
                                    if 'Edit':
                                        __append(translate('Edit', mapping=None, default=__msgid_139673028377904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</a>')
                                __append('\n\n                                ')

                                # <Static value=<ast.Dict object at 0x7f08293d8820> name=None at 7f08293d8f70> -> __attrs_139673028362304
                                __attrs_139673028362304 = _static_139673028364320

                                # <Value 'not: auth_token' (111:51)> -> __condition
                                __token = 5842
                                try:
                                    __zt_tmp = __attrs_139673028362304
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139673118568608('not', ' auth_token', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="edit"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028372912
                                    __default_139673028372912 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@edit-comment' (112:59)> -> __attr_action
                                    __token = 5918
                                    try:
                                        __zt_tmp = __attrs_139673028362304
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_139673118568608('string', '${reply/absolute_url}/@@edit-comment', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="get" class="comment-action action-edit"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028375216
                                    __default_139673028375216 = _DEFAULT_MARKER

                                    # <Substitution 'string:edit-${comment_id}' (113:50)> -> __attr_id
                                    __token = 6013
                                    try:
                                        __zt_tmp = __attrs_139673028362304
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_139673118568608('string', 'edit-${comment_id}', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n\n                                    ')

                                    # <Static value=<ast.Dict object at 0x7f08293d86d0> name=None at 7f08293d83d0> -> __attrs_139673030030960
                                    __attrs_139673030030960 = _static_139673028363984

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.EditComment" class="context btn btn-primary btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030019776
                                    __default_139673030019776 = _DEFAULT_MARKER

                                    # <Translate msgid='label_edit' node=<ast.Constant object at 0x7f082956f550> at 7f082956ce20> -> __attr_value
                                    __attr_value = 'Edit'
                                    __attr_value = translate('label_edit', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_139673028367344 = []
                                    __append_139673028367344 = __stream_139673028367344.append
                                    __append_139673028367344('Edit')
                                    __msgid_139673028367344 = __re_whitespace(''.join(__stream_139673028367344)).strip()
                                    if 'label_edit':
                                        __append(translate('label_edit', mapping=None, default=__msgid_139673028367344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n\n                                </form>')
                                __append('\n\n                            </div>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f082956c9a0> name=None at 7f082956f3d0> -> __attrs_139673030025728
                            __attrs_139673030025728 = _static_139673030019488

                            # <Value 'python:canDelete' (127:47)> -> __condition
                            __token = 6659
                            try:
                                __zt_tmp = __attrs_139673030025728
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139673118568608('python', 'canDelete', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-delete">\n\n                                <!-- delete own comment -->\n                                ')

                                # <Static value=<ast.Dict object at 0x7f082956c8b0> name=None at 7f082956ff70> -> __attrs_139673030019872
                                __attrs_139673030019872 = _static_139673030019248

                                # <Value 'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)' (134:51)> -> __condition
                                __token = 7011
                                try:
                                    __zt_tmp = __attrs_139673030019872
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139673118568608('python', 'not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="delete"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030031968
                                    __default_139673030031968 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@delete-own-comment' (135:59)> -> __attr_action
                                    __token = 7155
                                    try:
                                        __zt_tmp = __attrs_139673030019872
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_139673118568608('string', '${reply/absolute_url}/@@delete-own-comment', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="post" class="comment-action action-delete"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030025680
                                    __default_139673030025680 = _DEFAULT_MARKER

                                    # <Substitution "python:view.can_delete_own(reply) and 'display: inline' or 'display: none'" (136:53)> -> __attr_style
                                    __token = 7259
                                    try:
                                        __zt_tmp = __attrs_139673030019872
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_style = _static_139673118568608('python', "view.can_delete_own(reply) and 'display: inline' or 'display: none'", econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_style is not None):
                                        __append((' style="%s"' % __attr_style))

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030024192
                                    __default_139673030024192 = _DEFAULT_MARKER

                                    # <Substitution 'string:delete-${comment_id}' (137:49)> -> __attr_id
                                    __token = 7385
                                    try:
                                        __zt_tmp = __attrs_139673030019872
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_139673118568608('string', 'delete-${comment_id}', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n                                    ')

                                    # <Static value=<ast.Dict object at 0x7f082956e590> name=None at 7f082956ef20> -> __attrs_139673030031344
                                    __attrs_139673030031344 = _static_139673030026640

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.DeleteComment" class="destructive btn btn-danger btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030032592
                                    __default_139673030032592 = _DEFAULT_MARKER

                                    # <Translate msgid='label_delete' node=<ast.Constant object at 0x7f082956e5c0> at 7f082956fd00> -> __attr_value
                                    __attr_value = 'Delete'
                                    __attr_value = translate('label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_139673030032160 = []
                                    __append_139673030032160 = __stream_139673030032160.append
                                    __append_139673030032160('Delete')
                                    __msgid_139673030032160 = __re_whitespace(''.join(__stream_139673030032160)).strip()
                                    if 'label_delete':
                                        __append(translate('label_delete', mapping=None, default=__msgid_139673030032160, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n                                </form>')
                                __append('\n\n                                <!-- delete -->\n                                ')

                                # <Static value=<ast.Dict object at 0x7f082956de40> name=None at 7f082956df00> -> __attrs_139673030027744
                                __attrs_139673030027744 = _static_139673030024768

                                # <Value 'python:canDelete' (151:51)> -> __condition
                                __token = 8210
                                try:
                                    __zt_tmp = __attrs_139673030027744
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139673118568608('python', 'canDelete', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="delete"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030031440
                                    __default_139673030031440 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@moderate-delete-comment' (152:59)> -> __attr_action
                                    __token = 8287
                                    try:
                                        __zt_tmp = __attrs_139673030027744
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_139673118568608('string', '${reply/absolute_url}/@@moderate-delete-comment', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="post" class="comment-action action-delete"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030029616
                                    __default_139673030029616 = _DEFAULT_MARKER

                                    # <Substitution 'string:delete-${comment_id}' (153:50)> -> __attr_id
                                    __token = 8393
                                    try:
                                        __zt_tmp = __attrs_139673030027744
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_139673118568608('string', 'delete-${comment_id}', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n                                    ')

                                    # <Static value=<ast.Dict object at 0x7f0829618bb0> name=None at 7f082961a0b0> -> __attrs_139673028337120
                                    __attrs_139673028337120 = _static_139673030724528

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.DeleteComment" class="destructive btn btn-danger btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673030024576
                                    __default_139673030024576 = _DEFAULT_MARKER

                                    # <Translate msgid='label_delete' node=<ast.Constant object at 0x7f082b91fe80> at 7f082b91fbe0> -> __attr_value
                                    __attr_value = 'Delete'
                                    __attr_value = translate('label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_139673030020400 = []
                                    __append_139673030020400 = __stream_139673030020400.append
                                    __append_139673030020400('Delete')
                                    __msgid_139673030020400 = __re_whitespace(''.join(__stream_139673030020400)).strip()
                                    if 'label_delete':
                                        __append(translate('label_delete', mapping=None, default=__msgid_139673030020400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n                                </form>')
                                __append('\n\n                            </div>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f08293d1600> name=None at 7f08293d1660> -> __attrs_139673028343408
                            __attrs_139673028343408 = _static_139673028335104

                            # <Value 'reply_dict/actions|nothing' (165:47)> -> __condition
                            __token = 9070
                            try:
                                __zt_tmp = __attrs_139673028343408
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139673118568608('path', 'reply_dict/actions|nothing', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-workflow d-flex flex-row">\n\n                                ')

                                # <Static value=<ast.Dict object at 0x7f08293d0ee0> name=None at 7f08293d0a60> -> __attrs_139673028341536
                                __attrs_139673028341536 = _static_139673028333280

                                # <Value 'canReview' (171:51)> -> __condition
                                __token = 9371
                                try:
                                    __zt_tmp = __attrs_139673028341536
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139673118568608('path', 'canReview', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                if __condition:
                                    __backup_action_139673028053120 = get('action', __marker)

                                    # <Value 'reply_dict/actions|nothing' (172:55)> -> __iterator
                                    __token = 9437
                                    try:
                                        __zt_tmp = __attrs_139673028341536
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __iterator = _static_139673118568608('path', 'reply_dict/actions|nothing', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                    (__iterator, ____index_139673028340000, ) = getname('repeat')('action', __iterator)
                                    econtext['action'] = None
                                    for __item in __iterator:
                                        econtext['action'] = __item

                                        # <form ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<form')

                                        # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028342352
                                        __default_139673028342352 = _DEFAULT_MARKER

                                        # <Substitution 'action/id' (174:52)> -> __attr_name
                                        __token = 9625
                                        try:
                                            __zt_tmp = __attrs_139673028341536
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_name = _static_139673118568608('path', 'action/id', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_name is not None):
                                            __append((' name="%s"' % __attr_name))

                                        # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028335056
                                        __default_139673028335056 = _DEFAULT_MARKER

                                        # <Substitution 'string:${reply/absolute_url}/@@transmit-comment' (173:59)> -> __attr_action
                                        __token = 9524
                                        try:
                                            __zt_tmp = __attrs_139673028341536
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_action = _static_139673118568608('string', '${reply/absolute_url}/@@transmit-comment', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_action is not None):
                                            __append((' action="%s"' % __attr_action))
                                        __append(' method="get"')

                                        # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028330832
                                        __default_139673028330832 = _DEFAULT_MARKER

                                        # <Interpolation value=<Substitution 'comment-action action-${action/id}' (170:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f08293d34c0> -> __attr_class
                                        __token = 9284
                                        __token = 9308
                                        try:
                                            __zt_tmp = __attrs_139673028341536
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_class = _static_139673118568608('path', 'action/id', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                        __attr_class = ('%s%s' % ('comment-action action-', (__attr_class if (__attr_class is not None) else ''), ))
                                        if (__attr_class is None):
                                            pass
                                        else:
                                            if (__attr_class is _DEFAULT_MARKER):
                                                __attr_class = None
                                            else:
                                                __tt = type(__attr_class)
                                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                    __attr_class = str(__attr_class)
                                                else:
                                                    if (__tt is bytes):
                                                        __attr_class = decode(__attr_class)
                                                    else:
                                                        if (__tt is not str):
                                                            try:
                                                                __attr_class = __attr_class.__html__
                                                            except get('AttributeError', AttributeError):
                                                                __converted = convert(__attr_class)
                                                                __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                            else:
                                                                __attr_class = __attr_class()
                                        if (__attr_class is not None):
                                            __append((' class="%s"' % __attr_class))

                                        # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028345040
                                        __default_139673028345040 = _DEFAULT_MARKER

                                        # <Substitution 'string:${action/id}-${comment_id}' (175:49)> -> __attr_id
                                        __token = 9686
                                        try:
                                            __zt_tmp = __attrs_139673028341536
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_id = _static_139673118568608('string', '${action/id}-${comment_id}', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_id is not None):
                                            __append((' id="%s"' % __attr_id))
                                        __append('>\n                                    ')

                                        # <Static value=<ast.Dict object at 0x7f08293d1ed0> name=None at 7f08293d0130> -> __attrs_139673028338368
                                        __attrs_139673028338368 = _static_139673028337360

                                        # <input ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<input type="hidden" name="workflow_action"')

                                        # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028335776
                                        __default_139673028335776 = _DEFAULT_MARKER

                                        # <Substitution 'action/id' (179:62)> -> __attr_value
                                        __token = 9956
                                        try:
                                            __zt_tmp = __attrs_139673028338368
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_value = _static_139673118568608('path', 'action/id', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_value is not None):
                                            __append((' value="%s"' % __attr_value))
                                        __append(' />\n                                    ')

                                        # <Static value=<ast.Dict object at 0x7f08293d1750> name=None at 7f08293d2da0> -> __attrs_139673028338032
                                        __attrs_139673028338032 = _static_139673028335440

                                        # <button ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<button name="form.button.TransmitComment" class="context btn btn-primary btn-sm" type="submit">')
                                        __stream_139673028337888 = []
                                        __append_139673028337888 = __stream_139673028337888.append

                                        # <Interpolation value=<Substitution '${action/title}' (183:58)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f08293d14e0> -> __content_139673205368624
                                        __token = 10240
                                        __token = 10242
                                        try:
                                            __zt_tmp = __attrs_139673028338032
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __content_139673205368624 = _static_139673118568608('path', 'action/title', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                                        __content_139673205368624 = __quote(__content_139673205368624, '\x00', '&#0;', None, None)
                                        __content_139673205368624 = __content_139673205368624
                                        if (__content_139673205368624 is None):
                                            pass
                                        else:
                                            if (__content_139673205368624 is None):
                                                __content_139673205368624 = None
                                            else:
                                                __tt = type(__content_139673205368624)
                                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                    __content_139673205368624 = str(__content_139673205368624)
                                                else:
                                                    if (__tt is bytes):
                                                        __content_139673205368624 = decode(__content_139673205368624)
                                                    else:
                                                        if (__tt is not str):
                                                            try:
                                                                __content_139673205368624 = __content_139673205368624.__html__
                                                            except get('AttributeError', AttributeError):
                                                                __converted = convert(__content_139673205368624)
                                                                __content_139673205368624 = (str(__content_139673205368624) if (__content_139673205368624 is __converted) else __converted)
                                                            else:
                                                                __content_139673205368624 = __content_139673205368624()
                                        if (__content_139673205368624 is not None):
                                            __append_139673028337888(__content_139673205368624)
                                        __msgid_139673028337888 = __re_whitespace(''.join(__stream_139673028337888)).strip()
                                        if __msgid_139673028337888:
                                            __append(translate(__msgid_139673028337888, mapping=None, default=__msgid_139673028337888, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                        __append('</button>\n                                </form>')
                                        ____index_139673028340000 -= 1
                                        if (____index_139673028340000 > 0):
                                            __append('\n                                ')
                                    if (__backup_action_139673028053120 is __marker):
                                        del econtext['action']
                                    else:
                                        econtext['action'] = __backup_action_139673028053120
                                __append('\n\n                            </div>')
                            __append('\n\n                        </div>\n                        <!-- end comment actions -->\n\n\n                    </div>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f08293d0c70> name=None at 7f08293d1fc0> -> __attrs_139673028345808
                            __attrs_139673028345808 = _static_139673028332656

                            # <Value 'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (194:39)> -> __condition
                            __token = 10607
                            try:
                                __zt_tmp = __attrs_139673028345808
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139673118568608('python', 'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                            if __condition:

                                # <button ... (0:0)
                                # --------------------------------------------------------
                                __append('<button class="context reply-to-comment-button hide allowMultiSubmit btn btn-primary btn-sm">')
                                __stream_139673028339808 = []
                                __append_139673028339808 = __stream_139673028339808.append
                                __append_139673028339808('\n                    Reply\n                    ')
                                __msgid_139673028339808 = __re_whitespace(''.join(__stream_139673028339808)).strip()
                                if 'label_reply':
                                    __append(translate('label_reply', mapping=None, default=__msgid_139673028339808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</button>')
                            __append('\n\n                </div>')
                        if (__backup_colorclass_139673028018336 is __marker):
                            del econtext['colorclass']
                        else:
                            econtext['colorclass'] = __backup_colorclass_139673028018336
                        if (__backup_canDelete_139673028028224 is __marker):
                            del econtext['canDelete']
                        else:
                            econtext['canDelete'] = __backup_canDelete_139673028028224
                        if (__backup_canEdit_139673028027936 is __marker):
                            del econtext['canEdit']
                        else:
                            econtext['canEdit'] = __backup_canEdit_139673028027936
                        if (__backup_review_state_139673028034320 is __marker):
                            del econtext['review_state']
                        else:
                            econtext['review_state'] = __backup_review_state_139673028034320
                        if (__backup_portrait_url_139673028018624 is __marker):
                            del econtext['portrait_url']
                        else:
                            econtext['portrait_url'] = __backup_portrait_url_139673028018624
                        if (__backup_has_author_link_139673028028368 is __marker):
                            del econtext['has_author_link']
                        else:
                            econtext['has_author_link'] = __backup_has_author_link_139673028028368
                        if (__backup_author_home_url_139673028034272 is __marker):
                            del econtext['author_home_url']
                        else:
                            econtext['author_home_url'] = __backup_author_home_url_139673028034272
                        if (__backup_depth_139673028032592 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_139673028032592
                        if (__backup_depth_139673029894560 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_139673029894560
                        if (__backup_comment_id_139673029896816 is __marker):
                            del econtext['comment_id']
                        else:
                            econtext['comment_id'] = __backup_comment_id_139673029896816
                        if (__backup_reply_139673029892496 is __marker):
                            del econtext['reply']
                        else:
                            econtext['reply'] = __backup_reply_139673029892496
                        __append('\n\n            ')
                        ____index_139673031113504 -= 1
                        if (____index_139673031113504 > 0):
                            __append('')
                    if (__backup_reply_dict_139673029888560 is __marker):
                        del econtext['reply_dict']
                    else:
                        econtext['reply_dict'] = __backup_reply_dict_139673029888560
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f08293c0e80> name=None at 7f082938f100> -> __attrs_139673028337792
                    __attrs_139673028337792 = _static_139673028267648

                    # <Value 'python: has_replies and not isDiscussionAllowed' (203:32)> -> __condition
                    __token = 10905
                    try:
                        __zt_tmp = __attrs_139673028337792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139673118568608('python', ' has_replies and not isDiscussionAllowed', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="discreet">')
                        __stream_139673029893792 = []
                        __append_139673029893792 = __stream_139673029893792.append
                        __append_139673029893792('\n            Commenting has been disabled.\n            ')
                        __msgid_139673029893792 = __re_whitespace(''.join(__stream_139673029893792)).strip()
                        if 'label_commenting_disabled':
                            __append(translate('label_commenting_disabled', mapping=None, default=__msgid_139673029893792, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>')
                    __append('\n\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f08293d39a0> name=None at 7f08293d3130> -> __attrs_139673028335152
                __attrs_139673028335152 = _static_139673028344224

                # <Value 'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)' (212:27)> -> __condition
                __token = 11179
                try:
                    __zt_tmp = __attrs_139673028335152
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139673118568608('python', 'has_replies and (isAnon and not isAnonymousDiscussionAllowed)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply">\n            ')

                    # <Static value=<ast.Dict object at 0x7f08293d3880> name=None at 7f08293d0490> -> __attrs_139673028408080
                    __attrs_139673028408080 = _static_139673028343936

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="mb-3"')

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028337840
                    __default_139673028337840 = _DEFAULT_MARKER

                    # <Substitution 'view/login_action' (213:41)> -> __attr_action
                    __token = 11291
                    try:
                        __zt_tmp = __attrs_139673028408080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_139673118568608('path', 'view/login_action', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x7f08293e3e80> name=None at 7f08293e3910> -> __attrs_139673028397952
                    __attrs_139673028397952 = _static_139673028411008

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="standalone loginbutton btn btn-primary" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028409232
                    __default_139673028409232 = _DEFAULT_MARKER

                    # <Translate msgid='label_login_to_add_comments' node=<ast.Constant object at 0x7f08293e1720> at 7f08293e25f0> -> __attr_value
                    __attr_value = 'Log in to add comments'
                    __attr_value = translate('label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_139673028404672 = []
                    __append_139673028404672 = __stream_139673028404672.append
                    __append_139673028404672('Log in to add comments')
                    __msgid_139673028404672 = __re_whitespace(''.join(__stream_139673028404672)).strip()
                    if 'label_login_to_add_comments':
                        __append(translate('label_login_to_add_comments', mapping=None, default=__msgid_139673028404672, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f08293e3f40> name=None at 7f08293e1000> -> __attrs_139673028396416
                __attrs_139673028396416 = _static_139673028411200

                # <Value 'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (225:27)> -> __condition
                __token = 11795
                try:
                    __zt_tmp = __attrs_139673028396416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139673118568608('python', 'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="commenting" class="reply border p-3">\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673028409808
                    __attrs_139673028409808 = _static_139673198743600

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673028399392
                    __attrs_139673028399392 = _static_139673198743600

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append('<legend>')
                    __stream_139673028403232 = []
                    __append_139673028403232 = __stream_139673028403232.append
                    __append_139673028403232('Add comment')
                    __msgid_139673028403232 = __re_whitespace(''.join(__stream_139673028403232)).strip()
                    if 'label_add_comment':
                        __append(translate('label_add_comment', mapping=None, default=__msgid_139673028403232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</legend>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673028400496
                    __attrs_139673028400496 = _static_139673198743600

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028407120
                    __default_139673028407120 = _DEFAULT_MARKER

                    # <Value 'view/comment_transform_message' (231:32)> -> __cache_139673028398240
                    __token = 12034
                    try:
                        __zt_tmp = __attrs_139673028400496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139673028398240 = _static_139673118568608('path', 'view/comment_transform_message', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/comment_transform_message' (231:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f082eb5a980> at 7f08293e0b20> -> __condition
                    __expression = __cache_139673028398240

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                You can add a comment by filling out the form below. Plain text\n                formatting.\n                ')
                    else:
                        __content = __cache_139673028398240
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f0833655030> name=None at 7f0833655300> -> __attrs_139673028397328
                    __attrs_139673028397328 = _static_139673198743600

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __default_139673028406016
                    __default_139673028406016 = _DEFAULT_MARKER

                    # <Value 'view/form/render' (236:44)> -> __cache_139673028402656
                    __token = 12241
                    try:
                        __zt_tmp = __attrs_139673028397328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139673028402656 = _static_139673118568608('path', 'view/form/render', econtext=econtext)(_static_139673118568320(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/form/render' (236:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f082eb5a980> at 7f08293e3760> -> __condition
                    __expression = __cache_139673028402656

                    # <Symbol value=<DEFAULT> at 7f082eb5a980> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div />')
                    else:
                        __content = __cache_139673028402656
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n            </fieldset>\n        </div>')
                __append('\n    </div>\n')
                __i18n_domain = __previous_i18n_domain_139673029901664
            if (__backup_auth_token_139673027991328 is __marker):
                del econtext['auth_token']
            else:
                econtext['auth_token'] = __backup_auth_token_139673027991328
            if (__backup_wtool_139673027997856 is __marker):
                del econtext['wtool']
            else:
                econtext['wtool'] = __backup_wtool_139673027997856
            if (__backup_errors_139673027988784 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_139673027988784
            if (__backup_showCommenterImage_139673027986768 is __marker):
                del econtext['showCommenterImage']
            else:
                econtext['showCommenterImage'] = __backup_showCommenterImage_139673027986768
            if (__backup_has_replies_139673027986672 is __marker):
                del econtext['has_replies']
            else:
                econtext['has_replies'] = __backup_has_replies_139673027986672
            if (__backup_replies_139673027987680 is __marker):
                del econtext['replies']
            else:
                econtext['replies'] = __backup_replies_139673027987680
            if (__backup_canReview_139673027988352 is __marker):
                del econtext['canReview']
            else:
                econtext['canReview'] = __backup_canReview_139673027988352
            if (__backup_isAnon_139673027991808 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_139673027991808
            if (__backup_isDeleteOwnCommentAllowed_139673027988976 is __marker):
                del econtext['isDeleteOwnCommentAllowed']
            else:
                econtext['isDeleteOwnCommentAllowed'] = __backup_isDeleteOwnCommentAllowed_139673027988976
            if (__backup_isEditCommentAllowed_139673027990704 is __marker):
                del econtext['isEditCommentAllowed']
            else:
                econtext['isEditCommentAllowed'] = __backup_isEditCommentAllowed_139673027990704
            if (__backup_isAnonymousDiscussionAllowed_139673027990800 is __marker):
                del econtext['isAnonymousDiscussionAllowed']
            else:
                econtext['isAnonymousDiscussionAllowed'] = __backup_isAnonymousDiscussionAllowed_139673027990800
            if (__backup_isDiscussionAllowed_139673027994208 is __marker):
                del econtext['isDiscussionAllowed']
            else:
                econtext['isDiscussionAllowed'] = __backup_isDiscussionAllowed_139673027994208
            if (__backup_userHasReplyPermission_139673027996032 is __marker):
                del econtext['userHasReplyPermission']
            else:
                econtext['userHasReplyPermission'] = __backup_userHasReplyPermission_139673027996032
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }