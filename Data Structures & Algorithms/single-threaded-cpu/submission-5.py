class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, task in enumerate(tasks):
            task.append(index)
        tasks.sort(key = lambda t: t[0])
                
        heap = []
        index = 0
        result = []
        time = tasks[0][0]

        while heap or index < len(tasks):
            while index < len(tasks) and time >= tasks[index][0]:
                heapq.heappush(heap, [tasks[index][1], tasks[index][2]])
                index +=1
            
            if heap:
                processing, ind = heapq.heappop(heap)
                time += processing
                result.append(ind)
            else:
                time = tasks[index][0]
        
        return result