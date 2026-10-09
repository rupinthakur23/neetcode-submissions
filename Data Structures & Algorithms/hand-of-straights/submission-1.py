class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handCount = Counter(hand)
        minHeap = list(handCount.keys())
        heapq.heapify(minHeap)

        while minHeap:
            minVal = minHeap[0]

            for i in range(minVal, minVal + groupSize):
                if handCount[i] > 0:
                    handCount[i] -= 1
                else:
                    return False
                
                if handCount[i] == 0:
                    print(i)
                    print(minHeap[0])
                    if i != minHeap[0]:
                        return False
                    else:
                        heapq.heappop(minHeap)

        return True