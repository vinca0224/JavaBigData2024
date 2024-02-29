# file : p44_nothread.py
# desc : PyQt5 스레드 학습용

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
        uic.loadUi('./Day07/testThread.ui', self)
        self.setWindowTitle('노쓰레드 앱')
        self.setWindowIcon(QIcon('./images/windows.png')) 
        # 버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show() # 윈도우 창 그리기

    def btnStartClicked(self):
        self.pgbTask.setValue(0) # 재설정
        self.pgbTask.setRange(0,999_999) # 프로그래스바 범위 설정
        self.btnStart.setDisabled(True)
        # UI(메인)스레드가 화면을 그릴 수 있는 여유가 없음(응답없음 발생)
        
        for i in range(0, 1_000_000) : #0 ~ 99
            print(f'노쓰레드 진행 >> {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'노쓰레드 진행 >> {i}')

        self.btnStart.setEnabled(True)

    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

app = QApplication(sys.argv) # 
inst = qtApp() # 객체생성
app.exec_() # 실행