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

