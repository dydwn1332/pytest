
import cv2
    
last_time = None
video_name = 'test'
videoNum = 0
frameNum = 0

def video_cap(cap):
    global last_time
    global frameNum
    global videoNum
    global video_name
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    cap = cap
    out = cv2.VideoWriter("video/" + video_name + str(videoNum) + '.mp4', fourcc, 30, (1280, 720))
    if cap.isOpened():
        while True:
            frameNum += 1
            ret, frame = cap.read()
            out.write(frame)
            if frameNum == 150:
                videoNum += 1
                break
        cap.release()
        out.release()
    frameNum = 0
