# file : p22_carClass.py
# desc : 객체지행 클래스 학습

class Car:
    carNum = ''
    company = ''
    realeaseYear = 1960
    color = 'white'
    carType = ''
    fuelType = 'gasoline'

    def getColor(self):
        print(f'{self.carNum}은(는) {self.color}입니다')

    def start(self):
        print(f'{self.carNum}, 시동을 겁니다')
    
    def accel(self):
        print(f'{self.carNum}, 엑셀을 밟습니다')
    
    def brake(self):
        print(f'{self.carNum}, 브레이크를 밟습니다')
    
    def turnLeft(self):
        print(f'{self.carNum}, 좌회전합니다')
    
    def turnRight(self):
        print(f'{self.carNum}, 우회전합니다')