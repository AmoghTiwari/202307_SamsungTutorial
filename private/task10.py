import os
import cv2
import numpy as np
# from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

def linear_contrast_stretching(image):
    # Calculate the minimum and maximum pixel values in the image
    min_pixel_value = np.min(image)
    # max_pixel_value = np.max(image)
    max_pixel_value = 100
    
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
    cv2.imwrite("../data/03_contrast_stretching/02_lc_img_orig.png", img_gray)
    cv2.imwrite("../data/03_contrast_stretching/02_lc_hist_orig.png", img_gray_stretched)

    plt.hist(img_gray)
    # plt.show()
    plt.savefig("../data/03_contrast_stretching/02_lc_img_stretched.png")

    plt.hist(img_gray_stretched)
    # plt.show()
    plt.savefig("../data/03_contrast_stretching/02_lc_hist_stretched.png")



    # for gamma in GAMMAS:
    #     img_transformed = gamma_transform(img, gamma)
    #     # cv2.imshow(f"{gamma}", img_transformed)
    #     # if cv2.waitKey(0) == ord('q'):
    #     #     cv2.destroyAllWindows()
    #     cv2.imwrite(os.path.join("../data/gamma_transforms", f"aston{str(gamma).replace('.', '_')}.png"), img_transformed)
    
# cv2.imwrite(os.path.join(DATA_DIR, "representation", "rabbit_orig.jpg"), img)
# print("Dimensions: ", img.shape)
# print("Type: ", type(img))
# print("data type: ", img.dtype)
# print("##### Uniqueness #####")
# print("\tNum Unique: ", len(np.unique(img)))
# print("\tMax: ", np.max(img))
# print("\tMin: ", np.min(img))
# print("\tMean: ", np.mean(img))
# print("\tAll Unique: ", np.unique(img))
