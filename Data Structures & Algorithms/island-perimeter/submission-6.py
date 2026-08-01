class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # connected horizontally and vertically ONLY 
        # there is exactly one island

        # i want to bruteforce this, 
        # how do you even calculate perimeter please ???
        
        ROWS = len(grid)
        COLS = len(grid[0])
        # visited = set()

        # def dfs(r, c):
        #     # if we nearly hit out of bound, or we hit a 0 from an island, 1, return 1
        #     if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0:
        #         return 1
        #     # if already seen, no count

            

        #     # make sure we dont have duplicates
        #     visited .add((r, c))
        #     # add perim
        #     perim = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        #     return perim

        # # double for loop
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c]:
        #             return dfs(r, c)

        # return 0

        # # this is o(n*m) time as we dobule loop
        # # this is o(n*m) space in the worst case, due to the set ?    
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res += 4

                    if r > 0 and grid[r - 1][c] == 1:
                        res -= 2

                    if c > 0 and grid[r][c - 1] == 1:
                        res -= 2

        return res