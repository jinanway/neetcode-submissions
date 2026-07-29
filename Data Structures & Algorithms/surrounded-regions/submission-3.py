class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if((row == 0 or row == len(board) - 1 or col == 0 or col == len(board[row]) - 1)
                and board[row][col] == 'O'):
                    board[row][col] = 'T'
    
        print(board)
        
        def dfs(row, col):
            if(row - 1 > 0 and board[row - 1][col] == 'O'):
                board[row - 1][col] = 'T'
                dfs(row - 1, col)
            if(row + 1 < len(board) and board[row + 1][col] == 'O'):
                board[row + 1][col] = 'T'
                dfs(row + 1, col)
            if(col - 1 > 0 and board[row][col - 1] == 'O'):
                board[row][col - 1] = 'T'
                dfs(row, col - 1)
            if(col + 1 < len(board[row]) and board[row][col + 1] == 'O'):
                board[row][col + 1] = 'T'
                dfs(row, col + 1)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if(board[row][col] == 'T'):
                    dfs(row, col)
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if(board[row][col] == 'O'):
                    board[row][col] = 'X'
                if(board[row][col] == 'T'):
                    board[row][col] = 'O'


        return
            
        