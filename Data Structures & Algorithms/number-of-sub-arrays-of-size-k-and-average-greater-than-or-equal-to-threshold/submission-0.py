class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output = 0
        result = 0
        L = 0

        for R in range(len(arr)):
            output += arr[R]
            if (R - L + 1 == k):
                if ((output / k) >= threshold):
                  result+=1
                output -= arr[L]
                L+=1  
        return result