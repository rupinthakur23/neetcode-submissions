class Unionfind:
    def __init__(self, n):
        self.rank, self.parent = {}, {}
        for i in range(len(n)):
            self.rank[i] = 1
            self.parent[i] = i
    
    def find(self, node):
        while node!= self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return

        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.parent[par1] = par2
        else:
            self.parent[par2] = par1
        return 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = Unionfind(accounts)
        emails = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email not in emails:
                    emails[email] = i
                else:
                    uf.union(i, emails[email])
        resultEmails = defaultdict(list)

        for email, index in emails.items():
            ind = uf.find(index)
            resultEmails[ind].append(email)
        
        result = []
        for i, email in resultEmails.items():
            name = accounts[i][0]
            result.append([name] + email)

        return result










