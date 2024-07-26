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
