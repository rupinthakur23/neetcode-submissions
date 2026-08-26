class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right, result = max(weights), sum(weights), sum(weights)
        
        def calculateBoats(mid):
            day, cap = 1, mid

            for weight in weights:
                if cap - weight < 0:
                    day +=1
                    if day > days:
                        return False
                    cap = mid
                cap -= weight
            
            return True



        while(left <= right):
            mid = left + (right - left)//2

            if calculateBoats(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return result