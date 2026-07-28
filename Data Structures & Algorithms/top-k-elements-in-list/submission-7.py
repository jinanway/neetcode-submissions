class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        output = []
        for num in nums:
            if(num in check):
                check[num] += 1
            else:
                check[num] = 1
        
        i = 0
        while(i < k):
            largestCount = 0
            largestNum = 0
            for key in check:
                if(check[key] > largestCount):
                    largestCount = check[key]
                    largestNum = key
            output.append(largestNum)
            del check[largestNum]
            i += 1
        
        return output