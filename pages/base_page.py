
class BasePage():
    def __init__(self, l_browser, url):
        self.l_browser = l_browser
        self.url = url

    def open(self):
        self.l_browser.get(self.url)
