from pdf2image import convert_from_path

def create_cover_image(pdf_path, target_path, pdf_filename):
    image= convert_from_path(pdf_path + pdf_filename, first_page= 0, last_page= 1)[0]
    image.save(target_path + pdf_filename.replace(".pdf", ".png"), "PNG")
    return target_path + pdf_filename.replace(".pdf", ".png")

if __name__ == "__main__":
    pdf_path= "C:\\Users\\Hussein\\Desktop\\MicroBiology\\"
    target_path= "C:\\Users\\Hussein\\Desktop\\MicroBiology\\Images-Microbiolog\\"
    pdf_filename= "Wastewater Microbiology - Gabriel Bitton.pdf"
    create_cover_image(pdf_path, target_path, pdf_filename)