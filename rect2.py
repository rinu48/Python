class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
print("Rectngle 1")
a=int(input("enter the length:"))
b=int(input("enter the breadth:"))
obj=rectangle(a,b)

print("Area of Rectangle 1:",obj.area())

print("Rectngle 2")
a=int(input("enter the length:"))
b=int(input("enter the breadth:"))
ob=rectangle(a,b)


print("Area of Rectangle 2= ",ob.area())
rec1 = obj.area()
rec2 = ob.area()
if(rec1>rec2):
    print("Area of Rectangle 1 is greater than Rectangle 2")
elif(rec1==rec2):
    print("Area of Rectangle 1 is equal to Rectangle 2")
else:
    print("Area of Rectangle 2 is greater than Rectangle 1")

