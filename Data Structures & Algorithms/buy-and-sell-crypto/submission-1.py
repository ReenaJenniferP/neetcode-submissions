class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        start = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < start:
                start = prices[i]
            
            else:
                p = max(p, prices[i]-start)
        
        return p

