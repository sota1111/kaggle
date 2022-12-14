import os
import numpy as np
import pandas as pd
import cv2
from matplotlib import pyplot as plt
import seaborn as sn
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from IPython.display import Video


img = cv2.imread('jpg/throwin_101.jpg') # ファイル読み込み

# bgrでの色抽出
bgrLower = np.array([0, 0, 100])    # 抽出する色の下限(bgr)
bgrUpper = np.array([255, 150, 255])    # 抽出する色の上限(bgr)
img_mask = cv2.inRange(img, bgrLower, bgrUpper) # bgrからマスクを作成
extract = cv2.bitwise_and(img, img, mask=img_mask) # 元画像とマスクを合成
cv2.imwrite('jpg/throwin_101_red.jpg',extract)


img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# bgrでの色抽出
hsvLower = np.array([30, 0, 0])    # 抽出する色の下限(hsv)
hsvUpper = np.array([90, 255, 255])    # 抽出する色の上限(hsv)
img_mask1 = cv2.inRange(img_hsv, hsvLower, hsvUpper) # hsvからマスクを作成



frame_mask = img_mask1 

extract = cv2.bitwise_and(img_hsv, img_hsv, mask=frame_mask) # 元画像とマスクを合成
extract = cv2.cvtColor(extract, cv2.COLOR_YCrCb2BGR)
cv2.imwrite('jpg/throwin_101_hsv.jpg',extract)