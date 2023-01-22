from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        login_url = self.l_browser.current_url
        assert 'login' in login_url, "It is not a login link!"

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not present"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not present"

    def register_new_user(self, email, password):
        # Регистрация нового пользователя
        self.l_browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_STRING).send_keys(email)
        self.l_browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_STRING).send_keys(password)
        self.l_browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_STRING).send_keys(password)
        self.l_browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
