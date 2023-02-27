# implement a function for finding the maximum and minimum value in a BSTSynthesizing 7/10 solutions

=======

# implement a function for finding the maximum and minimum value in a BST
# implement a function for finding the successor and predecessor of a node in a BST
# implement a function for calculating the height of a BST
# implement a function for calculating the size of a BST
# implement a function for checking if a BST is empty

=======

# implement a function for finding the maximum and minimum value in a BST.
# 
# def find_min(tree):
#     if tree.left is None:
#         return tree.value
#     return find_min(tree.left)
# 
# def find_max(tree):
#     if tree.right is None:
#         return tree.value
#     return find_max(tree.right)
# 
# =======
# implement a function for finding the successor and predecessor of a node in a BST.
# 
# def successor(tree, node):
#     if node.right is not None:
#         return find_min(node.right)
#     else:
#         succ = None
#         while tree is not None:
#             if node.value < tree.value:
#                 succ = tree
#                 tree = tree.left
#             elif node.value > tree.value:
#                 tree = tree.right
#             else:
#                 break
#         return succ
# 
# def predecessor(tree, node):
#     if node.left is not None:
#         return find_max(node.left)
#     else:
#         pred = None
#         while tree is not None:
#             if node.value < tree.value:
#                 tree = tree.left
#             elif node.value > tree.value:
#                 pred = tree
#                 tree = tree.right
#             else:
#                 break
#         return pred
# 
# =======
# implement a function for finding the height of a BST.
# 
# def get_height(tree):
#     if tree is None:
#         return -1
#     return 1 + max(get_height(tree.left), get_height(tree.right))
# 
# =======
# implement a function for finding the size of a BST.
# 
# def get_size(tree):
#     if tree is None:
#         return 0
#     return 1 + get_size(tree.left) + get_size(tree.right)
# 
# =======
# implement a function for checking if a BST is empty.
# 
# def is_empty(tree):
#     return tree is None
# 
# =======
# implement a function for inserting a new node into a BST.
# 
# def insert(tree, value):
#     if tree is None:
#         return BST(value)
#     if value < tree.value:
#         tree.left = insert(tree.left, value)
#     else:
#         tree.right = insert(tree.right, value)
#     return tree
# 
# =======
#

=======

# implement a function for finding the maximum and minimum value in a BST
# 
# =======
# 
# # implement a function for finding the successor and predecessor of a given node in a BST
# 
# =======
# 
# # implement a function for calculating the height of a BST
# 
# =======
# 
# # implement a function for calculating the size of a BST
# 
# =======
# 
# # implement a function for checking if a BST is empty
# 
# =======
# 
# # implement a function for checking if a BST is a binary search tree
# 
# =======
# 
# # implement a function for checking if a BST is balanced
# 
# =======
# 
# # implement a function for printing the values of a BST in order
# 
# =======
# 
# # implement a function for printing the values of a BST in pre-order
# 
# =======
# 
# # implement a function for printing the values of a BST in post-order
# 
# =======
# 
# # implement a function for printing the values of a BST in level-order
# 
# =======
# 
# # implement a function for inserting a value into a BST
# 
# =======
# 
# # implement a function for removing a value from a BST
# 
# =======
# 
# # implement a function for checking if a value is contained in a BST
# 
# =======
# 
# # implement a function for finding the max value in a BST
# 
# =======
# 
# # implement a function for finding the min value in a BST
# 
# =======
# 
# # implement a function for finding the successor of a given node in a BST
# 
# =======
# 
# # implement a function for finding the predecessor of a given node in a BST
# 
# =======
# 
# # implement a function for calculating the height of a BST
# 
# =======
# 
# # implement a function for calculating the size of a BST
# 
# =======
# 
# # implement a function for checking if a BST is empty
# 
# =======
# 
# # implement a function for checking if a BST is a binary search tree
# 
# =======
# 
# # implement a function for checking if a BST is balanced
# 
# =======
# 
# # implement a function for printing the values of a BST in order
#

=======

# implement a function for finding the maximum and minimum value in a BST
# 
# =======
# implement a function for finding the successor and predecessor of a node in a BST
# 
# =======
# Implement a function for calculating the height of a BST
# 
# =======
# Implement a function for calculating the size of a BST
# 
# =======
# Implement a function for checking if a BST is empty
# 
# =======
# Implement a function for inserting a node into a BST
# 
# =======
# Implement a function for checking if a BST contains a node with a given value
# 
# =======
# Implement a function for removing a node from a BST
# 
# =======
# Implement a function for finding the successor of a node in a BST
# 
# =======
# Implement a function for finding the predecessor of a node in a BST
# 
# =======
# Implement a function for calculating the height of a BST
# 
# =======
# Implement a function for calculating the size of a BST
# 
# =======
# Implement a function for checking if a BST is empty
# 
# =======
# Implement a function for inserting a node into a BST
# 
# =======
# Implement a function for checking if a BST contains a node with a given value
# 
# =======
# Implement a function for removing a node from a BST
# 
# =======
# Implement a function for finding the successor of a node in a BST
# 
# =======
# Implement a function for finding the predecessor of a node in a BST
# 
# =======
# Implement a function for calculating the height of a BST
# 
# =======
# Implement a function for calculating the size of a BST
# 
# =======
# Implement a function for checking if a BST is empty
# 
# =======
# Implement a function for inserting a node into a BST
# 
# =======
# Implement a function for checking if a BST contains a node with a given value
# 
# =======
# Implement a function for removing a node from a BST
# 
# =======
# Implement a function for finding the successor of a node in a BST
# 
# =======
# Implement a function for finding the predecessor of a node in a BST
# 
# =======
# Implement a function for calculating the height of a BST
# 
# =======
# Implement a function for calculating the size of a BST
#

=======

# implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have the following signature:
# def find_min_max(root):
#     # your code here
# 
# =======
# 
# # implement a function for finding the maximum and minimum value in a BST. The function should have

=======

# implement a function for finding the maximum and minimum value in a BST. The function should return a list with the minimum value at index 0 and the maximum value at index 1.
# 
# =======
# 
# # implement a function for finding the successor and predecessor of a given node in a BST. The function should return a list with the predecessor at index 0 and the successor at index 1. If the predecessor or successor does not exist, then return None for that index.
# # 
# # For example, the successor of the node with value 9 in the following BST is the node with value 12, and the predecessor is the node with value 10.
# #       10
# #      /  \
# #     5    12
# #    / \   / \
# #   2   9 11  15
# #  / \
# # 1   3
# 
# 
# # implement a function for finding the height of a BST. The height of a BST is the number of edges between the tree's root and its furthest leaf. For example, the height of the following tree is 3:
# #       10
# #      /  \
# #     5    12
# #    / \   / \
# #   2   9 11  15
# #  / \
# # 1   3
# 
# =======
# 
# # implement a function for finding the size of a BST. The size of a BST is the total number of nodes in the tree. For example, the size of the following tree is 8:
# #       10
# #      /  \
# #     5    12
# #    / \   / \
# #   2   9 11  15
# #  / \
# # 1   3
# 
# =======
# 
# # implement a function for checking whether or not a BST is empty. The function should return a boolean value.
# 
# =======
# 
# # implement a function for inserting a new value into a BST. The function should not return anything.
# 
# =======
# 
# # implement a function for checking whether or not a BST contains a value. The function should return a boolean value.
# 
# =======
# 
# # implement a function for removing a value from

=======

# implement a function for finding the maximum and minimum value in a BST
#
