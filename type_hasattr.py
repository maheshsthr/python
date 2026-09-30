#Write a program to check the object type to know
#whether the method exists in the object or not.

class Vehicle:
    def show(self):
        print("Vehicle is way of travel from point a to point b")

v1= Vehicle()
print(type(v1))

print(hasattr(v1,"show"))
