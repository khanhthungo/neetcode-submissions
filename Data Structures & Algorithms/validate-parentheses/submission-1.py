class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            ')': '(', 
            '}': '{', 
            ']':  '['
        }

        for b in s: 
            if b in valid: 
                if len(stack) > 0 and stack[-1] == valid[b]: 
                    stack.pop() 
                else: 
                    return False 
            else: 
                stack.append(b)
        return True if len(stack) == 0 else False