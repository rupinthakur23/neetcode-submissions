class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, result = 1, max(piles), max(piles)

        while left <= right:
            time = 0
            mid = left + ((right - left)//2)

            for pile in piles:
                time += math.ceil(pile/mid)
            
            if time <= h:
                right = mid -1
                result = min(mid,result)
            else:
                left = mid + 1
        
        return result
                