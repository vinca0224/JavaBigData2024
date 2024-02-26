# file : p26_exceptionHandle.py
# desc : 예외처리
# 오류(Error) : 코드상 빨간 밑줄이 그어지는 것
# 예외(Exception) : 프로그램 실행 중에 생기는 오류(비정상적 종료)

# 1. 파일 읽기
try:
    f = open('./sanple.txt', mode='r',encoding='utf-8')
    res = f.readline()
    print(res)
    #....
    f.close()
except:
    print('파일 오픈 예외발생')
else: # 오류가 없는 경우에만 수행
    f.close()
# finally:
#     try: # try~except는 다중으로 사용하면 성능에 별로 안 좋다
#         f.close # f에 파일 객체 자체가 없어서 close() 불가
#     except NameError as e:
#         print('파일 오픈실패')

# 2. 계산 결과
try:
    print(5 / 0)
except ZeroDivisionError as e:
    print('나누기 예외 발생', e.args)

a, b = 5, 3
if a == b:
    print(True)