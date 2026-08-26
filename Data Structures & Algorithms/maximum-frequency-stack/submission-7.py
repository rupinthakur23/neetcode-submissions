class FreqStack:

    def __init__(self):
        self.freqStack = {}
        self.countStack = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        count = self.countStack.get(val, 0) + 1
        self.countStack[val] = count

        self.maxFreq = max(self.maxFreq, count)

        if self.maxFreq not in self.freqStack:
            self.freqStack[self.maxFreq] = []
        
        self.freqStack[count].append(val)

    def pop(self) -> int:
        value = self.freqStack[self.maxFreq].pop()

        if not self.freqStack[self.maxFreq]:
            self.maxFreq -=1
        
        self.countStack[value] -=1

        return value


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()