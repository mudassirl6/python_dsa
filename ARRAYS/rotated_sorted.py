target = 5

nums = [4,5,6,7,0,1,2]

lft = 0
right = len(nums) - 1

while lft <= right:
    mid = (lft+right)//2

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] <= nums[right]:
        if target > nums[mid] and target <= nums[right]:
            low = mid+1
        else:
            right = mid-1
            
    else:
        if target >= nums[lft] and target < nums[mid]:
            right = mid-1
            
        else:
            lft = mid+1
            

            