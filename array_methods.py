#various methods of array class mentioned: append, insert, remove, pop, index, tolist and count.
import array
arr = array.array('i',[10,20,30,40,50])

arr.append(60) #10 20 30 40 50 60
arr.insert(1,15) # 10 15 20 30 40 50 60
arr.remove(15) # 10 20 30 40 50 60
arr.pop() # 10 20 30 40 50 
print(arr.index(20)) #1
print(arr.tolist())
print(arr.count(20)) #1