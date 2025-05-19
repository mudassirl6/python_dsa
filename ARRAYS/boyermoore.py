# If we pair each occurrence of the majority element with a different element, the majority element will still remain because it appears more than half the time.

# ⸻

# 🧠 How the Algorithm Works:
# 	1.	Initialize two variables:
# 	•	candidate = None
# 	•	count = 0
# 	2.	Iterate through the array:
# 	•	If count == 0: set candidate = current number
# 	•	If current number == candidate: increment count
# 	•	Else: decrement count
# 	3.	After the loop, candidate will hold the majority element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        times = len(nums) // 2
        # 🧠 Approach (Boyer-Moore Voting Algorithm)
            
        count = 0
        candidate = float('inf')

        for element in nums:

            if count == 0:
                candidate = element
                count += 1

            elif candidate == element:
                count += 1

            else:
                count -= 1


        return candidate



        



# Time Complexity: O(n)
# Space Complexity: O(1)
# The Boyer-Moore Voting Algorithm is a linear time algorithm that finds the majority element in an array. It works by maintaining a count of the current candidate for the majority element and adjusting it based on the elements encountered in the array.
# The algorithm is efficient and has a space complexity of O(1) since it only uses a few variables to keep track of the candidate and its count.