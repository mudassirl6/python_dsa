arr  = [-2, -3, -1, -5]
maxSum = float('-inf')

s = temp = e = 0

currSum = 0

for i in range(len(arr)):
    
    currSum += arr[i]
    
    if currSum > maxSum:
        maxSum = currSum
        s = temp
        e = i
        
    if currSum < 0:
        currSum = 0
        temp = i + 1
        
if maxSum < 0:
    print(max(arr),[max(arr)])   
        
else:
    print(maxSum,arr[s:e+1])
        