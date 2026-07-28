class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        currMax = 0

        while(l < r and r < len(heights)):
            currMax = max(currMax, (min(heights[l], heights[r]) * (r - l)))
            if(heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        
        return currMax


