class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        letters = []

        check = True
        
        i = 0
        j = 0
        while(check):
            print(i)
            if(i == 0):
                if(j >= len(strs[i])):
                    check = False
                    break
                letters.append(strs[i][j])
            
            if(j >= len(strs[i]) or strs[i][j] != letters[j]):
                letters.pop()
                check = False
                break
            
            i += 1
            if(i == len(strs)):
                j += 1
                i = 0
            
            
        
        return "".join(letters)

