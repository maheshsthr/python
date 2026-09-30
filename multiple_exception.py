#multiple exception
try:
    list1= [1,2,3]
    print(list1[1])
    print(10/0)
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Zero division error")
except Exception as e:
    print(e)
    
