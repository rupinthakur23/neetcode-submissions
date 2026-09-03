class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = []

        for count in counts.values():
            heapq.heappush(maxHeap,-count)

        time = 0
        queue = deque()

        while maxHeap or queue:
            time +=1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt +=1

                if cnt:
                    queue.append([cnt, time + n])
            
            if queue and time == queue[0][1]:
                 heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time
