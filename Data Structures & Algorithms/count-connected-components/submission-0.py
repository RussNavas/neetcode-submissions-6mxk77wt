class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[ self.parent[p] ]
            p = self.parent[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False # already in the same comp
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        uf = UnionFind(n)
        for a, b in edges:
           if uf.union(a, b):
            res -= 1

        return res