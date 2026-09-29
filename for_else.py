#for else
list1 = [10,20,30,40,50]
target = int(input("Enter target "))
for i in list1:
    if target == i:
        print("Found")
        break
else:
    print("not found")