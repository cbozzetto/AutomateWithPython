from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#chromedriver.exe is needed in order for this script to work properly. Download it from
#http://chromedriver.storage.googleapis.com/index.html (choose the latest, as of now it is 2.9)
#and add it to the same directory of the python script. This script only works with Chrome.

email = '...'
pw = '...'

browser = webdriver.Chrome()
browser.get('https://it.bidoo.com')

WebDriverWait(browser, 20)

login_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_btn"]')))
login_btn.click()

field_email = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="field_email"]')))
field_email.click()
field_email.send_keys(email)

password = browser.find_element_by_xpath('//*[@id="password"]')
password.click()
password.send_keys(pw)

entra = browser.find_element_by_xpath('//*[@id="logMeIn"]/div/div/div/div/div/form/div[4]/button')
entra.click()



