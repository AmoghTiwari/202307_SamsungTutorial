import os
import cv2
import numpy as np
# from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

def linear_contrast_stretching(image):
    # Calculate the minimum and maximum pixel values in the image

    min_pixel_value = np.min(image)
    max_pixel_value = np.max(image)
    
    # Calculate the range of pixel values
    pixel_range = max_pixel_value - min_pixel_value

    # Perform linear contrast stretching
    stretched_image = ((image - min_pixel_value) / pixel_range) * 255.0
    stretched_image = np.clip(stretched_image, 0, 255).astype(np.uint8)

    return stretched_image

if __name__ == "__main__":
    # DATA_DIR = "202307_SamsungTutorial/data"
    DATA_DIR = "../data/00_src_imgs"

    img_name = "aston.png"
    img_path = os.path.join(DATA_DIR, img_name)
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray_stretched = linear_contrast_stretching(img_gray)

    cv2.imwrite("../data/03_contrast_stretching/01_lc_img_orig.png", img_gray)
    plt.hist(img_gray)
    # plt.show()
    plt.savefig("../data/03_contrast_stretching/01_lc_hist_orig.png")

    cv2.imwrite("../data/03_contrast_stretching/01_lc_img_stretched.png", img_gray_stretched)
    plt.hist(img_gray_stretched)
    # plt.show()
    plt.savefig("../data/03_contrast_stretching/01_lc_hist_stretched.png")
