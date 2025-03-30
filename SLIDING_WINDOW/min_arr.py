arr = [2, 3, 1, 2, 4, 3]
s = 7

i, j = 0, 0
n = len(arr)

curr_sum = 0
min_len = float('inf')  # Initialize to a very large value

while j < n:
    # Expand the window by including arr[j]
    curr_sum += arr[j]
    
    # Shrink the window while the sum is >= s
    while curr_sum >= s:
        min_len = min(min_len, j - i + 1)  # Update the minimum length
        curr_sum -= arr[i]  # Remove arr[i] from the current sum
        i += 1  # Shrink the window from the left
    
    j += 1  # Expand the window from the right

# If no valid subarray is found, return 0
print(min_len if min_len != float('inf') else 0)