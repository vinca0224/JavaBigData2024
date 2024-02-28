# file : p38_qtApp.py

# desc : PyQt5 앱 만들기(이어서)

'''
PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C, C++ 에서 사용할 GUI(WinApp) 프레임워크(멀티 플랫폼)

설치 > pip install PyQt5
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# QMainWindow, QLabel, QPushButton 등은 QWidget을 상속한 자식 클래스(부모 클래스의 능력들을 다 사용할 수 있음)
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow, Qlabel, QPushButton

class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되야 함
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 320, 230) # 바탕화면 정해진 위치에 넓이와 높이로 그릴 설정
        self.setWindowTitle('세번째 Qt앱')
        self.setWindowIcon(QIcon('./images/windows.png'))  
        self.show() # 윈도우 창 그리기 

app = QApplication(sys.argv) # 
inst = qtApp() # 객체생성
app.exec_() # 실행