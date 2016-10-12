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
        row_length = len(matrix)
        col_length = len(matrix[0])

        dp_matrix = [[0]*col_length] * row_length

        for ind in len(dp_matrix[0]):
            if matrix[0][ind] == 1:
                dp_matrix[0][ind] = 1
            if matrix[ind][0] == 1:
                dp_matrix[ind][0] = 1

        for row in range(1, row_length):
            for col in range(1, col_length):
                if matrix[row][col] == 1:
                    dp_matrix[row][col] = min(dp_matrix[row - 1][col - 1], dp_matrix[row - 1][col], dp_matrix[row][col - 1]) + 1
        return max(map(max, dp_matrix))            
