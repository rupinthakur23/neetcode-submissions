class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = []
        for char, cnt in counts.items():
            heapq.heappush(maxHeap, [-cnt, char])
        
        prev = None
        result = ''

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt +=1

            if prev:
                heapq.heappush(maxHeap, [prev[0], prev[1]])
                prev = None

            if cnt and not prev:
                prev = [cnt, char]
        
        return result
