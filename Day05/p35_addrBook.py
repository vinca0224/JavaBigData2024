# file : p35_addrBook.py
# desc : 콘솔 주소록 프로그램
import os 

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
    
    # 연락처 여부 확인
    def isNameExist(self, name):
        if self.__name__ == name: # 찾는 이름 존재
            return True
        else:
            return False
    
    def getInfo(self):
        return self.__name__, self.__phoneNumber__, self.__eMail__, self.__addr__
        
    
def setContact(): # 사용자 입력으로 주소록 받기
    (name, phoneNumber, eMail, addr) = input('주소록 입력(이름,핸드폰,이메일,주소[/]) > ').split('/')
    name = name.strip() # 사용자 실수로 들어간 스페이스 제거
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    # print(f'"{name}","{phoneNumber}","{eMail}","{addr}"')
    contact = Contact(name, phoneNumber, eMail, addr) # 매개변수명과 동일하게 로컬변수 이름 지정
    return contact

def delContact(lst, name): # 연락처 삭제함수
    for i, item in enumerate(lst):
        if item.isNameExist(lst):
            del lst[i]

def saveContact(lst): # 연락처 저장 함수
    with open(file='./contacts.txt', mode='w', encoding='utf-8') as fp:
        for item in lst:
            name, phoneNumber, eMail, addr = item.getInfo()
            fp.write(f'{name}/{phoneNumber}/{eMail}/{addr}\n')

def displayMenu():
    menu =('주소록 프로그램\n'
           '1. 연락처 추가\n'
           '2. 연락처 출력\n'
           '3. 연락처 삭제\n'
           '4. 종료\n')
    print(menu)
    sel = int(input('메뉴입력 : '))
    return sel

def clearConsole(): 
    cmd = 'clear' # MacOS, Linux, Unix 명령어
    if os.name in ('nt', 'dos'): # Windows
        cmd = 'cls' # Windows 명령어
    os.system(cmd)

def getContacts(lst): # 리스트를 받아서 출력
    for i, item in enumerate(lst):
        print(f'{i+1}==========>')
        print(item)

def run():
    # 연락처를 담을 주소록 리스트
    lstContact =  []
    clearConsole() # 화면을 클리어
    while True:
        selMenu = displayMenu()
        if selMenu == 1: # 연락처 추가
            clearConsole()
            contact = setContact()
            lstContact.append(contact)
            input('입력 성공') # 엔터를 입력하도록 유도
            clearConsole()
        elif selMenu == 2: # 연락처 출력
            clearConsole()
            getContacts(lstContact)
            input('출력성공')
            clearConsole() 
        elif selMenu == 3: # 연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력 : ')
            delContact(lstContact, name)
            input('삭제성공')
            clearConsole()
        elif selMenu == 4: # 종료
            saveContact(lstContact)
            break
        else:
            clearConsole()

if __name__ == '__main__': # 메인 엔트리
    print('프로그램 시작')
    run() # 메인 함수 실행

print('프로그램 종료')