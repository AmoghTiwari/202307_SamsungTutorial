import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = None ### Write your code here

img = np.full((300, 300), 127).astype('uint8')
img[:, 100:200] = 255
img[0,0] = 0

# cv2.imshow("My Image", img)
# cv2.waitKey(0)
# if cv2.waitKey(0) == ord('q'):
#     cv2.destroyAllWindows()

plt.imshow(img, cmap='gray')
plt.show()
cv2.imwrite("../data/02_representation/my_image_cv.png", np.repeat(img[:, :, np.newaxis], 3, axis=2))
plt.imsave("../data/02_representation/my_image_mp.png", np.repeat(img[:, :, np.newaxis], 3, axis=2))
