class MyStack:

    def __init__(self):
        self.stack = []
        self.t = -1
        

    def push(self, x: int) -> None:
        self.t += 1
        self.stack.append(x)

    def pop(self) -> int:
        self.t -= 1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[self.t]

    def empty(self) -> bool:
        return self.t == -1 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()