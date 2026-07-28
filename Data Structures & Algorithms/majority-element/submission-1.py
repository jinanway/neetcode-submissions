class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()

        for i in nums:
            if(i in counts):
                counts[i] += 1
            else:
                counts[i] = 1
        
        ret = 0
        for k, v in counts.items():
            if(v == max(counts.values())):
                return k
        
        return 