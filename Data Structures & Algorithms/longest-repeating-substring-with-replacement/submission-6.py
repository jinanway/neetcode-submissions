class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}

        l = 0
        r = 0
        best = 0

        while(r < len(s)):
            if(s[r] not in chars):
                chars[s[r]] = 1
            else:
                chars[s[r]] += 1
            c = max(chars, key=chars.get)
            while((r - l + 1) - chars[c] > k):
                chars[s[l]] -= 1
                l += 1
                c = max(chars, key=chars.get)

            r += 1
            best = max(best, r - l)

        return best