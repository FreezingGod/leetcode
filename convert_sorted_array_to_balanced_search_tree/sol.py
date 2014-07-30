# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.arrayToTree(num)
    def arrayToTree(self, num):
        if not num:
            return None
        middle = len(num)/2
        node = TreeNode(num[middle])
        left = self.arrayToTree(num[:middle])
        right = self.arrayToTree(num[middle+1:])
        node.left = left
        node.right = right
        return node
