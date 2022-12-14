import cv2
import numpy as np

img = cv2.imread("jpg/throwin_265_mol.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,90,450,apertureSize = 3)
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=80, minLineLength=10, maxLineGap=20)
for line in lines:
    print(line)
    x1, y1, x2, y2 = line[0]
    if abs(x2-x1)<5000 and abs(y2-y1)>100 :
        red_line_img = cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 3)

cv2.imwrite("jpg/haugh_straight.jpg", red_line_img)