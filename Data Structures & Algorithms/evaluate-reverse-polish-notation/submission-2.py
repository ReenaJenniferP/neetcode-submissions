class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i.lstrip("-").isdigit():
                s.append(i)
            else:
                b = int(s.pop())
                a = int(s.pop())
                
                if i == '+':
                    s.append(a+b)
                elif i == '-':
                    s.append(a-b)
                elif i == '*':
                    s.append(a*b)
                elif i == '/':
                    s.append(int(a/b))
        
        return int(s[0])