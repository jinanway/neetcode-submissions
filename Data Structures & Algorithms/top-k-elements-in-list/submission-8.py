class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(nums == []):
            return []
        
        j = 0
        check = [[] for _ in range(len(nums) + 1)]

        count = {}
        for num in nums:
            if(num in count):
                count[num] += 1
            else:
                count[num] = 1
        
        for key in count:
            check[count[key]].append(key)
        
        output = []
        i = len(check) - 1
        while(len(output) < k):
            output += check[i]
            i -= 1

        return output