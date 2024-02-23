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

a, b, c, d  = 10, 5, 7, 9
print(a >= b) # True
print(c > d) # False

print(a >= b and c > d) # False / 1 and 1 = 1 / 1 and 0 == 0 / 0 and 1 == 0 / 0 and 0 == 0
print(a >=b or c > d) # True / 1 or 1 == 1 / 0 or 1 == 1 / 1 or 0 == 1 / 0 or 0 == 0
## and 80% / or 20%

print(not(a >= b)) # False


## print() end 옵션(많이 씀), sep옵션
print(1 in [1,3,5,7,9], end=',')
print(6 in [1,3,5,7,9])

print('13579', '24680', sep=' | ')

# 파이썬에서는 조건연산자를 잘 안쓴다
score = 60
print('success' if score >= 60 else 'failure') # (score >= 60 ? "success" : "failure")