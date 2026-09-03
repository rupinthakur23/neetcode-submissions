class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, char in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if count!=0:
                heapq.heappush(maxHeap, [count, char])
        result = ""

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            
            if len(result) >1 and result[-1] == result[-2] == char:
                if not maxHeap:
                    return result
                cnt2, char2 = heapq.heappop(maxHeap)

                result += char2
                cnt2+=1
                if cnt2:
                    heapq.heappush(maxHeap, [cnt2, char2])
            else:
                result += char
                cnt+=1
            if cnt:
                heapq.heappush(maxHeap, [cnt, char])
        
        return result


