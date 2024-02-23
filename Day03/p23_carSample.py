# file : p23_carSample.py
# desc : Car 클래스 사용해보기

from p22_carClass import Car

myCar = Car('12삼4567') # 클래스를 사용해서 객체를 하나 생성(instance)
yourCar = Car('98칠6543')

# print(myCar)
# print(yourCar)
# myCar.__carNum = '12삼4567'#불가
myCar.company = 'jeep'
myCar.fuelType = 'gasoline'
myCar.carType = 'hybrid'
myCar.color = 'white'
myCar.realeaseYear = 2024
# yourCar.__carNum = '98칠6543' #불가

myCar.getColor()
myCar.start()
myCar.accel()
myCar.brake()
myCar.turnLeft()
myCar.turnRight()

yourCar.start()
print(myCar)