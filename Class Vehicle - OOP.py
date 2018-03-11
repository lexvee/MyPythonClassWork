class Vehicle():

    def __init__(self,body_type,no_of_wheels,year_manufactured,cost,speed):
        self.speed=speed
        self.body_type=body_type
        self.year_manufactured=year_manufactured
        self.cost=cost
        self.no_of_wheels=no_of_wheels

    def can_fly(self):
        return self.body_type=="Aeroplane"


    def sound_horn(self):
        return "Pipiiii"

    def can_sail(self):
        return self.body_type=="ship"

    def accelerate(self,value):
        self.speed+=value
        return self.speed

class Car(Vehicle): #we can inherit multiple class like class Car(Vehicle,Xxxx,Yyyy)
    pass

my_car=Car("Car",4,2018,10000,100)
print("is it an airplane?: ",my_car.can_fly())
print("what is the acceleration?: ",my_car.accelerate(200))
print("is it a ship?: ",my_car.can_sail())
print("what is the current acceleration?: ", my_car.speed)
print("what is the new acceleration?: ",my_car.accelerate(10))


