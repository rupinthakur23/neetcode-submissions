class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            a = -heapq.heappop(maxHeap)
            b = -heapq.heappop(maxHeap)

            if a == b:
                continue
            else:
                heapq.heappush(maxHeap, -(a-b))
        
        return 0 if len(maxHeap) == 0 else -maxHeap[0]