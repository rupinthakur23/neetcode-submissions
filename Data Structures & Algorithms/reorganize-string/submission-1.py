class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-value, key] for key, value in count.items()]
        heapq.heapify(maxHeap)

        result = ""
        prev = None

        while maxHeap or prev:

            if not maxHeap and prev:
                return ""

            cnt, output = heapq.heappop(maxHeap)
            result +=output
            cnt +=1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
 
            if cnt!=0:
                prev = [cnt, output]
        
        return result
