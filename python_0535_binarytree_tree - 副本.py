
'''
--------------------------
install binarytree module
--------------------------
mouse hover 'binarytree', click 'Install package binarytree'
wait till progress bar disappears at the bottom of pycharm
'''



print("---------------------------------")
print("build tree solution 1: use Node class")
print("---------------------------------")



from binarytree import Node

root = Node(0)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root)


print("---------------------------------")
print("build tree solution 2: use tree function")
print("---------------------------------")



from binarytree import tree

tree1 = tree()
print(tree1)
print(type(tree1))
print(tree1.values)
print(type(tree1.values))

'''
IMPORTANCE!!! -------------------------------------
1) Node class defined in the binarytree module, is the same as what we defined in 0441 / 0530
2) tree() function helps generate a random tree, so that we don't need to take trouble to define a tree ourselves.
---------------------------------------------------
'''
print("-" * 20)

tree2 = tree(4)
print(tree2)
print(tree2.values)
print("-" * 20)

tree3 = tree(4, True) # True means: let the tree be a perfect binary tree
print(tree3)
print(tree3.values)
print("-" * 20)

'''
IMPORTANCE!!! -------------------------------------
for a perfect binary tree:
level No.       Node Count for level        Node Count Total
#1              2^0=1                       1
#2              2^1=2                       1+2=3
#3              2^2=4                       1+2+4=7
...
#h              2^(h-1)                     2^h-1
Summary:
Total node count for a perfect binary tree (height=h) is: 2^h-1
------------------------------------------------
'''

tree4 = tree(4, False, True) # 2nd True means: let's use letter as node value, instead of int
print(tree4)
print(tree4.values)
print("-" * 20)




print("---------------------------------")
print("build tree solution 2: use build function")
print("---------------------------------")

from binarytree import build
nodes = [3, 6, 8, 2, 11, 13, 20, 4, 8]

tree5 = build(nodes)
print(tree5)

print(f"Is tree5 a complete binary tree? {tree5.is_complete}")

'''
IMPORTANCE!!! -------------------------------------
For complete binary tree, if it is not perfect: 
Then its left sub tree and right sub tree are 1 perfect and 1 complete
------------------------------------------------
'''