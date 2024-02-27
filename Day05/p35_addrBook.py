# file : p34_unicode.py
# desc : 콘솔 주소록 프로그램

class Contact: # 주소록 클래스
    # 생성자
    def __init__(self, name, phoneNumber, eMail, addr) -> None:
        self.__name__ = name
        self.__phoneNumber__ = phoneNumber
        self.__eMail__ = eMail
        self.__addr__ = addr

    def __str__(self) -> str: # 객체의 상태출력 사용자가 원하는 형태로 출력
        res = (f'이  름 : {self.__name__}\n'
               f'핸드폰 : {self.__phoneNumber__}\n'
               f'이메일 : {self.__eMail__}\n'
               f'주  소 : {self.__addr__}')
        return res

def run():
    # first = Contact(addr='경성', phoneNumber='010-1234-5678', name='홍길동', eMail='sdf@naver.com')
    first = Contact('홍길동', '010-1234-5678', 'seee@naver.com', '경성')
    print(first)

if __name__ == '__main__': # 메인 엔트리
    print('프로그램 시작')
    run()

print('프로그램 종료')