class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minDay, profit = prices[0], 0

        for r in range(1, len(prices)):
            if prices[r] < minDay:
                minDay = prices[r]
            else:
                profit = max(profit, prices[r] - minDay)
        
        return profit
