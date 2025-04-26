from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

driver.quit()
