import  cv2
import  numpy as  np
image =cv2.imread("a.jpg")

B,G,R=cv2.split(image)

zeroes=np.zeros(image.shape[:2],dtype="uint8")


cv2.imshow("RED",cv2.merge([zeroes,zeroes,R]))
cv2.waitKey(0)


cv2.imshow("GREEN",cv2.merge([zeroes,G,zeroes]))
cv2.waitKey(0)

cv2.imshow("BLUE",cv2.merge([B,zeroes,zeroes]))
cv2.waitKey(0)
cv2.destroyAllWindows()