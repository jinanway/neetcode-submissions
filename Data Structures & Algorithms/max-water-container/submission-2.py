class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while(l < r):
            area = (heights[l] if heights[l] < heights[r] else heights[r]) * (r - l)
            maxArea = maxArea if maxArea > area else area
            if(heights[l] < heights[r]):
                l += 1
            else:
                r -= 1

        return maxArea