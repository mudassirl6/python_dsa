list1 =  [0, 1, 0,  2, 1, 0, 1, 3, 2, 1, 2, 1]

lft_max = [0]*len(list1)
rgt_max = [0]*len(list1)

lft_max[0] = list1[0]
rgt_max[-1] = list1[-1]

for i in range(1,len(list1)):
    lft_max[i] = max(lft_max[i-1], list1[i])
    
for i in range(len(list1)-2,-1,-1):
    rgt_max[i] = max(rgt_max[i+1],list1[i])
    
    
total_trapped_water = 0
    
for i in range(len(list1)):
    total_trapped_water += min(lft_max[i],rgt_max[i]) - list1[i]
    
print(total_trapped_water)