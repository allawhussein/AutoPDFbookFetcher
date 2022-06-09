from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import pdf_file_fetcher

def google_books(filename, driver = None):
    filename = filename.replace('.pdf', '')

    if driver == None:
        driver = webdriver.Chrome(service = ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get("https://www.google.com/search?q=" + filename + '&tbm=bks&hl=en')
    #searching for the first book card
    book_card = driver.find_element(by = By.CLASS_NAME, value= "Yr5TG")

    #searching for the book name
    for h3_tag in book_card.find_elements(by= By.TAG_NAME, value= "h3"):
        if "LC20lb MBeuO DKV0Md" in h3_tag.get_attribute("class"):
            book_name = h3_tag.text
            break
    else:
        book_name = None
    
    #searching for the book author
    author_name_field = book_card.find_element(by= By.CLASS_NAME, value= "N96wpd")
    author_name_field_spans = author_name_field.find_elements(by = By.TAG_NAME, value= "span")
    authors = []
    for author_element in author_name_field_spans[:-2]:
        authors.append(author_element.text)
    publication_date = author_name_field_spans[-1].text
    #searching for book preview
    book_preview = book_card.find_element(by= By.CLASS_NAME, value= "cmlJmd").text

    return book_name, authors, publication_date, book_preview

if __name__ == '__main__':
    # #this source, destination are for Hussein Allaw
    # src = "C:\\Users\\Hussein\\Desktop\\Microbiology\\"
    # dest = "C:\\Users\\Hussein\\Desktop\\Microbiology\\DONE-MicroBiology\\"
    # dest, pdf_filename = pdf_file_fetcher.move_pdf(source, dest)
    #this source, destination is for S. Jinan Al-Mswi
    dest, pdf_filename = pdf_file_fetcher.move_pdf()
    google_books(pdf_filename)