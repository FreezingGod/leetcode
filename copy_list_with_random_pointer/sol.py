# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# use O(n) extra space
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return head
        lst = []
        p = head
        d = {}
        c = 0
        while p:
            node = RandomListNode(p.label)
            lst.append(node)
            d[p] = c
            p = p.next
            c += 1
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]
        p1 = head
        p2 = lst[0]
        while p1:
            if p1.random:
                c = d[p1.random]
                p2.random = lst[c]
            p1 = p1.next
            p2 = p2.next
        return lst[0]
