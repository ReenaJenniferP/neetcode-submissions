class Solution:
    def isValid(self, st: str) -> bool:
        stack = []

        for s in st:

            if s == '(' or s == '[' or s == '{':
                stack.append(s)

            elif stack != [] and ((s == ')' and stack[-1] == '(') or (s == ']' and stack[-1] == '[') or (s == '}' and stack[-1] == '{')):
                stack.pop()
            
            else:
                return False 
            
        return stack == []
            
            