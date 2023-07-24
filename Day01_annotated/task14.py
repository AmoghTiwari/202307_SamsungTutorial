import cv2
import numpy as np
import matplotlib.pyplot as plt

def otsu_thresholding(image):
    # Convert the image to grayscale if it's not already in that format
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarize the image using the best threshold
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return binary_image

# Load the image (make sure to replace 'your_image.png' with your image's filename)
image = cv2.imread('../data/00_src_imgs/thumbprint02.jpeg')

# Apply Otsu's method for thresholding
binary_image = otsu_thresholding(image)

# binary_image = binary_image // 255
# binary_image = np.repeat(binary_image[:, :, np.newaxis], 3, axis=2)
# masked_img = image * binary_image

# Display the original and binary images side by side for comparison
plt.imshow(image, 'gray')
plt.show()
cv2.imwrite("../data/04_thresholding/otsu_orig.png", image)

plt.imshow(binary_image, 'gray')
plt.show()
cv2.imwrite("../data/04_thresholding/otsu_thresh.png", binary_image)

# plt.imshow(masked_img, 'gray')
# plt.show()
# cv2.imwrite("../data/04_thresholding/masked_img.png", masked_img)
