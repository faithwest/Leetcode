# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):  # Added 'self' as the first parameter
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[value] = i







###################################################
#works but long
# class Solution(object):
#     def twoSum(nums,target):#2 params
#         summation=set()#keep track of numbers in the solution
#         for num in range(len(nums)):#iterate over the indices of the two numbers to find their sum
#             if target - nums[num] in summation:#checking the diff btn current and target
#                 return [nums.index(target - nums[num]), num]
#             else:
#                 summation.add(nums[num])

# nums1 = [1, 2, 3, 4, 5]
# target1 = 6
# solution = Solution()
# print(solution.twoSum(nums1, target1))  # Output: [0, 3] (1 + 5 = 6)