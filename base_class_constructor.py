#Write a program to access the base class constructor
#and method in a sub class by using super().
class Person:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)

class Student(Person):
    def __init__(self,name,course):
        super().__init__(name)
        self.course = course
    def show(self):
        super().show()

s1 = Student("mahesh","bca")
s1.show()
