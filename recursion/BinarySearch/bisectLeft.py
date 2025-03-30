from bisect import bisect_left

ints = [1, 3, 5, 7, 9, 11]

# Try different values of N
N = 6  # Number we are searching for

# Find the position where N would be inserted
pos = bisect_left(ints, N)

print(f"List: {ints}")
print(f"N = {N}")
print(f"bisect_left(ints, {N}) returns position: {pos}")

# Show where it would be inserted
ints_with_N = ints[:pos] + [N] + ints[pos:]
print(f"If we insert {N}, the list would look like: {ints_with_N}")