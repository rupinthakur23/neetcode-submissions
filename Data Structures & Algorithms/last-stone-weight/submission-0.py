class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            x = -1 * heapq.heappop(heap)
            heapq.heapify(heap)
            y = -1 * heapq.heappop(heap)

            if x > y:
                x = x -y
                heapq.heappush(heap,-1 * x)
        
        return -1 * heap[0] if len(heap) > 0 else 0
