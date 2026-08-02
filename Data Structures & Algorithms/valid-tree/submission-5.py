# class DSU:
#     def __init__(self, n):
#         self.rank = {}
#         self.parent = {}
        
#         for i in range(n):
#             self.rank[i] = 0
#             self.parent[i] = i

#     def find(self, x):
#         p = self.parent[x]

#         while p != self.parent[p]:
#             self.parent[p] = self.parent[self.parent[p]]
#             p = self.parent[p]

#         return p

#     def union(self, n1, n2):
#         p1 = self.find(n1)
#         p2 = self.find(n2)

#         if p1 == p2:
#             return False

#         elif p1 < p2:
#             self.parent[p2] = p1
#             self.rank[p1] += 1

#         elif p2 < p1:
#             self.parent[p1] = p2
#             self.rank[p2] += 1

#         else:
#             self.parent[p1] = p2
#             self.rank[p2] += 1

#         return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dsu = DSU(n)

        # if n != len(edges) + 1: return False

        # for n1, n2 in edges:
        #     if dsu.union(n1, n2) == False:
        #         return False

        # return True
        if len(edges) + 1 != n:
            return False

        adj_list = {}

        for i in range(n):
            adj_list[i] = []
        
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)

        # run a dfs to see if there is a cycle...
        path = set()

        def dfs(i, parent):
            # check if it is a cycle
            if i in path:
                return False

            # add i to the path
            path.add(i)

            # postorderly check of destinations
            for dest in adj_list[i]:
                if dest == parent:
                    continue

                if dfs(dest, i) == False:
                    return False

            # no cycle found
            return True

        if not dfs(0, -1):
            return False

        return len(path) == n
        # i feel like i am missing to take into account the fact that it is undirected.. give clues please