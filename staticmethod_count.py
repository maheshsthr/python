class Student:
    count=0
    def __init__(self,name):
        Student.count+=1
        self.name = name
    @staticmethod
    def return_count():
        return Student.count

s1 = Student("Mahesh")
s2 = Student("Kailash")
s3 = Student("Ankit")
print(Student.return_count())
    
