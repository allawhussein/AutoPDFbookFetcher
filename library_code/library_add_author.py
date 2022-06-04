from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from local_credentials_and_urls import *

def add_author(driver, author_name, author_description = ""):
    if (driver.current_url != author_url):
        driver.get(author_url)
    while driver.execute_script("return document.readyState;") != "complete":
        pass

    for button in driver.find_elements(by=By.TAG_NAME, value="button"):
        if "إضافة" in button.text:
            button.click()

    author_name_field = driver.find_element(by=By.NAME, value="name")
    author_name_field.send_keys(author_name)

    for button in driver.find_elements(by=By.TAG_NAME, value="button"):
        if "أضف" in button.text:
            driver.execute_script("arguments[0].click();", button)
    
    while driver.execute_script("return document.readyState;") != "complete":
        pass

if __name__ == "__main__":
    import library_login
    driver = library_login.login()
    add_author(driver, "Paul N. MacDonald")