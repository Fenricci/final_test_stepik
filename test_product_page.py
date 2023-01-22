from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
from .pages.basket_page import BasketPage
import time

params = list(map(str, range(10)))


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, l_browser):  # Регистрация нового пользователя
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        new_user = LoginPage(l_browser, link)
        new_user.open()
        email = str(time.time()) + "@fakemail.org"
        password = "234fenricci"
        time.sleep(1)
        new_user.register_new_user(email, password)
        new_user.should_be_authorized_user() # Проверка авторизованности пользователя
        time.sleep(1)

    # @pytest.mark.parametrize('param', [
    #     x if x != '7' else pytest.param(x, marks=pytest.mark.xfail) for x in params
    # ])
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, l_browser):
        # Пользователь может добавить товар в корзину
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
        product_page = ProductPage(l_browser, link)
        product_page.open()
        product_page.checking_the_match_of_the_goods_in_basket()

    def test_user_cant_see_success_message(self, l_browser):  # Пользователь не видит сообщения об успехе
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        checking_pages = ProductPage(l_browser, link)
        checking_pages.open()
        checking_pages.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(l_browser):
    # Гость может добавить товар в корзину
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
    product_page = ProductPage(l_browser, link)
    product_page.open()
    product_page.checking_the_match_of_the_goods_in_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(l_browser):
    # Пользователь не видит сообщения после добавления в корзину
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    add_checking = ProductPage(l_browser, link)
    add_checking.open()
    add_checking.add_product_to_basket()
    add_checking.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(l_browser):
    # Гость не видит появляющегося сообщения, после добавления товара в корзину
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    dissapear_message_checking = ProductPage(l_browser, link)
    dissapear_message_checking.open()
    dissapear_message_checking.add_product_to_basket()
    dissapear_message_checking.should_not_be_dissapear_success_message()


def test_guest_should_see_login_link_on_product_page(l_browser):
    # Гость видит кнопку перехода к странице авторизации на странице товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(l_browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(l_browser):
    # Гость может перейти на страницу регистрации со страницы товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(l_browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(l_browser):
    # Гость не видит товаров в корзине после перехода со страницы товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(l_browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.text_in_basket_no_items()
