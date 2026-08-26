class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        minHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(minHeap)

        time = 0
        q = deque()

        while minHeap or q:
            time +=1 

            if not minHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(minHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            
            if q and time == q[0][1]:
                heapq.heappush(minHeap, q.popleft()[0])
        
        return time