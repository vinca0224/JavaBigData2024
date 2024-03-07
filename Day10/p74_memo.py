# file : p74_memo.py
# desc : 메모장 만들기

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *
import cv2

class WinApp(QMainWindow): #Qwidget 아님
    def __init__(self) -> None:
        super().__init__()
        self.initUi()
        self.initSignal()

    def initUi(self):
        uic.loadUi('./Day10/memo.ui',self)
        
        # self.setWindowIcon(QIcon('./Day10/imgs/editor.png'))
        
        self.setWindowTitle('메모장 v0.5')
        text = QPlainTextEdit()
        self.show()

    def initSignal(self):
    # 메뉴 / 툴바 액션에 대한 시그널 처리함수 선언
        self.actionOpen.triggered.connect(self.actionOpenClicked)
        self.actionSave.triggered.connect(self.actionSaveClicked)
        self.actionSaveAs.triggered.connect(self.actionSaveAsClicked)
        self.actionQuit.triggered.connect(self.actionQuitClicked)
        self.actionAbout.triggered.connect(self.actionAboutClicked)

    def actionOpenClicked(self):
        text = QFileDialog.getOpenFileName(self, '텍스트 열기', '', 'Text file(*.txt)')
        pass

    def actionSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '텍스트 저장', '', 'Text file(*.txt)')
        if filePath == '' : return
        textBox = self.QPlainTextEdit.text()
        textBox.save(filePath)

    def actionSaveAsClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '텍스트 저장', '', 'Text file(*.txt)')
        if filePath == '' : return
        text = self.plainTextEdit.text()
        text.save(filePath)

    def actionQuitClicked(self):
        cv2.destroyAllWindows() # 메모리 정리
        exit(0)

    def actionAboutClicked(self):
        QMessageBox.about(self, '프로그램 정보', '메모장 Ver 0.5')

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes: QCloseEvent.accept()
        else: QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())