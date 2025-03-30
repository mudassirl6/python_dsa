s = "Mudassir"

i,j = 0,0
size = 0
set1 = set()

while j < len(s):
    
    if s[j] not in set1:
        set1.add(s[j])
        size = max(size,j-i+1)
        j += 1
        
    else:
        set1.remove(s[i])
        i += 1
        
        
# brute force approach
        
# for i in range(len(s)):
#     substr = ""
#     for j in range(i,len(s)):
#         if s[j] not in substr:
#             substr += s[j]
#             size = max(size,len(substr))
#         else:
#             break
            
        
        
print(size)
    
    

    
    
    
    