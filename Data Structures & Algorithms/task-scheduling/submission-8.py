class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = Counter(tasks)
        queue = deque()
        maxHeap = [-x for x in taskMap.values()]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or queue:
            time +=1

            if maxHeap:
                cnt = -heapq.heappop(maxHeap)
                cnt = cnt - 1
                if cnt > 0:
                    queue.append([time + n, cnt])

            if queue and not maxHeap:
                time == queue[0][0]
            
            if queue and time == queue[0][0]:
                heapq.heappush(maxHeap, -queue.popleft()[1])

        return time
