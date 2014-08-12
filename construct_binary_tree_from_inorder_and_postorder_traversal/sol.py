# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.recursive(inorder, postorder)
    def recursive(self, inorder, postorder):
        if not postorder:
            return None
        node = TreeNode(postorder[-1])
        partition = inorder.index(postorder[-1])
        left = self.recursive(inorder[0:partition], postorder[0:partition])
        right = self.recursive(inorder[partition+1:], postorder[partition:-1])
        node.left = left
        node.right = right
        return node
