#Bimary image || convert greyscale image to Binary Image

import  cv2
img =cv2.imread("a.jpg",0)
cv2.imshow("Grey Image",img)
cv2.waitKey(0)

ret, bw=cv2.threshold(img,112,255,cv2.THRESH_BINARY)


cv2.imshow("Binary image",bw)
cv2.waitKey(0)

cv2.destroyAllWindows()
