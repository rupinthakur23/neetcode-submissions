class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, result = 1, max(piles), max(piles)

        while left <= right:
            mid = left + ((right - left)//2)
            count = 0

            for pile in piles:
                count += math.ceil(pile/mid)
            
            if count <=h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return result
