#Write a program to store data into instances using
#mutator methods and to retrieve data from the instances using
#accessor methods.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def set_course(self,course):
        self.course=course
    def get_course(self):
        print(self.course)

s1= Student("Mahesh",19)
s1.set_course("BCA")
s1.get_course()
