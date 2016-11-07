"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
 number on it represented by array nums. You are asked to burst all the
  balloons. If the you burst balloon i you will get
   nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent
    indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you
 can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def burst(balloons, start, end):
            if end - start + 1 < 3:
                return 0
            if end - start + 1 == 3:
                return balloons[start] * balloons[start + 1] * balloons[start + 2]
            if dp[start][end] != -1: return dp[start][end]
            new = 0
            for i in range(start + 1, end):
                new = max(new, balloons[i] * balloons[start] * balloons[end] + burst(balloons, i, end) + burst(balloons, start, i))
            dp[start][end] = new
            for row in dp:
                print(row)
            print()    
            return new
        dp = [[-1 for _ in range(len(nums) + 2)] for _ in range(len(nums) + 2)]
        return burst([1] + nums + [1], 0, len(nums) + 1)

print(Solution().maxCoins([3, 1, 5, 8]))
