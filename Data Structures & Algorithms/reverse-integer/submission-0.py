class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        check = False
        if(x < 0):
            check = True
            x = x * -1

        while(x != 0):
            num += (x % 10)
            num = num * 10
            x = x // 10
        num = num // 10

        if(num < -2 ** 31 or num > (2 ** 31)):
            return 0

        if(check):
            num = num * -1

        return num

