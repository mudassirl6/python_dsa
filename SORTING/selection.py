
arr = [2,4,5,6,1,88]

n = len(arr)
for i in range(n-2):
    minval = float("inf")
    for j in range(i+1,n):
        minval = min(minval,arr[j])
        
    if arr[i] > minval:
        temp = minval
        minval = arr[i]
        arr[i] = temp
        
        
a = 2
b = 3
c = 4
a += b

        
        
        