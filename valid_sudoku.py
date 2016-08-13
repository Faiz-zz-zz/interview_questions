class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowHash = {i:[] for i in range(9)}
        columnHash = {i:[] for i in range(9)}
        squareHash = {i:[] for i in range(9)}
        hardCoding = {"00":0, "01":1, "02":2, "10":3, "11":4, "12":5, "20":6, "21":7, "22":8}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rowHash[i]:
                        return False
                    else:
                        rowHash[i].append(board[i][j])    
                    if board[i][j] in columnHash[j]:
                        return False
                    else:
                        columnHash[j].append(board[i][j])
                    the = str(i//3) + str(j//3)
                    if board[i][j] in squareHash[hardCoding[the]]:
                        return False
                    else:
                        squareHash[hardCoding[the]].append(board[i][j])       
        return True                 

        