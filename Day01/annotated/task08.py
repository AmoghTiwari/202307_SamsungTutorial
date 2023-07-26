import os
import cv2
import numpy as np

def gamma_transform(img, gamma):
    C = 255**(1-gamma)
    return C * (img**gamma)

if __name__ == "__main__":
    # DATA_DIR = "202307_SamsungTutorial/data"
    DATA_DIR = "../data/00_src_imgs"
    GAMMAS = [1, 0.75, 1.5]

    img_name = "aston.png"
    img_path = os.path.join(DATA_DIR, img_name)
    img = cv2.imread(img_path)

    for gamma in GAMMAS:
        img_transformed = gamma_transform(img, gamma)
        cv2.imshow(f"{gamma}", img_transformed)
        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()
        # cv2.imwrite(os.path.join("../data/contrast_stretching", f"gamma_aston{str(gamma).replace('.', '_')}.png"), img_transformed)
    