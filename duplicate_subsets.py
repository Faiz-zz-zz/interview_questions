"""Given a collection of integers that might contain duplicates, nums, return
 all possible subsets.

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
]"""


class Solution(object):
    def duplicates(self, nums):
        """
        type nums: [int]
        rtype: [int]
        """
        ret_array = []
        for i in range(2**len(nums)):
            seq = bin(i)[2:]
            if len(seq) < len(nums):
                seq = "0" * (len(nums) - len(seq)) + seq
            sub_ans = []
            for index, letter in enumerate(seq):
                if letter == '1':
                    sub_ans.append(nums[index])
            if sub_ans not in ret_array:
                ret_array.append(sub_ans)
        return(ret_array)
print(Solution().duplicates([1, 2, 2]))
