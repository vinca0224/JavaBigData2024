# file : p02_number.py
# desc : 숫자형 자료타입

#일반 숫자형
age = 40 #int형 담는 변수
taxRate = 8.8 #float형을 담는 변수
highValue = 4.24E10 #지수승(float)

print('나이는', age) #문자열이 '',"" 둘다 사용가능
print('세율은', taxRate,'입니다.')
print('지수값은', highValue, '입니다.')

#특수 숫자형
binVal = 0b11111111 #255 0~1
octVal = 0o11 #9  0~7
hexVal = 0xFF #255 0~9ABCDEF

print('2진수', binVal, '8진수', octVal, '16진수',hexVal)

# 파이썬은 타입을 적을 필요가 없다!

# 사칙연산
a, b, c = 3, 4, 9
print(a + b)
print(a - c)
print(a * c)
print(b / c)
# 단, 나누기는 3가지로 분류
print(c / b) # 정확하게 실수로 나누기
print(c // b) # 정수로만 나눈 몫
print(c % b) # 정수로 나눈 나머지

print(2 ** 10) #1024 *(아스트릭) 두번 쓰면 제곱승 import math; math.pow()

print((a + b) * c) # 연산자 우선순위는 ()만 잘 쓰면 된다.