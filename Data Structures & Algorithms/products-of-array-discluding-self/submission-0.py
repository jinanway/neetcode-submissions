class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        retNums = [0] * len(nums)
        i = 0;
        j = 0;
        product = 1
        while(i < len(nums)):
            if(j == len(nums)):
                retNums[i] = product
                product = 1
                i += 1
                j = 0
            if(i != j):
                product *= nums[j]
                print(product)
            j += 1

        return retNums
