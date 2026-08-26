class FreqStack:

    def __init__(self):
        self.counts = {}
        self.stacks = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.counts[val] = self.counts.get(val, 0) + 1
        if self.counts[val] > self.maxFreq:
            self.maxFreq = self.counts[val]
            self.stacks[self.maxFreq] = []
        
        self.stacks[self.counts[val]].append(val)

    def pop(self) -> int:
        val = self.stacks[self.maxFreq].pop()
        if not self.stacks[self.maxFreq]:
            self.maxFreq -=1
        
        self.counts[val] -=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()