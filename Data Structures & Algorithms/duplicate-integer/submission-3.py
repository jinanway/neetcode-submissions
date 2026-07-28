class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 0:
            return False
        i = 0;
        j = 1;
        num = nums[i]
        while i < len(nums) - 1:
            if j >= len(nums):
                i = i + 1
                j = i + 1
            elif nums[i] == nums[j]:
                return True
            else:
                j = j + 1
        
        return False
