# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root: return
        lastNode = root
        l = root.left
        r = root.right
        lastNode = self.myFlatten(l, lastNode)
        lastNode = self.myFlatten(r, lastNode)
        lastNode.left = None
        lastNode.right = None
    def myFlatten(self, root, lastNode):
        if not root:
            return lastNode
        l = root.left
        r = root.right
        root.left = None
        root.right = None
        lastNode.left = None
        lastNode.right = root
        lastNode = root
        if l:
            lastNode = self.myFlatten(l, lastNode)
        if r:
            lastNode = self.myFlatten(r, lastNode)
        return lastNode


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n1.left = n2
n1.right = n5
n2.left = n3
n2.right = n4
n5.right = n6
sol = Solution()
sol.flatten(n1)
#print n1.right.val
#print n2.right.val
#print n3.right.val
#print n4.right.val
#print n5.right.val
#print n6.right.val
