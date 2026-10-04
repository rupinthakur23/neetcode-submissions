class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right, result = max(weights), sum(weights), float('inf')

        def calculateDays(capacity):
            total, count = 0, 1

            for weight in weights:
                total += weight
                if total > capacity:
                    count +=1
                    total = weight
            return count

        while left <= right:
            mid = left + (right - left)//2

            totalDays = calculateDays(mid)

            if totalDays <= days:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result