class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort( key = lambda t: t[1])
        minHeap = []
        totalPassenger = 0

        for passengers, start, end in trips:
            totalPassenger+= passengers

            while minHeap and start >= minHeap[0][0]:
                totalPassenger -= minHeap[0][1]
                heapq.heappop(minHeap)

            if totalPassenger > capacity:
                return False
            
            heapq.heappush(minHeap, [end, passengers])
        
        return True