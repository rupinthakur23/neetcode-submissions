class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r
        
        def validSpeed(speed):
            output = 0
            for pile in piles:
                output += math.ceil(pile/speed)
            if(output <= h):
                return True
            else:
                return False


        while(l <=r ):
            mid = (l + r)//2

            if validSpeed(mid):
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1

        return result