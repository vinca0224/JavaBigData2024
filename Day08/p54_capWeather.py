# file : p54_capWeather.py
# desc : 네이버 날씨화면 캡쳐 

import pyautogui as auto
import pyperclip as clip
import time

regions = ['서울', '강원', '대전', '대구', '부산']

# auto.mouseInfo() #마우스 위치확인 452 138
for region in regions:
    auto.moveTo(452,138, duration=0.5)
    auto.leftClick()
    for _ in range(5):
        auto.press('delete')
    time.sleep(0.2)

    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl', 'v')
    time.sleep(0.2)

    auto.press('enter')
    time.sleep(1.0)

    # 캡쳐시작위치:400 258, 종료위치:1070 900
    startX, startY = 400, 258
    endX, endY = 1070, 900
    # auto.screenshot()만 사용하면 macos에서 동작안함
    im = auto.screenshot(region=(startX,startY, endX-startX, endY-startY))
    im.save(f'./Day08/{region}날씨.png')
    print('저장완료!')