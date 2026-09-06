class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result, minheap = [], []

        for x, y in points:
            distance = (x * x) + (y * y)
            heapq.heappush(minheap, [distance, [x, y]])
        
        while len(result) < k:
            result.append(heapq.heappop(minheap)[1])
        
        return result