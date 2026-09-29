#Positional Argument, keyword argument, default arguments, variable length
def positional(a,b):
    print(a+b)

def keyword(name,age):
    print(f"name : {name} age : {age}")

def default(name,greet="Hello "):
    print(f"{greet} {name}")

def keywords(*args,**kwargs):
    print(args)
    print(kwargs)

positional(1,2)
keyword(age=19,name="mahesh")
default("Mahesh")
keywords(1,2,3,city = "Ahm")
