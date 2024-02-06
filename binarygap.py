def solution(N):
    # Convert integer N to binary representation
    binary = bin(N)[2:]
    
    # Initialize variables to track the longest gap and current gap length
    max_gap = 0
    current_gap = 0
    
    # Iterate through the binary representation
    for digit in binary:
        if digit == '0':#inerates over each character in the array
            # Increment current gap length if digit is 0
            current_gap += 1
        else:
            # Update max_gap if current gap is longer
            max_gap = max(max_gap, current_gap)
            # Reset current gap length
            current_gap = 0
    
    print("Binary representation:", binary)
    print("Max gap:", max_gap)
    
    return binary,max_gap

# Test the function
print(solution(1041))  # Output should be 5
print(solution(32))    # Output should be 0
