class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, result = 1, max(piles), max(piles)

        while(left <= right):
            output = 0
            mid = left + (right - left)//2

            for banana in piles:
                output += math.ceil(banana/mid)
            
            if output <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return result

                
