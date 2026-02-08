import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import unittest

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

class TestCheckboxes_and_radiobuttons(unittest.TestCase):
    def test_checkboxes_and_radiobuttons(self):
        with webdriver.Chrome() as browser:
            browser.get("https://suninjuly.github.io/math.html")
            x_element = browser.find_element(By.ID, "input_value")
            x = x_element.text
            y = calc(x)
            browser.find_element(By.ID, "answer").send_keys(y)
            browser.find_element(By.ID, "robotCheckbox").click()
            browser.find_element(By.ID, "robotsRule").click()
            browser.find_element(By.CSS_SELECTOR, "button").click()
            alert = browser.switch_to.alert
            alert_text = alert.text
            print(alert_text)
            alert.accept()
