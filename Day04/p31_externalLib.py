# file : p31_externalLib.py
# desc : 외부라이브러리 사용법

# >pip install LibName
# Successfully installed / Requirement already satisfied 가 나와야 함
# >pip uninstall LibName
# Successfully uninstalled 나와야 함

from faker import Faker

dummy = Faker('ko-KR') # 한국어 설정
print(dummy.name())
print(dummy.address())
# print(dummy.profile())

dummyData = [dummy.profile() for _ in range(10)]
print(dummyData)

## urlLib3 외부 웹페이지 분석모듈
import requests
from bs4 import BeautifulSoup

# res = requests.get('http://www.naver.com')
# print(res.status_code)
# print(res.content) # 내용 가져오기

res = requests.get('http://www.google.com')
if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)