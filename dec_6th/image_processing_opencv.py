import cv2

from PIL import Image

import pytesseract


def crop_the_image():
    image="images/page_1.jpg"
    image=cv2.imread(image)

    # print(image.shape) #(4094, 2898, 3)
    crop_img=image[1:1000, 1:2898] #image[rows,columns]
    resize_img=cv2.resize(crop_img,(1500,500))  #width,height
    cv2.imshow("cropeed",resize_img) 

    cv2.waitKey(10) 
    cv2.destroyAllWindows()

    imgheight=image.shape[0]
    imgwidth=image.shape[1]
    print(imgwidth)
    print(imgheight)


    #call the function to fetch the data
    read_data_from_img(resize_img)



def read_data_from_img(image):
   # Convert the OpenCV image (NumPy array) to a PIL Image
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Use pytesseract to extract text
    print(pytesseract.image_to_string(pil_image))



crop_the_image()