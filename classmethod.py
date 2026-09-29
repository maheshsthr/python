#Write a program to use class method to handle the
#Common features of all the instance of Student class.

class Student:
    college = "LJ"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_college(cls, newname):
        cls.college=newname

s1 = Student("Mahesh")
print(Student.college)
Student.change_college("LJ UNIVERSITY")
print(Student.college)

