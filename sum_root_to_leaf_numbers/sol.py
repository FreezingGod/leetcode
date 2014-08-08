# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        s = 0
        for i in self.traverse(root, 0):
            s += i
        return s
    def traverse(self, root, value=0):
        if not root:
            return
        newval = value*10 + root.val
        if not root.left and not root.right:
            yield newval
        if root.left:
            for i in self.traverse(root.left, newval):
                yield i
        if root.right:
            for i in self.traverse(root.right, newval):
                yield i
