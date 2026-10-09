class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}

        for i in range(num_courses):
            adj_list[i] = []

        for course, preq in prerequisites:
            adj_list[course].append(preq)

        visited = set()
        path = set()

        def dfs(crs):
            if crs in visited:
                return True

            if crs in path:
                return False

            if adj_list[crs] == '[]':
                return True

            path.add(crs)
            for nei in adj_list[crs]:
                if dfs(nei) == False:
                    return False

            path.remove(crs)
            visited.add(crs)
            return True

        for i in range(num_courses):
            if dfs(i) == False:
                return False

        return True