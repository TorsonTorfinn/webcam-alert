import numpy as np
import cv2

img_px = np.array(
[[[255, 0, 0],
  [255, 255, 255],
  [127, 55, 151],
  [187, 41, 160]],

 [[0, 255, 0],
  [255, 55, 255],
  [33,  255,  133],
  [100, 200, 40]],

 [[255, 255, 255],
  [0, 255, 0],
  [47, 89, 173],
  [255, 255, 255]]]
)

cv2.imwrite('imgs/image1.png', img_px) # basically img_px';; be written in this .png