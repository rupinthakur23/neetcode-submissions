class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            distance = (x * x) + (y * y)
            heapq.heappush(heap, (distance, [x,y]))
        
        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k-=1
        return result


