def find_pairs_with_sum(numbers, target_sum):
    # Create a set to keep track of visited numbers
    seen = set()
    # Create a set to store unique pairs
    pairs = set()

    # Iterate through the list of numbers
    for num in numbers:
        # Calculate the complement that would add up to the target_sum with the current number
        complement = target_sum - num
        
        # Check if the complement is in the seen set
        if complement in seen:
            # Add the pair (min, max) to ensure uniqueness
            pairs.add((min(num, complement), max(num, complement)))
        
        # Add the current number to the seen set
        seen.add(num)

    # Convert the set of pairs to a list and return it
    return list(pairs)

# Example usage:
print(find_pairs_with_sum([2, 4, 3, 5, 7, 8, 9], 7))  
# Output: [(2, 5), (3, 4)]

print(find_pairs_with_sum([1, 2, 3, 4, 3, 6], 6))  
# Output: [(2, 4), (3, 3)]

def two_sum(nums, target):
    # Create a dictionary to store the indices of the elements
    num_to_index = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            # If it exists, return the indices
            return [num_to_index[complement], i]
        
        # Otherwise, store the index of the current element
        num_to_index[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
