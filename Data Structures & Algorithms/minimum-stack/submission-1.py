class MinStack:

    def __init__(self):
        self.stack1 = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack1.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack1.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack1[-1]
                

    def getMin(self) -> int:
        return self.minStack[-1]
