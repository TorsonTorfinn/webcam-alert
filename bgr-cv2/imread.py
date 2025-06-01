import cv2

image = cv2.imread('imgs/image.png')
print(image.shape)
print(image, "\n")

kitty = cv2.imread('imgs/kitty.png')
print(kitty.shape)