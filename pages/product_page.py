import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def start(self):
        self.add_to_basket()
        self.equals_title()
        self.equals_price()
        self.should_not_be_success_message()

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        #self.solve_quiz_and_get_code()

    def equals_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_NAME_CATALOG).text
        book_title_in_bskt = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADD).text
        assert book_title == book_title_in_bskt, 'Title do not equals'

    def equals_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price == basket_price, 'Prices do not equals'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
