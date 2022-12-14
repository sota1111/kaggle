import os
import numpy as np
import pandas as pd
import cv2
from matplotlib import pyplot as plt
import seaborn as sn
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from IPython.display import Video



sirokuro = cv2.imread('jpg/throwin_265_canny.jpg') # ファイル読み込み
kernel = np.ones((15,15),np.uint8)

closing = cv2.morphologyEx(sirokuro, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('jpg/sirokuro_mol_.jpg',closing)

kurosiro = 255-closing
cv2.imwrite('jpg/kurosiro.jpg',kurosiro)

img = cv2.imread('jpg/throwin_101.jpg') # ファイル読み込み
and_kurosiro =  cv2.bitwise_and(img, closing)
cv2.imwrite('jpg/and_sirokuro_test.jpg',and_kurosiro)