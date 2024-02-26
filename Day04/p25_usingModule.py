# file : p25_usingModule.py
# desc : 모듈 사용

# import calc as c # calc.py라는 모듈을 사용하겠다
from calc import mul # mul() 함수명만 쓰면 됨

from Math import Math  # from의 Math는 모듈(파일) 이름, import의 Math느 클래스명

from Day03.p22_carClass import Car # 디렉토리(모듈을 모아놓은 것은 패키리라 한다).모듈명

if __name__ == '__main__': ## 자바의 void main()과 동일
    result = mul(10,7)
    print(result)

    print(__name__) #__main__ = 나는 메인 엔트리입니다.

    myMath = Math()
    myMath.solv(10)
    print(myMath.solv(10))

