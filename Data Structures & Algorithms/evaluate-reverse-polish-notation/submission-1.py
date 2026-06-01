class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if t not in ["+","-","*","/"]:
                stack.append(t)
            elif t == "+": 
                stack.append(int(stack[-2]) + int(stack[-1]))
                stack.pop(-2)
                stack.pop(-2)
            elif t == "-":
                stack.append(int(stack[-2]) - int(stack[-1]))
                stack.pop(-2)
                stack.pop(-2)
            elif t == "*":
                stack.append(int(stack[-2]) * int(stack[-1]))
                stack.pop(-2)
                stack.pop(-2)
            else:
                stack.append(int(stack[-2]) / int(stack[-1]))
                stack.pop(-2)
                stack.pop(-2)
        
        return int(stack[-1])
