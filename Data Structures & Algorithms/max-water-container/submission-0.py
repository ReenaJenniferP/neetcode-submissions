class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1 

        m = 0

        while l < r:
            if heights[l] < heights[r]:
                m = max(m, (r-l)*heights[l])
                l += 1
            else:
                m = max(m, (r-l)*heights[r])
                r -= 1
        
        return m
    