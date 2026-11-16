class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length
    def getHeight(self):
        return self.height
    def setHeight(self, height):
        self.height = height
    def getLength(self):
        return self.length
    def setLength(self, length):
        self.length = length
    def area(self):
        self.area = self.length * self.height
        return self.area
    def addRectangle(self, rect):
        self.height = self.height + rect.height
        self.setLength(self.length + rect.length)
    def __str__(self):
        return "Height is: " + str(self.height) + ". Length is: " + str(self.length)


rect1 = Rectangle(5,10)
print(rect1.getHeight())
print(rect1.getLength())
rect1.setHeight(7)
print("The new height is:  " + str(rect1.getHeight()))
rect2 = Rectangle(3,6)
print(rect2.getHeight())
print(rect2.getLength())
print(rect1.area())
print(rect1.area)
print(rect1)

rect1.addRectangle(rect2)
print(rect1)


class Human:
    def __init__(self, health = 100):
        self.health = health
    def takeDamage(self, damager):
        self.health -= damager.damage

class Monster:
    def __init__(self, damage, health = 50):
        self.health = health
        self.damage = damage

Paul = Human()
mon = Monster(10, 25)

print(Paul.health)
Paul.takeDamage(mon)
print(Paul.health)
