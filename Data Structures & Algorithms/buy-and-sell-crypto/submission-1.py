class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, result = 0, 1, 0

        while(right < len(prices)):
            if(prices[left] > prices[right]):
                left = right
            else:
                result = max(prices[right] - prices[left], result)
            
            right +=1
        
        return result
