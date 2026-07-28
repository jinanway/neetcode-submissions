class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        i = 0
        last = nums[0]
        while(i < len(nums)):
            if((i+1) % 2 == 0 and nums[i] != last):
                return last
            
            last = nums[i]
            i += 1
        
        return last
        