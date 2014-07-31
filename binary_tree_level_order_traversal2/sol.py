# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root:
            return []
        result = []
        current, previous = [], []
        current.append(root)
        while True:
            current, previous = previous, current
            current = []
            cl = []
            for node in previous:
                cl.append(node.val)
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
            result.append(cl)
            if not current:
                break
        result.reverse()
        return result
