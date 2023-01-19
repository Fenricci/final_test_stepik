import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math

class BasePage():
    def __init__(self, l_browser, url, timeout=8):
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

    def solve_quiz_and_get_code(self):
        alert = self.l_browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        time.sleep(1)
        alert.accept()
        time.sleep(1)
        try:
            alert = self.l_browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")