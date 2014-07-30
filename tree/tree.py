class TreeNode:
    @staticmethod
    def createTree(lst):
        if not lst:
            return None
        root = TreeNode(lst[0])
        queue = [root]
        count = 1
        while queue:
            cn = queue.pop()
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
