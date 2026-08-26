class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ajaencyList = defaultdict(list)
        for i, q in enumerate(equations):
            ajaencyList[q[0]].append([q[1], values[i]])
            ajaencyList[q[1]].append([q[0], 1/values[i]])
        
        q = deque()
        visited = set()

        def bfs(src, target):
            if src not in ajaencyList or target not in ajaencyList:
                return -1
            
            q = deque([[src,1]])
            visited = set()
            visited.add(src)

            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight
                
                for nei, w in ajaencyList[node]:
                    if nei not in visited:
                        q.append([nei, w * weight])
                        visited.add(nei)
            
            return -1


        res = [bfs(q[0], q[1]) for q in queries]
        return res