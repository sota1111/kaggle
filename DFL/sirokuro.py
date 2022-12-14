# Modules used in this notebook
import os
import numpy as np
import pandas as pd
import cv2 
from matplotlib import pyplot as plt
import seaborn as sn
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from IPython.display import Video

def vis_event(row, name, before=5, after=5):
    print(row["event_attributes"])
    filename = str(name) + "_"+ str(row['index']) + ".mp4"
    ffmpeg_extract_subclip(
        f"input/dfl-bundesliga-data-shootout/train/{row['video_id']}.mp4", 
        int(row['time']) - before, 
        int(row['time']) + after, 
        targetname=filename,
    )
    return filename, Video(filename, width=800)

## Rescaling Frame (for videos, live videos and images)
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def draw_line_hough(img, filename):
    lines = cv2.HoughLinesP(img, rho=1, theta=np.pi/360, threshold=80, minLineLength=10, maxLineGap=20)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if abs(x2-x1)<5000 and abs(y2-y1)>100 :
            red_line_img = cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 3)
    cv2.imwrite("jpg/" + filename.replace(".mp4","") + "_line.jpg", red_line_img)
    return red_line_img


# Grab a frame from a video
df = pd.read_csv("input/dfl-bundesliga-data-shootout/train.csv")
df_throwin = df[df["event"] == "throwin"].reset_index()

event_index = df_throwin.iloc[4]
event_name, _ = vis_event(event_index, name='throwin')
filename = str(event_name)# + "_"+ str(event_index)

# Grab a frame from a video
path_to_vid = filename
vidcap = cv2.VideoCapture(path_to_vid)
success, img = vidcap.read()

# ここで秒数をずらしてloopする処理を追加する
for i in range(1):
    read_fps= vidcap.get(cv2.CAP_PROP_FPS) # 1秒あたりのフレーム数を取得
    start_point = i*0.05 # i*1秒間隔で読む
    # 秒数と１秒あたりフレーム数をかけたフレームからスタート
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_point * read_fps)     
    success, img = vidcap.read()

    rescaled = rescaleFrame(img, 1)
    gray = cv2.cvtColor(rescaled, cv2.COLOR_BGR2GRAY)
    
    # Get canny edges
    max_val = 175
    min_val = 100
    canny = cv2.Canny(gray, min_val, max_val, cv2.THRESH_BINARY)
    cv2.imwrite('jpg/test.jpg',canny) # ファイル読み込み
    canny = cv2.imread('jpg/test.jpg') # ファイル読み込み
    kernel = np.ones((15,15),np.uint8)
    closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
    img_line = draw_line_hough(closing, filename)

    img_last = closing
    if i > 0:
        img_last = img_last | img_old
    img_old = img_last
    # Take a look at the frame

cv2.imwrite("jpg/" + filename.replace(".mp4","")  + "_canny.jpg", canny)
cv2.imwrite("jpg/" + filename.replace(".mp4","") + "_mol.jpg", closing)
cv2.imwrite("jpg/" + filename.replace(".mp4","") + "_line.jpg", img_line)
#cv2.imwrite("jpg/" + filename + "_line.jpg", img_line)


vidcap.release()