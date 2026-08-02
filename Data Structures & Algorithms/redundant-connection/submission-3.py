class DSU:
    def __init__(self, n):
        self.components = n
        self.rank = {}
        self.parent = {}

        for i in range(1, n + 1):
            self.rank[i] = 0
            self.parent[i] = i

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1

        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2

        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

        self.components -= 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # basically trying to find the edge that makes it a cycle
        n = len(edges)
        dsu = DSU(n)

        for n1, n2 in edges:
            if dsu.union(n1, n2) == False:
                return [n1, n2]

        