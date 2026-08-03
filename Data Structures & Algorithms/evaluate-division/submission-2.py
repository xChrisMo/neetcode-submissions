from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # equations = [["a","b"],["b","c"],["ab","bc"]], 
        # values = [4.0,1.0,3.25], 
        # queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]

        # if no answer, return -1

        # a/b = 4
        # b/c = 1
        # ab / bc = 3.25

        adj_list = defaultdict(list)
        # map each a -> b, a/b

        for i, value in enumerate(equations):
            src, dst = value
            adj_list[src].append([dst, values[i]])
            adj_list[dst].append([src, 1 / values[i]])

        def dfs(src, dst, seen):
            if src not in adj_list or dst not in adj_list:
                return -1
                
            if src == dst:
                return 1

            seen.add(src)

            for nei, weight in adj_list[src]:
                if nei not in seen:
                    seen.add(nei)
                    val = dfs(nei, dst, seen)
                    if val != -1:
                        return val * weight

            return -1

        return [dfs(q[0], q[1], set()) for q in queries]