"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [[0 for i in range(n)] for j in range(n)]

        result = []

        def valid(i, j, array):
            for elem in array:
                if ((i + j) == (elem[0] + elem[1])) or ((j - i) == elem[1] - elem[0]):
                    return False
                if i == elem[0] or j == elem[1]:
                    return False
            return True

        def dfs(occupied, row):
            if row > n - 1:
                result.append(occupied)
                return

            for i in range(n):
                if valid(row, i, occupied):
                    dfs(occupied + [[row, i]], row + 1)

        for i in range(n):
            dfs([[0, i]], 1)

        answer = []

        for board in result:
            new_ans = [["." for i in range(n)] for j in range(n)]
            for elem in board:
                new_ans[elem[0]][elem[1]] = "Q"
            new = ["".join(array) for array in new_ans]
            answer.append(new)
        return answer
