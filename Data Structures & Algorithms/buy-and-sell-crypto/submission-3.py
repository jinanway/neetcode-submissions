class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        max = 0

        while(r < len(prices)):
            if(prices[r] - prices[l] > max):
                max = prices[r] - prices[l]

            r += 1

            if(r == len(prices)):
                l += 1
                r = l + 1
        
        return max