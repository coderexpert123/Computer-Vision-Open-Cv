#image information

import cv2

img=cv2.imread("a.jpg")
cv2.imshow("Output Image",img)

print("Height :",img.shape[0])

print("Width :",img.shape[1])

print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


