from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, ('There is no substring "login" in url')

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), ('There is no login form')

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRY_FORM), ('There is no register form')

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRY_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRY_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRY_BUTTON).click()
