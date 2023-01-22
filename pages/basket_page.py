from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "There are items in the basket"

    def text_in_basket_no_items(self):
        assert self.l_browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), \
            "There is no message that the basket is empty"
