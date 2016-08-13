"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)


"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        position = 0
        jumps = 0
        if len(nums) == 1 or len(nums) == 0:
            return 0
        while (position != len(nums) - 1) and (len(nums) > (position + nums[position])):
            maxima = 0
            maxI = position + 1 
            print(position)
            for i in range(1, nums[position] + 1):
                if maxima < nums[position + i] + i:
                    maxI = i
                    maxima = nums[position + i] + i
            print("maxI = "+str(maxI))        
            position = position + maxI

            jumps += 1
        return jumps



obj = Solution()

print(obj.jump([1, 2]))        