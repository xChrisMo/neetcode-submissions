from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # so spread from 0 OUT
        # modify only inf or -inf
        
        # the grid can only be traversed up, down, left, or right.
        
        # get all the sources

        # dimenstions

        # row, col, use a queue, add sources to the queue
        # modify the grid

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        q = deque()


        # note all starts
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

    
        # do a bfs
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))

        