# -*- coding: utf-8 -*-

from plone import api
from plone.all_in_one_accessibility import _
from plone.autoform import directives as form
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.schema import Choice
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


def _humanize(token):
    """Human-readable label for a machine-readable choice token.

    "bottom_right" -> "Bottom Right", "to_the_left" -> "To The Left",
    "aioa-big-icon" -> "Big Icon" (this add-on's own "aioa-" prefix and
    "-icon" suffix are internal implementation details, not something a
    site editor needs to see in a dropdown).
    """
    text = token
    if text.startswith('aioa-'):
        text = text[len('aioa-'):]
    if text.endswith('-icon'):
        text = text[:-len('-icon')]
    text = text.replace('_', ' ').replace('-', ' ')
    return text.title()


def _humanized_vocabulary(tokens):
    """A SimpleVocabulary whose terms keep the original token as the
    stored value, but show a human-readable title in the widget --
    e.g. the select shows "Bottom Right" while "bottom_right" is what
    actually gets saved (and what aioa_utils/aioa_skynet_sync.js expect).
    """
    return SimpleVocabulary(
        [SimpleTerm(value=t, token=t, title=_humanize(t)) for t in tokens]
    )


AIOA_SELECT_CHOICES = [
    'top_left',
    'top_center',
    'top_right',
    'middle_left',
    'middle_right',
    'bottom_left',
    'bottom_center',
    'bottom_right',
]

AIOA_SIZE_CHOICES = [
    'regular',
    'oversize',
]

TO_THE_RIGHT_CHOICES = [
    'to_the_left',
    'to_the_right',
]

TO_THE_BOTTOM_CHOICES = [
    'to_the_bottom',
    'to_the_top',
]

AIOA_ICON_SIZE_CHOICES = [
    'aioa-big-icon',
    'aioa-medium-icon',
    'aioa-default-icon',
    'aioa-small-icon',
    'aioa-extra-small-icon',
]

ICON_CHOICES = [
    (f'aioa-icon-type-{i}', f'https://www.skynettechnologies.com/sites/default/files/aioa-icon-type-{i}.svg')
    for i in range(1, 30)
]

class IAllInOneAccessibilitySetting(model.Schema):
   
    aioa_color = schema.TextLine(
        title='Hex color code',
        description='You can customize the ADA Widget color. For example: #FF5733',
        required=False,
    )
    
    enable_widget_icon_position = schema.Bool(
        title="Enable Precise widget icon positioning",
        default=False,
        required=False,
    )

    aioa_place = schema.Choice(
        title='Where would you like to place the accessibility icon on your site',
        vocabulary=_humanized_vocabulary(AIOA_SELECT_CHOICES),
        default='bottom_right',
        required=True,
    )

    to_the_right_px = schema.Int(
        title="Right offset (PX)",
        description="Allowed range 0 - 250",
        min=0,
        max=250,
        default=20,
        required=False,
    )

    to_the_right = schema.Choice(
        title="To the right",
        vocabulary=_humanized_vocabulary(TO_THE_RIGHT_CHOICES),
        default='to_the_left',
        required=True,
    )

    to_the_bottom_px = schema.Int(
        title="Bottom offset (PX)",
        description="Allowed range 0 - 250",
        min=0,
        max=250,
        default=20,
        required=False,
    )

    to_the_bottom = schema.Choice(
        title="To the bottom",
        vocabulary=_humanized_vocabulary(TO_THE_BOTTOM_CHOICES),
        default='to_the_bottom',
        required=True,
    )

    aioa_size = schema.Choice(
        title="Widget Size",
        vocabulary=_humanized_vocabulary(AIOA_SIZE_CHOICES),
        default='oversize',
        required=True,
    )
    
    aioa_icon_type = Choice(
    title="Icon Type",
    vocabulary="plone.all_in_one_accessibility.icon_vocabulary",
    default='aioa-icon-type-1',
    required=True,
    )

    enable_icon_custom_size = schema.Bool(
        title="Enable Custom Icon Size",
        default=False,
        required=False,
    )

    # 50 is only the first-install/schema default. The form JavaScript
    # must never reset this field when Custom Icon Size is toggled off;
    # the last saved value should remain available when it is enabled again.
    aioa_size_value = schema.Int(
        title="Select exact icon size (PX)",
        description="Allowed range 20 - 150",
        min=20,
        max=150,
        default=50,
        required=False,
    )

    aioa_icon_size = schema.Choice(
        title="Desktop Icon Size",
        vocabulary=_humanized_vocabulary(AIOA_ICON_SIZE_CHOICES),
        default='aioa-default-icon',
        required=True,
    )

    # Not a user choice any more (see the CDN-selection fix in
    # browser/static/aioa_skynet_sync.js): showing a manual "EU vs non-EU"
    # toggle let it drift out of sync with what add-user-domain actually
    # registered for this domain, which made the widget load from the
    # wrong CDN host and fail to render (mismatched CORS/script errors).
    # The field stays in the schema -- aioa_utils.build_widget_script_url
    # still reads it, and diagnose.py/the REST API still report it -- but
    # it is hidden from the add/edit form. aioa_skynet_sync.js writes the
    # auto-detected value into this field's hidden input before every
    # Save, using the same EU/non-EU lookup that add-user-domain uses, so
    # the two are always consistent.
    form.mode(no_required_eu='hidden')
    no_required_eu = schema.Bool(
        title="Serve widget from the non-EU CDN",
        description=(
            "Auto-detected: the widget script is loaded from "
            "eu.skynettechnologies.com for sites detected as being in the "
            "EU, and from www.skynettechnologies.com otherwise. Kept in "
            "sync with Skynet's own add-user-domain registration so the "
            "widget always loads from the CDN Skynet actually registered "
            "this domain under."
        ),
        default=True,
        required=False,
    )

    # Populated once this site's account/plan info is fetched from Skynet
    # (see the widget-settings API call in aioa_skynet_sync.js). Hidden
    # rather than shown in 'display' mode: with no sync yet run this was
    # always empty, which just left a bare "Widget token" label with no
    # value sitting on the settings page. The token itself, and the
    # account/plan panel (upgrade / free-trial link, cache note), are
    # rendered by aioa_skynet_sync.js instead, next to the rest of that
    # live Skynet data.
    form.mode(aioa_token='hidden')
    aioa_token = schema.TextLine(
        title="Widget token",
        description="Set automatically once this site is registered with Skynet.",
        required=False,
        default='',
    )

@implementer(IAllInOneAccessibilitySetting)
class AllInOneAccessibilitySetting(Item):
    # def __init__(self, id=None, **kwargs):
    #     catalog = api.portal.get_tool('portal_catalog')
    #     brains = catalog(portal_type='All in One Accessibility Setting')
    #     if brains:
    #         raise Exception('Only one "All in One Accessibility setting" object is allowed per Plone instance')
    #     super(AllInOneAccessibilitySetting, self).__init__(id, **kwargs)
    pass
    
from z3c.form.object import registerFactoryAdapter
registerFactoryAdapter(IAllInOneAccessibilitySetting, AllInOneAccessibilitySetting)





