import os
from pdf2image import convert_from_path

def create_cover_image(pdf_path, target_path):
    poppler_path= os.getcwd() + "\\bin"
    pages = convert_from_path(pdf_path, dpi= 300, first_page= 0, output_folder= target_path, last_page= 1, poppler_path=poppler_path)
    pdf_file = pdf_file[:-4]

    for page in pages:
        page.save("%s-page%d.png" % (pdf_file,pages.index(page)), "PNG")

if __name__ == "__main__":
    pdf_path= "C:\\Users\\Hussein\\Desktop\\MicroBiology\\Wastewater Microbiology - Gabriel Bitton.pdf"
    target_path= "C:\\Users\\Hussein\\Desktop\\MicroBiology\\Images-Microbiolog"
    create_cover_image(pdf_path, target_path)