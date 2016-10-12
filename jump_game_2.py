"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        capacity = 0
        total_jumps = 0
        for index, jump in enumerate(nums):
            if ((capacity + index) >= (len(nums) - 1)):
                return total_jumps + 1
            if capacity <= jump:
                total_jumps += 1
                capacity = jump
            print(index)
        return total_jumps
print(Solution().jump([3, 1, 1, 1]))
