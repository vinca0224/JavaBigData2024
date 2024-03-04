# file : p50_mouseAuto.py
# desc : PyAutoGui로 마우스 조작

'''
파이썬 모듈 설치 시 명령프롬프트보다 VScode 내 터미널에서 설치를 추천
PyAutoGui 모듈 설치
> pip install pyautogui
'''

import pyautogui as auto
 
print(auto.size()) # 현재 모니터의 해상도 확인 Size(wodth = 1920, height = 1080)
print(auto.position()) # 현재 마우스의 위치

# pyautogui 마우스 설정 창
# pillow 모듈이 같이 설치되어야 색상 표시 가능
# auto.mouseInfo()

## 마우스 이동(절대좌표)
# auto.moveTo(1,1) 
# auto.moveTo(365,50, duration=1.0) # x축 365, y축 50으로 1.0초 동안 이동
# auto.moveTo(1000,500)

# ## 마우스 이동(상대좌표)
# # auto.move(500,500,duration=1.5) # 현재 위치에서 x축 500, y축 500으로 1.5초 동안 이동

# ## 마우스 클릭
# # auto.leftClick(x=365, y=50) # 해당 위치로 가서 바로 좌클릭
# # auto.rightClick(x=800, y=400) # 해당 위치로 가서 바로 우클릭
# auto.click(clicks=4, interval=0.1, button='left') # 왼쪽 버튼을 소스코드 에디터에서 0.1초 단위로 네번 클릭, 소스 전체 선택

## 마우스 드래그
# 406,315에서 # 1727,626까지 드래그
auto.leftClick(x=406,y=315, duration=1.0)
auto.dragTo(x=1727, y=626, duration=2.0, button='left')

auto.dragRel(100,100,duration=1.0, button='left') # 현재 위치에서 500, 400으로 1초동안 드래그

## 마우스 휠
auto.scroll(1000) # 양수 : 위로 스크롤
auto.scroll(-800) # 음수 : 아래로 스크롤