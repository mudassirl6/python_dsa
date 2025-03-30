arr = [1, 1, 0, 0, 1, 1, 1, 0]
k = 2

hm = {}

i,j = 0,0
max_len = float('-inf')
# brute force approach

# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         sub_arr = arr[i:j+1]
#         most_freq_char_count = arr.count(1)
#         replacement = len(sub_arr)-most_freq_char_count
#         if replacement <= k:
#             max_len  =  max(max_len,len(sub_arr))
            
# print(max_len)

replacements = 0

while j < len(arr):
    
    if arr[j] == 0:
        replacements += 1
        
    
    while replacements > k:
        if arr[i] == 0:
            replacements -= 1
        i += 1

    max_len = max(max_len,j-i+1)
        
    j += 1
    
print(max_len)

# orr

# i = 0
# zero_count = 0

# max_len = 0

# for j in range(len(arr)):
#     if arr[j] == 0:
#         zero_count += 1
        
#     while zero_count > k:
#         if arr[i] == 0:
#             zero_count -= 1
            
            
#         i += 1
        
#     max_len = max(max_len,j-i+1)
    
# print(max_len)