class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)): 
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-": 
                subtracted = stack.pop()
                stack.append(stack.pop() - subtracted)
            elif tokens[i] == "*": 
                stack.append(stack.pop()*stack.pop())
            elif tokens[i] == "/": 
                divided = stack.pop() 
                stack.append(int((float(stack.pop())/divided)))
            else: 
                stack.append(int(tokens[i]))
        return stack.pop() 