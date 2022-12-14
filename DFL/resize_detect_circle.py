import cv2
import numpy as np

img = cv2.imread('jpg/sirokuro_mol.jpg')
img = cv2.imread('jpg/kurosiro.jpg')
height = img.shape[0]
width = img.shape[1]
img_big = cv2.resize(img , (int(width*1.0), int(height*3.0)))
cv2.imwrite('jpg/sirokuro_mol_resize.jpg' , img_big)
cv2.imwrite('jpg/kurosiro_resize.jpg' , img_big)

# ここから下を関数化

flg_ok = False
for i in range(20):
    big_ratio = i * 0.1 + 2
    print(big_ratio)
    img_big = cv2.resize(img , (int(width*1.0), int(height*big_ratio)))
    gray = cv2.cvtColor(img_big, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=1000, param1=100, param2=50, minRadius=200, maxRadius=2000)
    try:
        if len(circles) > 0 and len(circles) < 5:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                if height*big_ratio*0.2 < circle[1] and circle[1] < height*big_ratio*0.8:
                    # 円周を描画する
                    cv2.circle(img_big, (circle[0], circle[1]), circle[2], (0, 0, 255), 10)#img, center, radius, thickness, lineType, shift 
                    # 中心点を描画する
                    cv2.circle(img_big, (circle[0], circle[1]), 2, (0, 0, 255), 3)
                    img_nol = cv2.resize(img_big , (int(width*1.0), int(height)))
                    cv2.imwrite("jpg/sample_after.png", img_big)
                    
                    flg_ok = True
                    print("ok")
                    break
            if flg_ok == True:
                print("")
    except:
        print("no circle")

