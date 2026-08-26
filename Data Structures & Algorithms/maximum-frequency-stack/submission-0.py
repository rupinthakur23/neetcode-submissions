class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxFreq = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        counter = self.count.get(val, 0) + 1
        self.count[val] = counter
        if counter > self.maxFreq:
            self.maxFreq +=1
            self.stacks[self.maxFreq] = []
        self.stacks[counter].append(val)
        

    def pop(self) -> int:
        res = self.stacks[self.maxFreq].pop()
        self.count[res] -=1
        if not self.stacks[self.maxFreq]:
            self.maxFreq -=1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()