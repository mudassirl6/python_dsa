arr = [0,0,1,0,1,0,1,1,0,0,1,1,1]

ans = 0
dict1 = {0:-1}
sum1 = 0
for i in range(len(arr)):
    
    if arr[i] == 0:
        sum1 += -1
        
    else:
        sum1 += 1
        
    if sum1 in dict1:
        idx = i - dict1[sum1]
        if idx > sum1:
            ans = idx
            
    else:
        dict1[sum1] = i
        
        
print(ans)