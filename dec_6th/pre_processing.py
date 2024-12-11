################### sonali ############


import cv2
import numpy as np
from PIL import Image

def preprocessing(image):
    """
    Optimized preprocessing pipeline for document images.
    Args:
        image (PIL.Image): The input image to preprocess
    Returns:
        PIL.Image: The preprocessed image
    """
    try:
        np_img = np.array(image.convert('L')) # L (8-bit pixels, grayscale)
        
        # Apply fast contrast stretching using numpy operations
        p2, p98 = np.percentile(np_img, (2, 98))
        img_stretched = np.interp(np_img, (p2, p98), (0, 255)).astype(np.uint8)
        # Simple Gaussian blur (small kernel) to reduce noise
        blurred = cv2.GaussianBlur(img_stretched, (3, 3), 0)
        # Use Otsu's thresholding - computationally efficient and good for document images
        cv2.imshow("blurred_img",blurred)
        # cv2.waitKey(0)
        _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # Quick morphological operation to clean up text
        kernel = np.ones((1, 1), np.uint8)
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        cv2.imshow("cleaned_img",cleaned)
        cv2.waitKey(0)
        return Image.fromarray(cleaned)
    except Exception as e:
        logger.exception(e)
        return None
    


if __name__=="__main__":
    image=Image.open("hummingbird.jpg")
    preprocessing(image)
