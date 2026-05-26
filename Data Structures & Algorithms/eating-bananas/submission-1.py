class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        low = 1 
        high = k

        while low < high:
            mid = (low+high)//2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            
            if time <= h:
                high = mid 
            else:
                low = mid + 1
            
        return low
