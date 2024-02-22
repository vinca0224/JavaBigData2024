# file : p06_bool.py
# desc : 불타입 None 학습, 

# 참 / 거짓
a = True
b = False
print(a)
print(type(a)) # <class 'bool'>
print(type(1))# <class 'int'>
print(type(3.14))# <class 'float'>
print(type('hi'))# <class 'str'>
print(type([1,2,3]))# <class 'list'>
print(type((1,2,3)))# <class 'tuple'>

print(a == b)
print(a == (not b))

print(bool(''))# 참/거짓 구분 : 빈값, 0, none 외에는 True

# None 타입
None
a = 1
b = 0
c = None
print(None)
print(a + b)

c = 3
print(a + c)