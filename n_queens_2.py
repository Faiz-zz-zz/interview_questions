
"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [[0 for i in range(n)] for j in range(n)]

        result = [0]

        def valid(i, j, array):
            for elem in array:
                if ((i + j) == (elem[0] + elem[1])) or ((j - i) == elem[1] - elem[0]):
                    return False
                if i == elem[0] or j == elem[1]:
                    return False
            return True

        def dfs(occupied, row):
            if row > n - 1:
                result[0] += 1
                return

            for i in range(n):
                if valid(row, i, occupied):
                    dfs(occupied + [[row, i]], row + 1)

        for i in range(n):
            dfs([[0, i]], 1)

        return result[0]
