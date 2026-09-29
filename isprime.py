limit = 50
count=0
def isprime(n):
    if n<2:
        return False
    for i in range(2,n):        
        if n%i==0:
            return False
    else : 
        return True

for n in range(2,limit+1):
    if isprime(n):
        print(n)
