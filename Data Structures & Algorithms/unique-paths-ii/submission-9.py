class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0

        # cache = {}
        # cache[(r, c)]

        # def dfs(r, c):
        #     if (r, c) in cache:
        #         return cache[(r, c)]

        #     if r == ROWS - 1 and c == COLS - 1:
        #         cache[(r, c)] = 1
        #         return cache[(r, c)]

        #     if r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1:
        #         cache[(r, c)] = 0
        #         return cache[(r, c)]

        #     cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return cache[(r, c)]

        # return dfs(0, 0)

        dp = [[0] * COLS for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1] = 1
        
        for r in range(ROWS - 2, -1, -1):
            if obstacleGrid[r][COLS - 1] == 1:
                dp[r][COLS - 1] = 0
            else:
                dp[r][COLS - 1] = dp[r + 1][COLS - 1]

        for c in range(COLS - 2, -1, -1):
            if obstacleGrid[ROWS - 1][c] == 1:
                dp[ROWS - 1][c] = 0
            else:
                dp[ROWS - 1][c] = dp[ROWS - 1][c + 1]

        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS - 2, -1, -1):
                if obstacleGrid[r][c] != 1:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1] 

        return dp[0][0]