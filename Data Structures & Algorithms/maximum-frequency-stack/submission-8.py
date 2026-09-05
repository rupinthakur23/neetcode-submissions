class FreqStack:

    def __init__(self):
        self.freqStack = defaultdict(list)
        self.maxFreq = 0
        self.elemFreq = defaultdict(int)

    def push(self, val: int) -> None:
        count = self.elemFreq.get(val, 0) + 1
        self.elemFreq[val] = count
        self.freqStack[count].append(val)
        self.maxFreq = max(self.maxFreq, count)
        
    def pop(self) -> int:
        result = self.freqStack[self.maxFreq].pop()
        self.elemFreq[result] -=1
        if not self.freqStack[self.maxFreq]:
            self.maxFreq -= 1
        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()