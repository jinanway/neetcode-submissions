class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        output = []
        while(l < r):
            if(numbers[l] + numbers[r] == target):
                output.append(l + 1)
                output.append(r + 1)
            r += 1
            if(r == len(numbers)):
                l += 1
                r = l + 1
                if(l == len(numbers) - 1):
                    l = r + 1
        
        return output