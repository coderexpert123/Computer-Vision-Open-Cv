#Reading image in open cv2
import  cv2

img=cv2.imread("a.jpg")

cv2.imshow("output imgae",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
