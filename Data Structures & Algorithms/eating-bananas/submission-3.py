class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1, max(piles)
        result = right


        while(left <= right):
            totalTime = 0
            mid = left + (right - left) //2

            for banana in piles:
                totalTime += math.ceil(float(banana)/ mid)

            if totalTime <= h:
                result = mid
                right = mid -1
            else:
                left = mid + 1


        return result