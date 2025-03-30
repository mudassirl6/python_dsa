arr = [1,-2,3,4,-6,8]

curr_sum = arr[0]
max_sum = arr[0]

for i in range(1,len(arr)):
    curr_sum = max(curr_sum,curr_sum+arr[i])
    max_sum = max(max_sum,curr_sum)
    
    
print(max_sum)