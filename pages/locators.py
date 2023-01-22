from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # login
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # register
    REGISTRATION_EMAIL_STRING = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_PASSWORD_STRING = (By.CSS_SELECTOR, "input#id_registration-password1")
    CONFIRM_PASSWORD_STRING = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1)')


class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a:nth-child(1).btn")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items")
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner>p")
