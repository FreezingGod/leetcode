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

# this solution use O(1) space, using threaded tree to do inorder traversal
class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        n1, n2, previous, parent = None, None, None, None
        if not root:
            return None
        current = root
        while current:
            if not current.left:
                if parent and current.val < parent.val:
                    if not n1:
                        n1 = parent
                    n2 = current
                parent = current
                current = current.right
            else:
                previous = current.left
                while previous.right and previous.right != current:
                    previous = previous.right
                if not previous.right:
                    previous.right = current
                    current = current.left
                else:
                    previous.right = None
                    if parent and current.val < parent.val:
                        if not n1:
                            n1 = parent
                        n2 = current
                    parent = current
                    current = current.right
        print n1, n2
        print n1.val, n2.val
        if n1 and n2:
            n1.val, n2.val = n2.val, n1.val
        return root

sol = Solution()
lst = [3,1,2]
root = TreeNode.createTree(lst)
print root.serialize()
root = sol.recoverTree(root)
print root.serialize()
