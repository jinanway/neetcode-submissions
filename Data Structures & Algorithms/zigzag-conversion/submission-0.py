class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = []
        for i in range(numRows):
            matrix.append([])
        
        i = 0
        direction = True
        for c in s:
            if(i == numRows - 1):
                direction = False
            matrix[i].append(c)

            if(direction):
                i += 1
            else:
                i -= 1

            if(i == 0):
                direction = True
        
        print(matrix)

        output = ""
        for i in matrix:
            output += "".join(i)
        
        return output