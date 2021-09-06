from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (
    By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'form.basket_summary div.basket-items')

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    BOOK_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    BASKET_PRICE = (
    By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    SUCCESS_ADD = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    BOOK_NAME_ADD = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    BOOK_NAME_CATALOG = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
