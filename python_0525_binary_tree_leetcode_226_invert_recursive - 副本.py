from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:

        # Step 1) base condition
        if root == None:
            return root

        #Step 2) invert left subTree
        root.left = self.invertTree(root.left)

        #Step 3) invert right subTree
        root.right = self.invertTree(root.right)

        #Step 4) invert left subTree and right subTree
        root.left, root.right = root.right, root.left

        #Step 5) return tree
        return root



