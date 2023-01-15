from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, l_browser, url, timeout=10):
        self.l_browser = l_browser
        self.url = url
        self.l_browser.implicitly_wait(timeout)

    def open(self):
        self.l_browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.l_browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
