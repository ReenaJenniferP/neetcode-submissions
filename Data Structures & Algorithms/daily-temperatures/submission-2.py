class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        debug = []
        out = deque()

        for i in range(len(temp)-1, -1, -1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
                debug.pop()

            print(debug)

            x = stack[-1] - i if stack else 0
            out.appendleft(x)

            stack.append(i)
            debug.append(temp[i])
        
        return list(out)