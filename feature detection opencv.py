import numpy as np
import cv2

img = cv2.imread("img.jpeg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "haarcascade.xml"

cascade = cv2.CascadeClassifier(path)

detected = cascade.detectMultiScale(gray, scaleFactor=1.02,minNeighbors=20,minSize=(10,10))

for (x, y, w, h) in image:
	xc = (x + x+w)/2
	yc = (y + y+h)/2
	radius = w/2
	cv2.circle(img, (int(xc),int(yc)), int(radius), (255,0,0), 2)
  
cv2.imshow("detected",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
