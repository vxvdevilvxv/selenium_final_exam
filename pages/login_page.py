from .base_page import BasePage

class LoginPage(BasePage):

    def should_be_login_page(self):
        assert 'login' in self.browser.current_url, 'This is not login page'