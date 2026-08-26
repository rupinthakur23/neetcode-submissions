class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = [[-val, key] for key, val in counts.items()]
        heapq.heapify(maxHeap)
        result = ""
        prev = None


        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)

            cnt+=1
            result += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt and not maxHeap:
                return ""
        
            if cnt:
                prev = [cnt, char]
            print(result)
        
        return result

        