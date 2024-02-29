# file : p45_threadApp.py
# desc : PyQt5 스레드 학습용

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow, Qlabel, QPushButton

class BackgroundWorker(QThread): # PyQt용 스레드
    initUiSignal = pyqtSignal(int) # 스레드로 진행할 때에 UI에서 초기화부분 시그널 전달
    setPgbSignal = pyqtSignal(int) # 스레드 진행 시 변경되는 숫자를 UI로 전달
    setTxbSignal = pyqtSignal(str) # 스레드 진행 시 화면에 출력될 문자열 UI쪽으로 전달
 
    def __init__(self, parent) -> None: # 부모는 qtApp 클래스
        super().__init__(parent)
        self.parent = parent

    def run(self) -> None:
        maxVal = 1000
        self.initUiSignal.emit(maxVal)

        for i in range(maxVal):
            print(f'스레드 진행 >> {i}')
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'스레드 진행 >> {i}')
            # self.parent.pgbTask.setValue(i) # UI 스레드의 권한을 백그라운드 스레드에 주지않음
            # self.parent.txbLog.append(f'스레드 진행 >> {i}') # 사용 불가

class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되야 함
        self.initUi()

    def initUi(self): # UI 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./Day07/testThread.ui', self)
        self.setWindowTitle('쓰레드 앱')
        self.setWindowIcon(QIcon('./images/windows.png')) 
        # 버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show() # 윈도우 창 그리기

    def btnStartClicked(self):
        self.btnStart.setDisabled(True)
        th = BackgroundWorker(self) # qtApp 부모클래스
        th.start() # 스래드 내 run() 함수 실행
        th.initUiSignal.connect(self.initpgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbLog)

        self.btnStart.setEnabled(True)

    @pyqtSlot(str)
    def setTxbLog(self, msg):
        self.txbLog.append(msg)

    @pyqtSlot(int)
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

    @pyqtSlot(int) # pyqtSignal에서 넘어온 값을 처리해 주는 부분이라고 선언
    def initpgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0,maxVal-1)

    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

app = QApplication(sys.argv) # 
inst = qtApp() # 객체생성
app.exec_() # 실행