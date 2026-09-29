#byte array read modify display
import array 
arr = array.array('b',[10,20,30,40])

print(arr[2]) #read
print(arr.tolist()) #display
arr[2] = 31 #modify
for i in arr: #display
    print(i)
