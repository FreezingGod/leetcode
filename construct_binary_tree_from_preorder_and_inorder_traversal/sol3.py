# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.recursive(preorder, inorder)
    def recursive(self, preorder, inorder):
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        partition = inorder.index(preorder[0])
        left = self.recursive(preorder[1:1+partition], inorder[0:partition])
        right = self.recursive(preorder[1+partition:], inorder[partition+1:])
        node.left = left
        node.right = right
        return node
