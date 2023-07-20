
import cgi
from io import StringIO
import os
from plone.app.multilingual.browser.interfaces import make_relation_root_path

from plone.autoform import directives

from plone.supermodel import model
import requests
from plone.app.textfield import RichText
import random
from zope.interface import invariant, Invalid
from plone import api
from plone.all_in_one_accessibility import _
from plone.dexterity.content import Item
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.utils import getToolByName
from zope import schema
from zope.interface import implementer
from zope.i18n import translate
from plone.autoform import directives
from z3c.form.browser.radio import RadioFieldWidget


aioa_NOTE = "<span class='validate_pro'><p>You are currently using Free version which have limited features. </br>Please <a href='https://www.skynettechnologies.com/add-ons/product/all-in-one-accessibility/'>purchase</a> License Key for additional features on the ADA Widget</p></span><script>if(document.querySelector('#form-widgets-aioa_key').value != ''){document.querySelector('.validate_pro').style.display='none';} else {document.querySelector('.validate_pro').style.display='block';}</script>"

img_tag = '<img src="https://www.skynettechnologies.com/sites/default/files/python/aioa-icon-type-1.svg" width="55" height="55" />'

        # checkbox = document.createElement("img"),
        
        # checkbox.class = "aioa_type_icon";
        # checkbox.src = "https://www.skynettechnologies.com/sites/default/files/python/aioa-icon-type-1.svg";
        # checkbox.width="55"
        # checkbox.height="55"
        # element.appendChild(checkbox);
# [0].innerHTML = '<img src="https://www.skynettechnologies.com/sites/default/files/python/aioa-icon-type-1.svg" width="55" height="55"/>';

javascript_for_img = '''<script>

        var element = document.querySelectorAll('input[name="form.widgets.aioa_icon_type"]');
        var total = 0
        console.log(element)
        for( var img of element) {
            total += 1
            const next = img.nextElementSibling;
            console.log(next)
            next.innerHTML= '<img src="https://www.skynettechnologies.com/sites/default/files/python/aioa-icon-type-'+total+'.svg" width="55" height="55"/>'
        }

</script>'''




JS_for_size = '''<script>
        var element = document.querySelectorAll('input[name="form.widgets.aioa_icon_size_desktop"]')
        var element_value = document.querySelector('input[name="form.widgets.aioa_icon_type"]:checked').value
        var total = 0
        console.log(element)
        for( var img of element) {
            total += 1
            const next = img.nextElementSibling;
            console.log(next)
            next.innerHTML= '<img src="https://www.skynettechnologies.com/sites/default/files/python/'+element_value+'.svg" width="55" height="55"/>'
        }
</script>'''

icon_type = SimpleVocabulary(
    [
        SimpleTerm(value=u'aioa-icon-type-1',title=''),
        SimpleTerm(value=u'aioa-icon-type-2',title=''),
        SimpleTerm(value=u'aioa-icon-type-3',title='')
    ]
)
icon_desktop = SimpleVocabulary(
    [
        SimpleTerm(value=u'aioa-big-icon', title=_(u'')),
        SimpleTerm(value=u'aioa-medium-icon', title=_(u'')),
        SimpleTerm(value=u'aioa-default-icon', title=_(u'')),
        SimpleTerm(value=u'aioa-small-icon', title=_(u'')),
        SimpleTerm(value=u'aioa-extra-small-icon', title=_(u''))
    ]
)
icon_mobile = SimpleVocabulary(
    [
        SimpleTerm(value=u'aioa-big-icon', title=_(u'')),
        SimpleTerm(value=u'aioa-medium-icon', title=_(u'')),
        SimpleTerm(value=u'aioa-default-icon', title=_(u'')),
        SimpleTerm(value=u'aioa-small-icon', title=_(u'')),
        SimpleTerm(value=u'aioa-extra-small-icon', title=_(u'')),
    ]
)
place = SimpleVocabulary(
    [
        SimpleTerm(value=u'top_left', title=_(u'Top left')),
        SimpleTerm(value=u'top_center', title=_(u'Top Center')),
        SimpleTerm(value=u'top_right', title=_(u'Top Right')),
        SimpleTerm(value=u'middel_left', title=_(u'Middle left')),
        SimpleTerm(value=u'middel_right', title=_(u'Middle Right')),
        SimpleTerm(value=u'bottom_left', title=_(u'Bottom left')),
        SimpleTerm(value=u'bottom_center', title=_(u'Bottom Center')),
        SimpleTerm(value=u'bottom_right', title=_(u'Bottom Right')),
    ]
)
[('top_left','Top left'),
      ('top_center','Top Center'),
      ('top_right','Top Right'),
      ('middel_left','Middle left'),
      ('middel_right','Middle Right'),
      ('bottom_left','Bottom left'),
      ('bottom_center','Bottom Center'),
      ('bottom_right','Bottom Right')]
