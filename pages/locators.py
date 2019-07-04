from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRY_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRY_EMAIL = (By.ID, 'id_registration-email')
    REGISTRY_PASSWORD = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRY_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators(object):
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.alert-success strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')


class CartPageLocators(object):
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
