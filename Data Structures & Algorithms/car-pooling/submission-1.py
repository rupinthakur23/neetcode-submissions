class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        minHeap = []
        totalPassenger = 0

        for passenger, start, end in trips:
            totalPassenger += passenger

            while minHeap and start >= minHeap[0][1]:
                totalPassenger -= minHeap[0][0]
                heapq.heappop(minHeap)

            if totalPassenger > capacity:
                return False

            heapq.heappush(minHeap, [passenger, end])
        
        return True