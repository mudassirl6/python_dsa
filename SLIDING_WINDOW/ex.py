arr = [1,2,-3,4,5,-6,-7,9,-8]

size = 4
max_val = 0
curr_val = 0

j = 0
i = 0

while i < len(arr):
    curr_val += arr[i]
    
    if i-j+1 == size:
        max_val = max(max_val,curr_val)
        curr_val -= arr[j]
        j += 1
    
    i += 1
    
print(max_val)
        
    