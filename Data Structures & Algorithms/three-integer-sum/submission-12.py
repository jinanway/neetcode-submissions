class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                curSum = nums[i] + nums[l] + nums[r]
                if(curSum > 0):
                    r -= 1
                elif(curSum < 0):
                    l += 1
                else:
                    if([nums[i],nums[l],nums[r]] not in output):
                        output.append([nums[i],nums[l],nums[r]])
                    l += 1

        return output