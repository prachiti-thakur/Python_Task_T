import cv2

def crop_the_image():
    image="images/page_1.jpg"
    image=cv2.imread(image)

    # print(image.shape) #(4094, 2898, 3)
    crop_img=image[1:1000, 1:2898]
    cv2.imshow("cropeed",crop_img) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

    imgheight=image.shape[0]
    imgwidth=image.shape[1]
    print(imgwidth)
    print(imgheight)



crop_the_image()