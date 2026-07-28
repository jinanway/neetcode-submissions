class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 1

        while(l < len(nums)):
            if(nums[l] + nums[r] == target):
                break
            else:
                r += 1
            if(r == len(nums)):
                l += 1
                r = l+1

        return [l, r]