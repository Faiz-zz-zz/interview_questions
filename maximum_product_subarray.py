"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_end = 0
        min_end = 0
        maxima = 0
        for i in nums:
        	if i > 0:
        		max_end = max_end * i 
        		min_end = max(min_end * i , 1)
        	elif  i == 0:
        		max_end = min_end = 1
        	else:
        		tmp = max_end
        		max_end = max(min_end * i, 1)	
        		min_end = max_end * i
        	if max_end > maxima:
        		maxima = max_end
        return maxima
        
        			
