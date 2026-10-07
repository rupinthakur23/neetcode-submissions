class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = (x*x) +(y*y)
            heapq.heappush(minHeap, [distance, (x,y)])
        
        count, result = 0, []

        while count < k:
            dist, node = heapq.heappop(minHeap)
            result.append(node)
            count +=1
        
        return result