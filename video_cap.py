
import cv2
import time
import os

videoNum = 0
frameNum = 0
videonames = []


def video_cap():
    global frameNum
    global videoNum
    videoAutoRemove()
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter("static/videos/" + time.strftime("%Y-%m-%d-%X",
                          time.localtime(time.time())) + '.mp4', fourcc, 30, (1280, 720))
    if cap.isOpened():
        while True:
            frameNum += 1
            ret, frame = cap.read()
            out.write(frame)
            if frameNum == 300:
                videoNum += 1
                break
        cap.release()
        out.release()
    frameNum = 0
    print("영상이 저장되었습니다.")


def videoAutoRemove():
    global videonames
    videoname = os.listdir("static/videos")
    if len(videoname) >= 10:
        videoname.sort()
        temp = videoname.pop(0)
        os.remove("static/videos/" + temp)
        print(temp + "를 삭제하였습니다.")
