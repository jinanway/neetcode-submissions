class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        i = len(digits)
        multiplier = 1
        while(i > 0):
            num += (digits[i - 1]*multiplier)
            multiplier *= 10
            i -= 1

        num = str(num)
        print(num)
        newDigits = []
        count == 0

        for j in range(len(num)):
            newDigits.append(int(num[j]))
        

        return newDigits
