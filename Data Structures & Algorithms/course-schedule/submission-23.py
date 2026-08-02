class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make an adjacency list
        # append course to prereq
        # check if the current node has been seen
        # if its tempty, return true 
        # else check its neighbors 
        # if true; set the current to []
        # rehtn True

        adj_list = {}

        for i in range(numCourses):
            adj_list[i] = []

        for crs, prereq in prerequisites:
            adj_list[crs].append(prereq)
        path = set()

        def dfs(i):
            if i in path:
                # cyclic
                return False

            if adj_list[i] == []:
                return True

            path.add(i)
            for prereq in adj_list[i]:
                if dfs(prereq) == False:
                    return False
            
            adj_list[i] = []
            path.remove(i)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False

        return True