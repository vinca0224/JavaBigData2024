# file : p60_opncv.py
# desc : OpenCV 이미지 처리 계속

import cv2

image = cv2.imread('./Day09/coby.jpg', cv2.IMREAD_UNCHANGED) # 원본
dst = cv2.flip(image, 2) # 0: 위아래 반전, 1: 좌우반전

height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width//2, height//2), 180, -1) #scale -> CCW(-x): 반시계 방향, CW(x): 시계 방향, x는 배율
thrd = cv2.warpAffine(image,matrix,(width,height))
reverse = cv2.bitwise_not(image) # 역상, 반전색
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) # 이진화


cv2.imshow('Coby the Cat', image)
cv2.imshow('flip', dst)
cv2.imshow('rotation', thrd)
cv2.imshow('reverse', reverse)
cv2.imshow('gray', gray)
cv2.imshow('bin', bny)

cv2.waitKey(0)
cv2.destroyAllWindows()