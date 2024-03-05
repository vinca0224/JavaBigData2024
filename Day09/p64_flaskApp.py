# file : p64_flaskApp.py
# desc : 플라스크 웹서버

'''
> pip install Flask
'''

from flask import Flask

app = Flask(__name__) # 현재의 모듈로 flask 앱 만듬

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/1')
def testPage1():
    return 'Page1'

@app.route('/2')
def testPage2():
    return 'Page2'

def main():
    app.run(debug=True, port=80)

if __name__ == '__main__':
    main()