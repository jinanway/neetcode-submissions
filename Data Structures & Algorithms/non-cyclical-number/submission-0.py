class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = str(n)

        curr = 0
        while(curr != 1):
            curr = 0
            for i in range(len(num)):
                curr += (int(num[i]) * int(num[i]))
            
            if(curr in seen):
                return False
            
            num = str(curr)
            seen.add(curr)
        
        return True

