# file : p53_imgLoad.py
# desc : pyautogui에서 이미지 읽어오기

import pyautogui as auto

# capImg = auto.locateOnScreen('./Day08/screen.png') # 이미지 로드
# print(capImg)
# auto.click(capImg)


auto.alert('테스트!', title = 'PyAutoGui')

auto.confirm('계속 진행하시겠습니까?')

text = auto.prompt('원하는 메시지 입력')
print(text)

pwd = auto.password('암호 입력')
print(pwd)