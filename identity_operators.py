#identity operators
a = [1,2,3]
b = [1,2,3]
c = a

print(f" A {id(a)}\n B {id(b)}\n C {id(c)}")
print("A is B",a is b) #false because same value not same identiy object
print("A is C", a is c) # true because c have same identity object of a