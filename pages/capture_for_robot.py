from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CaptureForRobot:
    link = "http://suninjuly.github.io/selects1.html"

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.get(self.link)

    def get_numbers_sum(self):
        num_1 = int(self.browser.find_element(By.ID, 'num1').text)
        num_2 = int(self.browser.find_element(By.ID, 'num2').text)
        return str(num_1 + num_2)

    def select(self):
        total = self.get_numbers_sum()
        dropdown = Select(self.browser.find_element(By.ID, 'dropdown'))
        dropdown.select_by_value(total)

    def click_submit(self):
        self.browser.find_element(By.CSS_SELECTOR, 'button').click()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text

        alert.accept()
        return alert_text


