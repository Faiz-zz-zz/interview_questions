"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        left = [1 for i in nums]
        left[1] = nums[0]
        for i in range(2, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
        right = [1] * len(nums)
        right[-2] = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        print right, left    
        retArray = [right[i] * left[i] for i in range(len(nums))]
        return retArray
        
            
        