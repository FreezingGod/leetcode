# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return head
        p = head
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = node.next
        pre = head
        while pre:
            p = pre.next
            if pre.random:
                p.random = pre.random.next
            pre = p.next
        p1, p2 = head, head.next
        rtn = head.next
        while p1 and p2:
            p1.next = p2.next
            p1 = p1.next
            if p1:
                p2.next = p1.next
                p2 = p2.next
        return rtn
