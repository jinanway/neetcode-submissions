class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set();
        l = 0;
        num = 0;

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l+1
            charSet.add(s[r])
            num = max(num, r - l + 1)

        return num

            