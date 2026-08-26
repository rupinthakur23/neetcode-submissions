class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjencyList = defaultdict(list)
        for uv, uw in edges:
            adjencyList[uv].append(uw)
            adjencyList[uw].append(uv)
        
        visited = set()

        q = deque()
        q.append((0, -1))

        while q:
            node, parent = q.popleft()
            if node in visited:
                return False
            
            visited.add(node)

            for nextNode in adjencyList[node]:
                if nextNode != parent:
                    q.append((nextNode, node))

        return True if len(visited) == n else False
                    

