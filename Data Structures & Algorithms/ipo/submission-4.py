class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[cap, prof] for prof, cap in zip(profits, capital)]
        heapq.heapify(projects)
        profitHeap = []

        profit = w

        for _ in range(k):
            while projects and projects[0][0] <= profit:
                heapq.heappush(profitHeap, -heapq.heappop(projects)[1])
            
            if not profitHeap:
                return profit
            
            profit += -heapq.heappop(profitHeap)
        
        return profit
            



