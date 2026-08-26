class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, v in enumerate(tasks):
            v.append(i)
        
        tasks.sort(key = lambda t: t[0])

        result, minHeap = [], []
        index, time = 0, tasks[0][0]

        while minHeap or index < len(tasks):
            while index < len(tasks) and time >= tasks[index][0]:
                heapq.heappush(minHeap, [tasks[index][1], tasks[index][2]])
                index +=1
                
            if not minHeap:
                time = tasks[index][0]
            else:
                procTime, idx = heapq.heappop(minHeap)
                result.append(idx)
                time += procTime
        return result