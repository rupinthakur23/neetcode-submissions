class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        task = Counter(tasks)
        maxHeap = [-cnt for cnt in task.values()]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or q:
            time +=1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt = cnt + 1 

                if cnt < 0:
                    q.append([cnt,time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
            

