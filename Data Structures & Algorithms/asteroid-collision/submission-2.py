class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            add = True
            while stack and stack[-1] > 0 and ast < 0: 
                if abs(stack[-1]) < abs(ast):
                    stack.pop()

                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    add = False
                    break
                    
                else:
                    add = False
                    break 
                    
            if add:
                stack.append(ast)

        return stack