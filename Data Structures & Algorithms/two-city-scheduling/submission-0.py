class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        # merge [[1:00, 4:00]] into [[23:00, 3:00], [12:30, 3:00]]
        costs.sort(key=lambda x:x[0] - x[1])

        n = len(costs)
        res = 0

        for i in range(0, n // 2):
            res += costs[i][0]


        for i in range(n // 2, n):
            res += costs[i][1]

        return res