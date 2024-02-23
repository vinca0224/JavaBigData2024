# file : p23_carSample.py
# desc : Car 클래스 사용해보기

from p22_carClass import Car

myCar = Car() # 클래스를 사용해서 객체를 하나 생성(instance)
yourCar = Car()

# print(myCar)
# print(yourCar)
myCar.carNum = '12삼4567'
myCar.company = 'jeep'
myCar.fuelType = 'gasoline'
myCar.carType = 'hybrid'
myCar.color = 'white'
myCar.realeaseYear = 2024
yourCar.carNum = '98칠6543'

myCar.getColor()
myCar.start()
myCar.accel()
myCar.brake()
myCar.turnLeft()
myCar.turnRight()

yourCar.start()
