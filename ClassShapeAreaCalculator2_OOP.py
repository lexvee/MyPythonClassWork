class ShapeArea():

    pi=3.142

    def __init__(self):
        pass
    
    def circle(self):
        radius=input("radius=")
        return int(radius)**2*self.pi

    def triangle(self):
        length=input("length=")
        width=input("width=")
        return int(length)*int(width)/2    

    def rectangle(self):
        length=input("length=")
        width=input("width=")
        return int(length)*int(width)

class Circle(ShapeArea): #we can inherit multiple class like class Car(Vehicle,Xxxx,Yyyy)
    pass

my_circle=Circle()
print("what is the area of circle?: ",my_circle.circle())


class Triangle(ShapeArea): #we can inherit multiple class like class Car(Vehicle,Xxxx,Yyyy)
    pass

my_triangle=Triangle()
print("what is the area of triangle?: ",my_triangle.triangle())

class Rectangle(ShapeArea): #we can inherit multiple class like class Car(Vehicle,Xxxx,Yyyy)
    pass

my_rectangle=Rectangle()
print("what is the area of rectangle?: ",my_rectangle.rectangle())
