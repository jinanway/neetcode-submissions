class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        i = 0
        j = 0
        count = 0
        nums = []
        while(i < len(temperatures)):
            if(temperatures[i] < temperatures[j]):
                nums.append(count)
                i += 1
                j = i
                count = 0
            else:
                j += 1
                count += 1
            
            if(j == len(temperatures)):
                nums.append(0)
                i += 1
                j = i
                count = 0
        
        return nums