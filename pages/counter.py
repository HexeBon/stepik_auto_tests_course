from selenium.webdriver.common.by import By

class Counter:
    link = 'https://parsinger.ru/selenium/3/3.3.3/index.html'

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.get(self.link)

    def counter_stormtroopers(self):
        stormtroopers = self.browser.find_elements(By.TAG_NAME, 'a')
        count = 0
        for i in stormtroopers:
            if i.get_attribute('stormtrooper').isdigit():
                count += int(i.get_attribute('stormtrooper'))
        return count

    def entering_a_number(self):
        number = self.counter_stormtroopers()
        self.browser.find_element(By.ID, 'inputNumber').send_keys(number)
        self.browser.find_element(By.ID, 'checkBtn').click()

    def get_code (self):
        code = self.browser.find_element(By.ID, 'feedbackMessage').text
        return code