from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators(object):
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.alert-success strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')
    

