# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if (p and not q) or (not p and q): return False
        if not p and not q: return True
        le = self.isSameTree(p.left, q.left)
        re = self.isSameTree(p.right, q.right)
        return le and re and (p.val == q.val)
