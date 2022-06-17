import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pdf_cover_page_skimmer import pdf_cover_page_skimmer
from local_books_manager import book_metadata_seeker
from local_books_manager import details_fetcher_to_csv

source_folder_path= "D:\\programming\\Projects\\AutoPDFbookFetcher\\Microbiology\\"
destination_folder_path= "D:\\programming\\Projects\\AutoPDFbookFetcher\\Microbiology\\DONE-MicroBiology\\"
image_folder_path= "D:\\programming\\Projects\\AutoPDFbookFetcher\\Images-Microbiolog\\"
csv_path= "D:\\programming\\Projects\\AutoPDFbookFetcher\\Microbiology Metadata.csv"
driver = webdriver.Chrome(service = ChromeService(executable_path=ChromeDriverManager().install()))

for filename in os.listdir(source_folder_path):
    if ".pdf" in filename:
        print("Processing: ", filename)
        image_path= pdf_cover_page_skimmer.create_cover_image(source_folder_path, image_folder_path, filename)
        book_name, book_authors, publication_date, book_review = book_metadata_seeker.google_books(filename, driver)
        book_path = source_folder_path + filename
        if not isinstance(book_authors, str):
            book_authors = " & ".join(book_authors)
        details_fetcher_to_csv.csv_book_details(book_name, book_authors, book_review, publication_date, book_path, image_path, csv_path)