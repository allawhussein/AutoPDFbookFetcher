
# import module
from pdf2image import convert_from_path
from pathlib import Path
from pdf2image.exceptions import (
PDFInfoNotInstalledError,
PDFPageCountError,
PDFSyntaxError
)
p_path = Path(__file__).parent / "bin"

#def new_func(pdfp):
#pdfpathe=p_path.parent/"From Goat to Cheese by Lisa Owings (z-lib.org)"
pdfp="E:/2/DONE"
pdfpa=Path(pdfp)/"From Goat to Cheese by Lisa Owings (z-lib.org)"
print(pdfpa)
#Store Pdf with convert_from_path function
images = convert_from_path(pdf_path=Path('E:/2/DONE/From Goat to Cheese by Lisa Owings (z-lib.org).pdf'),poppler_path =p_path ,first_page=0,last_page=1)

#images[0].save('cover.jpg','JPEG')

#new_func(pdfp="E:/2/DONE/From Goat to Cheese by Lisa Owings (z-lib.org).pdf")
