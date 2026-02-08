from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    stormtroopers = browser.find_elements(By.TAG_NAME, 'a')
    n = 0
    for i in stormtroopers:
        if i.get_attribute('stormtrooper').isdigit():
            n += int(i.get_attribute('stormtrooper'))
    browser.find_element(By.ID, 'inputNumber').send_keys(n)
    browser.find_element(By.ID, 'checkBtn').click()
    code = browser.find_element(By.ID, 'feedbackMessage').text
    print(code)