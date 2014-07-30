# Definition for a  binary tree node
import sys
sys.setrecursionlimit(10000)
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
                    if count < len(lst) and lst[count] != '#':
                        node = TreeNode(lst[count])
                        cn.right = node
                        queue.append(node)
                count += 1
                if count >= len(lst):
                    break
            else:
                break
        return root
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# sol cannot pass leetcode test
# nested function uses more stack space
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        def myBalanced(root):
            if not root:
                return (0, True)
            if not root.left and not root.right:
                return (1, True)
            lh,lb = myBalanced(root.left)
            rh,rb = myBalanced(root.right)
            balanced = lb and rb and abs(lh-rh) <= 1
            return (max(lh, rh)+1, balanced)
        h,b = myBalanced(root)
        return b

# sol2 can pass leetcode test
class Solution2:
    def isBalanced(self, root):
        return self.check(root)[1]

    # @param root, a tree node
    # @return a tuple (int height, bool isBalanced)
    def check(self, root):
        if root == None: return (0, True)
        LH, LisB = self.check(root.left)
        RH, RisB = self.check(root.right)
        return ( max(LH, RH) + 1, LisB and RisB and abs(LH - RH) <= 1 )

lst =[0,1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9,'#',0,'#',1,'#',2,'#',3,'#',4,'#',5,'#',6,'#',7,'#',8,'#',9]

root= TreeNode.createTree(lst)


sol = Solution()
print sol.isBalanced(root)