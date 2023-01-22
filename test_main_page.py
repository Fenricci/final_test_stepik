from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(l_browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(l_browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(l_browser, l_browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(l_browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(l_browser, link)
    page.open()
    page.should_be_login_link()

# def test_guest_cant_see_product_in_basket_opened_from_main_page(l_browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(l_browser, link)
#     page.open()
#     