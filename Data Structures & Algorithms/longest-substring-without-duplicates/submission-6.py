class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        l = 0
        curr = 0
        highest = 0
        for r in range(len(s)):
            while s[r] in used:
                used.remove(s[l])
                l += 1
            used.add(s[r])
            curr = len(used)
            if(curr > highest):
                highest = curr

        return highest

            