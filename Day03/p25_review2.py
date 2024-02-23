# file : p25_review2.py
# desc : 되새김 문제 2

# Q1. 홀수, 짝수 판별하기
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
    
# Q2. 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)

# Q3. 프로그램의 오류 수정하기 1
input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")

total = int(input1)+ int(input2)
print("두 수의 합은 %s입니다" % total)

# Q4. 출력결과가 다른 것은?
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

# Q5. 프로그램 오류 수정하기 2
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

# Q6. 사용자 입력 저장하기
user_input = input("저장할 내용을 입력하세요:")
f = open('test1.txt', mode= 'a', encoding='utf-8')
f.write(user_input)
f.write('\n')
f.close()