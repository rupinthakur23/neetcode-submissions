class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        expenditure = [[capital, profit] for profit, capital in zip(profits, capital)]
        heapq.heapify(expenditure)
        resultSet = []
        totalCapital = w
        projects = 0

        while projects <k:
            while expenditure and totalCapital >= expenditure[0][0]:
                capital, profit = heapq.heappop(expenditure)
                heapq.heappush(resultSet, -profit)

            if resultSet:
                totalCapital += (-heapq.heappop(resultSet))
            projects +=1
        return totalCapital

