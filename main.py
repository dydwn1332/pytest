import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter('test.mp4', fourcc, 30, (1280, 720))
if cap.isOpened():
    while True:
        ret, img = cap.read()
        cv2.imshow('test', img)
        out.write(img)
        if cv2.waitKey(1) == ord('q'):
            break
        if cv2.waitKey(1) == ord('c'):
            cv2.imwrite('test.png', img)
cap.release()
out.release()
cv2.destroyAllWindows()
