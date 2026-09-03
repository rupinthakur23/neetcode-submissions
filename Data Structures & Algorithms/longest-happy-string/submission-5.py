class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = [[cnt, char] for cnt, char in [[a, 'a'], [b, 'b'], [c, 'c']]]
        maxHeap = []
        for cnt, char in counts:
            if cnt:
                heapq.heappush(maxHeap, [-cnt, char])

        result = ""

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)

            if len(result) > 1 and result[-1] == result[-2] == char:
                if maxHeap:
                    cnt2, char2 = heapq.heappop(maxHeap)
                    result += char2
                    cnt2 +=1
                    if cnt2:
                        heapq.heappush(maxHeap, [cnt2, char2])
                else:
                    return result
            
            else:
                result += char
                cnt +=1
            
            if cnt:
                heapq.heappush(maxHeap, [cnt, char])
            
        return result
            
        

