from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

class WebAutomation:
    def __init__(self):
        # Define driver, option, service
        chrome_option = Options()
        chrome_option.add_argument("--disable-search-engine-choice-screen")

        # Declare the folder to download files from the web
        download_pth = os.getcwd()
        prefs = {"download.default_directory": download_pth}
        chrome_option.add_experimental_option('prefs', prefs)

        # Define the driver
        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_option, service=service)

        # Declare the folder to download files from the web
        download_pth = os.getcwd()
        prefs = {"download.default_directory": download_pth}
        chrome_option.add_experimental_option('prefs', prefs)

    def login(self, username, password):
        # Load the webpage
        self.driver.get('https://demoqa.com/login')

        # Locate username , password, login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in forms and click button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the element dropdown and Text Box
        elements = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                    '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
        elements.click()
        time.sleep(2)
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()
        time.sleep(2)

        # Locate the form fields
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Upload and Download
        upload_download = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                             '//*[@id="item-7"]'))))
        upload_download.click()
        time.sleep(3)
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)
        time.sleep(3)

    def close(self):
        input("Press Enter to close...")
        self.driver.quit()

if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login(username="Alinatest", password="Alinatest1!")
    webautomation.fill_form(fullname="Alina Rozhko", email="rojko.alina@gmail.com",
                            current_address="EH64RU", permanent_address="EH64RU")
    webautomation.download()
    webautomation.close()














