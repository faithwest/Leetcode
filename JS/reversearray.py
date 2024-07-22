def reverse_array_and_tuples(arr):
    # Reverse the numbers in each tuple
    reversed_tuples = [tuple(reversed(t)) for t in arr]
    # Reverse the order of the array
    reversed_array = reversed_tuples[::-1]
    return reversed_array

# Example usage
arr = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
reversed_result = reverse_array_and_tuples(arr)
print(reversed_result)

def reverse_array_and_strings(arr):
    # Reverse each string in the array
    reversed_strings = [s[::-1] for s in arr]
    # Reverse the order of the array
    reversed_array = reversed_strings[::-1]
    return reversed_array

# Example usage
arr = ["hello", "world", "python", "programming"]
reversed_result = reverse_array_and_strings(arr)
print(reversed_result)
