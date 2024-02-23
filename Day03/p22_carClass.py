# file : p22_carClass.py
# desc : 객체지행 클래스 학습

class Car:
    __carNum = '' # __ 변수를 지정하면 private, 없으면 private
    company = ''
    realeaseYear = 1960
    color = 'white'
    carType = ''
    fuelType = 'gasoline'

    def __init__(self, carNum) -> None: # 생성자 -> None : 리턴할 게 없음
        print('Car 객체를 생성합니다.')
        self.__carNum = carNum
        print(f'{self.__carNum}객체를 생성합니다.')

    def __str__(self) -> str: # 객체변수를 print()할 때 출력 커스터마이징 함수
        return f'내 차는 {self.company}, {self.__carNum}입니다' 

    def setCarNum(self, carNum) -> None:
        self.__carNum = carNum

    def getCarNum(self) -> str:
        return self.__carNum

    def getColor(self):
        print(f'{self.__carNum}은(는) {self.color}입니다')

    def start(self):
        print(f'{self.__carNum}, 시동을 겁니다')
    
    def accel(self):
        print(f'{self.__carNum}, 엑셀을 밟습니다')
    
    def brake(self):
        print(f'{self.__carNum}, 브레이크를 밟습니다')
    
    def turnLeft(self):
        print(f'{self.__carNum}, 좌회전합니다')
    
    def turnRight(self):
        print(f'{self.__carNum}, 우회전합니다')