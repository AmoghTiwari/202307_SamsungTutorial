import os
import cv2
import numpy as np
# from google.colab.patches import cv2_imshow

# DATA_DIR = "202307_SamsungTutorial/data"
DATA_DIR = "../data/00_src_imgs"

img_name = "rabbit_gray.jpg"
img_path = os.path.join(DATA_DIR, img_name)
img = cv2.imread(img_path)

print("Dimensions: ", img.shape)
print("Type: ", type(img))
print("data type: ", img.dtype)
print("##### Uniqueness #####")
print("\tNum Unique: ", len(np.unique(img)))
print("\tMax: ", np.max(img))
print("\tMin: ", np.min(img))
print("\tMean: ", np.mean(img))
print("\tAll Unique: ", np.unique(img))

cv2.imshow("img", img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
cv2.imwrite(os.path.join("../data/02_representation", "rabbit_orig.jpg"), img)