from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import pdf_file_fetcher

def amazon(filename):
    driver = driver = webdriver.Chrome(service = ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    
    search = driver.find_element_by_name("q")
    search.send_keys(filename)
    search.send_keys(Keys.RETURN)
    x =input()

if __name__ == '__main__':
    dest, pdf_filename = pdf_file_fetcher.move_pdf()
    amazon(pdf_filename + "amazon")
