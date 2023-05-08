import cv2, numpy as np

thresh = 25  # threshold이진화 기준값
max_diff = 5
# 웹캠 연결
cap = cv2.VideoCapture(0)

# 웹캠 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
def video_feed():
    # 프레임 스트리밍
    if cap.isOpened():
        ret, a = cap.read()
        ret, b = cap.read()
        while ret:
            ret, c = cap.read()
            draw = c.copy()
            if ret == False:
                break

            a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)  # 변화된 위치를 알기위해 그레이 스케일로 변경
            b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
            c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

            diff1 = cv2.absdiff(a_gray, b_gray)  # 그레이스케일로 변환된 이미지를 비교하여 절대값의 차를 구한다.
            diff2 = cv2.absdiff(b_gray, c_gray)  # 변화가 있는 부분은 이전 픽셀과 이후 픽셀의 약간의 차이 생삭은 오묘한색이나옴

            ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)  # 절대값 이미지를 thresh(25)와 비교해서 작으면 0
            ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)  # 크면 255로 설정 이미지는 움직이는 부분만 흰색으로 나옴
            #                                           #absd에서 격한 차이가 나면 흰색
            diff = cv2.bitwise_and(diff1_t, diff2_t)  # 엔드 연산을 해서 두개의 이미지의 변화부분을 하나로 합채

            k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))  # 부호가 없는 8비트 넘파이 3X3배열을 생성하고 원소는

            diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)  # 모폴로지 연산 수행 노이즈제거 및 변동픽셀을 커널로 초기화
            # 오픈연산은 침식연산이후 팽창연산을 수행
            diff_cnt = cv2.countNonZero(diff)  # 모폴로지 연산을 수행한 영상의 변경된 픽셀 위치 수의 기준값
            if diff_cnt > max_diff:  # 기준값보다 낮으면 네모를 그림
                nzero = np.nonzero(diff)  # 0이 아닌 배열의 인덱스 위치를 반환 2차원 배열형태(y배열, x배열)
                cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])),
                              (max(nzero[1]), max(nzero[0])), (0, 255, 0), 2)

                cv2.putText(draw, "Motion detected", (10, 30),
                            cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
            ret, buffer = cv2.imencode('.jpg', draw)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            a = b
            b = c