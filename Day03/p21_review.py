# file : p21_review.py
# desc : 되새김 문제

# Q1. 파일의 문자열 바꾸기
f = open('./Day03/test.txt', 'r')
body = f.read()
f.close()
body = body.replace('java', 'python')
f = open('./Day03/test.txt', 'w')
f.write(body)
f.close()