class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            if self.min[-1] >= val:
                self.min.append(val)
        
    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min[-1]:
            self.min.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
