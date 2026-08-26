class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, result =  prices[0], 0

        for day in range(1, len(prices)):
            if(prices[day] < lowest):
                lowest = prices[day]
            else:
                result = max(result, prices[day] - lowest)
        
        return result