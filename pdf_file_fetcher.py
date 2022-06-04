import os
import shutil as sh


def move_pdf(source = 'C:\\Users\\LenovoPc\\Desktop\\MicroBiology\\', dest = "C:\\Users\\LenovoPc\\Desktop\\Destination\\"):
    pdf_filename = ""


    for filename in os.listdir(source):
        if '.pdf' in filename:
            pdf_filename = filename
            print(filename)
            break


    if (pdf_filename != ""):
        os.replace(source + pdf_filename, dest + pdf_filename)
        print(pdf_filename, "was successfuly moved")

    return [dest, pdf_filename]

if __name__ == "__main__":
    move_pdf()