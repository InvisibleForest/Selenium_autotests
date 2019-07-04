from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS),\
                        'Basket is not empty, but should be'

    def should_be_empty_basket_message(self):
        empty_message = self.browser.find_element(*CartPageLocators.BASKET_MESSAGE).text
        assert 'Your basket is empty' in empty_message, 'empty basket message not found'
