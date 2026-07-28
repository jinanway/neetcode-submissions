class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l <= r):
            if(nums[l] == target):
                return l
            if(nums[r] == target):
                return r
            
            if(nums[int((r+l)/2)] < target):
                l = int((r+l)/2) + 1
            elif(nums[int((r+l)/2)] > target):
                r = int((r+l)/2) - 1
            else:
                return int((r+l)/2)

        return -1
            