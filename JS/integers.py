# # # Assigning integer values to variables
# # positive_integer = 42
# # negative_integer = -17
# # zero = 0

# # # Performing basic arithmetic operations with integers
# # sum_result = positive_integer + negative_integer  # 42 + (-17) = 25
# # difference_result = positive_integer - negative_integer  # 42 - (-17) = 59
# # multiplication_result = positive_integer * 2  # 42 * 2 = 84
# # division_result = positive_integer // 5  # Integer division: 42 // 5 = 8
# # modulus_result = positive_integer % 5  # Remainder: 42 % 5 = 2

# # # Printing the results
# # print("Sum:", sum_result)
# # print("Difference:", difference_result)
# # print("Multiplication:", multiplication_result)
# # print("Integer Division:", division_result)
# # print("Modulus:", modulus_result)
# def two_sum(nums, target):
#     # Create a dictionary to store the complement and its index
#     num_to_index = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         # If the complement is in the dictionary, return the pair of indices
#         if complement in num_to_index:
#             return [num_to_index[complement], i]
        
#         # Store the index of the current number
#         num_to_index[num] = i

# # Example usage
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))  # Output: [0, 1]

# nums = [3, 2, 4]
# target = 6
# print(two_sum(nums, target))  # Output: [1, 2]

# nums = [3, 3]
# target = 6
# print(two_sum(nums, target))  # Output: [0, 1]

# # Example 1:
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# # Example 2:
# # Input: nums = [3,2,4], target = 6
# # Output: [1,2]

# # Example 3:
# # Input: nums = [3,3], target = 6
# # Output: [0,1]

function mergeSort(arr):
    if length of arr <= 1:
        return arr  # Base case: If the array has 1 or no elements, it's already sorted
    
    # Step 1: Split the array into two halves
    mid = length of arr / 2
    leftHalf = arr[0 to mid - 1]
    rightHalf = arr[mid to end]

    # Step 2: Recursively sort both halves
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    # Step 3: Merge the two sorted halves
    return merge(sortedLeft, sortedRight)

function merge(left, right):
    result = []  # Array to store the merged result
    i = 0  # Pointer for left array
    j = 0  # Pointer for right array

    # Step 4: Compare elements from both arrays and merge them in sorted order
    while i < length of left and j < length of right:
        if left[i] <= right[j]:
            append left[i] to result
            i = i + 1
        else:
            append right[j] to result
            j = j + 1

    # Step 5: Append any remaining elements in left or right array
    while i < length of left:
        append left[i] to result
        i = i + 1

    while j < length of right:
        append right[j] to result
        j = j + 1

    return result  # Return the merged array

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sortedArr = mergeSort(arr)
print(sortedArr)  # Output: [3, 9, 10, 27, 38, 43, 82]
