class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name , age, school):
        Person.__init__(self, name, age)
        self.school = school
        if(age >= 5 and age <= 11):
            self.division = "Elementary"
        else:
            self.division = "Undefined"
class Worker(Person):
    def __init__(self, name, age, dollarsPerHour):
        Person.__init__(self, name, age)
        self.dollarsPerHour = dollarsPerHour
    def cost(self, hours):
        return self.dollarsPerHour * hours

Paul = Person("Paul", 36)
Morty = Student("Morty", 9, "The Grayson School")
Samantha = Worker("Samantha", 29, 20)

print(Morty.division)
print(Samantha.cost(10))