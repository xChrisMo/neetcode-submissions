class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = []

        adj_list = {}

        for i in range(numCourses):
            adj_list[i] = []

        for crs, prereq in prerequisites:
            adj_list[crs].append(prereq)

        seen = set()
        path = set()

        def dfs(i):
            if i in path:
                return False

            if i in seen:
                return True

            path.add(i)

            for nei in adj_list[i]:
                if dfs(nei) == False:
                    return False

            path.remove(i)
            seen.add(i)
            out.append(i)

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return out