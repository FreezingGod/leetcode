# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmetricTrees(root.left, root.right)
    def isSymmetricTrees(self, node1, node2):
        if not node1 and not node2:
            return True
        if (node1 and not node2) or (not node1 and node2):
            return False
        return (node1.val == node2.val) and self.isSymmetricTrees(node1.left, node2.right) and self.isSymmetricTrees(node1.right, node2.left)
