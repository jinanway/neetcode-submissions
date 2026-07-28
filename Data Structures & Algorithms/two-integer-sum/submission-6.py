class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = dict()
        
        i = 0;
        while(i < len(nums)):
            if(target - nums[i] in sums):
                if(i < sums[target - nums[i]]):
                    return [i, sums[target - nums[i]]]
                else:
                    return [sums[target - nums[i]], i]
            else:
                sums[nums[i]] = i
                i = i + 1
        