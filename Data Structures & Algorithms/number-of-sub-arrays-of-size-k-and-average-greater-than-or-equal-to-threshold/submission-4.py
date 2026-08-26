class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, result, total = 0, 0, 0

        for right in range(len(arr)):
            total += arr[right]

            if (right - left + 1) == k:
                if (total // (right - left + 1)) >= threshold:
                    result +=1
                total -= arr[left]
                left +=1
        return result
