# file : p05_dict.py
# desc : 딕셔너리 자료형 학습, 집합 학습

## 딕셔더리 구성
spiderMan = {'name':'Peter Parker', 'age':18, 'weapon':'Web shooter', 'friends':['Iron man', 'Thor', 'Captain America']}
print(spiderMan)

## 출력
print(spiderMan['name'])

## 값 추가
spiderMan['job'] = 'Camera man'

print(spiderMan)

## 값 삭제
del spiderMan['friends']
print(spiderMan)

## 딕셔너리 함수
print(spiderMan.keys()) # 딕셔너리에 현재 존재하는 키 목록
print(list(spiderMan.keys())) # 키 목록을 리스트 형태로 형변환
print(spiderMan.items()) # 딕셔너리 내 모든 아이템 출력
print(spiderMan.get('job')) # 딕셔너리의 값을 가져오기
print('friedns' in spiderMan) # 딕셔너리 안에 키가 있는지 확인

print(spiderMan.values())
res = spiderMan.pop('job') #값을 꺼냄
print(res)
print(spiderMan.pop('age'))
print(spiderMan)

## 데이터 삭제
spiderMan.clear()
print(spiderMan)

del spiderMan # 완전 삭제
print(spiderMan)

## 집합은 중복을 허용하지않고, 순서도 없다.
#s = set([1,2,3,4,2,1]) #= {1,2,3,4}
#print(s)