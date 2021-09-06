import pytest
import unittest
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.items_is_absent()
    basket.should_be_empty()


if __name__ == "__main__":
    unittest.main()
