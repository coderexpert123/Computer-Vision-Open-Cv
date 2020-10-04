#Hue :0-180 || Saturation|| 0-255,value 0-255
#color Filter Coor Shape
import  cv2


img=cv2.imread("a.jpg")
img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("origina image ",img_HSV)
cv2.imshow("HUE IMAGE",img_HSV[:,:,0])
cv2.imshow("SATURATION IMAGE",img_HSV[:,:,1])
cv2.imshow("VALUE IMAGE",img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()

