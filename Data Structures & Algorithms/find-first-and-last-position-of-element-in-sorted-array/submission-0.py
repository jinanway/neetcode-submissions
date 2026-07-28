class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        if(l == r and nums[l] == nums[r] == target):
            return [l, r]

        while(l < r):
            if(nums[l] != target):
                l += 1
            if(nums[r] != target):
                r -= 1
            if(nums[l] == nums[r] == target):
                return [l, r]

        return [-1,-1]
        