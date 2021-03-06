# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        def myInorder(root):
            if not root:
                return
            myInorder(root.left)
            result.append(root.val)
            myInorder(root.right)
        myInorder(root)
        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n3.left = n4
n4.right = n5
sol = Solution()
print sol.inorderTraversal(n1)
