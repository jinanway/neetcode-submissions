class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = ""
        maxLen = 0
        for i in range(len(s)):
            l, r = i, i
            currLen = 1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
                currLen = r - l - 1
            
            if(currLen > maxLen):
                curr = s[l + 1:r]
                maxLen = currLen 

            l, r = i, i + 1
            currLen = 1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
                currLen = r - l - 1

            if(currLen > maxLen):
                curr = s[l + 1:r]
                maxLen = currLen 
               

        return curr
            