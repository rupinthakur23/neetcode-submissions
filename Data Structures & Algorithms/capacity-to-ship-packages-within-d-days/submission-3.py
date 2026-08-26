class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right, result = max(weights), sum(weights), sum(weights)

        def calculateDays(capacity):
            day, total = 1, 0

            for weight in weights:
                total += weight
                if total > capacity:
                    day +=1
                    total = weight
            
            return day

        while left <= right:
            mid = left + ((right - left)// 2)

            daySpent = calculateDays(mid)

            if daySpent<= days:
                right = mid - 1
                result = min(result, mid)
            else:
                left = mid + 1
        
        return result