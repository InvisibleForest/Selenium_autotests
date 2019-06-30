from .pages.product_page import ProductPage
import time

link ='http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def  test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_is_the_same()
    page.should_be_current_product_price()
