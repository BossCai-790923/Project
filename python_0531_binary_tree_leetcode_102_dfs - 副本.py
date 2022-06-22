'''
https://leetcode.com/problems/binary-tree-level-order-traversal
'''
from typing import Optional, List
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #base case
        if root == None:
            return []

        # Preparation: enqueue the root to the queue
        q = Queue()
        q.put(root)

        # Create a result_list, which I will return at the last step
        result_list = []

        # repeat as long as the queue is not empty
        while q.qsize() > 0:


            node_count = q.qsize()

            level_list = []

            for _ in range(node_count):

                node = q.get()
                level_list.append(node.val)

                if node.left != None:
                    q.put(node.left)

                if node.right != None:
                    q.put(node.right)

            # append the level_list to the result_list
            result_list.append(level_list)









        return result_list