import numpy as np
import cv2

# img = 
img[np.where(img[:,:,-1]==0)]=[0,0,0,0]
cv2.imwrite("abcd.jpg", img[:,:,:3])
