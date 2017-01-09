"""

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if matrix == []: return 0

        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for i in range(len(matrix[0])):
            if matrix[0][i] == "1":
                dp[0][i] = 1
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return max(map(max, dp))**2

        
