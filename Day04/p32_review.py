# file : p32_review.py
# desc : 되새김 문제

# Q1. 클래스 상속받고 메소드 추가하기 1
class Calculator:
    def __init__(self) -> None:
        self.value = 0
    def add(self, val):
        self.value += val
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# Q2. 클래스 상속받고 메소드 추가하기 2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        if val > 100:
            print('100 이상의 값을 넣을 수 없습니다.')
        else: super().add(val)

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# Q3. 리스트 항목마다 3 곱하여 리턴하기
def mul3(x):
    return x * 3
list1 = [1,2,3,4]
print(list(map(mul3, list1)))

# Q4. 최댓값과 최솟값의 합 구하기
list2 = [-8,2,7,5,-3,5,0,1]
maxNum = max(list2)
minNum = min(list2)
print(minNum + maxNum)

# Q5. 날짜 표시하기
import datetime
currTime = datetime.datetime.now()
print(f'{currTime.year}/{currTime.month}/{currTime.day} {currTime.hour}:{currTime.minute}:{currTime.second}')