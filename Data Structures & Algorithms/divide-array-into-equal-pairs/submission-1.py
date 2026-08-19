class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numbers = {}

        for num in nums:
            if(num not in numbers):
                numbers[num] = 1
            else:
                numbers[num] += 1
        

        for num in numbers:
            if(numbers[num] % 2 != 0):
                return False
        

        return True