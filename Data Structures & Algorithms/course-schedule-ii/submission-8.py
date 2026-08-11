class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = set()
        visited = set()
        out = []   

        adj_list = {}
        
        for i in range(numCourses):
            adj_list[i] = []

        for crs, prereq in prerequisites:
            adj_list[crs].append(prereq)
        
        def dfs(i):
            if i in path:
                return False

            if i in visited:
                return True

            path.add(i)

            for prereq in adj_list[i]:
                if dfs(prereq) == False:
                    return False

            path.remove(i)
            visited.add(i)
            out.append(i)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return out