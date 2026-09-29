#menu driven program for area circle , area triangle , area sqr , simple interest

while True:
    print("1. Area of Circle\n2. Area of triangle\n3. Area of Square\n4. Simple Interest\n5. Exit")
    choice = int(input("Enter Choice"))
    match(choice):
        case 1:
            r = float(input("enter radius")); print(3.14 * r **2)
        case 2:
            b,h = float(input("enter base ")), float(input("enter height"));print(0.5*b*h) 
        case 3: 
            s = float(input("enter sides ")); print(s*s)
        case 4:
            p,r,t = (float(input(x)) for x in ("principal","rate","time"))
            print((p*r*t)/100)
        case 5:
            print("Exiting... ")
            break
        case _: print("invalid")


