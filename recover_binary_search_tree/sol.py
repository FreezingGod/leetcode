# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# this solution use O(n) space, not optimal
class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        lst = self.preOrder(root)
        n1, n2 = None, None
        for i in range(len(lst)-1):
            if lst[i].val > lst[i+1].val:
                if not n1:
                    n1 = lst[i]
                n2 = lst[i+1]
        n1.val, n2.val = n2.val, n1.val
        return root
    def preOrder(self, root):
        result = []
        def run(root):
            if not root:
                return
            if not root.left and not root.right:
                result.append(root)
            else:
                run(root.left)
                result.append(root)
                run(root.right)
        run(root)
        return result
