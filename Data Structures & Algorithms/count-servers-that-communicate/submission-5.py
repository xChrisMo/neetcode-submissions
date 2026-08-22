class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # so recurse through all rows
        if not grid: return 0

        row_set = defaultdict(int)
        col_set = defaultdict(int)
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_set[r] += 1
                    col_set[c] += 1

        total = 0
        for r in row_set:
            for c in col_set:
                if grid[r][c] == 1:
                    if row_set[r] > 1 or  col_set[c] > 1:
                        total += 1

        return total