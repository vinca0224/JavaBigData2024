# file : p59_opencv.py
# desc : OpenCv 활용

# OpenCV 실시간 이미지 프로세싱 라이브러리
'''
> pip install opencv-python
'''

import cv2

# print(cv2.__version__) #OpenCV 설치 확인용

image = cv2.imread('./Day09/coby.jpg', cv2.IMREAD_UNCHANGED) # cv2.IMREAD_GRAYSCALE -> 컬러 이미지를 흑백으로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 원본을 흑백으로 변경

height, width, channel = image.shape
print(width, height, channel)

sizeSmall = cv2.resize(image, (width//2, height//2))
img_cropped = image[:,:(width//2)] # y축, x축

cv2.imshow('Coby the Cat, color', image) # 원본
cv2.imshow('Small Coby', sizeSmall) # 높이,너비 반으로 줄인 사이즈
cv2.imshow('Cobythe Cat, gray', gray) # 흑백
cv2.imshow('cropped Coby', img_cropped) # x축을 반으로 자름

cv2.waitKey(0)
cv2.destroyAllWindows()