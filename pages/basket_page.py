from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):

    def should_be_empty(self):
        assert 'Ваша корзина пуста' in self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET).text, 'Basket is not empty'

    def items_is_absent(self, timeout=3):
        flag = False
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(BasketPageLocators.BASKET_ITEMS))
        except TimeoutException:
            flag = True

        assert flag, 'Some items in basket'
