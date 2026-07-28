class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen = set()
            for num in row:
                if(num != "." and num not in seen):
                    seen.add(num)
                elif(num in seen):
                    return False
            
        for i in range(len(board[0])):
            seen = set()
            for row in board:
                num = row[i]
                if(num != "." and num not in seen):
                    seen.add(num)
                elif(num in seen):
                    return False

        coords = [[1, 1], [1, 4], [1, 7], 
                  [4, 1], [4, 4], [4, 7],
                  [7, 1], [7, 4], [7, 7]]

        
        for c in coords:
            seen = set()
            for i in range(-1, 2):
                x = c[0]
                x += i
                for j in range(-1, 2):
                    y = c[1]
                    y += j
                    num = board[x][y]
                    if(num != "." and num not in seen):
                        seen.add(num)
                    elif(num in seen):
                        return False

        return True