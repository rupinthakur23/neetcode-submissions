class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        prev = None
        result = ''
            
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt = 1 + cnt

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt:
                prev = [cnt, char]
        
        return result
            




