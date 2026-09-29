#range of array updae 
import array
arr = array.array('i',[10,20,30,40,50])

print(arr.tolist())
print(arr[1:3].tolist())
arr[1:3]=array.array('i',[15,25])
print(arr.tolist())
