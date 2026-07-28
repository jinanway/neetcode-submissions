class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if(len(s) == 1):
        #     if(s[0] != " "):
        #         return 1
        #     else:
        #         return 0

        count = 0
        i = len(s) - 1
        
        while(s[i] == " "):
            i -= 1

        while(i >= 0 and s[i] != " "):
            i -= 1
            count += 1
        
        return count