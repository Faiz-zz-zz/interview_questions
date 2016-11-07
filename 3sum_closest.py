"""
Given an array S of n integers, find three integers in S such that the sum
 is closest to a given number, target. Return the sum of the three integers.
  You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        min_now = sys.maxsize
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                diff = abs(total - target)
                if diff == 0: return target
                if diff <= min_now:
                    min_now = diff
                    result = total
                if total < target:
                    start += 1
                else:
                    end -= 1
        return result
print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
