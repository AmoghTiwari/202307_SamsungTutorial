import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    # Compute the histogram of the input image
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    
    # Calculate the cumulative distribution function (CDF) of the histogram
    cdf = hist.cumsum()
    
    # Normalize the CDF to lie in the range [0, 255]
    cdf_normalized = cdf * 255 / cdf[-1]
    
    # Use the CDF values as the new pixel intensities to perform equalization
    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    
    # Reshape the equalized pixel intensities back to the original image shape
    equalized_image = equalized_image.reshape(image.shape)
    
    # Convert to uint8 format (0-255) to save the image correctly
    equalized_image = equalized_image.astype(np.uint8)
    # equalized_image = cv2.equalizeHist(image)    
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
