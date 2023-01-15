from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(l_browser):
    link = "http://selenium1py.pythonanywhere.com/"
    l_browser.get(link)
    login_link = l_browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()