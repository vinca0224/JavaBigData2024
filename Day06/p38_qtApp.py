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
from PyQt5.QtGui import QCloseEvent
# QMainWindow, QLabel, QPushButton 등은 QWidget을 상속한 자식 클래스(부모 클래스의 능력들을 다 사용할 수 있음)
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow, Qlabel, QPushButton

class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되야 함
        self.initUi()

    def initUi(self):
        self.setGeometry((1920-300)//2, (1080-300)//2, 320, 230) # 해상도 1920x1080에서 정중앙에서 위치
        self.setWindowTitle('세번째 Qt앱')
        self.setWindowIcon(QIcon('./images/windows.png'))  
    
        # 화면 UI에서 추가/변경할 것
        btn1 = QPushButton('클릭', self)
        btn1.setGeometry(210, 180, 100, 40)
        btn1.clicked.connect(self.btn1Clicked) # 버튼클릭 시그널이 발생하면 이를 처리하는 함수 연결
        self.show() # 윈도우 창 그리기

    def btn1Clicked(self):
        QMessageBox.about(self, '버튼클릭', '버튼을 눌렀습니다.')

    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소
            # ree = QMessageBox.question(self, '퇴근', '퇴근하시겠습니까?', QMessageBox.Yes)
            # if ree == QMessageBox.Yes: # 종료
            #     QCloseEvent.accept()
            # else: QCloseEvent.ignore()

app = QApplication(sys.argv) # 
inst = qtApp() # 객체생성
app.exec_() # 실행