from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import pdf_file_fetcher

def google_books(filename, driver = None):
    final_fn = filename.replace('.pdf', '')

    if driver == None:
        driver = driver = webdriver.Chrome(service = ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get("https://www.google.com/search?q=" + final_fn + '&tbm=bks')
    x =input()

if __name__ == '__main__':
    # #this source, destination are for Hussein Allaw
    # src = "C:\\Users\\Hussein\\Desktop\\Microbiology\\"
    # dest = "C:\\Users\\Hussein\\Desktop\\Microbiology\\DONE-MicroBiology\\"
    # dest, pdf_filename = pdf_file_fetcher.move_pdf(source, dest)
    #this source, destination is for S. Jinan Al-Mswi
    dest, pdf_filename = pdf_file_fetcher.move_pdf()
    google_books(pdf_filename)