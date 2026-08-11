class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}

        for i in range(numCourses):
            adj_list[i] = []
        
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        path = set()

        def dfs(i):
            if i in path:
                return False

            if adj_list[i] == []:
                return True

            path.add(i)

            for pre in adj_list[i]:
                if dfs(pre) == False:
                    return False

            path.remove(i)
            adj_list[i] = []
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False

        return True