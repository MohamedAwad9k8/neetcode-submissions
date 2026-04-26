# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs_depth(root)

    def dfs_depth(self,root: Optional[TreeNode]) -> int:
        #base case
        if not root:
            return 0
        depth = max (self.dfs_depth(root.left), self.dfs_depth(root.right))
        depth += 1
        return depth