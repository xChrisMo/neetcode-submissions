"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # n by n
        # return Node
        # if 1s, True
        # if 0s, False
        # isLeaf, Leaf == True, not a Leaf == False

        # break this into 4s
        # toplelft to middle, if they are the same, 

        def dfs(n, r, c):
            isLeaf = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        isLeaf = False
                        break
            if isLeaf:
                return Node(grid[r][c], True) # not a leaf, it is pure !

            # for nonleaf nodes now
            n = n // 2
            # we get the topleft
            topLeft = dfs(n, r, c)
            # we get the topRight
            topRight = dfs(n, r, c + n)
            # we get the bottomLeft
            bottomLeft = dfs(n, r + n, c)
            # we get the bottomRight
            bottomRight = dfs(n, r + n, c + n)
            
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)