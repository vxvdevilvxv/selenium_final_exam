from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        _email = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-email')
        _email.send_keys(email)

        _password = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password1')
        _password.send_keys(password)

        _repeat_password = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password2')
        _repeat_password.send_keys(password)

        _button = self.browser.find_element(By.CSS_SELECTOR, '#register_form button.btn.btn-lg.btn-primary')
        _button.click()

    def should_be_login_page(self):
        assert 'login' in self.browser.current_url, 'This is not login page'