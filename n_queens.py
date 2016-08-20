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
        def recurMethod(list_of_placements, queens_left):
            if queens_left == 0:
                return True

            nextPos = findNextValidSpace(list_of_placements)

            if nextPos == None:
                return False

            return recurMethod(list_of_placements.append(nextPos), queens_left - 1)    

        def findNextValidSpace(list_of_placements):
            for i in range(n):
                for j in range(n):
                    for places in list_of_placements:
                        row = i == places[0]
                        columns = j == places[1]
                        diagonal = (i -- places[0]) == (j -- places[1]) 
                        if not (row and columns and diagonal):
                            return [i, j]

