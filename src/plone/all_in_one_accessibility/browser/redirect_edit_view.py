from plone.all_in_one_accessibility.browser.viewlets import get_widget_settings
from Products.Five.browser import BrowserView


class RedirectToSettingEditView(BrowserView):
    def __call__(self):
        # Go to the settings object that actually exists. The id is not
        # always "all-in-one-accessibility-setting" (it becomes "...-2" if
        # the object was ever deleted and re-added), so look it up.
        setting = get_widget_settings()
        if setting is not None:
            target = setting.absolute_url() + '/edit'
        else:
            target = (
                self.context.absolute_url()
                + '/++add++All in One Accessibility Setting'
            )
        self.request.response.redirect(target)
        return ''
