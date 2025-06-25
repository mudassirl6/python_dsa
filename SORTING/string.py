def sort_strings(strings):
    """
    Sorts a list of strings in lexicographical order.
    
    Args:
        strings (list): A list of strings to be sorted.
        
    Returns:
        list: A new list containing the sorted strings.
    """
    sorted_arr = sorted(strings,key = lambda x:(len(x),x))
    return sorted_arr


arr = ["banana", "apple", "fig", "kiwi", "apricot"]

# Custom sort logic
sorted_arr = sorted(arr, key=lambda x: (len(x), x))

# sort by len(x) then by x
print(sorted_arr)
