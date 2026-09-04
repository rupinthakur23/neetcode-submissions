class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, result = 1, max(piles), float('inf')

        while left <= right:
            mid = left + (right - left)//2

            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/mid)
            
            if totalHours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return result

