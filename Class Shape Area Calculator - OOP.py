class ShapeArea():

    def __init__(self,length,width,radius):
        self.length=length
        self.width=width
        self.radius=radius

    def circle(self,valueR):
        self.radius=valueR
        area_of_circle=valueR**2*3.142
        return area_of_circle

    def triangle(self,valueL,valueW):
        self.length=valueL
        self.width=valueW
        area_of_triangle=valueL*valueW/2
        return area_of_triangle

    def rectangle(self,valueL,valueW):
        self.length=valueL
        self.width=valueW
        area_of_rectangle=valueL*valueW
        return area_of_rectangle

class Circle(ShapeArea): #we can inherit multiple class like class Car(Vehicle,Xxxx,Yyyy)
    pass

my_circle=Circle(0,0,0)
print("what is the area of circle?: ",my_circle.circle(4))


class Triangle(ShapeArea): #we can inherit multiple class like class Car(Vehicle,Xxxx,Yyyy)
    pass

my_triangle=Triangle(0,0,0)
print("what is the area of triangle?: ",my_triangle.triangle(4,5))

class Rectangle(ShapeArea): #we can inherit multiple class like class Car(Vehicle,Xxxx,Yyyy)
    pass

my_rectangle=Rectangle(0,0,0)
print("what is the area of rectangle?: ",my_rectangle.rectangle(4,5))
