#Write a program to understand the order of execution of
#methods in several base classes according to method
#resolution order (MRO)

class Father:
    def show(self):
        print("Father")
class Mother:
    def show(self):
        print("Mother")

class Child(Father,Mother):
    pass

c1= Child()
c1.show()

print(Child.mro())
print(Child.__mro__)
