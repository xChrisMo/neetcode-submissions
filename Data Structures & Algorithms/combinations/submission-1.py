class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]
        print(arr)

        out = []

        def dfs(i, curSet):
            # base condition
            if len(curSet) == k:
                out.append(curSet[:])
                return 

            if i >= len(arr):
                return
                
            # include i
            curSet.append(arr[i])
            dfs(i + 1, curSet)
            curSet.pop() #backtrack


            #exclude i
            dfs(i + 1, curSet)

        dfs(0, [])
        return out