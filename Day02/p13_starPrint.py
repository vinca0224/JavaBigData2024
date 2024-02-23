# file : p13_starPrint.py
# desc : 별 찍기

print('예제 그림')
for i in range(1 , 5+1):
    print('*' * i)

# 2중 for문으로 결과를 똑같이 만드시오
print('\n')

print('별찍기 ----------->> ')

for i in range(1,6): # 손 댈 필요 없음
    for j in range(i, 6):
        print(' ', end='')

    for j in range(6-i, 6):
        print('*', end='')
    print()

print('별찍기 ----------->> ')

for i in range(1,6): # 손 댈 필요 없음
    for j in range(i):
        print('*',end='')
    print()