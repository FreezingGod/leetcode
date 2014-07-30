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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# optimal solution, O(n)
class Solution2:
    # @param head, a list node
    # @return a tree node
    def __init__(self):
        self.ch = None
    def sortedListToBST(self, head):
        self.ch = head
        length = self.listLength(head)
        print length
        return self.listToTree(0, length)
    def listToTree(self, start, end):
        if start >= end: return None
        mid = (start+end)/2
        left = self.listToTree(start,mid)
        parent = TreeNode(self.ch.val)
        parent.left = left
        self.ch = self.ch.next
        right = self.listToTree(mid+1, end)
        parent.right = right
        return parent
    def listLength(self, head):
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        return l

# naive solution, time complexity is O(nlogn)
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        length = self.listLength(head)
        return self.listToTree(length, head, None)
    def listToTree(self, length, head, end=None):
        if head == end:
            return None
        middle = length / 2
        p = head
        for i in range(middle):
            p = p.next
        node = TreeNode(p.val)
        left = self.listToTree(middle,head, p)
        right = self.listToTree(length-1-middle,p.next, end)
        node.left = left
        node.right = right
        return node
    def listLength(self, head, end=None):
        l = 0
        p = head
        while p and p != end:
            l += 1
            p = p.next
        return l

ln = []
for i in range(10):
    ln.append(ListNode(i))
for i in range(0, 9):
    ln[i].next = ln[i+1]

sol1 = Solution()
sol2 = Solution2()
root1 = sol1.sortedListToBST(ln[0])
root2 = sol2.sortedListToBST(ln[0])
print root1.serialize()
print root2.serialize()
