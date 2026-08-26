class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result, left, total = 0, 0, 0

        for right in range(0, len(arr)):

            if(right - left + 1 > k):
                total -= arr[left]
                left +=1
            
            total += arr[right]
    
            if ((right - left + 1 == k) and (total//k >= threshold)):
                result +=1
        
        return result
