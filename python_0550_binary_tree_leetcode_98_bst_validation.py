'''
https://leetcode.com/problems/validate-binary-search-tree/
challenging Q for today
'''

'''
BST:
all values in my left sub tree are smaller than the node value
all values in my right sub tree are bigger than the node value
So ->
IMPORTANCE!!! -------------------------------------------------
BST inorder depth first traversal gives you an strictly increasing list
So, we say: BST is an ordered data structure
---------------------------------------------------------------
'''

from binarytree import bst, Node, tree


class Solution:
    def isValidBST(self, root: Node) -> bool:

        l = self.dfs_inorder(root)

        # this is to confirm: l is strictly increasing
        for i in range(len(l)-1):
            if l[i] >= l[i+1]:
                # bst doesn't allow duplicate value. If you see same value, then it is not BST
                return False

        return True


    def dfs_inorder(self, root: Node) -> list:

        if root == None:
            return []

        return self.dfs_inorder(root.left) + [root.val] + self.dfs_inorder(root.right)




# TEST CODE ------------------------------------

s = Solution()

print("TEST 1 BST ----------------------------")

bst = bst()
print(bst)

l = s.dfs_inorder(bst)
print(l) # inorder dfs of bst always gives you a strictly increasing list

isValidBST = s.isValidBST(bst)
print(isValidBST)

print("TEST 2 Normal tree ----------------------------")

tree = tree()
print(tree)

l = s.dfs_inorder(tree)
print(l) # inorder dfs of bst always gives you a strictly increasing list

isValidBST = s.isValidBST(tree)
print(isValidBST)