"""
Given an array of integers and an integer k, find out whether there are
two distinct indices i and j in the array such that nums[i] = nums[j] and
the difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            start = max(i-k, 0)
            for j in range(start, i):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        position_array = sorted(range(len(nums)), key = lambda x: nums[x])
        for i in range(len(nums)-1):
            j = i + 1
            while j < len(nums) and nums[position_array[j]] - nums[position_array[i]] <= t:
                if abs(position_array[i]-ind[j]) <= k:
                    return True
                j += 1
        return False

print(Solution().containsNearbyDuplicate([2, 2], 3))
