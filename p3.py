#write  file usinng open cv2

import cv2
img=cv2.imread("a.jpg")

cv2.imshow("output image",img)


cv2.imwrite("Outputimage.png",img)

cv2.imwrite("Outputimage.jpeg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
