"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # run an adjacency list
        # make a node of same value basically
        oldTonew = {}

        def dfs(node):
            # check if in
            if node in oldTonew:
                return oldTonew[node]

            # make a copy
            copy = Node(node.val)

            # save inside oldTonew
            oldTonew[node] = copy

            # recursively add neigbors....
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            # return the created copu
            return copy

        return dfs(node) if node else None