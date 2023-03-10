from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFormMainPage():
    def test_guest_can_go_to_login_page(self, l_browser):
        # Проверка того, что гость может перейти к странице логина
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(l_browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(l_browser, l_browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, l_browser):
        # Гость видит кнопку для авторизации
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(l_browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(l_browser):
    # Корзина пустая и гость не видит никаких товаров
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(l_browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.text_in_basket_no_items()
