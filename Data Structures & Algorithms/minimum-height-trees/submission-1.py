class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        edgeMap = defaultdict(list)

        for uv, uw in edges:
            edgeMap[uv].append(uw)
            edgeMap[uw].append(uv)
        
        leaves = deque()
        nodeCount = {}

        for i, val in edgeMap.items():
            if len(val) == 1:
                leaves.append(i)
            nodeCount[i] = len(val)
    
        while leaves:
            if n<=2:
                return list(leaves)
            
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n-=1

                for nei in edgeMap[node]:
                    nodeCount[nei] -=1
                    
                    if nodeCount[nei] == 1:
                        leaves.append(nei)

        return []
