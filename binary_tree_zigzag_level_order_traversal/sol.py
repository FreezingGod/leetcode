# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        result = []
        current, previous = [], []
        if not root:
            return []
        current.append(root)
        normalOrder = True
        while True:
            previous = current
            current = []
            result.append([])
            if normalOrder:
                normalOrder = False
                for n in previous:
                    result[-1].append(n.val)
            else:
                normalOrder = True
                for i in range(len(previous)-1,-1,-1):
                    result[-1].append(previous[i].val)
            for n in previous:
                if n.left:
                    current.append(n.left)
                if n.right:
                    current.append(n.right)
            if not current:
                break
        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n1.left = n2
sol = Solution()
print sol.zigzagLevelOrder(n1)
