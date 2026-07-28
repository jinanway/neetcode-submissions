class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = ""

        for l in range(len(s)):
            for r in range(l, len(s)):
                sub = s[l:r + 1]
                if(sub == sub[::-1]):
                    if(len(sub) > len(curr)):
                        curr = sub
        
        return curr
            