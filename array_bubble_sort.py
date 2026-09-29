import array 
arr = array.array('i',[10,40,20,31,90])

#bubble sort
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr.tolist())