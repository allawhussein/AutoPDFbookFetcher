from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from local_credentials import *

def login(username = login_username, password = login_password):
    driver = webdriver.Chrome(service = ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get(login_url)
    while driver.execute_script("return document.readyState;") != "complete":
        pass

    username_field = driver.find_element(by=By.NAME, value="username")
    password_field = driver.find_element(by=By.NAME, value="password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    for button in driver.find_elements(by=By.TAG_NAME, value="button"):
        if "btn-success" in  button.get_attribute("class"):
            button.click()

    return driver

if __name__ == "__main__":
    driver = login()
    x = input("enter anything to exit")