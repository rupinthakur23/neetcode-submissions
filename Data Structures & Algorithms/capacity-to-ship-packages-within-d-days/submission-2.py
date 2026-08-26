class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right, result = max(weights), sum(weights), sum(weights)

        def countDays(capacity):
            result, total = 1, 0
            for weight in weights:
                total += weight
                
                if total > capacity:
                    result += 1
                    total = weight
            
            return result


        while left <= right:
            mid = left + ((right - left)//2)

            day = countDays(mid)

            if day <= days:
                right = mid - 1
                result = min(mid, result)
            else:
                left = mid + 1
        
        return result
        