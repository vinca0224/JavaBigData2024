# file : p35_addrBook.py
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
def setContact(): # 사용자 입력으로 주소록 받기
    (name, phoneNumber, eMail, addr) = input('주소록 입력(이름, 핸드폰, 이메일, 주소[구분자 /]) > ').split('/')
    name = name.strip() # 사용자 실수로 들어간 스페이스 제거
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    print(f'"{name}","{phoneNumber}","{eMail}","{addr}"')

def displayMenu():
    menu =('주소록 프로그램\n'
           '1. 연락처 추가\n'
           '2. 연락처 출력\n'
           '3. 연락처 삭제\n'
           '4. 종료\n')
    print(menu)
    sel = int(input('메뉴입력 : '))
    return sel

def run():
    while True:
        selMenu = displayMenu()
        if selMenu == 4:
            break

if __name__ == '__main__': # 메인 엔트리
    print('프로그램 시작')
    displayMenu()
    run()

print('프로그램 종료')