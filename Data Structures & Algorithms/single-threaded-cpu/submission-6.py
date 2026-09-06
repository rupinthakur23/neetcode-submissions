class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
 
        tasks.sort(key = lambda t:t[0])
        minHeap = []
        time = tasks[0][0]
        index = 0
        result = []

        while minHeap or index < len(tasks):
            while index < len(tasks) and time >= tasks[index][0]:
                heapq.heappush(minHeap, [tasks[index][1], tasks[index][2]])
                index +=1
            
            if not minHeap:
                time = tasks[index][0]
            else:
                procTime, ind = heapq.heappop(minHeap)
                result.append(ind)
                time += procTime
        
        return result