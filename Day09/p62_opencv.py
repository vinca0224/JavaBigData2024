# file : p62_opencv.py
# desc : OpenCV 영상처리

import cv2

samplePath = './Day09/earth.mp4'
cap = cv2.VideoCapture(samplePath) # 0은 웹캠, 또는 문자열로 동영상 경로
while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue

    ## 영상 편집
    blur = cv2.blur(frame, (10,10))
    cv2.imshow('blur', blur)
    flip = cv2.flip(frame, 0)
    cv2.imshow('flip', flip)

    cv2.imshow('original', frame)
    key = cv2.waitKey(5) # 딜레이 5ms
    if key == ord('q') : # q, esc(27)
        break
    elif key == ord('c'):
        cv2.imwrite('./Day09/cap.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()