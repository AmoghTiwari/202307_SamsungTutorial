import cv2
import numpy as np
import matplotlib.pyplot as plt

def threshold_image(image_path, threshold_value):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    thresholded_image = np.zeros_like(image)
    thresholded_image[image > threshold_value] = 255
    # breakpoint()

    # Manually threshold the image
    threshold_image = None # Add your code here

    # Display the original and thresholded images
    plt.figure(figsize=(8,6))
    plt.subplot(1,2,1)
    plt.imshow(image, 'gray')

    plt.subplot(1,2,2)
    plt.imshow(thresholded_image, 'gray')
    plt.show()
    plt.savefig("../data/04_thresholding/thumbprint_man_thresh.png")
    # cv2.imshow("Original Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'your_image_path.jpg' with the path of your image file
    image_path = '../data/00_src_imgs/thumbprint02.jpeg'
    threshold_image(image_path, 127)