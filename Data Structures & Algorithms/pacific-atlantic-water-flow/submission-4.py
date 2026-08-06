class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # i basically want to see if a cell is lesser than previous ?
        # we want to have 2 sets to store values. one for pac, one for atl.
        # rows, col
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_set = set()
        atlantic_set = set()

        def dfs(r, c, seen, prevHeight):
            if r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < prevHeight or (r, c) in seen:
                return

            seen.add((r, c))
            dfs(r + 1, c, seen, heights[r][c])
            dfs(r - 1, c, seen, heights[r][c])
            dfs(r, c - 1, seen, heights[r][c])
            dfs(r, c + 1, seen, heights[r][c])

        # for the first row now, which is pacific (top) and atlantic (bottom)
        for r in range(ROWS):
            dfs(r, 0, pacific_set, heights[r][0])
            dfs(r, COLS - 1, atlantic_set, heights[r][COLS - 1])

        
        for c in range(COLS):
            dfs(0, c, pacific_set, heights[0][c])
            dfs(ROWS - 1, c, atlantic_set, heights[ROWS - 1][c])


        out = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    out.append([r, c])

        return out