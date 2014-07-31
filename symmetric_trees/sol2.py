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
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        current, previous = [],[]
        current.append(root)
        while True:
            # check if last level is symmetric
            l,r = 0, len(current)-1
            while l <= r:
                if not current[l] and not current[r]:
                    l += 1;r -= 1
                elif current[l] and current[r]:
                    if current[l].val == current[r].val:
                        l+=1;r-=1
                    else:
                        return False
                else:
                    return False
            # build a new level
            current, previous = previous, current
            current = []
            for node in previous:
                if not node:
                    continue
                current.append(node.left)
                current.append(node.right)
            if not any(current):
                break
        return True

lst = [1,2,2,3,4,4,3]
root = TreeNode.createTree(lst)
sol = Solution()
print sol.isSymmetric(root)
