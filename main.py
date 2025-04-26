from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Define driver, option, service
chrome_option = Options()
chrome_option.add_argument("--disable-search-engine-choice-screen")

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_option, service=service)

# Load the webpage
driver.get('https://demoqa.com/login')

# Locate username , password, login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in forms and click button
username_field.send_keys('Alinatest')
password_field.send_keys('Alinatest1!')
driver.execute_script("arguments[0].click();", login_button)

# Locate the element dropdown and Text Box
elements = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
elements.click()
time.sleep(2)
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()
time.sleep(2)

# Locate the form fields
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Fill in the form fields
fullname_field.send_keys('Alinatest')
email_field.send_keys('rojko.alina@gmail.com')
current_address_field.send_keys('EH64RU')
permanent_address_field.send_keys('EH64RU')
driver.execute_script("arguments[0].click();", submit_button)

# Upload and Download
upload_download = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="item-7"]'))))
upload_download.click()
time.sleep(3)
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)
time.sleep(3)


input("Press Enter to close...")
driver.quit()
