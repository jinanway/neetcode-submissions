class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0

        while(i < len(haystack)):
            if(i + len(needle) < len(haystack) and haystack[i:(i+len(needle))] == needle):
                return i
            elif(haystack[i:] == needle):
                return i
            i += 1

        return -1