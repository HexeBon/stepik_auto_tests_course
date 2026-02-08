import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest

class TestSelect(unittest.TestCase):
    def test_select(self):
        with webdriver.Chrome() as browser:
            browser.get("http://suninjuly.github.io/selects1.html")
            num_1 = int(browser.find_element(By.ID, 'num1').text)
            num_2 = int(browser.find_element(By.ID, 'num2').text)
            sum = str(num_1 + num_2)
            select = Select(browser.find_element(By.ID, 'dropdown'))
            select.select_by_value(sum)
            browser.find_element(By.CSS_SELECTOR, 'button').click()
            alert = browser.switch_to.alert
            alert_text = alert.text
            print(alert_text)
            alert.accept()