import this

import cv2, time

video_name = 'test'
videoNum = 0
fourcc = cv2.VideoWriter_fourcc(*'avc1')
cap = cv2.VideoCapture(0)
frameNum = 0
last_time = 0

def video_cap():
    global last_time
    global frameNum
    if last_time is not None and time.time() - last_time < 10:
        print("10초가 지나지 않았습니다.")
        return
    global frameNum
    out = cv2.VideoWriter('/video/' + video_name + str(videoNum) + '.mp4', fourcc, 30, (1280, 720))
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            out.write(frame)
            if frameNum == 300:
                break
        cap.release()
        out.release()
    frameNum = 0
