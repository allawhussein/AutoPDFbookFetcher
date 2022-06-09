import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pdf_cover_page_skimmer import pdf_cover_page_skimmer
from local_books_manager import book_metadata_seeker
from local_books_manager import details_fetcher_to_csv

source_folder_path= "C:\\Users\\Hussein\\Desktop\\Microbiology\\"
destination_folder_path= "C:\\Users\\Hussein\\Desktop\\Microbiology\\DONE-MicroBiology\\"
image_folder_path= "C:\\Users\\Hussein\\Desktop\\Microbiology\\Images-Microbiolog\\"