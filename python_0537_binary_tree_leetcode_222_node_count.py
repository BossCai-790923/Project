'''
https://leetcode.com/problems/count-complete-tree-nodes/
'''
from typing import Optional

'''
----------------
Analysis
----------------
Case 1) When a complete binary tree is perfect:
its total nodes count equals to 2^h-1
Case 2) When a complete binary tree is not perfect:
Its total nodes count equals to 1 + total nodes count of left sub tree + total nodes count of right sub tree
One of them is perfect, the other is complete
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:

        # Base case
        if root == None:
            return 0

        left_tree_height = self.height(root.left)
        right_tree_height = self.height(root.right)

        if left_tree_height == right_tree_height: # meaning left tree is perfect
            return 1 + 2 ** left_tree_height - 1 + self.countNodes(root.right)
        else:
            return 1 + self.countNodes(root.left) + 2 ** right_tree_height - 1



    def height(self, root):
        if root == None:
            return 0

        height = 0

        while root != None:
            height += 1
            root = root.left

        return height

    # Because this is a complete binary tree, so that I don't need to use the slow recursive algo, I can just walk in one direction -> left branch

# Time Complexity: O(logN) which is much faster than O(N)
'''
2^2 = 4     log4=2
2^10=1024   log1024=10
'''