class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if t not in ["+","-","*","/"]:
                stack.append(t)
            elif t == "+": 
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)
            elif t == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif t == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b / a)
        
        return int(stack[-1])
