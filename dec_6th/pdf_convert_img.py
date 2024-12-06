from pdf2image import convert_from_path
from PIL import Image

import pytesseract



#convert it into the image
def convert_pdf_to_images(pdf):
    pages = convert_from_path(pdf,350)

    i=1
    for page in pages:
        image_name="images/page_"+str(i)+".jpg"
        page.save(image_name,"JPEG")

        i=i+1

#extraxr the data from images to the string
def img_to_string():

    outputfile="/home/prachitit/Documents/Python_Task/dec_6th/extract_data.txt"

    
    for i in range(1,3):
        img=Image.open(f"images/page_{i}.jpg")
        text=str(pytesseract.image_to_string(img))
        textfile=open (outputfile,"a")
        textfile.writelines(text)
        


# main funciton for calling all the functions
def extract_data():
    pdf=r"/home/prachitit/Documents/Python_Task/dec_6th/PICT_insem_OCT24.pdf"
    convert_pdf_to_images(pdf)

    imgFoler=r"/home/prachitit/Documents/Python_Task/dec_6th/images"
    img_to_string()



extract_data()
