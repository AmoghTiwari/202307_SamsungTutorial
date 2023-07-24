import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    equalized_image = cv2.equalizeHist(image)    
    return equalized_image

# Load the image (you can replace 'input_image.jpg' with your own image file)
image = cv2.imread('../data/00_src_imgs/rabbit_gray.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = histogram_equalization(image)

# Plot the histograms
plt.figure(figsize=(16,12))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.hist(image.flatten(), 256, [0, 256], color='r', alpha=0.7)
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.title('Original Histogram')

plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')

# plt.figure(figsize=(15, 5))
plt.subplot(2, 2, 4)
plt.hist(equalized_image.flatten(), 256, [0, 256], color='g', alpha=0.7)
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.title('Equalized Histogram')

plt.show()
