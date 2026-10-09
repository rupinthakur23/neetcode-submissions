class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = [[-val, key] for key, val in counts.items()]
        heapq.heapify(maxHeap)
        prev = []
        result = ''

        while maxHeap or prev:
            if prev and not maxHeap:
                return ''
            
            cnt,char = heapq.heappop(maxHeap)

            result += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
                
            cnt = cnt + 1

            if cnt:
                prev = [cnt, char]
    
        return result


