# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# this solution use O(n) extra space and dfs
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return head
        dd = {}
        return self.dfs(head, dd)
    def dfs(self, node, dd):
        if not node: return node
        if node.label in dd:
            return dd[node.label]
        newnode = RandomListNode(node.label)
        dd[node.label] = newnode
        newnode.next = self.dfs(node.next, dd)
        newnode.random = self.dfs(node.random, dd)
        return newnode
