class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1: 
            self.mstack.append(val)
        else: 
            res = self.mstack[-1]
            self.mstack.append(min(val, res))

    def pop(self) -> None:
        self.stack.pop()
        self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]