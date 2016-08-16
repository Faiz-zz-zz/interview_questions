"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""

class Solution(object):
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		def solveRecursive(board):
			
			nextPos = findNextUnassigned(board)
			# print(nextPos)
			if nextPos == False:
				return True
			
			for i in range(1, 10):
				if not isValid(board, nextPos, i):
					continue
				string = list(board[nextPos[0]])	
				string[nextPos[1]] = str(i)	
				board[nextPos[0]] = ''.join(string)
				if solveRecursive(board):
					return True	
				string = list(board[nextPos[0]])		
				string[nextPos[1]] = '.'
				board[nextPos[0]] = ''.join(string)

			return False

		def findNextUnassigned(board):
			for i in range(9):
				for	j in range(9):
					if board[i][j] == '.':
						return [i, j]
			return False

		def isValid(board, position, i):	
			# print(row(board, position, i), column(board, position, i), square(board, position, i))
			return row(board, position, i) and column(board, position, i) and square(board, position, i)

		def row(board, position, num):
			for i in range(9):
				if str(num) == board[position[0]][i]:
					return False
			return True
		
		def column(board, position, num):
			for i in range(9):
				if str(num) == board[i][position[1]]:
					return False
			return True
		
		def square(board, position, num):
			row = position[0] // 3
			col = position[1] // 3

			for i in range(3):
				for j in range(3):
					if str(num) == board[row*3 + i][col*3 + j]:
						return False
			return True	

		solveRecursive(board)			

array = [".394..782", "4..2...5.", ".......9.", "....8..3.", "..8.3.5..", ".2..4....", ".6.......", ".7...4..1", "254..796."]
array1 = ["8........", "..36.....", ".7..9.2..", ".5...7...", "....547..", "...1...3.", "..1....68", "..85...1.", ".9....4.."] #hardest sudoku in the world
array3 = [".5..7....", ".2..5.3..", "...1.9..7", ".4......6", "..1...9..", "97....5..", "7..821...", "..56.3.7.", "...7..63."]
obj = Solution()
obj.solveSudoku(array3)
print(array3)