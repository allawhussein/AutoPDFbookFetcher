from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys

def amazon(filename = "pdf"):
    driver = driver = webdriver.Chrome(service = ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    
    search = driver.find_element_by_name("q")
    search.send_keys(filename)
    search.send_keys(Keys.RETURN)
    x =input()