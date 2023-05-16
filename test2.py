import cv2
import os

videoname = os.listdir("video/")
print(videoname)
videoname.sort()
print(videoname)

os.remove("video/" + videoname.pop(0))
print(videoname)
