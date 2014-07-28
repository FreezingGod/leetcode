# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        queue = []
        queue.append((root,1))
        while True:
            v, d = queue.pop(0)
            if not v.left and not v.right:
                return d
            if v.left:
                queue.append((v.left, d+1))
            if v.right:
                queue.append((v.right, d+1))
            if not queue:
                break
        return 0

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4
sol = Solution()
print sol.minDepth(n1)
print sol.minDepth(None)
print sol.minDepth(n4)
print sol.minDepth(n3)
print sol.minDepth(n2)
