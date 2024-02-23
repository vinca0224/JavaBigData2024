# file : p08_review.py
# desc : 리뷰

# Q1. 홀수, 짝수 판별하기
a = 13
print('a는 ', end='')
result = a % 2
if result == 0:
    print('짝수')
else:
    print('홀수')

# Q2. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[0:5+1] #pin.split('-')[0]
num = pin[7:] #pin.split('-')[1]
print(yyyymmdd)
print(num)

# Q3. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

# Q4. 리스트 역순 정렬하기
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse() #a.sort(reverse = True)
print(a)

# Q5. 딕셔너리 값 추출하기
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)