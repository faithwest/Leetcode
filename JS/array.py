def sum_of_evens(numbers):
    # Initialize a variable to store the sum of even numbers
    total = 0
    
    # Iterate through the list of numbers
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            # Add the even number to the total sum
            total += num
    
    # Return the total sum of even numbers
    return total

# Example usage:
print(sum_of_evens([1, 2, 3, 4, 5]))  # Output should be 6 (2 + 4)
print(sum_of_evens([10, 15, 20, 25])) # Output should be 30 (10 + 20)
