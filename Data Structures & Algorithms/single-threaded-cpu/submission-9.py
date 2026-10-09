class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[val[0], val[1], i] for i, val in enumerate(tasks)]
        tasks.sort(key = lambda t: t[0])
        minHeap, result = [], []
        time = tasks[0][0]
        index = 0

        while minHeap or index < len(tasks):
            while index < len(tasks) and time >= tasks[index][0]:
                heapq.heappush(minHeap, [tasks[index][1], tasks[index][2]])
                index +=1

            if minHeap:
                processingTime, i = heapq.heappop(minHeap)
                time += processingTime
                result.append(i)
            else:
                time +=1
        return result
            

