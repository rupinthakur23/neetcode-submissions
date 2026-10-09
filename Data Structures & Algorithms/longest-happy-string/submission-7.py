class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        countMap = {'a':a, 'b':b, 'c': c}
        maxHeap = []
        for key, val in countMap.items():
            if val > 0:
                maxHeap.append([-val, key])
        
        heapq.heapify(maxHeap)
        result = ''

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)

            if len(result) > 1 and char == result[-1] and char == result[-2]:
                if maxHeap:
                    newCount, newChar = heapq.heappop(maxHeap)
                    result += newChar
                    newCount +=1
                    if newCount:
                        heapq.heappush(maxHeap, [newCount, newChar])
                else:
                    return result
            else:
                result += char
                cnt +=1
            if cnt:
                heapq.heappush(maxHeap, [cnt, char])
        return result
