# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum(nums, target):
    num_to_index = {}
    for i, num in nums:
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
