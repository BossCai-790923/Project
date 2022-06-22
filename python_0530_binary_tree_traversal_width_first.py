
from queue import Queue

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def width_first_traversal(root):

    # base case
    if root == None:
        return

    # Preparation
    # create a queue, enqueue root
    queue = Queue()
    queue.put(root)

    while queue.qsize() > 0:

        # Step 1) dequeue
        node = queue.get()

        # Step 2) visit the node
        print(node.val, end = ' ')

        # Step 3) enqueue left child
        if node.left != None:
            queue.put(node.left)

        # Step 4) enqueue right child
        if node.right != None:
            queue.put(node.right)




# Driver code

# level 0 ----------------
root = Node(20)

# level 1 ----------------
root.left = Node(16)
root.right = Node(25)

# level 2 ----------------
root.left.left = Node(6)
root.left.right = Node(17)

root.right.left = Node(21)
root.right.right = Node(29)

# level 3 ----------------
root.left.left.left = Node(0)
root.left.left.right = Node(7)

root.right.right.left = Node(28)
root.right.right.right = Node(51)

# level 4 ----------------
root.right.right.right.left = Node(46)



# Main program -----------------------------
width_first_traversal(root)