# file : p17_fileIo.py
# desc : 파일 입/출력 학습

# 컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open(), close() / 파이썬에서는 안 닫아도 크게 지장은 없지만 닫아라
# 2. 네트워크 open(), close()
# 3. DB open(), close()

# 언어체계 추가 ASCII(한글:cp949), 유니코드(utf-8)
# 상대경로, 절대경로
# w는 매번 파일 새로 생성, a는 기존 파일에 내용 추가
# 로드 등을 남길 때에는 a로 작업해야 함
f = open('./Day 03/sample.txt', mode='a',encoding='utf-8')
# 파일 쓰기 진행
f.write('안녕하세요. 파이썬.\n') # 한 줄 내리기 시 \n 붙여야함
f.write('모두 화이팅!\n')
f.close() # 다른 언어에서는 무조건 close()해야 함
