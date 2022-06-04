import os
from pdf2image import convert_from_path

pdf_dir = r"E:\2\Food engineering"
os.chdir(pdf_dir)

for pdf_file in os.listdir(pdf_dir):

    if pdf_file.endswith(".pdf"):

        pages = convert_from_path(pdf_file, 300,first_page=0,last_page=1,poppler_path =r"C:\Users\Pc\Desktop\New folder\bin")
        pdf_file = pdf_file[:-4]

        for page in pages:

            page.save("%s-page%d.png" % (pdf_file,pages.index(page)), "PNG")