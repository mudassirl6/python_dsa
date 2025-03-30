# def recur(sum1,n):
#     if n < 1:
#         return sum1
    
#     return recur(sum1+n,n-1)
    
    
    
# print(recur(0,5))


# def mergeSort(arr,l,r):
    
#     mid = (l+r)//2
    
    
    
class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        

        i = 0
        n = len(blocks)
        j = 0




        minCon = 999999

        w_count = 0

        while i < n:

            if blocks[i] == 'W':
                w_count += 1

            
            while i - j + 1 == k:

                minCon = min(minCon,w_count)
                
                if blocks[j] == 'W':
                    w_count -= 1


                j += 1

            i += 1
            


        return minCon
    
    
# Feature
# Subsequence
# Subarray
# Definition
# A sequence derived by deleting some or no elements without changing the relative order.
# A contiguous part (continuous elements) of an array or string.
# Elements Order
# Must remain in the same order as the original array.
# Must also follow the original order.
# Contiguous?
# No (can skip elements).
# Yes (must be consecutive).
# Example (for [1, 2, 3])
# Possible subsequences: [1, 2], [1, 3], [2, 3], [1, 2, 3], [ ] (empty).
# Possible subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3].
# Total Count (for N elements)
# 2^N (including the empty subsequence).
# N(N+1)/2.
# Example Use Cases
# Longest Increasing Subsequence (LIS), Subsequence Matching.
# Maximum Subarray Sum (Kadaneâ€™s Algorithm), Sliding Window Problems.

    
    
s = Solution()

print(s.minimumRecolors("WBBWWBBWBW",7))