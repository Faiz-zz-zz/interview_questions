"""
Given a collection of integers that might contain duplicates, nums, return all
possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size_power_set = 2**len(nums)
        power_set = []

        iteration = 0
        for i in range(size_power_set):
            bit_notation = bin(i)[2:]
            elem = []
            bit_notation = "0" * (len(nums) - len(bit_notation)) + bit_notation
            print(bit_notation)
            for index, bit in enumerate(bit_notation):
                if bit == '1':
                    elem.append(nums[index])
            elem.sort()
            if elem not in power_set:
                power_set.append(elem)
        return power_set

print(Solution().subsetsWithDup([1, 2, 2]))
