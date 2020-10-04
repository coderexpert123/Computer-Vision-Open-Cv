#image rotaion

import  cv2

img=cv2.imread("a.jpg")

height,width=img.shape[:2]
r_matrix=cv2.getRotationMatrix2D((width/2,height/2),120,.7)
rotated_iamge=cv2.warpAffine(img,r_matrix,(width,height))

cv2.imshow("Rotated image",rotated_iamge)
cv2.imshow("originkl image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()