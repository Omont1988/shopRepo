from tests.page.login.page import LoginPage
from tests.model.login import Login
import pytest


class TestLogin:
    error_message = 'ERROR name not found'

    @staticmethod
    def open_homepage(driver):
        page = LoginPage(driver)
        current_url = driver.current_url
        if current_url is not page.route:
            page.open_page()
        return page

    @pytest.fixture
    def credentials(self):
        return Login(name='user', password='password')

    @pytest.fixture
    def credentials_incorrect(self):
        return [Login(name='obolduy'), Login(password='ololol'), Login(name='user', password='google')]

    def test_correct_login(self, driver, credentials):
        page = self.open_homepage(driver)
        page.login(credentials.name, credentials.password)
        user_name = page.user_footer_element().text
        assert credentials.name in user_name

    @pytest.mark.parametrize('credentials_incorrect', credentials_incorrect)
    def test_incorrect_login(self, driver, credentials_incorrect):
        page = self.open_homepage(driver)
        page.login(credentials_incorrect.name, credentials_incorrect.password)
        user_name = page.user_footer_element().text
        assert credentials_incorrect.name not in user_name
        assert 'anonymous' in user_name
        assert self.error_message in page.error_message()
