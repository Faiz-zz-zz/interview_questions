"""

229. Majority Element II  QuestionEditorial Solution  My Submissions
Total Accepted: 38707
Total Submissions: 142902
Difficulty: Medium
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

Show Hint

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums <= 2:
            return nums

        limit = n // 3

        ret_array = {[]}
