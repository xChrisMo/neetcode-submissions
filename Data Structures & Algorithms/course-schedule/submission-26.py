class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}

        for i in range(numCourses):
            adj_list[i] = []

        for src, dst in prerequisites:
            adj_list[src].append(dst)

        path = set()
        
        def dfs(i):
            # if in current path, its cyclic
            if i in path:
                return False 

            # if empty, it is True
            if adj_list[i] == []:
                return True 

            # add to the current path
            path.add(i)

            for nei in adj_list[i]:
                if dfs(nei) == False:
                    return False

            path.remove(i)
            adj_list[i] = [] # mark it..
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        