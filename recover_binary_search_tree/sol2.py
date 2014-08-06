# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
    @staticmethod
    def createTree(lst):
        if not lst:
            return None
        root = TreeNode(lst[0])
        queue = [root]
        count = 1
        while queue:
            cn = queue.pop(0)
            if count < len(lst):
                if lst[count] != '#':
                    node = TreeNode(lst[count])
                    cn.left = node
                    queue.append(node)
                count+= 1
                if lst[count] != '#':
                    node = TreeNode(lst[count])
                    cn.right = node
                    queue.append(node)
                count += 1
            else:
                break
        return root
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def serialize(self):
        result = []
        current, previous = [], []
        current.append(self)
        while True:
            current, previous = previous, current
            current = []
            for node in previous:
                if node:
                    result.append(node.val)
                    current.append(node.left)
                    current.append(node.right)
                else:
                    result.append('#')
            if not any(current):
                break
        return result


class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        n1, n2 = None, None
        if not root:
            return root
        p = root
        while p.left:
            p = p.left
        leftmost = p
        p = root
        while p.right:
            p = p.right
        rightmost = p
        n1 = self.findLeft(root, [leftmost])
        n2 = self.findRight(root, [rightmost])
        if n1 and n2:
            n1.val, n2.val = n2.val, n1.val
        return root
    def findLeft(self, root, previous):
        if root.left:
            node = self.findLeft(root.left, previous)
            if node:
                return node
        if root:
            if root.val < previous[0].val:
                return previous[0]
        previous[0] = root
        if root.right:
            node = self.findLeft(root.right, previous)
            if node:
                return node
        return None
    def findRight(self, root, previous):
        if root.right:
            node = self.findRight(root.right, previous)
            if node:
                return node
        if root:
            if root.val > previous[0].val:
                return previous[0]
        previous[0] = root
        if root.left:
            node = self.findRight(root.left, previous)
            if node:
                return node
        return None

sol = Solution()
lst = [2,'#', 1, '#', 3]
root = TreeNode.createTree(lst)
print root.serialize()
root = sol.recoverTree(root)
print root.serialize()
