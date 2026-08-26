class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        print(counts)
        maxHeap = [[-val, key] for key, val in counts.items()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][0]
            else:
                cnt, char = heapq.heappop(maxHeap)
                cnt +=1

                if cnt:
                    q.append([time + n, cnt, char])
            
            if q and time == q[0][0]:
                t, cnt, char = q.popleft()
                heapq.heappush(maxHeap, [cnt, char])
        
        return time