class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, result = 1, max(piles), 1

        while(left <= right):
            mid = left + (right - left)//2
            output = 0
            for pile in piles:
                output+= math.ceil(pile/mid)
            
            if output <= h:
                right = mid -1
                result = mid
            else:
                left = mid + 1
        
        return result
