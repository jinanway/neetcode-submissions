class Solution:

    def encode(self, strs: List[str]) -> str:
        retStr = ""
        for i in range(0, len(strs)):
            retStr += strs[i] + "."
        
        return retStr

    def decode(self, s: str) -> List[str]:
        strs = []
        retStr = ""
        i = 0
        while(i < len(s)):
            if(s[i] != "."):
                retStr += s[i]
            else:
                strs.append(retStr)
                retStr = ""
            i += 1
        return strs