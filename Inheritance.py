class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def printName(self):
        print(self.getName())
    def __str__(self):
        return "I am a person. My name is " + self.getName() + ". And my age is " + str(self.age)

class Student(Person):
    def __init__(self, name, age, grade, gpa):
        Person.__init__(self, name, age)
        self.grade = grade
        self.gpa = gpa
        self.goldenGears = 0 
    def __str__(self):
        return "I am a student. My name is " + self.getName() + ". My age is " + str(self.age) + ". I am in " + self.grade + "!"

Pigeon = Person("Mr. Pigeon", 21)
Shane = Student("Shane He", 80, "2nd", 1.1)
Simon = Student("Simon Lu", 11, "6th", 0.0)

Pigeon.printName()
Shane.printName()

print(Shane)
print(Pigeon)

