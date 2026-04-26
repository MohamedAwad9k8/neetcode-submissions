# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if node has left and has right
        # temp = node.left
        # node.left = node.right
        # node.rught = temp
        # switch_tree(1) -> switch_tree(2) & switch_tree(3)
        # switch_tree(2) -> switch_tree(4) &  switch_tree(5)
        # switch_tree(4) -> base case -> return
        # switch_tree(5) -> base case -> return
        # switch_tree(5) -> does the logic
        self.switch_tree(root)
        return root

    def switch_tree(self, root):
        #base case
        if not root:
            return

        self.switch_tree(root.left)
        self.switch_tree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
