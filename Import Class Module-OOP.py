from Module_dir.ClassShapeAreaCalculator2_OOP import ShapeArea as SA

class Circle(SA): #we can inherit multiple class like class Car(Vehicle,Xxxx,Yyyy)
    pass

class MathCalc(SA):

    def circle_perimeter(self):
        radius=input("radius=")
        return float(radius)*self.pi*2
        return self.circle(int(radius))


my_perimeter=MathCalc()   
print("my perimeter=",my_perimeter.circle_perimeter())
