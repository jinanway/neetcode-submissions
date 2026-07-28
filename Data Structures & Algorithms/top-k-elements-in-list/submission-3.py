class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if (num in counts):
                counts[num] += 1
            else:
                counts[num] = 1
        
        for key, value in counts.items():
            freq[value].append(key);
        
        i = len(freq) - 1
        retSet = set()
        while(len(retSet) is not k):
            if(freq[i]):
                retSet.update(freq[i])
            i = i - 1
        
        return list(retSet)