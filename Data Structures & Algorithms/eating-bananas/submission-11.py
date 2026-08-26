class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, result = 1, max(piles), max(piles)

        while left <= right:
            count = 0 
            mid = left + ((right - left)//2)

            for pile in piles:
                count += math.ceil(float(pile) / mid)
            
            if count <= h:
                right = mid -1
                result = min(result, mid)
            else:
                left = mid + 1
        
        return result


            
