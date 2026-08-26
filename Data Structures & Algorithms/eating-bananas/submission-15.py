class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right


        while left <= right:
            mid = left + ((right - left)//2)
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours <= h:
                right = mid -1
                result = min(result, mid)
            else:
                left = mid + 1
            
        
        return result
        