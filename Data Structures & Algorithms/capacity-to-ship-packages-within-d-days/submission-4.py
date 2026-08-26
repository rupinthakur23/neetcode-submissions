class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = right

        def calaculateDays(mid):
            count, total  = 1, 0

            for weight in weights:
                total += weight

                if total > mid:
                    count +=1
                    total = weight
            
            return count

        while left <= right:
            mid = left + ((right - left)//2)

            day = calaculateDays(mid)

            if day <= days:
                right = mid - 1
                result = min(result, mid)
            else:
                left = mid + 1
        return result