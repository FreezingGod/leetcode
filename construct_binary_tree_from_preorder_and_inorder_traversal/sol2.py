# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# this solution got memory limit exceeded
# inorder: left, mid, right
# preorder: mid, left, right
# postorder: left, right, mide
# level order: you know it
# this solution take preorder as inorder and inorder as level order
class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.recursive(preorder, inorder)
    def recursive(self, preorder, inorder):
        if not preorder:
            return None
        s = set(preorder)
        root = 0
        for i in range(len(inorder)):
            if inorder[i] in s:
                root = i
                break
        node = TreeNode(inorder[root])
        partition = preorder.index(inorder[root])
        preorderl = preorder[0:partition]
        preorderr = preorder[partition+1:]
        left = self.recursive(preorderl, inorder[root+1:])
        right = self.recursive(preorderr, inorder[root+1:])
        node.left = left
        node.right = right
        return node
