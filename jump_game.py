"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

"""



class Solution(object):
    def shittyCode(self, nums):
        print("aibdsaiuhds")
        if len(nums) == 1 and sum(nums) == 0:
            return True
        if sum(nums) == len(nums):
            return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = [None for i in range(len(nums))]
        def recurMethod(currPos):
            if currPos < len(nums):
                if currPos == len(nums) - 1:
                    return True             
                for i in range(nums[currPos], 0, -1):
                    if currPos + i < len(nums):
                        if memo[currPos + i] != False:
                            if recurMethod(currPos + i):
                                return True
            memo[currPos] = False           
            return False
        return True if recurMethod(0) else False
    # linear solution    
    def canJump(self, nums):
        jumpCounter = 0
        for i in reversed(nums[:-1]):
            jumpCounter += 1
            if jumpCounter <= i:
                jumpCounter = 0
        return True if jumpCounter == 0 else False            
array = [2, 0, 0]
print(Solution().canJump_1(array))