from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:

        # Base Condition
        if root == None:
            return root


        # Preparation
        # Create a queue, enqueue root
        queue = Queue()
        queue.put(root)

        # As long as the queue is not empty
        while queue.qsize() > 0:

            # dequeue
            node = queue.get()
            node.left, node.right = node.right, node.left

            # if left child is not None, then enqueue
            if node.left != None:
                queue.put(node.left)

            # if right child is not None, then enqueue
            if node.right != None:
                queue.put(node.right)