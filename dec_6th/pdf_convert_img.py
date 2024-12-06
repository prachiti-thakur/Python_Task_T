from pdf2image import convert_from_path

def convert_pdf_to_images(pdf):
    
    pages = convert_from_path(pdf,350)

    i=1
    for page in pages:
        image_name="page_"+str(i)+".jpg"
        page.save(image_name,"JPEG")

        i=i+1


# main funciton for calling all the functions
def extract_data():
    pdf=r""
    convert_pdf_to_images(pdf)



extract_data()
