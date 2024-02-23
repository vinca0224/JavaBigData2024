# file : p21_review.py
# desc : 되새김 문제

# Q1. 파일의 문자열 바꾸기
## read() 사용
# f = open('./Day03/test.txt', 'r', encoding='utf-8')
# body = f.read() # 문자열로 리턴, 그러나 read()는 텍스트가 길면 문장이 잘려서 나온다.(전부 출력할수없다) 
# f.close()
# body = body.replace('java', 'python')
# f = open('./Day03/test.txt', 'w', encoding='utf-8')
# f.write(body)
# f.close()

## readlines() 사용
f = open('./Day03/test.txt', 'r', encoding='utf-8')
body = f.readlines() # 리스트로 리턴
f.close()
body = [body[0],body[1].replace('java', 'python')]
f = open('./Day03/test.txt', 'w', encoding='utf-8')
f.write(body[0] + body[1])
f.close()