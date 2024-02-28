# file : p39_qtApp.py
# desc : PyQt5, QtDesigner 같이 사용

'''
PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C, C++ 에서 사용할 GUI(WinApp) 프레임워크(멀티 플랫폼)

설치 > pip install PyQt5
설치 > pip install PyQt5Designer
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow, Qlabel, QPushButton

class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되야 함
        self.initUi()

    def initUi(self): # UI 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./Day06/firstApp.ui', self)
        self.setWindowIcon(QIcon('./images/windows.png')) 
        # 버튼 시그널 처리
        self.btnMsg.clicked.connect(self.btnMsgClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show() # 윈도우 창 그리기

    def btnMsgClicked(self):
        self.label.setText('Don\'t click')
        QMessageBox.about(self, 'Qt디자이너', '클릭했습니다.')

    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

app = QApplication(sys.argv) # 
inst = qtApp() # 객체생성
app.exec_() # 실행