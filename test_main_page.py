from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def go_to_login_page(l_browser):
    login_link = l_browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(l_browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(l_browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(l_browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(l_browser, link)
    page.open()
    page.should_be_login_link()
