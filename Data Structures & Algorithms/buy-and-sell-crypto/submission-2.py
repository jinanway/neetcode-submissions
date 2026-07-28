class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0;
        l = 0
        r = 1

        while(l < len(prices) - 1):
            if(prices[r] - prices[l] > profit):
                profit = prices[r] - prices[l]

            r += 1

            if(r == len(prices)):
                l += 1
                r = l + 1

        return profit
        