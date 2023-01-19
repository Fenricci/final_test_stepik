import time

from pages.product_page import ProductPage
import pytest

params = list(map(str, range(10)))

@pytest.mark.parametrize('param', [
    x if x != '7' else pytest.param(x, marks=pytest.mark.xfail) for x in params
])
def test_guest_can_add_product_to_basket(l_browser, param):
    '''
        Тест кейс для проверки того, что юзер может добавить продукт в корзину
    '''
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_" \
           f"207/?promo=offer{param}"
    product_page = ProductPage(l_browser, link)
    product_page.open()
    product_page.add_product_to_basket()