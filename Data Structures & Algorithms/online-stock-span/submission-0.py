class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        curr = [price, 1]

        while self.stack and self.stack[-1][0] <= price:
            top = self.stack.pop()
            curr[1] += top[1]
        
        self.stack.append(curr)
            
        return self.stack[-1][1]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)