import cv2
img = cv2.imread(r'C:\Users\Gokuldas\Deep Learning\Gkdas2k1\opencv\data\men.jpeg')
print(img)
cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
