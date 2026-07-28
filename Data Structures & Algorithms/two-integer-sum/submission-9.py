class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        ret = []
        for i, num in enumerate(nums):
            if((target - num) in numbers):
                ret.append(numbers[(target - num)])
                ret.append(i)
                break
            else:
                numbers[num] = i

        return ret