class IAllInOneAccessibilitySetting(model.Schema):
    aioa_key = schema.TextLine(
        title='License Key',
        required=False,
        
        readonly=False,
        description = aioa_NOTE,
    )
    
    aioa_color = schema.TextLine(
        title='Hex color code',
        description='You can cutomize the ADA Widget color. For example: #FF5733',
        
       
        required=False,
        readonly=False,
    )
    
    aioa_place = schema.Choice(
        title='Where would you like to place the accessibility icon on your site',
        vocabulary=place
    )

    directives.widget(aioa_icon_type=RadioFieldWidget)
    aioa_icon_type = schema.Choice(
        title='Icon Type',
        # values=['<img src="https://www.skynettechnologies.com/sites/default/files/python/aioa-icon-type-1.svg" width="55" height="55" />', 'aioa-icon-type-2', 'aioa-icon-type-3'],
        vocabulary=icon_type,
        required=True,
        description=javascript_for_img
    )
    
    directives.widget(aioa_icon_size_desktop=RadioFieldWidget)
    aioa_icon_size_desktop = schema.Choice(
        title='Icon Size for Desktop',
        # values=['aioa-big-icon', 'aioa-medium-icon', 'aioa-default-icon','aioa-small-icon','aioa-extra-small-icon'],
        vocabulary=icon_desktop,
        required=True,
        description = JS_for_size
    )
    
    directives.widget(aioa_icon_size_mobile=RadioFieldWidget)
    aioa_icon_size_mobile = schema.Choice(
        title='Icon Size for Mobile',
        # values=['aioa-big-icon', 'aioa-medium-icon', 'aioa-default-icon','aioa-small-icon','aioa-extra-small-icon'],
        vocabulary=icon_mobile,
        required=True,
    )
    

    
    @invariant
    def validate_data(data):
     
        print(api.portal.get().absolute_url())
        print(data.aioa_icon_type)
        print(data.aioa_icon_size_mobile)
        print(data.aioa_icon_size_desktop)
        url = 'https://ada.skynettechnologies.us/api/widget-setting-update-platform'
        
        payload = {'u':api.portal.get().absolute_url(),
                   'widget_position':data.aioa_place,
                   'widget_color_code':data.aioa_color,
                   'widget_icon_type':data.aioa_icon_type,
                   'widget_icon_size':data.aioa_icon_size_desktop,
                   }
        response = requests.request('POST',url,data=payload)
        print(response.text)
        return data

@implementer(IAllInOneAccessibilitySetting)
class AllInOneAccessibilitySetting(Item):
    def __init__(self, id=None, **kwargs):
        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog(portal_type='All in One Accessibility Setting')
        if brains:
            raise Exception('Only one "All in One Accessibility setting" object is allowed per Plone instance')

        super(AllInOneAccessibilitySetting, self).__init__(id, **kwargs)
        
from z3c.form.object import registerFactoryAdapter
registerFactoryAdapter(IAllInOneAccessibilitySetting, AllInOneAccessibilitySetting)
