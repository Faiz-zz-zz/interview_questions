"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        front = 1
        end = 1

        for num in nums:
            if num <= 0:
                if front != 1 and front != -1:  # front == -1 means 1 is seen
                    front

        def remove_duplicates(array):
