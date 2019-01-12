from tests.page.base import BasePage
import tests.helpers.web as helper
import tests.page.login.locators as locator
from tests.model.login import Login


class LoginPage(BasePage):
    url = '/login'

    def user_footer_element(self):
        return helper.find_element(self.webdriver, locator.user_footer)

    def _fill_login_form(self, name, password):
        fields = {name: locator.name_field, password: locator.passw_field}
        for val, field in fields.items():
            if val is not None:
                helper.type_text(self.webdriver, field, val)

    def _open_login_page(self):
        helper.click(self.webdriver, locator.login_link)

    def _submit_login_form(self):
        helper.click(self.webdriver, locator.login_button)

    def login(self, name=None, password=None):
        self._open_login_page()
        self._fill_login_form(name, password)
        self._submit_login_form()

    def error_message(self):
        return helper.get_text(self.webdriver, locator.error_credentials_message)
