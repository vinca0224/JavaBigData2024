# file : p64_flaskApp.py
# desc : 플라스크 웹서버

'''
> pip install Flask
'''

from flask import Flask, render_template

app = Flask(__name__) # 현재의 모듈로 flask 앱 만듬

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/unit')
def testPage1():
    return render_template('unit.html')

@app.route('/naver')
def testPage2():
    return render_template('register.html')

def main():
    app.run(debug=True, port=80)

if __name__ == '__main__':
    main()