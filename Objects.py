class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length *self.width
        print(self.area)
    def perimeter(self):
        print(2*self.length+2*self.width)
    def __str__(self):
        return "Length is " + str(self.length) + ". Width is " + str(self.width)

rect1 = Rectangle(5,10)
print("Length is " + str(rect1.length))
print(rect1.area)
rect1.area()
print(rect1.area)
rect1.perimeter()
print(rect1)