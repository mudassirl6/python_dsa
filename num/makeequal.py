def min_operations_to_equal(p, q, r):
    total = p + q + r
    if total % 3 != 0:
        return -1  # Not possible

    max_val = max(p, q, r)
    sum_diff = (3 * max_val - total) // 2

    return sum_diff

# Test case
p, q, r = 1, 1, 7
print(min_operations_to_equal(p, q, r))  # Output: 3