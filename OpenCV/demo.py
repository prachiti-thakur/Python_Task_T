#take a input of img from user then convert it into the grayscale and save it
import cv2
path=input("Enter the path of the Image:")

image1=cv2.imread(path,0) # to convert it into the grayscale

imgheight=image1.shape[0]
imgwidth=image1.shape[1]
print(imgwidth)
print(imgheight)
original_image=cv2.resize(image1,(1000,700))

cv2.imshow("org_to_grayscale",original_image)
k=cv2.waitKey(0)

if k==ord("s"):
    #to save the image into the particular location with that name 
    cv2.imwrite("/home/prachitit/Documents/Python_Task/OpenCV/grayscale_flower.jpg",original_image)
else:
    # kill all another windows and release the memory
    cv2.destroyAllWindows()
