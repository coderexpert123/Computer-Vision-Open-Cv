import  cv2

img=cv2.imread("a.jpg")

height,width=img.shape[:2]
print(height)
print(width)
q_height,q_width=height/3,width/3
print(q_height)
print(q_width)
cv2.waitKey(0)
cv2.destroyAllWindows()
