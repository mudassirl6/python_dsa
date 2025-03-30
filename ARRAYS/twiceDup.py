nums = [1,3,4,2]
dict1 = {}

Flag = False
for num in nums:
    if num in dict1:
        if dict1[num] == 2:
            Flag = True
            break
        else:
            dict1[num] += 1
            
    else:
        dict1[num] = 1
        
print(Flag)