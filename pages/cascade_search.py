from selenium.webdriver.common.by import By

class Cascade:
    link = "https://parsinger.ru/selenium/3/3.3.1/index.html"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.link)

    def find_parent_element(self):
        parent_element = self.browser.find_element(By.ID, "parent_id")
        return parent_element

    def find_child_element(self):
        parent = self.find_parent_element()
        child_element = parent.find_element(By.CLASS_NAME, "child_class")
        return child_element

    def get_password(self):
        child = self.find_child_element()
        child.click()
        password = child.get_attribute("password")
        return password