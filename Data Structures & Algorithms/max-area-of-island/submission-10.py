class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        u go as deep as possible and while doing that , while processing each node, u track the islands
        '''

        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        
        maxArea=0
        if not grid:
            return 0

        def dfs(r,c,visit):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if (r,c) in visit:
                return 0
            if grid[r][c]==0:
                return 0
            visit.add((r,c))
            area=1

            dir=[[0,-1],[0,1],[1,0],[-1,0]]
            for dr,dc in dir:
                nr=r+dr
                nc=c+dc
                area+=dfs(nr,nc,visit)
            return area
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]==1:
                    maxArea=max(maxArea,dfs(r,c,visit))
        return maxArea
