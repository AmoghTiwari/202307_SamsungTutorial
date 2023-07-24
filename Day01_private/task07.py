import os
import cv2
import numpy as np
# from google.colab.patches import cv2_imshow

# DATA_DIR = "202307_SamsungTutorial/data"
DATA_DIR = "../data/00_src_imgs"

img_name = "rabbit_gray.jpg"
img_path = os.path.join(DATA_DIR, img_name)
img = cv2.imread(img_path)

for num_bits in range(8):
    print(f"#### Using {256//(2**num_bits)} bits ####")
    img_new = (img / (2**num_bits)) * (2**(num_bits))

    print("Dimensions: ", img_new.shape)
    print("Type: ", type(img_new))
    print("data type: ", img_new.dtype)
    print("##### Uniqueness #####")
    print("\tNum Unique: ", len(np.unique(img_new)))
    print("\tMax: ", np.max(img_new))
    print("\tMin: ", np.min(img_new))
    print("\tMean: ", np.mean(img_new))
    print("\tAll Unique: ", np.unique(img_new))
    print()
    print()

    cv2.imshow(f"{256//(2**num_bits)} Bits", img_new)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    # cv2.imwrite(os.path.join(DATA_DIR, "bitplane_slicing", f"rabbit{(256 // (2**num_bits))}_bits.jpg"), img_new)
