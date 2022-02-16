from skimage import io, img_as_float
import numpy as np
import cv2

img=img_as_float(io.imread("images/index.jpg"))

resized_img=cv2.resize(img, (512,512))


kernel1=np.array(([-1,2,-1], [0,0,0], [1,2,1]))
kernel2=np.array(([-1,0,1], [-2,0,2], [-1,0,1]))

conv_img_1=np.absolute(cv2.filter2D(img, -1, kernel1, borderType=cv2.BORDER_CONSTANT))
conv_img_2=np.absolute(cv2.filter2D(img, -1, kernel2, borderType=cv2.BORDER_CONSTANT))

sum=cv2.add(conv_img_1, conv_img_2)

cv2.imshow("original", img)
cv2.imshow("resized", resized_img)
cv2.imshow("cv2 filter 1", conv_img_1)
cv2.imshow("cv2 filter 2", conv_img_2)
cv2.imshow("final result", sum)

cv2.waitKey(0)
cv2.destroyAllWindows()