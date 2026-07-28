class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int profit = 0;
        while(r < prices.length && l < prices.length){
            
            if(prices[r] - prices[l] > profit){
                profit = prices[r] - prices[l];
            }

            r++;
            if(r >= prices.length){
                l++;
                r = l + 1;
            }
        } 

        return profit;  
    }
}
