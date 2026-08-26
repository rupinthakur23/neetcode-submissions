class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        answer = []

        for index in points:
            distance = -(index[0] **2 + index[1] **2)

            heapq.heappush(result, [distance, index[0], index[1]])

            if len(result) >k:
                heapq.heappop(result)
        
        while result:
            distance, x, y = heapq.heappop(result)
            answer.append([x,y])
        
        return answer
