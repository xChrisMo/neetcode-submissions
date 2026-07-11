# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # determine if leaf or not
        # if tree, it's parent would point to None
        
        # a bfs might be perfect here
        # 

        # q = deque()
        # q.append(root)

        # if not root: return None

        # while len(q) > 1:
        #     for _ in range(len(q)):
        #         node = q.popleft()

        #         # as long as it has kids
        #         # left child
        #         if node.left:
        #             q.append(node.left)

        #         # left child
        #         if node.right:
        #             q.append(node.right)

        #         # if neither left nor right
        #         if not node.left and not node.right and node.val == target:
        #             q.append(null)

        # inorder traversal to convert list back into binary tree ?? near impossible 
        # def inorder(q):
        #     for val in q:

        # has to be recursive from bottom to top really, so postorder traversal lets us do that

        def dfs(root):
            if not root: return None

            # explore left
            root.left = dfs(root.left)

            # explore right
            root.right = dfs(root.right)

            # we want to check children first before parent, we have explored parents first
            if not root.left and not root.right and root.val == target:
                # explicitly setting it to None
                return None
                # need some way to make this perforate upwards!

            return root 

        return dfs(root)
