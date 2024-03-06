def remove_duplicates(input_list):
    """
    Removes duplicates from a list while preserving the order of elements.
    
    Args:
    input_list (list): The list from which duplicates are to be removed.
    
    Returns:
    list: A new list with duplicates removed.
    """
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage:
my_list = [1, 2, 3, 3, 4, 5, 5, 6]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5, 6]
