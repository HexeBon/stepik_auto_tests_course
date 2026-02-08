from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestFindChildElement(unittest.TestCase):
    def test_find_child_element(self):
        with webdriver.Chrome() as browser:
            browser.get("https://parsinger.ru/selenium/3/3.3.1/index.html")
            parent_element = browser.find_element(By.ID, "parent_id")
            child_element = browser.find_element(By.CLASS_NAME, "child_class")
            child_element.click()
            password = child_element.get_attribute("password")
            print(password)