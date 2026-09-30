#Write a program to show method overloading to find sum of
#two or three numbers
class Calculator:
    def sum(self, a,b,c=0):
        print(a+b+c)

c1= Calculator()
c1.sum(2,3)
c1.sum(2,3,4)
