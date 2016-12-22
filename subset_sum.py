"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such
that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false


"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums)//2
        table = [
                [False for i in range(len(nums) + 1)]
                for i in range(target + 1)
        ]
        for i in range(len(nums) + 1):
            table[0][i] = True
        for i in range(target + 1):
            table[i][0] = False

        for i in range(1, target + 1):
            for j in range(1, len(nums) + 1):
                table[i][j] = table[i][j - 1]
                if i >= nums[j - 1]:
                    table[i][j] = table[i][j] or table[i - nums[j - 1]][j - 1]
        for row in table:
            print(row)
        return table[target][len(nums)]

    def solution1(self, nums):
        if sum(nums) % 2 == 1:
            return False

        def recurMethod(target, index):
            if target < 0:
                return False

            if target == 0:
                return True

            for i in range(index, len(nums) + 1):
                if recurMethod(target - nums[i], i + 1):
                    return True

            return False

        return recurMethod(target, 0)

print(Solution().canPartition([1, 2, 3]))
