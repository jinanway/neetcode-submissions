class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while(l <= r):
            m = r + l // 2
            if(nums[l] == target):
                return l 
            if(nums[r] == target):
                return r 
            if(nums[m] == target):
                return m 
            elif(nums[m] < target):
                l = m + 1
            else:
                r = m - 1

        if(nums[r] > target):
            return l
        else:
            return r + 1

    

            