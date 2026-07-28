class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        check = True
        i = len(nums) - 1
        while(nums[i - 1] >= nums[i] and i != 0):
            i -= 1
        i -= 1

        if(i <= 0):
            nums.sort()
            return

        j = len(nums) - 1
        while(nums[j] <= nums[i]):
            j -= 1

        bucket = nums[j] 
        nums[j] = nums[i]
        nums[i] = bucket

        nums[i+1:] = sorted(nums[i+1:])



        