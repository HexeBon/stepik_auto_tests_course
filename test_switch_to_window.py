from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

class TestSwitchToWindow(unittest.TestCase):
    def test_switch_to_window(self):
        with webdriver.Chrome() as browser:
            browser.get("http://suninjuly.github.io/redirect_accept.html")
            browser.find_element(By.CSS_SELECTOR, "button").click()
            new_window = browser.window_handles[1]
            first_window = browser.window_handles[0]
            browser.switch_to.window(new_window)
            x_number = int(browser.find_element(By.ID, "input_value").text)
            answer = calc(x_number)
            browser.find_element(By.CLASS_NAME, "form-control").send_keys(answer)
            browser.find_element(By.CSS_SELECTOR, "button").click()
            alert = browser.switch_to.alert
            alert_text = alert.text
            print(alert_text)
            alert.accept()
            browser.switch_to.window(first_window)
            time.sleep(3)
