class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buyDay = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[buyDay]:
                buyDay = r
            else:
                result = max(result, prices[r] - prices[buyDay])
        
        return result