# file : p63_opencv.py
# desc : OpenCV 영상처리

import cv2

samplePath = './Day09/news.mp4'
faceCascade = cv2.CascadeClassifier('./Day09/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(samplePath) # 0은 웹캠, 또는 문자열로 동영상 경로
while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue

    ## 영상 편집
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor= 1.2,
        minNeighbors= 5,
        minSize= (20, 20)
    )
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, pt1=(x,y),pt2=(x+w, y+h), color= (255,0,0), thickness= 2)

    cv2.imshow('original', frame)

    key = cv2.waitKey(5) # 딜레이 5ms
    if key == ord('q') : # q, esc(27)
        break

cap.release()
cv2.destroyAllWindows()