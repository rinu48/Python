class Rectangle:
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return 2*(self.length + self.breadth)
print("Rectangle 1")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
obj=Rectangle(a,b)

print("Area of Rect 1 = ",obj.area())
print("Perimeter = ",obj.perimeter())

print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
ob=Rectangle(a,b)

print("Area of Rect 2= ",ob.area())
print("Perimeter=",ob.perimeter())
if obj.area() == ob.area():
    print("The area's are equal")
else:
    print("area's are not equal")