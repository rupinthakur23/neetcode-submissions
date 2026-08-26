class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        result = []

        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(minHeap, [distance, (x, y)])
        
        counter = 0

        
        while counter < k:
            distance, coordinates = heapq.heappop(minHeap)
            result.append(coordinates)
            counter +=1
        
        return result
