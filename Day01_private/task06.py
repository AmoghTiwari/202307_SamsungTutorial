import cv2
import numpy as np
import matplotlib.pyplot as plt

img = None ### Write your code here

cv2.imshow("My Image", img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()

cv2.imwrite("../data/02_representation/my_image_cv.png", np.repeat(img[:, :, np.newaxis], 3, axis=2))
plt.imsave("../data/02_representation/my_image_mp.png", np.repeat(img[:, :, np.newaxis], 3, axis=2))
