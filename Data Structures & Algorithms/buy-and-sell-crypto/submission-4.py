class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, profit = prices[0], 0

        for day in range(1,len(prices)):
            if(prices[day] < lowest):
                lowest = prices[day] 
            else:
                profit = max(profit, prices[day] - lowest)
        
        return profit