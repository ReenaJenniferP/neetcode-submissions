class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        l_max = [0]*n

        for i in range(n):
            l_max[i] = l
            l = max(l, height[i])

        r = 0
        r_max = [0]*n

        for i in range(n-1, -1, -1):
            r_max[i] = r
            r = max(r, height[i])
        
        print(l_max)
        print(r_max)
        print(height)
        w = 0
        for i in range(n):
            v = min(l_max[i], r_max[i]) - height[i]
            if v > 0:
                w += v

        return w
            
