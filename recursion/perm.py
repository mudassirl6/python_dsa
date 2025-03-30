def perm(idx,arr):
    
    if idx == len(arr):
        ans.append(arr[:])
        
        
    for i in range(idx,len(arr)):
        
        arr[i],arr[idx] = arr[idx],arr[i]
        
        perm(idx+1,arr)
        
        arr[i],arr[idx] = arr[idx],arr[i]
        
    
ans = []
perm(0,[1,2,3])

ans.sort()

print(ans)
        