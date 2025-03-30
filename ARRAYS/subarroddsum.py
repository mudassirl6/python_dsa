arr = [1,2,3]

count = 0
for i in range(len(arr)):
    j = i
    sum1 = 0
    
    while j < len(arr):
        

        sum1 += arr[j]
        
        if sum1 % 2 != 0:
            print(arr[i:j+1])
            count += 1
            
        j += 1
            
            
print(count)