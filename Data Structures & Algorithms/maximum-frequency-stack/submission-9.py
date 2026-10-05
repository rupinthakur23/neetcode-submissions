class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.freqStack = defaultdict(list)
        self.maxFreq = 0
        
    def push(self, val: int) -> None:
        self.count[val] +=1
        freq = self.count[val] 
        self.freqStack[freq].append(val)
        self.maxFreq = max(self.maxFreq, freq)

    def pop(self) -> int:
        val = self.freqStack[self.maxFreq].pop()
        self.count[val] -=1
        if not self.freqStack[self.maxFreq]:
            self.maxFreq = self.count[val]
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()