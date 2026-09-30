#Write a program to implement single inheritance in
#hich two sub classes are derived from a single base class

class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def info(self):
        print(self.brand)

class Bike(Vehicle):
    def wheels(self):
        print("wheels : 2")

class Car(Vehicle):
    def wheels(self):
        print("Wheels : 4")

b1= Bike("yahma")
c1= Car("BMW")

b1.info()
c1.info()
b1.wheels()
c1.wheels()
