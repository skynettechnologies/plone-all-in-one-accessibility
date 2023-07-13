# -*- coding: utf-8 -*-
__filename = '/home/skynet/my_project/plone.all_in_one_accessibility/eggs/plone.app.discussion-4.0.1-py3.10.egg/plone/app/discussion/browser/comments.pt'

__tokens = {46: ('view/can_reply', 1, 46), 104: (' view/is_discussion_allowe', 2, 42), 183: ('d view/anonymous_discussion_allow', 3, 50), 261: ('ed view/edit_comment_allo', 4, 41), 336: ('wed view/delete_own_comment_all', 5, 45), 398: ('Anon view/is_anon', 6, 25), 449: ('eview view/can_', 7, 27), 496: ('eplies python:view.get_replies(can', 8, 24), 566: ('replies python:view.has_replies(ca', 9, 27), 643: ('terImage view/show_commen', 10, 33), 699: ('   errors options/state/getErro', 11, 20), 760: ('     wtool context/@@plone_too', 12, 18), 825: (' auth_token context/@@authenticator/t', 13, 22), 895: ('python:isDiscussionAllowed or has_replies', 14, 19), 1050: ('python:isAnon and not isAnonymousDiscussionAllowed', 18, 27), 1144: ('view/login_action', 19, 41), 1567: ('has_replies', 29, 27), 1628: ('replies', 30, 47), 1714: ('reply_dict/comment', 33, 38), 1773: (' reply/getI', 34, 39), 1820: ('h reply_dict/depth|python', 35, 33), 1881: ("th python: depth > 10 and '10' or de", 36, 32), 1963: ('url python:view.get_commenter_home_url(username=reply.author_usern', 37, 41), 2075: ('link python:author_home_url and not i', 38, 40), 2155: ('t_url python:view.get_commenter_portrait(reply.author_use', 39, 36), 2255: ("_state python:wtool.getInfoFor(reply, 'review_state', ", 40, 35), 2347: ('canEdit python:view.can_edi', 41, 29), 2414: ('anDelete python:view.can_dele', 42, 30), 2484: ("olorclass python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else '", 43, 30), 2817: ("python:canReview or review_state == 'published'", 46, 35), 2641: ("python:'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))", 44, 42), 2769: (' comment_i', 45, 35), 3091: ('showCommenterImage', 52, 43), 3198: ('has_author_link', 54, 47), 3268: ('author_home_url', 55, 53), 3444: ('portrait_url', 58, 56), 3461: (' reply/author_nam', 58, 73), 3658: ('not: has_author_link', 62, 47), 3732: ('portrait_url', 63, 52), 3749: (' reply/author_nam', 63, 69), 4001: ('has_author_link', 70, 47), 4071: ('author_home_url', 71, 53), 4088: ('${reply/author_name}', 71, 70), 4090: ('reply/author_name', 71, 72), 4163: ('not: has_author_link', 73, 49), 4185: ('${reply/author_name}', 73, 71), 4187: ('reply/author_name', 73, 73), 4263: ('not: reply/author_name', 75, 49), 4505: ('python:view.format_time(reply.modification_date)', 81, 45), 4842: ('reply/getText', 93, 53), 5107: ('python:isEditCommentAllowed and canEdit', 99, 47), 5364: ('auth_token', 103, 51), 5433: ('string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', 104, 57), 5842: ('not: auth_token', 111, 51), 5918: ('string:${reply/absolute_url}/@@edit-comment', 112, 59), 6013: (' string:edit-${comment_id', 113, 50), 6659: ('python:canDelete', 127, 47), 7011: ('python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', 134, 51), 7155: ('string:${reply/absolute_url}/@@delete-own-comment', 135, 59), 7259: (" python:view.can_delete_own(reply) and 'display: inline' or 'display: none", 136, 53), 7385: ('d string:delete-${comment_i', 137, 49), 8210: ('python:canDelete', 151, 51), 8287: ('string:${reply/absolute_url}/@@moderate-delete-comment', 152, 59), 8393: (' string:delete-${comment_id', 153, 50), 9070: ('reply_dict/actions|nothing', 165, 47), 9371: ('canReview', 171, 51), 9437: ('reply_dict/actions|nothing', 172, 55), 9625: (' action/i', 174, 52), 9524: ('string:${reply/absolute_url}/@@transmit-comment', 173, 59), 9284: ('comment-action action-${action/id}', 170, 43), 9308: ('action/id', 170, 67), 9686: ('d string:${action/id}-${comment_i', 175, 49), 9956: ('action/id', 179, 62), 10240: ('${action/title}', 183, 58), 10242: ('action/title', 183, 60), 10607: ('python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 194, 39), 10905: ('python: has_replies and not isDiscussionAllowed', 203, 32), 11179: ('python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)', 212, 27), 11291: ('view/login_action', 213, 41), 11795: ('python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 225, 27), 12034: ('view/comment_transform_message', 231, 32), 12241: ('view/form/render', 236, 44)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139922408319408 = {'id': 'commenting', 'class': 'reply border p-3', }
_static_139922408322192 = {'class': 'standalone loginbutton btn btn-primary', 'type': 'submit', 'value': 'Log in to add comments', }
_static_139922408313696 = {'class': 'mb-3', 'action': 'view/login_action', }
_static_139922408315472 = {'class': 'reply', }
_static_139922408066544 = {'class': 'discreet', }
_static_139922408322816 = {'class': 'context reply-to-comment-button hide allowMultiSubmit btn btn-primary btn-sm', }
_static_139922408311344 = {'name': 'form.button.TransmitComment', 'class': 'context btn btn-primary btn-sm', 'type': 'submit', }
_static_139922408323008 = {'type': 'hidden', 'name': 'workflow_action', 'value': 'action/id', }
_static_139922408239696 = {'name': '', 'action': '', 'method': 'get', 'class': 'comment-action action-${action/id}', 'id': 'string:${action/id}-${comment_id}', }
_static_139922408231968 = {'class': 'comment-actions actions-workflow d-flex flex-row', }
_static_139922408227648 = {'name': 'form.button.DeleteComment', 'class': 'destructive btn btn-danger btn-sm', 'type': 'submit', 'value': 'Delete', }
_static_139922408235808 = {'name': 'delete', 'action': '', 'method': 'post', 'class': 'comment-action action-delete', 'id': 'string:delete-${comment_id}', }
_static_139922408234992 = {'name': 'form.button.DeleteComment', 'class': 'destructive btn btn-danger btn-sm', 'type': 'submit', 'value': 'Delete', }
_static_139922408287120 = {'name': 'delete', 'action': '', 'method': 'post', 'class': 'comment-action action-delete', 'style': "python:view.can_delete_own(reply) and 'display: inline' or 'display: none'", 'id': 'string:delete-${comment_id}', }
_static_139922408276416 = {'class': 'comment-actions actions-delete', }
_static_139922408287408 = {'name': 'form.button.EditComment', 'class': 'context btn btn-primary btn-sm', 'type': 'submit', 'value': 'Edit', }
_static_139922408279728 = {'name': 'edit', 'action': '', 'method': 'get', 'class': 'comment-action action-edit', 'id': 'string:edit-${comment_id}', }
_static_139922408280304 = {'class': 'pat-plone-modal context comment-action action-edit btn btn-primary btn-sm', 'href': 'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', }
_static_139922408284144 = {'class': 'comment-actions actions-edit', }
_static_139922408287648 = {'class': 'd-flex flex-row justify-content-end mb-3', }
_static_139922408139616 = {'class': 'comment-body', }
_static_139922408128816 = {'class': 'text-muted', }
_static_139922408130832 = {'href': '', }
_static_139922408132704 = {'class': 'comment-author', }
_static_139922408133520 = {'src': 'defaultUser.png', 'alt': '', }
_static_139922408139328 = {'src': 'defaultUser.png', 'alt': '', }
_static_139922408069520 = {'href': '', }
_static_139922408074944 = {'class': 'comment-image me-3', }
_static_139922408077248 = {'class': 'd-flex flex-row align-items-center mb-3', }
_static_139922408067024 = {'class': 'comment', 'id': 'comment_id', }
_static_139922408063952 = {'class': 'discussion', }
_static_139922408065440 = {'class': 'btn btn-primary mb-3', 'type': 'submit', 'value': 'Log in to add comments', }
_static_139922408027520 = {'action': 'view/login_action', }
_static_139922408027232 = {'class': 'reply', }
_static_139922408025024 = {'class': 'pat-discussion', }
_static_139922496189968 = __C2ZContextWrapper
_static_139922496190256 = __compile_zt_expr
_static_139922496178928 = {}

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

            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408151440
            __attrs_139922408151440 = _static_139922496178928
            __backup_userHasReplyPermission_139922408193664 = get('userHasReplyPermission', __marker)

            # <Value 'view/can_reply' (1:46)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'view/can_reply', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['userHasReplyPermission'] = __value
            __backup_isDiscussionAllowed_139922408193808 = get('isDiscussionAllowed', __marker)

            # <Value 'view/is_discussion_allowed' (2:42)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'view/is_discussion_allowed', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['isDiscussionAllowed'] = __value
            __backup_isAnonymousDiscussionAllowed_139922442814512 = get('isAnonymousDiscussionAllowed', __marker)

            # <Value 'view/anonymous_discussion_allowed' (3:50)> -> __value
            __token = 183
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'view/anonymous_discussion_allowed', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['isAnonymousDiscussionAllowed'] = __value
            __backup_isEditCommentAllowed_139922408152064 = get('isEditCommentAllowed', __marker)

            # <Value 'view/edit_comment_allowed' (4:41)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'view/edit_comment_allowed', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['isEditCommentAllowed'] = __value
            __backup_isDeleteOwnCommentAllowed_139922408153456 = get('isDeleteOwnCommentAllowed', __marker)

            # <Value 'view/delete_own_comment_allowed' (5:45)> -> __value
            __token = 336
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'view/delete_own_comment_allowed', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['isDeleteOwnCommentAllowed'] = __value
            __backup_isAnon_139922408154512 = get('isAnon', __marker)

            # <Value 'view/is_anonymous' (6:25)> -> __value
            __token = 398
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'view/is_anonymous', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_canReview_139922408154560 = get('canReview', __marker)

            # <Value 'view/can_review' (7:27)> -> __value
            __token = 449
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'view/can_review', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['canReview'] = __value
            __backup_replies_139922408151104 = get('replies', __marker)

            # <Value 'python:view.get_replies(canReview)' (8:24)> -> __value
            __token = 496
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('python', 'view.get_replies(canReview)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['replies'] = __value
            __backup_has_replies_139922408152400 = get('has_replies', __marker)

            # <Value 'python:view.has_replies(canReview)' (9:27)> -> __value
            __token = 566
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('python', 'view.has_replies(canReview)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['has_replies'] = __value
            __backup_showCommenterImage_139922408151056 = get('showCommenterImage', __marker)

            # <Value 'view/show_commenter_image' (10:33)> -> __value
            __token = 643
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'view/show_commenter_image', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['showCommenterImage'] = __value
            __backup_errors_139922408150768 = get('errors', __marker)

            # <Value 'options/state/getErrors|nothing' (11:20)> -> __value
            __token = 699
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'options/state/getErrors|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_wtool_139922408151392 = get('wtool', __marker)

            # <Value 'context/@@plone_tools/workflow' (12:18)> -> __value
            __token = 760
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'context/@@plone_tools/workflow', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['wtool'] = __value
            __backup_auth_token_139922408150816 = get('auth_token', __marker)

            # <Value 'context/@@authenticator/token|nothing' (13:22)> -> __value
            __token = 825
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139922496190256('path', 'context/@@authenticator/token|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            econtext['auth_token'] = __value

            # <Value 'python:isDiscussionAllowed or has_replies' (14:19)> -> __condition
            __token = 895
            try:
                __zt_tmp = __attrs_139922408151440
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139922496190256('python', 'isDiscussionAllowed or has_replies', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139922408027760 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f42396d2bc0> name=None at 7f42396d31f0> -> __attrs_139922408024352
                __attrs_139922408024352 = _static_139922408025024

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-discussion">\n        ')

                # <Static value=<ast.Dict object at 0x7f42396d3460> name=None at 7f42396d0580> -> __attrs_139922408025360
                __attrs_139922408025360 = _static_139922408027232

                # <Value 'python:isAnon and not isAnonymousDiscussionAllowed' (18:27)> -> __condition
                __token = 1050
                try:
                    __zt_tmp = __attrs_139922408025360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('python', 'isAnon and not isAnonymousDiscussionAllowed', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply">\n            ')

                    # <Static value=<ast.Dict object at 0x7f42396d3580> name=None at 7f42396d0550> -> __attrs_139922408026032
                    __attrs_139922408026032 = _static_139922408027520

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408027904
                    __default_139922408027904 = _DEFAULT_MARKER

                    # <Substitution 'view/login_action' (19:41)> -> __attr_action
                    __token = 1144
                    try:
                        __zt_tmp = __attrs_139922408026032
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_139922496190256('path', 'view/login_action', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x7f42396dc9a0> name=None at 7f423b812fe0> -> __attrs_139922408065104
                    __attrs_139922408065104 = _static_139922408065440

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-primary mb-3" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408070144
                    __default_139922408070144 = _DEFAULT_MARKER

                    # <Translate msgid='label_login_to_add_comments' node=<ast.Constant object at 0x7f42396de7d0> at 7f42396de650> -> __attr_value
                    __attr_value = 'Log in to add comments'
                    __attr_value = translate('label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_139922442889024 = []
                    __append_139922442889024 = __stream_139922442889024.append
                    __append_139922442889024('Log in to add comments')
                    __msgid_139922442889024 = __re_whitespace(''.join(__stream_139922442889024)).strip()
                    if 'label_login_to_add_comments':
                        __append(translate('label_login_to_add_comments', mapping=None, default=__msgid_139922442889024, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f42396dc3d0> name=None at 7f42396dc730> -> __attrs_139922408063232
                __attrs_139922408063232 = _static_139922408063952

                # <Value 'has_replies' (29:27)> -> __condition
                __token = 1567
                try:
                    __zt_tmp = __attrs_139922408063232
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('path', 'has_replies', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="discussion">\n            ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408067360
                    __attrs_139922408067360 = _static_139922496178928
                    __backup_reply_dict_139922408025504 = get('reply_dict', __marker)

                    # <Value 'replies' (30:47)> -> __iterator
                    __token = 1628
                    try:
                        __zt_tmp = __attrs_139922408067360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139922496190256('path', 'replies', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    (__iterator, ____index_139922408073120, ) = getname('repeat')('reply_dict', __iterator)
                    econtext['reply_dict'] = None
                    for __item in __iterator:
                        econtext['reply_dict'] = __item
                        __append('\n\n                ')

                        # <Static value=<ast.Dict object at 0x7f42396dcfd0> name=None at 7f42396dce80> -> __attrs_139922408070432
                        __attrs_139922408070432 = _static_139922408067024
                        __backup_reply_139922408014272 = get('reply', __marker)

                        # <Value 'reply_dict/comment' (33:38)> -> __value
                        __token = 1714
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('path', 'reply_dict/comment', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['reply'] = __value
                        __backup_comment_id_139922442891664 = get('comment_id', __marker)

                        # <Value 'reply/getId' (34:39)> -> __value
                        __token = 1773
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('path', 'reply/getId', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['comment_id'] = __value
                        __backup_depth_139922408078496 = get('depth', __marker)

                        # <Value 'reply_dict/depth|python:0' (35:33)> -> __value
                        __token = 1820
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('path', 'reply_dict/depth|python:0', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_depth_139922408076960 = get('depth', __marker)

                        # <Value "python: depth > 10 and '10' or depth" (36:32)> -> __value
                        __token = 1881
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('python', " depth > 10 and '10' or depth", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_author_home_url_139922408070528 = get('author_home_url', __marker)

                        # <Value 'python:view.get_commenter_home_url(username=reply.author_username)' (37:41)> -> __value
                        __token = 1963
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('python', 'view.get_commenter_home_url(username=reply.author_username)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['author_home_url'] = __value
                        __backup_has_author_link_139922408076480 = get('has_author_link', __marker)

                        # <Value 'python:author_home_url and not isAnon' (38:40)> -> __value
                        __token = 2075
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('python', 'author_home_url and not isAnon', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['has_author_link'] = __value
                        __backup_portrait_url_139922408072304 = get('portrait_url', __marker)

                        # <Value 'python:view.get_commenter_portrait(reply.author_username)' (39:36)> -> __value
                        __token = 2155
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('python', 'view.get_commenter_portrait(reply.author_username)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['portrait_url'] = __value
                        __backup_review_state_139922408072544 = get('review_state', __marker)

                        # <Value "python:wtool.getInfoFor(reply, 'review_state', 'none')" (40:35)> -> __value
                        __token = 2255
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('python', "wtool.getInfoFor(reply, 'review_state', 'none')", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['review_state'] = __value
                        __backup_canEdit_139922408070960 = get('canEdit', __marker)

                        # <Value 'python:view.can_edit(reply)' (41:29)> -> __value
                        __token = 2347
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('python', 'view.can_edit(reply)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['canEdit'] = __value
                        __backup_canDelete_139922408071776 = get('canDelete', __marker)

                        # <Value 'python:view.can_delete(reply)' (42:30)> -> __value
                        __token = 2414
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('python', 'view.can_delete(reply)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['canDelete'] = __value
                        __backup_colorclass_139922408070240 = get('colorclass', __marker)

                        # <Value "python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)" (43:30)> -> __value
                        __token = 2484
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139922496190256('python', "lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        econtext['colorclass'] = __value

                        # <Value "python:canReview or review_state == 'published'" (46:35)> -> __condition
                        __token = 2817
                        try:
                            __zt_tmp = __attrs_139922408070432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139922496190256('python', "canReview or review_state == 'published'", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div')

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408076864
                            __default_139922408076864 = _DEFAULT_MARKER

                            # <Substitution "python:'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))" (44:42)> -> __attr_class
                            __token = 2641
                            try:
                                __zt_tmp = __attrs_139922408070432
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_139922496190256('python', "'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', 'comment', _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408066928
                            __default_139922408066928 = _DEFAULT_MARKER

                            # <Substitution 'comment_id' (45:35)> -> __attr_id
                            __token = 2769
                            try:
                                __zt_tmp = __attrs_139922408070432
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_139922496190256('path', 'comment_id', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((' id="%s"' % __attr_id))
                            __append('>\n\n                    ')

                            # <Static value=<ast.Dict object at 0x7f42396df7c0> name=None at 7f42396decb0> -> __attrs_139922408073504
                            __attrs_139922408073504 = _static_139922408077248

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="d-flex flex-row align-items-center mb-3">\n\n                        <!-- commenter image -->\n                        ')

                            # <Static value=<ast.Dict object at 0x7f42396deec0> name=None at 7f42396dd390> -> __attrs_139922408078688
                            __attrs_139922408078688 = _static_139922408074944

                            # <Value 'showCommenterImage' (52:43)> -> __condition
                            __token = 3091
                            try:
                                __zt_tmp = __attrs_139922408078688
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('path', 'showCommenterImage', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-image me-3">\n                            ')

                                # <Static value=<ast.Dict object at 0x7f42396dd990> name=None at 7f42396dde10> -> __attrs_139922408142160
                                __attrs_139922408142160 = _static_139922408069520

                                # <Value 'has_author_link' (54:47)> -> __condition
                                __token = 3198
                                try:
                                    __zt_tmp = __attrs_139922408142160
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139922496190256('path', 'has_author_link', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408071488
                                    __default_139922408071488 = _DEFAULT_MARKER

                                    # <Substitution 'author_home_url' (55:53)> -> __attr_href
                                    __token = 3268
                                    try:
                                        __zt_tmp = __attrs_139922408142160
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_139922496190256('path', 'author_home_url', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((' href="%s"' % __attr_href))
                                    __append('>\n                                ')

                                    # <Static value=<ast.Dict object at 0x7f42396eea40> name=None at 7f42396eda50> -> __attrs_139922408129776
                                    __attrs_139922408129776 = _static_139922408139328

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<img')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408137120
                                    __default_139922408137120 = _DEFAULT_MARKER

                                    # <Substitution 'portrait_url' (58:56)> -> __attr_src
                                    __token = 3444
                                    try:
                                        __zt_tmp = __attrs_139922408129776
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_139922496190256('path', 'portrait_url', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', 'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408137024
                                    __default_139922408137024 = _DEFAULT_MARKER

                                    # <Substitution 'reply/author_name' (58:73)> -> __attr_alt
                                    __token = 3461
                                    try:
                                        __zt_tmp = __attrs_139922408129776
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_139922496190256('path', 'reply/author_name', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((' alt="%s"' % __attr_alt))
                                    __append(' />\n                            </a>')
                                __append('\n                            ')

                                # <Static value=<ast.Dict object at 0x7f42396ed390> name=None at 7f42396ef1f0> -> __attrs_139922408141104
                                __attrs_139922408141104 = _static_139922408133520

                                # <Value 'not: has_author_link' (62:47)> -> __condition
                                __token = 3658
                                try:
                                    __zt_tmp = __attrs_139922408141104
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139922496190256('not', ' has_author_link', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                if __condition:

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<img')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408142208
                                    __default_139922408142208 = _DEFAULT_MARKER

                                    # <Substitution 'portrait_url' (63:52)> -> __attr_src
                                    __token = 3732
                                    try:
                                        __zt_tmp = __attrs_139922408141104
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_139922496190256('path', 'portrait_url', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', 'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408130592
                                    __default_139922408130592 = _DEFAULT_MARKER

                                    # <Substitution 'reply/author_name' (63:69)> -> __attr_alt
                                    __token = 3749
                                    try:
                                        __zt_tmp = __attrs_139922408141104
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_139922496190256('path', 'reply/author_name', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((' alt="%s"' % __attr_alt))
                                    __append(' />')
                                __append('\n                        </div>')
                            __append('\n\n                        <!-- commenter name and date -->\n                        ')

                            # <Static value=<ast.Dict object at 0x7f42396ed060> name=None at 7f42396ece20> -> __attrs_139922408144800
                            __attrs_139922408144800 = _static_139922408132704

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="comment-author">\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f42396ec910> name=None at 7f42396efd30> -> __attrs_139922408143696
                            __attrs_139922408143696 = _static_139922408130832

                            # <Value 'has_author_link' (70:47)> -> __condition
                            __token = 4001
                            try:
                                __zt_tmp = __attrs_139922408143696
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('path', 'has_author_link', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408144080
                                __default_139922408144080 = _DEFAULT_MARKER

                                # <Substitution 'author_home_url' (71:53)> -> __attr_href
                                __token = 4071
                                try:
                                    __zt_tmp = __attrs_139922408143696
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_139922496190256('path', 'author_home_url', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))
                                __append('>')

                                # <Interpolation value=<Substitution '${reply/author_name}' (71:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f42396ecdc0> -> __content_139922583708144
                                __token = 4088
                                __token = 4090
                                try:
                                    __zt_tmp = __attrs_139922408143696
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_139922583708144 = _static_139922496190256('path', 'reply/author_name', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                __content_139922583708144 = __quote(__content_139922583708144, '\x00', '&#0;', None, None)
                                __content_139922583708144 = __content_139922583708144
                                if (__content_139922583708144 is None):
                                    pass
                                else:
                                    if (__content_139922583708144 is None):
                                        __content_139922583708144 = None
                                    else:
                                        __tt = type(__content_139922583708144)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139922583708144 = str(__content_139922583708144)
                                        else:
                                            if (__tt is bytes):
                                                __content_139922583708144 = decode(__content_139922583708144)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139922583708144 = __content_139922583708144.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139922583708144)
                                                        __content_139922583708144 = (str(__content_139922583708144) if (__content_139922583708144 is __converted) else __converted)
                                                    else:
                                                        __content_139922583708144 = __content_139922583708144()
                                if (__content_139922583708144 is not None):
                                    __append(__content_139922583708144)
                                __append('</a>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408132896
                            __attrs_139922408132896 = _static_139922496178928

                            # <Value 'not: has_author_link' (73:49)> -> __condition
                            __token = 4163
                            try:
                                __zt_tmp = __attrs_139922408132896
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('not', ' has_author_link', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span>')

                                # <Interpolation value=<Substitution '${reply/author_name}' (73:71)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f42396ef6a0> -> __content_139922583708144
                                __token = 4185
                                __token = 4187
                                try:
                                    __zt_tmp = __attrs_139922408132896
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_139922583708144 = _static_139922496190256('path', 'reply/author_name', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                __content_139922583708144 = __quote(__content_139922583708144, '\x00', '&#0;', None, None)
                                __content_139922583708144 = __content_139922583708144
                                if (__content_139922583708144 is None):
                                    pass
                                else:
                                    if (__content_139922583708144 is None):
                                        __content_139922583708144 = None
                                    else:
                                        __tt = type(__content_139922583708144)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139922583708144 = str(__content_139922583708144)
                                        else:
                                            if (__tt is bytes):
                                                __content_139922583708144 = decode(__content_139922583708144)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139922583708144 = __content_139922583708144.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139922583708144)
                                                        __content_139922583708144 = (str(__content_139922583708144) if (__content_139922583708144 is __converted) else __converted)
                                                    else:
                                                        __content_139922583708144 = __content_139922583708144()
                                if (__content_139922583708144 is not None):
                                    __append(__content_139922583708144)
                                __append('</span>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408141488
                            __attrs_139922408141488 = _static_139922496178928

                            # <Value 'not: reply/author_name' (75:49)> -> __condition
                            __token = 4263
                            try:
                                __zt_tmp = __attrs_139922408141488
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('not', ' reply/author_name', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span>')
                                __stream_139922408134432 = []
                                __append_139922408134432 = __stream_139922408134432.append
                                __append_139922408134432('Anonymous')
                                __msgid_139922408134432 = __re_whitespace(''.join(__stream_139922408134432)).strip()
                                if 'label_anonymous':
                                    __append(translate('label_anonymous', mapping=None, default=__msgid_139922408134432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</span>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408130928
                            __attrs_139922408130928 = _static_139922496178928

                            # <br ... (0:0)
                            # --------------------------------------------------------
                            __append('<br />\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f42396ec130> name=None at 7f42396ef640> -> __attrs_139922408131792
                            __attrs_139922408131792 = _static_139922408128816

                            # <small ... (0:0)
                            # --------------------------------------------------------
                            __append('<small class="text-muted">')

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408143216
                            __default_139922408143216 = _DEFAULT_MARKER

                            # <Value 'python:view.format_time(reply.modification_date)' (81:45)> -> __cache_139922408130544
                            __token = 4505
                            try:
                                __zt_tmp = __attrs_139922408131792
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139922408130544 = _static_139922496190256('python', 'view.format_time(reply.modification_date)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.format_time(reply.modification_date)' (81:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42396ef760> -> __condition
                            __expression = __cache_139922408130544

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('\n                      8/23/2001 12:40:44 PM\n                            ')
                            else:
                                __content = __cache_139922408130544
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</small>\n\n                        </div>\n                    </div>\n\n\n\n                    <!-- comment body -->\n                    ')

                            # <Static value=<ast.Dict object at 0x7f42396eeb60> name=None at 7f42396eebc0> -> __attrs_139922408140576
                            __attrs_139922408140576 = _static_139922408139616

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="comment-body">\n\n                        ')

                            # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408136304
                            __attrs_139922408136304 = _static_139922496178928

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408136064
                            __default_139922408136064 = _DEFAULT_MARKER

                            # <Value 'reply/getText' (93:53)> -> __cache_139922408135008
                            __token = 4842
                            try:
                                __zt_tmp = __attrs_139922408136304
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139922408135008 = _static_139922496190256('path', 'reply/getText', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                            # <BinOp left=<Value 'reply/getText' (93:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42396ee470> -> __condition
                            __expression = __cache_139922408135008

                            # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span />')
                            else:
                                __content = __cache_139922408135008
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n\n                        <!-- comment actions -->\n                        ')

                            # <Static value=<ast.Dict object at 0x7f4239712da0> name=None at 7f42396ee110> -> __attrs_139922408285344
                            __attrs_139922408285344 = _static_139922408287648

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="d-flex flex-row justify-content-end mb-3">\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f4239711ff0> name=None at 7f4239712380> -> __attrs_139922408276800
                            __attrs_139922408276800 = _static_139922408284144

                            # <Value 'python:isEditCommentAllowed and canEdit' (99:47)> -> __condition
                            __token = 5107
                            try:
                                __zt_tmp = __attrs_139922408276800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('python', 'isEditCommentAllowed and canEdit', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-edit">\n\n                                <!-- edit -->\n                                ')

                                # <Static value=<ast.Dict object at 0x7f42397110f0> name=None at 7f4239712560> -> __attrs_139922408277184
                                __attrs_139922408277184 = _static_139922408280304

                                # <Value 'auth_token' (103:51)> -> __condition
                                __token = 5364
                                try:
                                    __zt_tmp = __attrs_139922408277184
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139922496190256('path', 'auth_token', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a class="pat-plone-modal context comment-action action-edit btn btn-primary btn-sm"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408277712
                                    __default_139922408277712 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}' (104:57)> -> __attr_href
                                    __token = 5433
                                    try:
                                        __zt_tmp = __attrs_139922408277184
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_139922496190256('string', '${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((' href="%s"' % __attr_href))
                                    __append('>')
                                    __stream_139922408279248 = []
                                    __append_139922408279248 = __stream_139922408279248.append
                                    __append_139922408279248('Edit')
                                    __msgid_139922408279248 = __re_whitespace(''.join(__stream_139922408279248)).strip()
                                    if 'Edit':
                                        __append(translate('Edit', mapping=None, default=__msgid_139922408279248, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</a>')
                                __append('\n\n                                ')

                                # <Static value=<ast.Dict object at 0x7f4239710eb0> name=None at 7f42397108b0> -> __attrs_139922408277808
                                __attrs_139922408277808 = _static_139922408279728

                                # <Value 'not: auth_token' (111:51)> -> __condition
                                __token = 5842
                                try:
                                    __zt_tmp = __attrs_139922408277808
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139922496190256('not', ' auth_token', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="edit"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408285920
                                    __default_139922408285920 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@edit-comment' (112:59)> -> __attr_action
                                    __token = 5918
                                    try:
                                        __zt_tmp = __attrs_139922408277808
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_139922496190256('string', '${reply/absolute_url}/@@edit-comment', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="get" class="comment-action action-edit"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408285200
                                    __default_139922408285200 = _DEFAULT_MARKER

                                    # <Substitution 'string:edit-${comment_id}' (113:50)> -> __attr_id
                                    __token = 6013
                                    try:
                                        __zt_tmp = __attrs_139922408277808
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_139922496190256('string', 'edit-${comment_id}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n\n                                    ')

                                    # <Static value=<ast.Dict object at 0x7f4239712cb0> name=None at 7f42397131f0> -> __attrs_139922408289088
                                    __attrs_139922408289088 = _static_139922408287408

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.EditComment" class="context btn btn-primary btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408284432
                                    __default_139922408284432 = _DEFAULT_MARKER

                                    # <Translate msgid='label_edit' node=<ast.Constant object at 0x7f4239713010> at 7f4239713100> -> __attr_value
                                    __attr_value = 'Edit'
                                    __attr_value = translate('label_edit', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_139922408278528 = []
                                    __append_139922408278528 = __stream_139922408278528.append
                                    __append_139922408278528('Edit')
                                    __msgid_139922408278528 = __re_whitespace(''.join(__stream_139922408278528)).strip()
                                    if 'label_edit':
                                        __append(translate('label_edit', mapping=None, default=__msgid_139922408278528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n\n                                </form>')
                                __append('\n\n                            </div>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f42397101c0> name=None at 7f4239711c30> -> __attrs_139922408292208
                            __attrs_139922408292208 = _static_139922408276416

                            # <Value 'python:canDelete' (127:47)> -> __condition
                            __token = 6659
                            try:
                                __zt_tmp = __attrs_139922408292208
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('python', 'canDelete', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-delete">\n\n                                <!-- delete own comment -->\n                                ')

                                # <Static value=<ast.Dict object at 0x7f4239712b90> name=None at 7f4239712800> -> __attrs_139922408239984
                                __attrs_139922408239984 = _static_139922408287120

                                # <Value 'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)' (134:51)> -> __condition
                                __token = 7011
                                try:
                                    __zt_tmp = __attrs_139922408239984
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139922496190256('python', 'not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="delete"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408290528
                                    __default_139922408290528 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@delete-own-comment' (135:59)> -> __attr_action
                                    __token = 7155
                                    try:
                                        __zt_tmp = __attrs_139922408239984
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_139922496190256('string', '${reply/absolute_url}/@@delete-own-comment', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="post" class="comment-action action-delete"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408290768
                                    __default_139922408290768 = _DEFAULT_MARKER

                                    # <Substitution "python:view.can_delete_own(reply) and 'display: inline' or 'display: none'" (136:53)> -> __attr_style
                                    __token = 7259
                                    try:
                                        __zt_tmp = __attrs_139922408239984
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_style = _static_139922496190256('python', "view.can_delete_own(reply) and 'display: inline' or 'display: none'", econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_style is not None):
                                        __append((' style="%s"' % __attr_style))

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408285680
                                    __default_139922408285680 = _DEFAULT_MARKER

                                    # <Substitution 'string:delete-${comment_id}' (137:49)> -> __attr_id
                                    __token = 7385
                                    try:
                                        __zt_tmp = __attrs_139922408239984
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_139922496190256('string', 'delete-${comment_id}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n                                    ')

                                    # <Static value=<ast.Dict object at 0x7f4239705ff0> name=None at 7f4239706710> -> __attrs_139922408229136
                                    __attrs_139922408229136 = _static_139922408234992

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.DeleteComment" class="destructive btn btn-danger btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408233024
                                    __default_139922408233024 = _DEFAULT_MARKER

                                    # <Translate msgid='label_delete' node=<ast.Constant object at 0x7f42397078b0> at 7f4239707d30> -> __attr_value
                                    __attr_value = 'Delete'
                                    __attr_value = translate('label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_139922408243008 = []
                                    __append_139922408243008 = __stream_139922408243008.append
                                    __append_139922408243008('Delete')
                                    __msgid_139922408243008 = __re_whitespace(''.join(__stream_139922408243008)).strip()
                                    if 'label_delete':
                                        __append(translate('label_delete', mapping=None, default=__msgid_139922408243008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n                                </form>')
                                __append('\n\n                                <!-- delete -->\n                                ')

                                # <Static value=<ast.Dict object at 0x7f4239706320> name=None at 7f4239706a10> -> __attrs_139922408232880
                                __attrs_139922408232880 = _static_139922408235808

                                # <Value 'python:canDelete' (151:51)> -> __condition
                                __token = 8210
                                try:
                                    __zt_tmp = __attrs_139922408232880
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139922496190256('python', 'canDelete', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="delete"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408236768
                                    __default_139922408236768 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@moderate-delete-comment' (152:59)> -> __attr_action
                                    __token = 8287
                                    try:
                                        __zt_tmp = __attrs_139922408232880
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_139922496190256('string', '${reply/absolute_url}/@@moderate-delete-comment', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="post" class="comment-action action-delete"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408229184
                                    __default_139922408229184 = _DEFAULT_MARKER

                                    # <Substitution 'string:delete-${comment_id}' (153:50)> -> __attr_id
                                    __token = 8393
                                    try:
                                        __zt_tmp = __attrs_139922408232880
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_139922496190256('string', 'delete-${comment_id}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n                                    ')

                                    # <Static value=<ast.Dict object at 0x7f4239704340> name=None at 7f4239704490> -> __attrs_139922408230960
                                    __attrs_139922408230960 = _static_139922408227648

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.DeleteComment" class="destructive btn btn-danger btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408227744
                                    __default_139922408227744 = _DEFAULT_MARKER

                                    # <Translate msgid='label_delete' node=<ast.Constant object at 0x7f4239704d30> at 7f42397043d0> -> __attr_value
                                    __attr_value = 'Delete'
                                    __attr_value = translate('label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_139922408230096 = []
                                    __append_139922408230096 = __stream_139922408230096.append
                                    __append_139922408230096('Delete')
                                    __msgid_139922408230096 = __re_whitespace(''.join(__stream_139922408230096)).strip()
                                    if 'label_delete':
                                        __append(translate('label_delete', mapping=None, default=__msgid_139922408230096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n                                </form>')
                                __append('\n\n                            </div>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x7f4239705420> name=None at 7f4239705330> -> __attrs_139922408237488
                            __attrs_139922408237488 = _static_139922408231968

                            # <Value 'reply_dict/actions|nothing' (165:47)> -> __condition
                            __token = 9070
                            try:
                                __zt_tmp = __attrs_139922408237488
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('path', 'reply_dict/actions|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-workflow d-flex flex-row">\n\n                                ')

                                # <Static value=<ast.Dict object at 0x7f4239707250> name=None at 7f42397062c0> -> __attrs_139922408232400
                                __attrs_139922408232400 = _static_139922408239696

                                # <Value 'canReview' (171:51)> -> __condition
                                __token = 9371
                                try:
                                    __zt_tmp = __attrs_139922408232400
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_139922496190256('path', 'canReview', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                if __condition:
                                    __backup_action_139922408067936 = get('action', __marker)

                                    # <Value 'reply_dict/actions|nothing' (172:55)> -> __iterator
                                    __token = 9437
                                    try:
                                        __zt_tmp = __attrs_139922408232400
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __iterator = _static_139922496190256('path', 'reply_dict/actions|nothing', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                    (__iterator, ____index_139922408236192, ) = getname('repeat')('action', __iterator)
                                    econtext['action'] = None
                                    for __item in __iterator:
                                        econtext['action'] = __item

                                        # <form ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<form')

                                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408238160
                                        __default_139922408238160 = _DEFAULT_MARKER

                                        # <Substitution 'action/id' (174:52)> -> __attr_name
                                        __token = 9625
                                        try:
                                            __zt_tmp = __attrs_139922408232400
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_name = _static_139922496190256('path', 'action/id', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_name is not None):
                                            __append((' name="%s"' % __attr_name))

                                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408242528
                                        __default_139922408242528 = _DEFAULT_MARKER

                                        # <Substitution 'string:${reply/absolute_url}/@@transmit-comment' (173:59)> -> __attr_action
                                        __token = 9524
                                        try:
                                            __zt_tmp = __attrs_139922408232400
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_action = _static_139922496190256('string', '${reply/absolute_url}/@@transmit-comment', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_action is not None):
                                            __append((' action="%s"' % __attr_action))
                                        __append(' method="get"')

                                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408235664
                                        __default_139922408235664 = _DEFAULT_MARKER

                                        # <Interpolation value=<Substitution 'comment-action action-${action/id}' (170:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f4239707e50> -> __attr_class
                                        __token = 9284
                                        __token = 9308
                                        try:
                                            __zt_tmp = __attrs_139922408232400
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_class = _static_139922496190256('path', 'action/id', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
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

                                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408238928
                                        __default_139922408238928 = _DEFAULT_MARKER

                                        # <Substitution 'string:${action/id}-${comment_id}' (175:49)> -> __attr_id
                                        __token = 9686
                                        try:
                                            __zt_tmp = __attrs_139922408232400
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_id = _static_139922496190256('string', '${action/id}-${comment_id}', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_id is not None):
                                            __append((' id="%s"' % __attr_id))
                                        __append('>\n                                    ')

                                        # <Static value=<ast.Dict object at 0x7f423971b7c0> name=None at 7f423971b190> -> __attrs_139922408318640
                                        __attrs_139922408318640 = _static_139922408323008

                                        # <input ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<input type="hidden" name="workflow_action"')

                                        # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408309760
                                        __default_139922408309760 = _DEFAULT_MARKER

                                        # <Substitution 'action/id' (179:62)> -> __attr_value
                                        __token = 9956
                                        try:
                                            __zt_tmp = __attrs_139922408318640
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_value = _static_139922496190256('path', 'action/id', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_value is not None):
                                            __append((' value="%s"' % __attr_value))
                                        __append(' />\n                                    ')

                                        # <Static value=<ast.Dict object at 0x7f4239718a30> name=None at 7f4239719a80> -> __attrs_139922408322720
                                        __attrs_139922408322720 = _static_139922408311344

                                        # <button ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<button name="form.button.TransmitComment" class="context btn btn-primary btn-sm" type="submit">')
                                        __stream_139922408317920 = []
                                        __append_139922408317920 = __stream_139922408317920.append

                                        # <Interpolation value=<Substitution '${action/title}' (183:58)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f423971a710> -> __content_139922583708144
                                        __token = 10240
                                        __token = 10242
                                        try:
                                            __zt_tmp = __attrs_139922408322720
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __content_139922583708144 = _static_139922496190256('path', 'action/title', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                                        __content_139922583708144 = __quote(__content_139922583708144, '\x00', '&#0;', None, None)
                                        __content_139922583708144 = __content_139922583708144
                                        if (__content_139922583708144 is None):
                                            pass
                                        else:
                                            if (__content_139922583708144 is None):
                                                __content_139922583708144 = None
                                            else:
                                                __tt = type(__content_139922583708144)
                                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                    __content_139922583708144 = str(__content_139922583708144)
                                                else:
                                                    if (__tt is bytes):
                                                        __content_139922583708144 = decode(__content_139922583708144)
                                                    else:
                                                        if (__tt is not str):
                                                            try:
                                                                __content_139922583708144 = __content_139922583708144.__html__
                                                            except get('AttributeError', AttributeError):
                                                                __converted = convert(__content_139922583708144)
                                                                __content_139922583708144 = (str(__content_139922583708144) if (__content_139922583708144 is __converted) else __converted)
                                                            else:
                                                                __content_139922583708144 = __content_139922583708144()
                                        if (__content_139922583708144 is not None):
                                            __append_139922408317920(__content_139922583708144)
                                        __msgid_139922408317920 = __re_whitespace(''.join(__stream_139922408317920)).strip()
                                        if __msgid_139922408317920:
                                            __append(translate(__msgid_139922408317920, mapping=None, default=__msgid_139922408317920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                        __append('</button>\n                                </form>')
                                        ____index_139922408236192 -= 1
                                        if (____index_139922408236192 > 0):
                                            __append('\n                                ')
                                    if (__backup_action_139922408067936 is __marker):
                                        del econtext['action']
                                    else:
                                        econtext['action'] = __backup_action_139922408067936
                                __append('\n\n                            </div>')
                            __append('\n\n                        </div>\n                        <!-- end comment actions -->\n\n\n                    </div>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f423971b700> name=None at 7f4239718550> -> __attrs_139922408317584
                            __attrs_139922408317584 = _static_139922408322816

                            # <Value 'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (194:39)> -> __condition
                            __token = 10607
                            try:
                                __zt_tmp = __attrs_139922408317584
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139922496190256('python', 'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                            if __condition:

                                # <button ... (0:0)
                                # --------------------------------------------------------
                                __append('<button class="context reply-to-comment-button hide allowMultiSubmit btn btn-primary btn-sm">')
                                __stream_139922408235280 = []
                                __append_139922408235280 = __stream_139922408235280.append
                                __append_139922408235280('\n                    Reply\n                    ')
                                __msgid_139922408235280 = __re_whitespace(''.join(__stream_139922408235280)).strip()
                                if 'label_reply':
                                    __append(translate('label_reply', mapping=None, default=__msgid_139922408235280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</button>')
                            __append('\n\n                </div>')
                        if (__backup_colorclass_139922408070240 is __marker):
                            del econtext['colorclass']
                        else:
                            econtext['colorclass'] = __backup_colorclass_139922408070240
                        if (__backup_canDelete_139922408071776 is __marker):
                            del econtext['canDelete']
                        else:
                            econtext['canDelete'] = __backup_canDelete_139922408071776
                        if (__backup_canEdit_139922408070960 is __marker):
                            del econtext['canEdit']
                        else:
                            econtext['canEdit'] = __backup_canEdit_139922408070960
                        if (__backup_review_state_139922408072544 is __marker):
                            del econtext['review_state']
                        else:
                            econtext['review_state'] = __backup_review_state_139922408072544
                        if (__backup_portrait_url_139922408072304 is __marker):
                            del econtext['portrait_url']
                        else:
                            econtext['portrait_url'] = __backup_portrait_url_139922408072304
                        if (__backup_has_author_link_139922408076480 is __marker):
                            del econtext['has_author_link']
                        else:
                            econtext['has_author_link'] = __backup_has_author_link_139922408076480
                        if (__backup_author_home_url_139922408070528 is __marker):
                            del econtext['author_home_url']
                        else:
                            econtext['author_home_url'] = __backup_author_home_url_139922408070528
                        if (__backup_depth_139922408076960 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_139922408076960
                        if (__backup_depth_139922408078496 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_139922408078496
                        if (__backup_comment_id_139922442891664 is __marker):
                            del econtext['comment_id']
                        else:
                            econtext['comment_id'] = __backup_comment_id_139922442891664
                        if (__backup_reply_139922408014272 is __marker):
                            del econtext['reply']
                        else:
                            econtext['reply'] = __backup_reply_139922408014272
                        __append('\n\n            ')
                        ____index_139922408073120 -= 1
                        if (____index_139922408073120 > 0):
                            __append('')
                    if (__backup_reply_dict_139922408025504 is __marker):
                        del econtext['reply_dict']
                    else:
                        econtext['reply_dict'] = __backup_reply_dict_139922408025504
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f42396dcdf0> name=None at 7f42396dd090> -> __attrs_139922408323296
                    __attrs_139922408323296 = _static_139922408066544

                    # <Value 'python: has_replies and not isDiscussionAllowed' (203:32)> -> __condition
                    __token = 10905
                    try:
                        __zt_tmp = __attrs_139922408323296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139922496190256('python', ' has_replies and not isDiscussionAllowed', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="discreet">')
                        __stream_139922408065680 = []
                        __append_139922408065680 = __stream_139922408065680.append
                        __append_139922408065680('\n            Commenting has been disabled.\n            ')
                        __msgid_139922408065680 = __re_whitespace(''.join(__stream_139922408065680)).strip()
                        if 'label_commenting_disabled':
                            __append(translate('label_commenting_disabled', mapping=None, default=__msgid_139922408065680, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>')
                    __append('\n\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f4239719a50> name=None at 7f4239719db0> -> __attrs_139922408314944
                __attrs_139922408314944 = _static_139922408315472

                # <Value 'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)' (212:27)> -> __condition
                __token = 11179
                try:
                    __zt_tmp = __attrs_139922408314944
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('python', 'has_replies and (isAnon and not isAnonymousDiscussionAllowed)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply">\n            ')

                    # <Static value=<ast.Dict object at 0x7f4239719360> name=None at 7f42397193c0> -> __attrs_139922408313648
                    __attrs_139922408313648 = _static_139922408313696

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="mb-3"')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408314080
                    __default_139922408314080 = _DEFAULT_MARKER

                    # <Substitution 'view/login_action' (213:41)> -> __attr_action
                    __token = 11291
                    try:
                        __zt_tmp = __attrs_139922408313648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_139922496190256('path', 'view/login_action', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x7f423971b490> name=None at 7f423971b400> -> __attrs_139922408324640
                    __attrs_139922408324640 = _static_139922408322192

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="standalone loginbutton btn btn-primary" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408316288
                    __default_139922408316288 = _DEFAULT_MARKER

                    # <Translate msgid='label_login_to_add_comments' node=<ast.Constant object at 0x7f42397183a0> at 7f423971a350> -> __attr_value
                    __attr_value = 'Log in to add comments'
                    __attr_value = translate('label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_139922408311056 = []
                    __append_139922408311056 = __stream_139922408311056.append
                    __append_139922408311056('Log in to add comments')
                    __msgid_139922408311056 = __re_whitespace(''.join(__stream_139922408311056)).strip()
                    if 'label_login_to_add_comments':
                        __append(translate('label_login_to_add_comments', mapping=None, default=__msgid_139922408311056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f423971a9b0> name=None at 7f423971aec0> -> __attrs_139922408324016
                __attrs_139922408324016 = _static_139922408319408

                # <Value 'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (225:27)> -> __condition
                __token = 11795
                try:
                    __zt_tmp = __attrs_139922408324016
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139922496190256('python', 'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="commenting" class="reply border p-3">\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408319504
                    __attrs_139922408319504 = _static_139922496178928

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408354624
                    __attrs_139922408354624 = _static_139922496178928

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append('<legend>')
                    __stream_139922408353808 = []
                    __append_139922408353808 = __stream_139922408353808.append
                    __append_139922408353808('Add comment')
                    __msgid_139922408353808 = __re_whitespace(''.join(__stream_139922408353808)).strip()
                    if 'label_add_comment':
                        __append(translate('label_add_comment', mapping=None, default=__msgid_139922408353808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</legend>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408349776
                    __attrs_139922408349776 = _static_139922496178928

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408343200
                    __default_139922408343200 = _DEFAULT_MARKER

                    # <Value 'view/comment_transform_message' (231:32)> -> __cache_139922408353424
                    __token = 12034
                    try:
                        __zt_tmp = __attrs_139922408349776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139922408353424 = _static_139922496190256('path', 'view/comment_transform_message', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/comment_transform_message' (231:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f42397227d0> -> __condition
                    __expression = __cache_139922408353424

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                You can add a comment by filling out the form below. Plain text\n                formatting.\n                ')
                    else:
                        __content = __cache_139922408353424
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f423eae4af0> name=None at 7f423eae4e20> -> __attrs_139922408343440
                    __attrs_139922408343440 = _static_139922496178928

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __default_139922408342768
                    __default_139922408342768 = _DEFAULT_MARKER

                    # <Value 'view/form/render' (236:44)> -> __cache_139922408347040
                    __token = 12241
                    try:
                        __zt_tmp = __attrs_139922408343440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139922408347040 = _static_139922496190256('path', 'view/form/render', econtext=econtext)(_static_139922496189968(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/form/render' (236:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f423ec6a9b0> at 7f4239721930> -> __condition
                    __expression = __cache_139922408347040

                    # <Symbol value=<DEFAULT> at 7f423ec6a9b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div />')
                    else:
                        __content = __cache_139922408347040
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n            </fieldset>\n        </div>')
                __append('\n    </div>\n')
                __i18n_domain = __previous_i18n_domain_139922408027760
            if (__backup_auth_token_139922408150816 is __marker):
                del econtext['auth_token']
            else:
                econtext['auth_token'] = __backup_auth_token_139922408150816
            if (__backup_wtool_139922408151392 is __marker):
                del econtext['wtool']
            else:
                econtext['wtool'] = __backup_wtool_139922408151392
            if (__backup_errors_139922408150768 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_139922408150768
            if (__backup_showCommenterImage_139922408151056 is __marker):
                del econtext['showCommenterImage']
            else:
                econtext['showCommenterImage'] = __backup_showCommenterImage_139922408151056
            if (__backup_has_replies_139922408152400 is __marker):
                del econtext['has_replies']
            else:
                econtext['has_replies'] = __backup_has_replies_139922408152400
            if (__backup_replies_139922408151104 is __marker):
                del econtext['replies']
            else:
                econtext['replies'] = __backup_replies_139922408151104
            if (__backup_canReview_139922408154560 is __marker):
                del econtext['canReview']
            else:
                econtext['canReview'] = __backup_canReview_139922408154560
            if (__backup_isAnon_139922408154512 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_139922408154512
            if (__backup_isDeleteOwnCommentAllowed_139922408153456 is __marker):
                del econtext['isDeleteOwnCommentAllowed']
            else:
                econtext['isDeleteOwnCommentAllowed'] = __backup_isDeleteOwnCommentAllowed_139922408153456
            if (__backup_isEditCommentAllowed_139922408152064 is __marker):
                del econtext['isEditCommentAllowed']
            else:
                econtext['isEditCommentAllowed'] = __backup_isEditCommentAllowed_139922408152064
            if (__backup_isAnonymousDiscussionAllowed_139922442814512 is __marker):
                del econtext['isAnonymousDiscussionAllowed']
            else:
                econtext['isAnonymousDiscussionAllowed'] = __backup_isAnonymousDiscussionAllowed_139922442814512
            if (__backup_isDiscussionAllowed_139922408193808 is __marker):
                del econtext['isDiscussionAllowed']
            else:
                econtext['isDiscussionAllowed'] = __backup_isDiscussionAllowed_139922408193808
            if (__backup_userHasReplyPermission_139922408193664 is __marker):
                del econtext['userHasReplyPermission']
            else:
                econtext['userHasReplyPermission'] = __backup_userHasReplyPermission_139922408193664
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }