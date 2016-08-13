"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

"""

import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        minima = secondMinima = sys.maxsize
        
        for i in nums:
            if minima >= i:
                minima = i
            elif secondMinima >= i:
                secondMinima = i
            else:
                return True  
        return False  