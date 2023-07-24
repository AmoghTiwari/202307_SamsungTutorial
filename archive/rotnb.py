import os
import cv2
import numpy as np

def buildRotMatrix(angle_deg):
    angle_rad = np.pi * angle_deg / 180
    R = np.array([ 
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad), np.cos(angle_rad)]
    ])
    return R

def rotateImage(img, angle_deg):
    R = buildRotMatrix(angle_deg)
    h,w,c = img.shape
    center_h, center_w = (h//2, w//2)
    # new_img = np.zeros((h,w,c), 'uint8')

    max_h, min_h, max_w, min_w = -np.inf, np.inf, -np.inf, np.inf

    for i in range(h):
        for j in range(w):
            y,x = R @ np.array([i,j])
            
            if y > max_h:
                max_h = y
            if y < min_h:
                min_h = y
            if x > max_w:
                max_w = x
            if x < min_w:
                min_w = x
    # breakpoint()
    new_h = np.ceil(max_h - min_h).astype('int') + 1
    new_w = np.ceil(max_w - min_w).astype('int') + 1
    new_img = np.zeros((new_h, new_w, c), 'uint8')
    center_h, center_w = (new_h//2, new_w//2)

    for i in range(h):
        for j in range(w):
            orig_i, orig_j = np.floor(R.T @ np.array([i-center_h,j-center_w]) + np.array([center_h, center_w])).astype('int')
            if orig_i < h and orig_j < w:
                new_img[i,j] = img[orig_i, orig_j]
            else:
                pass
    return new_img

DATA_DIR = "../data/00_src_imgs"
img_name = "rabbit_gray.jpg"
img_path = os.path.join(DATA_DIR, img_name)
img = cv2.imread(img_path)

cv2.imshow("orig_img", img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()

new_img = rotateImage(img, 90)

cv2.imshow("rot_img", new_img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
