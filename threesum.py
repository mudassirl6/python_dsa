# class Solution:
#     def threeSum(self, nums):
#         result = []
#         sorted(nums)

#         i = 0
#         while i<len(nums)-2:
#             j = i+1
#             k = len(nums)-1
#             while j != k:
#                 currSum = nums[i]+nums[j]+nums[k]
#                 if currSum == 0:
#                     result.append([nums[i],nums[j],nums[k]])
#                     j += 1
#                     k -= 1

#                 elif currSum > 0:
#                     k -= 1

#                 else:
#                     j += 1
#             i += 1

#         return result
    
# sol = Solution()
# print(sol.threeSum([-1,0,1]))
        
        
arr = [1,23,4,5,6,7,8,9,10,10,11]
arr2 = [1,2,3,4,5,6,7,8,9,10,11]

for i,j in zip(arr,arr2):
    print(i,j)