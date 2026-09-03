class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(maxHeap)

        result = ""
        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt = cnt + 1

            if prev:
                heapq.heappush(maxHeap, [prev[0], prev[1]])
                prev = None
            
            if cnt:
                prev = [cnt, char]
        return result