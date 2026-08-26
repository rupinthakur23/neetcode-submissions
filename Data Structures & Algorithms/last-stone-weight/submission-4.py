class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-weight for weight in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x > y:
                heapq.heappush(maxHeap, -(x - y))
        

        return -maxHeap[0] if len(maxHeap) else 0
