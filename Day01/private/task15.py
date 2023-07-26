import cv2
import numpy as np
import matplotlib.pyplot as plt

def otsu_thresholding(image):
    # Convert the image to grayscale if it's not already in that format
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute histogram and normalize it
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.sum()

    # Initialization
    best_thresh = 0
    best_variance = 0
    total_pixels = image.shape[0] * image.shape[1]

    # Iterate through all possible threshold values
    for thresh in range(256):
        # Compute class probabilities and means for background and foreground
        w_background = np.sum(hist_norm[:thresh])
        w_foreground = 1.0 - w_background

        mean_background = np.sum(np.arange(thresh) * hist_norm[:thresh]) / (w_background + 1e-10)
        mean_foreground = np.sum(np.arange(thresh, 256) * hist_norm[thresh:]) / (w_foreground + 1e-10)

        # Compute between-class variance
        variance_between = w_background * w_foreground * (mean_background - mean_foreground) ** 2
    
        # Update if the variance is greater than the best variance found so far
        if variance_between > best_variance:
            best_variance = variance_between
            best_thresh = thresh

    _, binary_image = cv2.threshold(image, best_thresh, 255, cv2.THRESH_BINARY)

    return binary_image

# Load the image (make sure to replace 'your_image.png' with your image's filename)
image = cv2.imread('../data/00_src_imgs/thumbprint.jpeg')

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
