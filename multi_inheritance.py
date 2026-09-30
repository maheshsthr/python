class Father:
    def skill(self):
        print("Father : Business")

class Mother:
    def talent(self):
        print("Mother : Music")

class Child(Father,Mother):
    def own(self):
        print("Child : Coding")

c1= Child()

c1.skill()
c1.talent()
c1.own()
