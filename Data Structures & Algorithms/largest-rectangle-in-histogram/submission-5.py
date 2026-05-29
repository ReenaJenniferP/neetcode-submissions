class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i, v in enumerate(heights):
            next_start = i
            while stack and stack[-1][1] > v:
                prev_i, prev_v = stack.pop()
                next_start = prev_i
                max_area = max(prev_v*(i-prev_i), max_area)
                
            stack.append((next_start, v))

        return max_area
            
    
        

