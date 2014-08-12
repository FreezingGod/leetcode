# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# this solution got time limit exceeded
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
        if not inorder:
            return None
        node = TreeNode(inorder[0])
        partition = preorder.index(inorder[0])
        preorderl = preorder[0:partition]
        preorderr = preorder[partition+1:]
        inorderl, inorderr = [], []
        for i in inorder[1:]:
            if i in preorderl:
                inorderl.append(i)
            else:
                inorderr.append(i)
        left = self.recursive(preorderl, inorderl)
        right = self.recursive(preorderr, inorderr)
        node.left = left
        node.right = right
        return node
