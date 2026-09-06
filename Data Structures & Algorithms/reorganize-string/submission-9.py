class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxheap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(maxheap)
        result, prev = '', None

        while maxheap or prev:
            if prev and not maxheap:
                return ""
            
            cnt, char = heapq.heappop(maxheap)
            result += char
            cnt = cnt + 1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            
            if cnt:
                prev = [cnt, char]
        
        return result