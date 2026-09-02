class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        
        tasks.sort(key = lambda t: t[0])

        result, heap = [], []

        i, time = 0, tasks[0][0]

        while heap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i +=1
            
            if not heap:
                time = tasks[i][0]
            else:
                processing, index = heapq.heappop(heap)
                result.append(index)
                time += processing
        
        return result