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
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        current, previous = [], []
        current.append(root)
        while True:
            current, previous = previous, current
            current = []
            clevel = []
            for node in previous:
                clevel.append(node.val)
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
            result.append(clevel)
            if not current:
                break
        return result

lst = [3,9,20,'#','#',15,7]
root = TreeNode.createTree(lst)
print root.serialize()
sol = Solution()
print sol.levelOrder(root)
