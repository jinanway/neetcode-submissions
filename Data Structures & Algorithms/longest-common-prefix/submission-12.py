class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        check = True
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if(i >= len(strs[j]) or strs[0][i] != strs[j][i]):
                    check = False
                    break
            
            if(not check):
                break

            prefix += strs[0][i]
            
            
        
        return prefix

