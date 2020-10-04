#greySCale image || convert greyscale image to color imagr(RGB)

import  cv2
img =cv2.imread("a.jpg",0)



cv2.imshow("GreyScaleImage",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
