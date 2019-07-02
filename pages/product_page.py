from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def product_name_is_the_same(self):
        # создаём переменные с текущим и добавленным к корзину названиями товара
        current_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        assert current_product == added_product, 'product name is different'

    def should_be_current_product_price(self):
        # создаём переменные с ценой товара и ценой товара в корзине
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price == added_price, 'price is different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET),\
                    'Success message is presented, but should not be'

    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_BASKET),\
                    'Element is disappeared, but should not be'
              

