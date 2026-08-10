class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        cache = {}
        # cache[(r, c)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]

            if r == ROWS - 1 and c == COLS - 1:
                cache[(r, c)] = 1
                return cache[(r, c)]

            if r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1:
                cache[(r, c)] = 0
                return cache[(r, c)]

            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]

        return dfs(0, 0)