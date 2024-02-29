# file : p47_QrCodeApp.py
# desc : PyQt5 QR코드 앱

# pip install qrcode

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow, Qlabel, QPushButton
import qrcode

class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되야 함
        self.initUi()

    def initUi(self): # UI 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./Day07/qrApp.ui', self)
        self.setWindowTitle('QR코드 생성기')
        self.setWindowIcon(QIcon('./images/windows.png')) 
        # 버튼 시그널 처리
        self.btnGenerate.clicked.connect(self.btnGenerateClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show() # 윈도우 창 그리기

    def btnGenerateClicked(self):
        data = self.txtQrData.text()

        if len(data.strip()) == 0:
            QMessageBox.about(self,'경고','데이터를 입력하세요')
            return
        else : 
            imgPath = './Day07/qr.png'
            qrImage = qrcode.make(data)
            qrImage.save(imgPath)
            img = QPixmap(imgPath)
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))

    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

app = QApplication(sys.argv) # 
inst = qtApp() # 객체생성
app.exec_() # 실행