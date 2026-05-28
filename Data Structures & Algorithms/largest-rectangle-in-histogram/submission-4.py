class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0
        for i, v in enumerate(heights):
            new_start = i
            while stack and stack[-1][1] > v:
                prev_i, prev_v = stack.pop()
                max_area = max(max_area, (i - prev_i)*prev_v)
                new_start = prev_i
                
            
            stack.append((new_start, v))


        return max_area
            