class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y, x = -1 * heapq.heappop(heap), -1 * heapq.heappop(heap)
            if y > x:
                heapq.heappush(heap, -(y - x))
        
        return 0 if len(heap) == 0 else -heap[0]