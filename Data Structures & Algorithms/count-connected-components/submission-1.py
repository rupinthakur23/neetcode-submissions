class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjencyList = defaultdict(list)

        for uv, uw in edges:
            adjencyList[uv].append(uw)
            adjencyList[uw].append(uv)
        
        count = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for nextNode in adjencyList[node]:
                dfs(nextNode)
            return True


        for i in range(n):
            if dfs(i):
                count += 1

        return count