# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def serialize(self):
        se = []
        node = self
        queue = [node]
        while queue:
            node = queue.pop(0)
            se.append(node.val)
            if node.val == '#':
                continue
            if node.left:
                queue.append(node.left)
            else:
                queue.append(TreeNode('#'))
            if node.right:
                queue.append(node.right)
            else:
                queue.append(TreeNode('#'))
        return se

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        result = []
        def myGenerate(start, end):
            if start == end:
                yield None
            for i in range(start, end):
                for l in myGenerate(start, i):
                    for r in myGenerate(i+1, end):
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        yield node
        for r in myGenerate(1, n+1):
            result.append(r)
        return result

sol = Solution()
print [i.serialize() for i in sol.generateTrees(3)]
