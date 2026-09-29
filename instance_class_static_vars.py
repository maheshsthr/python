class Student:
    college = "LJ"
    def __init__(self,name):
        self.name= name

    @classmethod
    def displaycollege(cls):
        print(cls.college)
    @staticmethod
    def welcome():
        print("Welcome")

s1 = Student("Mahesh")
Student.displaycollege()
Student.welcome()

    
