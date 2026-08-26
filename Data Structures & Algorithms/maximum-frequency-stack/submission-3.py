class FreqStack:

    def __init__(self):
        self.maxFrequency = 0
        self.count = {}
        self.countStore = {}

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        if self.count[val] > self.maxFrequency:
            self.maxFrequency = self.count[val]
            self.countStore[self.maxFrequency] = []

        self.countStore[self.count[val]].append(val)

    def pop(self) -> int:
        result = self.countStore[self.maxFrequency].pop()
        self.count[result] -=1
        if not self.countStore[self.maxFrequency]:
            self.maxFrequency -= 1
        
        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()