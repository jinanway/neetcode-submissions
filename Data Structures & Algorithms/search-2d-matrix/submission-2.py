class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while(i < len(matrix)):
            j = 0
            if(matrix[i][len(matrix[i]) - 1] >= target):
                while(j < len(matrix[i])):
                    if(matrix[i][j] == target):
                        return True
                    j += 1
            i += 1
        
        return False
