# file : p48_transApp.py
# desc : PyQt5 구글 번역 앱
# 모듈, 라이브러리 설치 시 버전 업/다운

# pip install googletrans==3.1.0a0

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow, Qlabel, QPushButton

from googletrans import Translator

class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되야 함
        self.initUi()
        self.myTrans = Translator() # 구글번역기 객체 생성

    def initUi(self): # UI 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./Day07/transApp.ui', self)
        self.setWindowTitle('구글 번역앱')
        self.setWindowIcon(QIcon('./images/windows.png')) 
        # 버튼 시그널 처리
        self.txtBaseText.returnPressed.connect(self.btnTransClicked)
        self.btnTrans.clicked.connect(self.btnTransClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show() # 윈도우 창 그리기

    def btnTransClicked(self):
        QMessageBox.about(self,'번역','번역 시작')
        text = self.txtBaseText.text().strip()
        if len(text) != 0:
            result = self.myTrans.translate(text, src='auto', dest='en')
            self.txbResult.append(result.text)
        


    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

app = QApplication(sys.argv) # 
inst = qtApp() # 객체생성
app.exec_() # 실행