class Vehicle:
    def info(self):
        print("Vehicle")
class Car(Vehicle):
    def info(self):
        print("car")

v1 = Vehicle()
c1 = Car()

v1.info()
c1.info()
        
