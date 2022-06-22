from binarytree import tree, Node

tree1 = tree()
print(tree1)

def count_node(tree: Node):
    # base case
    if tree == None:
        return 0

    # recursive call
    return 1 + count_node(tree.left) + count_node(tree.right)

print(f"Tree1 has node count: {count_node(tree1)}")

# TimeComplexity: O(n)


def count_leaves(tree: Node):
    # base case
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    # recursive call
    return count_leaves(tree.left) + count_leaves(tree.right)

print(f"Tree1 has leaves count: {count_leaves(tree1)}")


def tree_height(tree: Node):
    # base case
    if tree == None:
        return 0
    # recursive call
    return 1+ max(tree_height(tree.left), tree_height(tree.right))

print(f"Tree1 has height: {tree_height(tree1)}")