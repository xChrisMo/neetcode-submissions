class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}

        for i in range(numCourses):
            adj_list[i] = []

        for crs, prereq in prerequisites:
            adj_list[crs].append(prereq)

        out = []
        cycle = set()
        visited = set()
        # do a dfs, have a cycle checker

        def dfs(i):
            if i in cycle:
                return False 

            if i in visited:
                return True
                
            cycle.add(i)

            for prereq in adj_list[i]:
                if dfs(prereq) == False:
                    return False

            adj_list[i] = []
            cycle.remove(i)
            visited.add(i)
            out.append(i)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return out