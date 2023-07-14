# -*- coding: utf-8 -*-
import random
from plone import api
from plone.restapi.interfaces import IExpandableElement
# from plone.restapi.services import Service
from plone.rest import Service

from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
import json
from plone.restapi.deserializer import json_body
from plone.restapi.serializer.converters import json_compatible
import requests


# class WidgetGet(Service):

#     def reply(self):
#         # service_factory = Widget(self.context, self.request)
#         # return service_factory(expand=True)['widget']
#         print(self.context.portal_type)
#         print(self.context.aioa_key)

#         session = requests.Session()
#         # session.auth = ('username', 'password')
#         session.headers.update({'Accept': 'application/json'})

#         response = session.get(self.context.absolute_url())
#         # value = {"url": "https://www.skynettechnologies.com/accessibility/js/all-in-one-accessibility-js-widget-minify.js?colorcode={}&token={}&t={}&position={}".format(self.context.aioa_color,self.context.aioa_key,str(random.randint(0,999999)),self.context.aioa_place)}
#         value = "https://www.skynettechnologies.com/accessibility/js/all-in-one-accessibility-js-widget-minify.js?colorcode={}&token={}&t={}&position={}".format(self.context.aioa_color,self.context.aioa_key,str(random.randint(0,999999)),self.context.aioa_place)
#         # print(json_compatible(value))
#         #base_URL = str(value)
#         # value = '{"url":"https://www.skynettechnologies.com/accessibility/js/all-in-one-accessibility-js-widget-minify.js?colorcode=420083&token=DRUPAL6CQ9-00H7-QXQS-30ZN-KA45-KTNL&t=0.5294880354467668&position=bottom_right"}'
        
#         # value = '{"test":"demo"}'
     
#         return value



from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse

@implementer(IPublishTraverse)
class WidgetGet(Service):

    def __init__(self, context, request):
        super(WidgetGet, self).__init__(context, request)
        self.params = []

    # def publishTraverse(self, request, name):
    #     value = "https://www.skynettechnologies.com/accessibility/js/all-in-one-accessibility-js-widget-minify.js?colorcode={}&token={}&t={}&position={}".format(self.context.aioa_color,self.context.aioa_key,str(random.randint(0,999999)),self.context.aioa_place)
    #     self.params.append(value)
        
    #     return self.params

    def render(self):
        value = {"URL": "https://www.skynettechnologies.com/accessibility/js/all-in-one-accessibility-js-widget-minify.js?colorcode={}&token={}&t={}&position={}".format(self.context.aioa_color,self.context.aioa_key,str(random.randint(0,999999)),self.context.aioa_place)}
        return value
