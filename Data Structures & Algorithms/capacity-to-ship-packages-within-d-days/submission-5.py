class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = right

        def calculateDays(capacity):
            total, count = 0, 1

            for weight in weights:
                total += weight
                if total > capacity:
                    count += 1
                    total = weight
            
            return count

        while left <= right:
            mid = left + (right - left)//2

            calculatedDays = calculateDays(mid)
            print(mid)
            print(calculatedDays)
            
            if calculatedDays <= days:
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid +1
        
        return result