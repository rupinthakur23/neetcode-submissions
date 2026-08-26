class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = {}
        self.maxValue = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        self.maxValue = max(self.maxValue, self.freq[val])

        if self.maxValue not in self.stacks:
            self.stacks[self.maxValue] = []
        
        self.stacks[self.freq[val]].append(val) 
        

    def pop(self) -> int:
        val = self.stacks[self.maxValue].pop()
        if not self.stacks[self.maxValue]:
            self.maxValue -=1
        
        self.freq[val] = self.freq.get(val, 0) - 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()