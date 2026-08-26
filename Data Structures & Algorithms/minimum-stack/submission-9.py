class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minValue = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val <= self.minValue:
            self.minValue = val
        self.minStack.append(self.minValue)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.minValue = self.minStack[-1]
        else:
            self.minValue = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
