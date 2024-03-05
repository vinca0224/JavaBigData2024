# 빅데이터 언어 2024
빅데이터을 이용한 자바 개발자 과정 : 파이썬 학습

##1일차('24. 02. 21)
- 파이썬 개발환경
    - [Github](https://github.com/) 가입
    - [Git](https://git-scm.com/) 설치
    - [Github desktop](https://desktop.github.com/) 설치
    - [Visual Studio Code](https://code.visualstudio.com/) 설치
    - [Python](https://www.python.org/) 설치
    - [나눔고딕코딩](https://github.com/naver/nanumfont) 설치

- 파이썬 학습
    - 파이썬 개요
        - 쉽고 간결한 문법, 무료
        - 빠른 개발속도
    - 파이썬 기초문법
        - 숫자형(정수, 실수, 지수, 진수)
            - 변수만 선언, 값만 할당하면 숫자형으로 지정
            - C, C++, Java와 달리 형 지정이 없음
        ```python
        #특수 숫자형
        binVal = 0b11111111 #255 0~1
        octVal = 0o11 #9  0~7
        hexVal = 0xFF #255 0~9ABCDEF
        print('2진수', binVal, '8진수', octVal, '16진수',hexVal)
        ```
        - 문자열(특수형태 리스트)형(연산, 문자열 포맷, 함수)
        ```python
        # '', "" 모두 사용 가능
        ```
        - 리스트형, 튜플형(연산, 함수)
            - 리스트는 수정, 삭제 가능
            - 튜플은 수정, 삭제 불가, 그외에는 리스트와 동일

##2일차('24. 02. 22)
- 파이썬 학습
    - 파이썬 기초문법
        - Dictionary, 집합
        - 불형
        - None형
        - 제어문(if, for, while)
        - 제어문 연습
        - 함수

##3일차('24. 02. 23)
- 파이썬 학습
    - 파이썬 기초문법
        - 입/출력
        - 객체지향

##4일차('24. 02. 26)
- 파이썬 학습
    - 파이썬 기초문법
        - 모듈, 패키지
        - (★)예외 처리, 디버깅 : 디버깅하면서 예외를 찾고 예외처리
        - 내장 함수
        - 표준 및 외부 라이브러리

##5일차('24. 02. 27)
- 파이썬 학습
    - 파이썬 응용
        - OS 내 디렉토리 검색
        - 아스키 및 유니코드
        - 주소록 앱 만들기

        ```python
        class Contact: # 주소록 클래스
            # 생성자
            def __init__(self, name, phoneNumber, eMail, addr) -> None:
                self.__name__ = name
                self.__phoneNumber__ = phoneNumber
                self.__eMail__ = eMail
                self.__addr__ = addr

            def __str__(self) -> str: # 객체의 상태출력 사용자가 원하는 형태로 출력
                res = (f'이  름 : {self.__name__}\n'
                    f'핸드폰 : {self.__phoneNumber__}\n'
                    f'이메일 : {self.__eMail__}\n'
                    f'주  소 : {self.__addr__}')
                return res
                
            # 연락처 여부 확인
            def isNameExist(self, name):
                if self.__name__ == name: # 찾는 이름 존재
                    return True
                else:
                    return False
                
            def getInfo(self):
                return self.__name__, self.__phoneNumber__, self.__eMail__, self.__addr__
        ```

        ![주소록앱](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata01.gif)

        - Windows App 만들기(PyQt 5)

        ![QtApp](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata02.png)

##6일차('24. 02. 28)
- 파이썬 학습
- 파이썬 응용
    - PyQt5 학습
        - QWidget 자식 클래스 종류 학습

        ![QtApp](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata03.png)

        - Naver 뉴스 API 검색 앱

        ![QtApp](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata04.png)

##7일차
- 파이썬 응용
     - PyQt5 학습
        - Naver 뉴스 API 검색 앱 완성
        - 스레드 개념, 학습

        ![스레드](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata05.png)
            
        - TTS(Text To Speech)
        - QR코드 생성기

         ![QR](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata06.png)
            
         - 구글번역기

        ![QR](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata07.png)

    - json 학습

##8일차
- 파이썬 응용
    - PyautoGui 모듈(마우스, 키보드, 화면 캡쳐)
    - 슬랙 webhook로 모바일 메시지 전송

    <!-- ![slack](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata08.png) -->
    <!-- html 태그로 이미지를 삽입하면 문제 없음 -->
    <img src="https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata08.png" width=250>

    - Tesseract 프로그램을 이용한 이미지에서 글자 추출(인식율을 높이려면 트레이닝을 통한 트레이닝 데이터가 쌓여야 함)

    ![OCR](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata09.png)

##9일차
- 파이썬 응용
    - 이미지 처리 OpenCV

    ![안면인식](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata10.gif)

    - [Flask](https://flask-docs-kr.readthedocs.io/ko/latest/index.html), [Django](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django) 웹서버
    - 이미지 에디터 만들기(with PyQt)

    ![이미지 에디터](https://raw.githubusercontent.com/vinca0224/JavaBigData2024/main/images/bigdata11.gif)
##10일차
- 파이썬 응용
    - 메모장 만들기
    - Jupyter Notebook(빅데이터 분석, 코딩 테스트)