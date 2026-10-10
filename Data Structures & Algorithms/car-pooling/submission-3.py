class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        minHeap = []
        totalPassengers = 0
        for passenger, start, end in trips:
            totalPassengers += passenger

            while minHeap and minHeap[0][0] <=start:
                endTime, oldPassenger = heapq.heappop(minHeap)
                totalPassengers -= oldPassenger
            
            if totalPassengers > capacity:
                return False


            heapq.heappush(minHeap, [end, passenger])
        return True
        