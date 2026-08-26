class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result, minHeap = [], []

        for index, task in enumerate(tasks):
            task.append(index)

        tasks.sort(key = lambda t: t[0])

        index, totalTime = 0, tasks[0][0]

        while minHeap or index < len(tasks):
            while index < len(tasks) and totalTime >= tasks[index][0]:
                heapq.heappush(minHeap, [tasks[index][1], tasks[index][2]])
                index +=1
            if not minHeap:
                totalTime = tasks[index][0] 
            else:          
                time, idx =  heapq.heappop(minHeap)
                totalTime += time
                result.append(idx)


        return result





            


