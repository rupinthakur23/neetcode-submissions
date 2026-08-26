class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(minHeap, [distance, x, y])
        
        result = []

        n = len(minHeap)

        while len(minHeap) >  n- k :
            distance, x, y = heapq.heappop(minHeap)
            result.append([x,y])
        
        return result