"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].



"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        prev = None
        retStart = -1
        retEnd = -1
        while index < len(nums):
        	if nums[index] == target:
        		prev = nums[index]
        		retStart = index
        		while prev == nums[index] and index < len(nums):
        			index += 1
                    if index == len(nums):
                        break
        		retEnd = index - 1
        	index += 1

        return [retStart, retEnd]
        
obj = Solution()

print(obj.searchRange([5, 7, 7, 8, 8, 10], 8))        		
