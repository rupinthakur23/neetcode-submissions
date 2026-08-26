class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adcencyList = defaultdict(list)

        for uv, uw in edges:
            adcencyList[uv].append(uw)
            adcencyList[uw].append(uv)
        
        visited = set()

        q = deque([(0, 0)])


        while q:
            node, parent= q.popleft()

            if node in visited:
                return False
            
            visited.add(node)

            for nei in adcencyList[node]:
                if nei != parent:
                    q.append((nei, node))
        
        return len(visited) == n  
            

