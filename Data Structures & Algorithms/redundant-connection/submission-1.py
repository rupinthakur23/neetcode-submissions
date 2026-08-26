class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent, rank = {}, {}
        for i in range(1, len(edges) + 1):
            parent[i] = i 
            rank[i] = 1
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node] 
            
            return node

        def union(node1, node2):
            par1, par2 = find(node1), find(node2)

            if par1 == par2:
                return False
            
            if rank[par1] > rank[par2]:
                parent[par2] = par1
            elif rank[par2] > rank[par1]:
                parent[par1] = par2
            else:
                parent[par1] = par2
                rank[par2] += 1
            return True

        for uv, uw in edges:
            if not union(uv, uw):
                return [uv, uw]