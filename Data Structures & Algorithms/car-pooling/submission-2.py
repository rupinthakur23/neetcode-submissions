class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        minHeap = []
        totalPassengers = 0

        for passenger, start, end in trips:
            totalPassengers += passenger

            while minHeap and start >= minHeap[0][0]:
                totalPassengers -= heapq.heappop(minHeap)[1]
            
            if totalPassengers > capacity:
                return False

            heapq.heappush(minHeap, [end, passenger])
        
        return True




