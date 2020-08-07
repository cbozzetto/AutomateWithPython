from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

#chromedriver.exe is needed in order for this script to work properly. Download it from
#http://chromedriver.storage.googleapis.com/index.html (choose the latest, as of now it is 2.9)
#and add it to the same directory of the python script. This script only works with Chrome.

usrname = '...'
pw = '...'

option = Options()
option.add_argument("user-data-dir=C:\\Users\\chrib\\AppData\\Local\\Google\\Chrome\\User Data\\")
#the following two lines allow the user to close the prompt window without closing the browser
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=option)

driver.get('https://elearning.unipd.it/economia/')

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerb"]/div/div[3]/span/a')))
login.click()

sso = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shib_si"]/a[1]/img')))
sso.click()

usr = driver.find_element_by_xpath('//*[@id="j_username_js"]')
usr.clear()
usr.send_keys(usrname)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(pw)

studenti = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radio2"]')))
studenti.click()

driver.find_element_by_xpath('//*[@id="login_button_js"]').click()

sys.exit(0)