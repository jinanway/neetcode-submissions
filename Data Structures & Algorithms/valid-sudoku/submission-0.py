class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = set()
        for row in board:
            for i in row:
                if(i.isdigit()):
                    if(i in rowCheck):
                        return False
                rowCheck.add(i)
            rowCheck = set()

        colCheck = set()
        for col in range(0, 9):
            for row in range (0, 9):
                if(board[row][col].isdigit()):
                    if(board[row][col] in colCheck):
                        return False
                colCheck.add(board[row][col])
            colCheck = set()

        i = 0
        j = 0
        boxCheck = set()
        while(i != 9 and j != 9):
            for row in range (i, i + 3):
                for col in range(j, j + 3):
                    if(board[row][col].isdigit()):
                        if(board[row][col] in boxCheck):
                            return False
                    boxCheck.add(board[row][col])
            boxCheck = set()

            j += 3

            if(j == 9 and i != 9):
                i += 3
                j = 0
        
        return True
            



