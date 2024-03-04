# file : p55_katalkAuto.py
# desc : 카톡 PC에서 자동으로 메시지 보내기

import pyautogui as auto
import pyperclip as clip
import os
import time

katalkLoc = auto.locateOnScreen('./Day08/findLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.doubleClick(clickPos)
time.sleep(0.5)

groupLoc = auto.locateOnScreen('./Day08/findLoc2.png')
clickPos = auto.center(groupLoc)
auto.doubleClick(clickPos)
time.sleep(0.2)

clip.copy('자동으로 보내는 메시지')
auto.hotkey('ctrl','v')
auto.press('\n')