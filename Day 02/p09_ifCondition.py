# file : p09_ifCondition
# desc : if 제어문

money = 1000

if money >= 5000:
    # indentation(들여쓰기) tab == space 4
    # 파이썬은 중괄호로 블록실행을 구분하지 않는 대신 들여쓰기로 구분하기때문에 들여쓰기를 맞추어주어야한다 
    print('택시를 타고 가자')
    print('ok')
elif money < 5000 and money >=2500:
    print('홈플까지')
    print('나머지 걸어가')
else:
    print('걸어가자')
    print('no')