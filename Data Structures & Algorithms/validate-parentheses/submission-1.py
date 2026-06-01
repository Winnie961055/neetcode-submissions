class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeBrackets = { ")" : "(", "]" : "[", "}" : "{" } 

        for b in s:
            if b in closeBrackets:
                if stack and stack[-1] == closeBrackets[b]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(b)        

        return not stack
                