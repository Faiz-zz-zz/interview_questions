"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inter = 0
        maxima = -9999999999

        for i in range(len(nums)):
        	inter = max(inter + nums[i], nums[i])
        	maxima = max(maxima, inter)
        return maxima	



obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))        			 