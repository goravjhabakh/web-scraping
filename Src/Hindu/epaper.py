from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle

email = 'goravjhabakh1301@gmail.com'
pwd = 'Quintal23$'

url = 'https://epaper.thehindu.com/reader'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

try:
    login_btn = driver.find_element(By.ID, 'myaccountBtn')
    login_btn.click()
    time.sleep(5)

    print('CLicked on Login button')

    pop_up = driver.find_element(By.CLASS_NAME, 'tp-modal')
    pop_up = driver.find_element(By.CLASS_NAME, 'tp-iframe-wrapper')
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@id, 'piano-id')]")
    print('Found pop up box')

    children = iframe.find_elements(By.XPATH, './/*')

    with open('Src/Hindu/children.txt','w') as f:
        for child in children:
            f.write(f'{child.tag_name}, {child.get_attribute("class")}, {child.get_attribute("id")}\n')


    # email_input = pop_up.find_element(By.TAG_NAME, 'input')
    # print('Found email input box')

    # email_input.send_keys(email)
    # print('Typed the email')

    # email_input.send_keys(Keys.RETURN)
    # print('Entered')

    time.sleep(1)

except Exception as e:
    print(e)

driver.close()