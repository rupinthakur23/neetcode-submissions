class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        result = right
        def isCap(cap):
            time, currentCap = 1, cap
            for w in weights:
                if(currentCap - w < 0):
                    time +=1
                    if(time > days):
                        return False
                    currentCap = cap
                
                currentCap -=w
            
            return True

        while(left <= right):
            mid = (left + right)// 2
            if(isCap(mid)):
                result = min(mid, result)
                right =mid - 1
            else:
                left = mid + 1
        
        return result


