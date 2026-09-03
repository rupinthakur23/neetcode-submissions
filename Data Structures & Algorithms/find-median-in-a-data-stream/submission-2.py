class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small , -num)

        if self.large and self.large[0] <= -self.small[0]:
            val1 = -heapq.heappop(self.small)
            val2 = heapq.heappop(self.large)
            heapq.heappush(self.small , -val2)
            heapq.heappush(self.large , val1)
        
        if len(self.small) > len(self.large) + 1:
            pop = -heapq.heappop(self.small)
            heapq.heappush(self.large , pop)

    def findMedian(self) -> float:
        if (len(self.large) + len(self.small)) % 2 == 0:
            return (self.large[0] + (-self.small[0]))/2
        else:
            return -self.small[0]
        