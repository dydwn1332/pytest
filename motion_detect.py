import cv2
import numpy as np, video_cap
import threading

def img_Connect(a, b, c, d):
    img = np.hstack((a, b))
    img2 = np.hstack((c, d))
    result = np.vstack((img, img2))
    return result


thresh = 25  # threshold이진화 기준값
max_diff = 5
motionnum = 0
title_num = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)

if cap.isOpened():
    ret, a = cap.read()
    ret, b = cap.read()
    while ret:
        print(motionnum)
        if motionnum >= 30:
            video_cap.video_cap()
            motionnum = 0
        ret, c = cap.read()
        draw = c.copy()
        if ret == False:
            break

        a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)  # 변화된 위치를 알기위해 그레이 스케일로 변경
        b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

        diff1 = cv2.absdiff(a_gray, b_gray)  # 그레이스케일로 변환된 이미지를 비교하여 절대값의 차를 구한다.
        diff2 = cv2.absdiff(b_gray, c_gray)  # 변화가 있는 부분은 이전 픽셀과 이후 픽셀의 약간의 차이 생삭은 오묘한색이나옴
        absimg = diff1
        ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)  # 절대값 이미지를 thresh(25)와 비교해서 작으면 0
        ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)  # 크면 255로 설정 이미지는 움직이는 부분만 흰색으로 나옴
        #                                           #absd에서 격한 차이가 나면 흰색
        diff = cv2.bitwise_and(diff1_t, diff2_t)  # 엔드 연산을 해서 두개의 이미지의 변화부분을 하나로 합채
        andimg = diff
        k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))  # 부호가 없는 8비트 넘파이 3X3배열을 생성하고 원소는
        # cross모양만 1로 설정 kk 와 동일한 동작
        # kk = np.array([[1, 1, 1],
        #                [1, 1, 1],
        #                [1, 1, 1]
        #                ], dtype=np.uint8)

        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)  # 모폴로지 연산 수행 노이즈제거 및 변동픽셀을 커널로 초기화
        # 오픈연산은 침식연산이후 팽창연산을 수행
        diff_cnt = cv2.countNonZero(diff)  # 모폴로지 연산을 수행한 영상의 변경된 픽셀 위치 수의 기준값
        if diff_cnt > max_diff:  # 기준값보다 낮으면 네모를 그림
            nzero = np.nonzero(diff)  # 0이 아닌 배열의 인덱스 위치를 반환 2차원 배열형태(y배열, x배열)
            cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])),
                          (max(nzero[1]), max(nzero[0])), (0, 255, 0), 2)

            cv2.putText(draw, "Motion detected", (10, 30),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
            motionnum += 1

        totalimg = img_Connect(draw, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR), cv2.cvtColor(absimg, cv2.COLOR_GRAY2BGR),
                              cv2.cvtColor(andimg, cv2.COLOR_GRAY2BGR))
        # 초반에 저장해둔 카메라 영상과
        # 모폴로지 연산이 끝난 diff를 3차원 이미지로 변경후 병합
        totalimg = cv2.resize(totalimg, dsize=(0, 0), fx=0.3, fy=0.3)
        cv2.imshow('motion', totalimg)

        a = b
        b = c

        if cv2.waitKey(1) & 0xFF == 27:
            break
