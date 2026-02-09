from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

class TestExpectation():
    def wait_price_100(self, browser):
        browser.get(link)
        WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
        browser.find_element(By.ID, "book").click()

    def capture_for_robot(self, browser):
        self.wait_price_100(browser)
        x_number = int(browser.find_element(By.ID, "input_value").text)
        answer = calc(x_number)
        browser.find_element(By.CLASS_NAME, "form-control").send_keys(answer)
        browser.find_element(By.ID, "solve").click()

    def accept_alert(self, browser):
        self.wait_price_100(browser)
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()






