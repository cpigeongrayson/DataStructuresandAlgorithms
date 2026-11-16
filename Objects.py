class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length *self.width
        print(self.area)
    def perimeter(self):
        print(2*self.length+2*self.width)
    def getLength(self):
        return self.length
    def getWidth(self):
        return self.width
    def setWidth(self, width):
        self.width = width
    def setLength(self, length):
        self.length = length
    def __str__(self):
        return "Length is " + str(self.length) + ". Width is " + str(self.width)

rect1 = Rectangle(5,10)
print("Length is " + str(rect1.length))
print(rect1.area)
rect1.area()
print(rect1.area)
rect1.perimeter()
print(rect1)

print("-------------------")
print(rect1.getWidth())
rect1.setWidth(13)
print(rect1.getWidth())
rect2 = Rectangle(2,9)
rect2.setLength(3.14159)
print(rect2.getLength())
rect2.length = 586527
print(rect2.getLength())
rect2.area()