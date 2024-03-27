def reverse_array_inplace(arr):
    """
    Reverse the elements of the given array in-place.
    
    Args:
        arr (list): The array to be reversed in-place.
    """
    arr.reverse()

# Example usage
my_array = [1, 2, 3, 4, 5]
reverse_array_inplace(my_array)
print(my_array)  # Output: [5, 4, 3, 2, 1]
