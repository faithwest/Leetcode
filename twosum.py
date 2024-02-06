# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self,nums,target):
        summation=set()
        for num in range(nums):
            if target_num in summation:
                return [summation&1,num]
            else:
                summation.add(num)

nums1 = [1, 2, 3, 4, 5]
print(Solution(nums1))