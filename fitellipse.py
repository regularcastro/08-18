# import required libraries
import cv2
import numpy as np

# load the input image
img = cv2.imread("mititoyosimpla.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Ellipse", gray)

# apply thresholding to convert grayscale to binary image
ret,thresh = cv2.threshold(gray,175,255,cv2.THRESH_BINARY_INV)



# find the contours
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours detected:", len(contours))

# select the first contour
print(contours[0])
cnt = contours[0]

# fit the ellipse to the selected object
ellipse = cv2.fitEllipse(cnt)

# draw the ellipse on the input image
cv2.ellipse(img,ellipse, (0,0,255), 3)

# display the image with an ellipse drawn on it.
cv2.imshow("Ellipse", img)
cv2.waitKey(0)
cv2.destroyAllWindows()