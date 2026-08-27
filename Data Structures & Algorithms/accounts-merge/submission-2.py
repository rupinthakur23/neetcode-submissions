class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)

        if par1 == par2:
            return False
        
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.par[par1] = par2
        else:
            self.par[par1] = par2
            self.rank[par2] +=1
    
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailMap = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e not in emailMap:
                    emailMap[e] = i
                else:
                    uf.union(i, emailMap[e])
        
        emailMerge = defaultdict(list)

        for e, i in emailMap.items():
            leader = uf.find(i)
            emailMerge[leader].append(e)
        
        res = []

        for i, val in emailMerge.items():
            name = accounts[i][0]
            res.append([name] + sorted(val))
        
        return res
        
























