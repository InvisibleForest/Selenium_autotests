def test_guest_can_go_to_login_page(browser):
    browser.get('http://selenium1py.pythonanywhere.com/')
    browser.find_element_by_css_selector("#login_link").click()
