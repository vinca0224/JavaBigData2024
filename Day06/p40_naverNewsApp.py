# file : p40_naverNewsApp.py
# desc : PyQt5, QtDesigner naver API 연동 뉴스검색 앱 만들기

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow, Qlabel, QPushButton
import webbrowser # 기본 웹브라우저 모듈
from naverSearch import NaverSearch
import time

class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되야 함
        self.initUi()

    def initUi(self): # UI 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./Day06/naverNews.ui', self) # ui 파일에 맞춰서 변경
        self.setWindowIcon(QIcon('./images/news.png')) # 아이콘 파일에 맞춰서 변경
        # 버튼 시그널 처리
        self.btnSearch.clicked.connect(self.btnSearchClicked) # ui파일 내 위젯은 자동완성 안됨
        self.txtSearchWord.returnPressed.connect(self.btnSearchClicked) # 검색버튼 시그널 함수 연결
        self.tblSearchResult.itemSelectionChanged.connect(self.tblResultSelected)

        self.show() # 윈도우 창 그리기

    def tblResultSelected(self): # 테이블 클릭시 처리
        selectRow = self.tblSearchResult.currentRow() # 현재 선택된 행의 인덱스
        url = self.tblSearchResult.item(selectRow, 1).text()
        # QMessageBox.about(self, 'popup', url)
        webbrowser.open(url)

    def btnSearchClicked(self):
        searchWord = self.txtSearchWord.text().strip()
        
        if len(searchWord) == 0: # Validation Check(입력 검증)
            QMessageBox.about(self, '네이버 검색', '검색어를 입력하세요')
            return #함수탈출
        
        # QMessageBox.about(self, '네이버 검색', '검색 시작')
        # 검색 시작
        api = NaverSearch() # api 객체 생성
        jsonSearch = api.getSearchResult(searchWord)
        # print(jsonSearch)
        self.makeTable(jsonSearch) # 검색 결과로 리스트 뷰를 만드는 함수 호출

    def makeTable(self, data):
        result = data['items'] # 네이버 검색결과의 키 items의 값들만 활용
        # tblSearchResult 리스트 뷰 작업 시작
        self.tblSearchResult.setColumnCount(3)
        self.tblSearchResult.setRowCount(len(result))
        self.tblSearchResult.setHorizontalHeaderLabels(['기사제목','뉴스링크', '게시일자'])

        n = 0
        for post in result:
            self.tblSearchResult.setItem(n,0,QTableWidgetItem(post['title']))
            self.tblSearchResult.setItem(n,1,QTableWidgetItem(post['link']))
            tempDate = str(post['pubDate']).split(' ')
            year = tempDate[3]
            month = time.strptime(tempDate[2],'%b').tm_mon
            day = tempDate[1]
            date = f'{year}-{month}-{day}'
            
            self.tblSearchResult.setItem(n,2,QTableWidgetItem(date))
            n += 2

        self.tblSearchResult.setColumnWidth(0, 465)
        self.tblSearchResult.setColumnWidth(1, 200)
        self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 더블클릭 금지

    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

app = QApplication(sys.argv) # 
inst = qtApp() # 객체생성
app.exec_() # 실행