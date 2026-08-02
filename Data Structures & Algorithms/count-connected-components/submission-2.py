class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # have an adjacency list 
        # build an adjacency list from every source to target, every target to source
        # we want to have a uniqueness checker for each connected component
        # so do postorder traversal in the dfs, check if seen, if not, check neighbours
        # in a foor loop, do dfs from 0, if not in visited; += 1
        # this is O(V + E) for time as we explore every vertex and edge, they mignhtny be connected 
        # same thing for the space complexities, we store all edges and all vertices


        adj_list = {}
        
        for i in range(n):
            adj_list[i] = []

        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        seen = set()

        def dfs(i):
            # if seen, return False
            # add to seen
            # check the neighbors, if False, return False
            # return True
            if i in seen:
                return

            # add to seen
            seen.add(i)

            # check the neighbors, if False, return False
            for target in adj_list[i]:
                dfs(target)

        count = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1

        return count